#! /bin/bash

# Create a new conda environment
conda create -n telfit_tutorial python=2 numpy scipy matplotlib astropy cython requests jupyter ipython-notebook seaborn

source activate telfit_tutorial
pip install -r requirements.txt
