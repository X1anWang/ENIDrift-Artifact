import time
from iP2Vmain import *
from numpy import *
from pandas import *
from measure import *
from ENIDrift_main import *


settings = {
        'num_run': 1,
        'release_speed': 1000,
        'lamda': [0.1, 0.1],
        'delta': [0.05, 0.05],
        'incremental': True,
        'save': True,
        'vector': False,
        'my_limit': 200000
        }

path_packet = '..//data//.csv'
path_label = '..//data//.npy'

vec = settings['vector']
my_limit = settings['my_limit']


if vec:
    path_vector = '..//rwdids//.npy'
else:
    path_vector = '-1'

########################################################

num_run = settings['num_run']
release_speed = settings['release_speed']
lamd = settings['lamda']
delt = settings['delta']
incre = settings['incremental']
s = settings['save']
label = load(path_label)
packets = read_csv(path_packet)

if vec:
    vector_packet = load(path_vector)

for i_run in range(num_run):
    ENIDrift = ENIDrift_train(lamda = lamd, delta=delt, incremental=incre)
    FE = increPacket2Vector_main(path = path_packet, incremental=incre)

    ENIDrift.loadpara()
    FE.loadpara()
    prediction = []
    num_released = 0

    start = time.time()
    for i_packet in range(my_limit):
        
        if i_packet%10000 == 0:
            print(str(i_packet)+' processed...')
    
        if vec:               
            # Execute
            prediction.append(ENIDrift.predict(vector_packet[i_packet,:].reshape(1, -1)))
        else:
            packet_extracted = FE.iP2Vrun().reshape(1, -1)
            prediction.append(ENIDrift.predict(packet_extracted))
        
        # Release labels
        if i_packet % release_speed == 0:
            ENIDrift.update(label[num_released:i_packet+1])
            num_released = i_packet + 1
            
    stop = time.time()
    if s:
        ENIDrift.save()
        if not vec:
            FE.save()
    print("Time elapsed for round "+str(i_run)+": "+str(stop-start)+" seconds")
    
    
    save("result//prediction.npy", prediction)
    # result: tp, fp, tn, fn, f1, gmean
    result = evaluate(prediction, label[:my_limit])
    save("result//metrics.npy", result)
    overall(prediction, label)