<p align="center"><img src="https://github.com/JustWhit3/my-scripts/blob/main/img/logo.svg" height=220></p>

<h3 align="center">A collection of personal Python and Bash scripts</h3>
<p align="center">
    <img title="v1.1" alt="v1.1" src="https://img.shields.io/badge/version-v1.1-informational?style=flat-square"
    <a href="LICENSE">
        <img title="MIT License" alt="license" src="https://img.shields.io/badge/license-MIT-informational?style=flat-square">
    </a>
	<img title="Python 3.8" alt="Python 3.8" src="https://img.shields.io/badge/Python-3.8-informational?style=flat-square">
	<img title="Bash" alt="Bash" src="https://img.shields.io/badge/Bash--informational?style=flat-square">
    </a><br>
	<img title="Code size" alt="code size" src="https://img.shields.io/github/languages/code-size/JustWhit3/my-scripts?color=red">
	<img title="Repo size" alt="repo size" src="https://img.shields.io/github/repo-size/JustWhit3/my-scripts?color=red">
	<img title="Total lines" alt="total lines" src="https://img.shields.io/tokei/lines/github/JustWhit3/my-scripts?color=red">
</p>

## Table of contents

- [Introduction](#introduction)
- [List of scripts](#list-of-scripts)
  - [python](#python)
  - [bash](#bash)

## Introduction

This repository contains some scripts I write for other personal and working projects. I keep them here for two reasons: first, to keep them easily accessible to me in case of the needing to retrieve some parts of code; secondly, to let everybody accessing them freely.

If you want to use one of my scripts please cite them with this [template citation file](https://github.com/JustWhit3/my-scripts/blob/main/CITATION.cff).

## List of scripts

### python

- [**size_of_dir.py**](https://github.com/JustWhit3/my-scripts/blob/main/scripts/python/file%20management/size_of_dir.py): script used to compute the size of a particular directory.
    > NOTE on the usage: it takes 3 arguments, `--paths` contains the directory paths (in form of `"path_1 path_2 path_n"`), `--message` is a flag to turn on/off the final message and `--exception` takes an extra file which should be removed from the final size count (it takes only the file name not the path).

- [**dirs_remover.py**](https://github.com/JustWhit3/my-scripts/blob/main/scripts/python/file%20management/dirs_remover.py): script used to efficiently remove directories in parallel.
    > NOTE on the usage: it takes 1 argument, `--dirs` which contains path to dirs to be removed (in form of `"dir_1 dir_2 dir_3"`).

- [**send_whatsapp.py**](https://github.com/JustWhit3/my-scripts/blob/main/scripts/python/social%20utils/send_whatsapp.py): script used to send whatsapp messages using Twilio.
    > NOTE on the usage: it takes 2 arguments, `--number` which is your personal number (with prefix and +) and `--message` which is the message to be sent.

### bash

- [**debug.sh**](https://github.com/JustWhit3/my-scripts/blob/main/scripts/bash/debugging/debug.sh): script used to debug C++ code with Valgrind and cppcheck.
    > More information about how to use this script can be found [here](https://github.com/JustWhit3/osmanip/blob/main/doc/Download%20and%20install.md#:~:text=repository%20home%20directory.-,debug.sh,./scripts/debug.sh%20cppcheck%20%5Bfile.cpp%5D,-%C2%A9%202022%20GitHub%2C%20Inc)

- [**install.sh**](https://github.com/JustWhit3/my-scripts/blob/main/scripts/bash/installation/install.sh): script used to install headers and libraries into the system.

- [**uninstall.sh**](https://github.com/JustWhit3/my-scripts/blob/main/scripts/bash/installation/uninstall.sh): script used to uninstall headers and libraries into the system.

- [**update.sh**](https://github.com/JustWhit3/my-scripts/blob/main/scripts/bash/installation/update.sh): script used to update a repository.
