#!/bin/bash

# System
sudo apt update
sudo apt upgrade

# Snap
sudo snap refresh

# Cargo
cargo install-update

# Conda
conda update conda
conda update conda-build

# Python modules
pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U
