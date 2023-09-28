#!/bin/bash

# enable debugging
set -x

export PATH="/home/ubuntu/miniconda/bin:$PATH"

source activate conda_env_name

python -m main_scipt $@