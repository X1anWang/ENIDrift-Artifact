# Artifact for paper #207 ENIDrift: A Fast and Adaptive Ensemble System for Network Intrusion Detection under Real-world Drift

# Artifact Summary
ENIDrift is a fast and adaptive ensemble system for network intrusion detection under real-world drift. The system has three components: an incremental packet-to-vector feature extraction module (iP2V), a performance-and-stability-considered sub-classifier generation module, and an ensemble update module. This artifact contains the implementation of ENIDrift and scripts to run the experiments of this work.

# Code Structure
    .
    ├── ENIDrift_ensemble.py        # ENIDrift ensemble
    ├── ENIDrift_main.py            # ENIDrift class
    ├── GenerationIndex.py          # G-idx of ENIDrift generation module
    ├── NegativePool.py             # negative pool class and its sampling function
    ├── SubLearner.py               # AutoEncoder for ensemble subclassifiers
    ├── VectorDict.py               # vector dictionary class used in iP2V
    ├── iP2Vmain.py                 # iP2V class & function
    ├── iP2Vutil.py                 # functions used in iP2V
    ├── increPacket2Vector.py       # detailed class & function
    ├── main.py                     # measure ENIDrift detection performance
    ├── measure.py                  # Scripts
    ├── (data)                      # follow below steps to get the data
    │   ├── (packets.csv)           # 
    │   └── (labels.npy)            #     
    ├── ENIDrift-AutoEncoder        # Code for ENIDrift-AutoEncoder
    │   ├── ENIDrift_ae.py          # AutoEncoder for ENIDrift
    │   ├── ENIDrift_ensemble.py    # ENIDrift ensemble
    │   ├── ENIDrift_main.py        # ENIDrift class
    │   ├── ENIDrift_utils.py       # Functions used in ENIDrift
    │   ├── GenerationIndex.py      # G-idx of ENIDrift generation module
    │   ├── NegativePool.py         # negative pool class and its sampling function
    │   ├── SubLearner.py           # AutoEncoder for ensemble subclassifiers
    │   ├── VectorDict.py           # vector dictionary class used in iP2V
    │   ├── iP2Vmain.py             # iP2V class & function
    │   ├── iP2Vutil.py             # functions used in iP2V
    │   ├── increPacket2Vector.py   # detailed class & function
    │   ├── main.py                 # main code, path & parameter initialization
    │   └── measure.py              # measure ENIDrift detection performance
    └── README.md

# Artifact Check-list
- Python 3.8.5
- scikit-learn 0.23.2
- tensorflow 2.4.1
- scapy 2.4.3
- scipy 1.7.1
- joblib 1.1.0

# Experiment

## Prepare

ENIDrift is easy to deploy in most python-supported platforms. We give experiment steps and provide following commands for reference. The commands can help build the environment for a machine with unbuntu OS, git and anaconda tools.

1. Configure python environment

First, please create a new environment with python 3.8, and activate it

```shell
conda create -n env_enidrift python=3.8
conda activate env_enidrift
```

Then, please download necessary python libraries (probably mainly pandas and scikit-learn 0.23.2)

```shell
conda install pandas -n env_enidrift
conda install -c cctbx202008 scikit-learn -n env_enidrift
```

2. Download code

Please use git to clone the Github repo, and enter it
```shell
git clone https://github.com/X1anWang/ENIDrift-Artifact
cd ENIDrift-Artifact
```

3. Download data

We prepare [data](https://drive.google.com/file/d/1HqND_mvOynDFqS8iH0FO2WRvnFuJPj2B/view?usp=sharing) and corresponding [labels](https://drive.google.com/file/d/1koy1UItBcjlZVtac_tGiCZSX7olwDPqC/view?usp=sharing) for the experiment. Please save them as packets.csv and labels.npy in a new directory named data. Command for reference
```shell
(Already in ENIDrift-Artifact directory)
mkdir data
cd data
```

We use the tool, gdown, to help download the data from google drive to our platfrom. If there is no better way to download the data from the above two links, we suggestion install the tool and download the data by gdown
```shell
pip install gdown
```

And download the two files to the data directory (the links are different from the previous two)
```shell
gdown https://drive.google.com/uc?id=1HqND_mvOynDFqS8iH0FO2WRvnFuJPj2B
gdown https://drive.google.com/uc?id=1koy1UItBcjlZVtac_tGiCZSX7olwDPqC
```

## Experiment: ENIDrift-PCA (30 min)
Since the data consists of 120,000 network packets, the experiment will end in 30 min. Please go back to the root directory of ENIDrift-Artifact from the data directory and run with python3
```shell
cd ../
python3 main.py
```

Since the experiment time is a bit long, we also suggest replacing the last command and recording the execution information in background
```shell
nohup python3 -u main.py >> record_ENIDriftPCA.txt 2>&1 &
```

The last command is only for ENIDrift running on ubuntu Linux and we can read the executuion information and results by
```shell
vim record_ENIDriftPCA.txt
```

## Supplementary experiment: ENIDrift-AutoEncoder (30 min)
ENIDrift-AE is another version of ENIDrift made of AutoEncoder. Please enter the ENIdrift-AutuoEncoder directory and run the main.py
```shell
cd ENIDrift-AutoEncoder
python3 main.py
(or nohup python3 -u main.py >> record_ENIDriftAE.txt 2>&1 &)
```

# Contact
If you have any questions about ENIDrift, please feel free to contact Sean (xwanggj@connect.hku.hk).