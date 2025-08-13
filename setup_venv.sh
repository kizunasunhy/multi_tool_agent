#!/bin/bash

# Create virtual environment
python3 -m venv .adk_env

# Activate virtual environment
source .adk_env/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
