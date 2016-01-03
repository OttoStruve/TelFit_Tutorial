# TelFit Tutorial
This repository holds materials for the tutorial on TelFit usage, taking place on January 12 at 10am in the RLM classroom at UT. The tutorial mostly consists of a series of jupyter notebooks that we will go through, as well as some scripts to setup your environment. 

## Getting started

The first thing to do is download the tutorial. The best way to do this is type:

```bash
git clone https://github.com/OttoStruve/TelFit_Tutorial
cd TelFit_Tutorial
```

If you don't have a github account and don't want one, you can also just download the zip file. Keep in mind though that you will not be able to update your local repository if any changes are made after you download the zip!

Before the tutorial, please make sure you have a working environment that includes TelFit and all of its required packages. If you use anaconda python, you should be able to just run

```bash
./setup_environment_conda.sh
source activate telfit_tutorial
```
If you don't use anaconda python, you should create a virtual environment for the tutorial and then type
```bash
pip install -r requirements.txt
```

Once you have the environment setup, run 
```bash
python check_env.py
```
to make sure that the environment is set up correctly. You can ignore warnings about "PYSYN_CDBS not found". It is telling you that datafiles for pysynphot are not downloaded, but telfit doesn't use that part of the code so it doesn't affect us. If you see any messages about some package not found, then you will need to make sure to install that package.
