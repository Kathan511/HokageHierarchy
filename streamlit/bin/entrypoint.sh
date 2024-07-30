#!/bin/bash

# enable debugging
set -x

export PATH="/home/ubuntu/miniconda/bin:$PATH"

source activate conda_env_name

streamlit run app.py $@
