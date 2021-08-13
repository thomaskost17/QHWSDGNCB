# QHWSDGNCB
Chaotic Systems

This repository is for the purpose of serving as a playground for modeling chaotic dynamical systems and playing around with them. Much of the original inspiration for this repository is from Steve Brunton's videos and Textbook: [Data-Driven Science and Engineering](http://databookuw.com/databook.pdf). As a result, there will also be a directory dedicated to learning topics required for modeling some of these systems to begin with. 

## Contents
This repo is intended to cover the following topics:

* Dynamic Mode Decomposition (DMD)
* Sparse Solutions for DMD
* Koopman analysis
* Spectral Koopman Analysis
    * Koopman Analysis for control
* Neural Networks to perform Koopman Analysis

## Environment and Installation

The repo can first be cloned with the following shell command:

```
git clone git@github.com:thomaskost17/QHWSDGNCB.git
```

This will install the repositoy locally on your computer. Since the project is at least paritally python based, conda will be used to manage the envrionment. First, install miniconda on your local machine. Then, create the envrionment using the following command:

```
cond env create --file chaos.yml
```

Now that you have created the envrionment, all you must do to execute the code is to activate the envrionment. To do so, run the following command:

```
conda activate chaos
```