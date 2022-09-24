#!/bin/bash

# $1: Python version.
# $2: Virtual environment name.
# $3: Requirements file. 

# Variables
version=$1
venv=$2
reqs=$3

# Creating the virtualenv
if [[ ! -d ${venv} ]] ; then
    if [ "${venv}" != "" ] ; then
        if ! virtualenv "${venv}" -p python"${version}" ; then
            echo "Error: missing Python ${version} installation."
            exit 1
        fi
    fi
    if  [ "${reqs}" != "" ] ; then
        echo "Installing prerequisites..."
        pip install -r "${reqs}"
    fi
fi

# Activating virtual environment
echo "Activating the virtual environment..."
source ${venv}/bin/activate
echo "Done."