<p align="center"><img src="https://github.com/JustWhit3/my-scripts/blob/main/img/logo.svg" height=220></p>

<h3 align="center">A collection of personal Python and Bash scripts</h3>
<p align="center">
    <img title="v1.0" alt="v1.0" src="https://img.shields.io/badge/version-v1.0-informational?style=flat-square"
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
- [Repository diagram structure](#repository-diagram-structure)
- [List of scripts](#list-of-scripts)
  - [python](#python)
  - [bash](#bash)

## Introduction

This repository contains some scripts I write for other personal and working projects. I keep them here for two reasons: first, to keep them easily accessible to me in case of the needing to retrieve some parts of code; secondly, to let everybody accessing them freely.

If you want to use one of my scripts please cite them with this [template citation file](https://github.com/JustWhit3/my-scripts/blob/main/CITATION.cff).

## Repository diagram structure

```txt
my-scripts/
├── scripts/
│   ├── python/
│   │   ├── data analysis/
│   │   │   ├── impact parameters/
│   │   │   │   ├── compare_plots.py
│   │   │   │   ├── impact_parameters_1D.py
│   │   │   │   ├── impact_parameters_1D.py
│   │   │   ├── WbWb/
│   │   │   │   ├── OverlapSelections.py
│   │   ├── file management/
│   │   │   ├── size_of_dir.py
│   │   │   ├── dirs_remover.py
│   │   ├── social utils/
│   │   │   ├── send_whatsapp.py
│   ├── bash/
│   │   ├── installation/
│   │   │   ├── install.sh
│   │   │   ├── uninstall.sh
│   │   │   ├── update.sh
│   │   │   ├── system_update.sh
│   │   ├── debugging/
│   │   │   ├── debug.sh
├── img/
├── README.mc
├── LICENSE/
```

## List of scripts

### python

- [**impact_parameters_1D.py**](https://github.com/JustWhit3/my-scripts/blob/main/scripts/python/data%20analysis/impact%20parameters/impact_parameters_1D.py): script used to produce 1D impact parameters plots, using the pyROOT framework, for some of my [master thesis](https://www.researchgate.net/publication/348806406_Study_of_the_quantum_interference_between_singly_and_doubly_resonant_top-quark_production_in_proton-proton_collisions_at_the_LHC_with_the_ATLAS_detector) studies (see Appendix A).

- [**impact_parameters_2D.py**](https://github.com/JustWhit3/my-scripts/blob/main/scripts/python/data%20analysis/impact%20parameters/impact_parameters_2D.py): script used to produce 2D impact parameters plots, using the pyROOT framework, for some of my [master thesis](https://www.researchgate.net/publication/348806406_Study_of_the_quantum_interference_between_singly_and_doubly_resonant_top-quark_production_in_proton-proton_collisions_at_the_LHC_with_the_ATLAS_detector) studies (see Appendix A).

- [**compare_plots.py**](https://github.com/JustWhit3/my-scripts/blob/main/scripts/python/data%20analysis/impact%20parameters/compare_plots.py): script used to compare impact parameters plots produced with [**impact_parameters_2D.py**](https://github.com/JustWhit3/my-scripts/blob/main/python/data%20analysis/impact%20parameters/impact_parameters_2D.py) and [**impact_parameters_1D.py**](https://github.com/JustWhit3/my-scripts/blob/main/Python/data%20analysis/Impact%20parameters/impact_parameters_1D.py) scripts, using the pyROOT framework.

- [**OverlapSelections.py**](https://github.com/JustWhit3/my-scripts/blob/main/scripts/python/data%20analysis/WbWb/OverlapSelections.py): script used to produce unfolding plots with overlapped b-tagging selections for each systematic. This script is produced with the pyROOT framework and is used in the ATLAS WbWb analysis.
    > NOTE on the usage: if this script is used with `./OverlapSelections` command it will produce overlapped plots for each selection of the `selections` dict. If it is used instead with the option `-o [selection_name]`, it will produce a plot with the `[selection_name]` selection modified (changes are given in the input file) and overlaps it to the real `[selection_name]`.

- [**size_of_dir.py**](https://github.com/JustWhit3/my-scripts/blob/main/scripts/python/file%management/size_of_dir.py): script used to compute the size of a particular directory.
    > NOTE on the usage: it takes 3 arguments, `--paths` contains the directory paths (in form of `"path_1 path_2 path_n"`), `--message` is a flag to turn on/off the final message and `--exception` takes an extra file which should be removed from the final size count (it takes only the file name not the path).

- [**dirs_remover.py**](https://github.com/JustWhit3/my-scripts/blob/main/scripts/python/file%management/dirs_remover.py): script used to efficiently remove directories in parallel.
    > NOTE on the usage: it takes 1 argument, `--dirs` which contains path to dirs to be removed (in form of `"dir_1 dir_2 dir_3"`).

- [**send_whatsapp.py**](https://github.com/JustWhit3/my-scripts/blob/main/scripts/python/social%utils/send_whatsapp.py): script used to send whatsapp messages using Twilio.
    > NOTE on the usage: it takes 2 arguments, `--number` which is your personal number (with prefix and +) and `--message` which is the message to be sent.

### bash

- [**debug.sh**](https://github.com/JustWhit3/my-scripts/blob/main/scripts/bash/debugging/debug.sh): script used to debug C++ code with Valgrind and cppcheck.
    > More information about how to use this script can be found [here](https://github.com/JustWhit3/osmanip/blob/main/doc/Download%20and%20install.md#:~:text=repository%20home%20directory.-,debug.sh,./scripts/debug.sh%20cppcheck%20%5Bfile.cpp%5D,-%C2%A9%202022%20GitHub%2C%20Inc)

- [**install.sh**](https://github.com/JustWhit3/my-scripts/blob/main/scripts/bash/installation/install.sh): script used to install headers and libraries into the system.

- [**uninstall.sh**](https://github.com/JustWhit3/my-scripts/blob/main/bash/installation/uninstall.sh): script used to uninstall headers and libraries into the system.

- [**update.sh**](https://github.com/JustWhit3/my-scripts/blob/main/bash/installation/update.sh): script used to update a repository.

- [**system_update.sh**](https://github.com/JustWhit3/my-scripts/blob/main/bash/installation/system_update.sh): script used to update the whole system of your computer (not only `apt`).
