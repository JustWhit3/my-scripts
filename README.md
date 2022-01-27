<p align="center"><img src="https://github.com/JustWhit3/my-scripts/blob/main/img/logo.svg" height=220></p>

<h3 align="center">A collection of scripts I developed for personal and working projects</h3>
<p align="center">
    <img title="v1.0" alt="v1.0" src="https://img.shields.io/badge/version-v1.0-informational?style=flat-square"
    <a href="LICENSE">
        <img title="MIT License" alt="license" src="https://img.shields.io/badge/license-MIT-informational?style=flat-square">
    </a>
	<img title="Python 3.8" alt="Python 3.8" src="https://img.shields.io/badge/Python-3.8-informational?style=flat-square">
	<img title="Bash" alt="Bash" src="https://img.shields.io/badge/Bash--informational?style=flat-square">
    </a>
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

All my posted scripts are and will stay **free**, but if you want to support me with a donation it would be really appreciated! 

<a href="https://www.buymeacoffee.com/JustWhit33" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## Repository diagram structure

```
my-scripts/
├── python/
│   ├── data analysis/
│   │   ├── impact parameters/
│   │   │   ├── compare_plots.py
│   │   │   ├── impact_parameters_1D.py
│   │   │   ├── impact_parameters_1D.py
│   │   ├── WbWb/
│   │   │   ├── OverlapSelections.py
├── bash/
│   ├── installation/
│   │   ├── install.sh
│   │   ├── uninstall.sh
│   │   ├── update.sh
│   ├── debugging/
│   │   ├── debug.sh
├── img/
├── README.mc
├── LICENSE/
```

## List of scripts

### python

- [**impact_parameters_1D.py**](https://github.com/JustWhit3/my-scripts/blob/main/python/data%20analysis/impact%20parameters/impact_parameters_1D.py): script used to produce 1D impact parameters plots, using the pyROOT framework, for some of my [master thesis](https://www.researchgate.net/publication/348806406_Study_of_the_quantum_interference_between_singly_and_doubly_resonant_top-quark_production_in_proton-proton_collisions_at_the_LHC_with_the_ATLAS_detector) studies (see Appendix A).

- [**impact_parameters_2D.py**](https://github.com/JustWhit3/my-scripts/blob/main/python/data%20analysis/impact%20parameters/impact_parameters_2D.py): script used to produce 2D impact parameters plots, using the pyROOT framework, for some of my [master thesis](https://www.researchgate.net/publication/348806406_Study_of_the_quantum_interference_between_singly_and_doubly_resonant_top-quark_production_in_proton-proton_collisions_at_the_LHC_with_the_ATLAS_detector) studies (see Appendix A).

- [**compare_plots.py**](https://github.com/JustWhit3/my-scripts/blob/main/python/data%20analysis/impact%20parameters/compare_plots.py): script used to compare impact parameters plots produced with [**impact_parameters_2D.py**](https://github.com/JustWhit3/my-scripts/blob/main/python/data%20analysis/impact%20parameters/impact_parameters_2D.py) and [**impact_parameters_1D.py**](https://github.com/JustWhit3/my-scripts/blob/main/Python/data%20analysis/Impact%20parameters/impact_parameters_1D.py) scripts, using the pyROOT framework.

- [**OverlapSelections.py**](https://github.com/JustWhit3/my-scripts/blob/main/python/data%20analysis/WbWb/OverlapSelections.py): script used to produce unfolding plots with overlapped b-tagging selections for each systematic. This script is produced with the pyROOT framework and is used in the ATLAS WbWb analysis.
    > NOTE on the usage: if this script is used with `./OverlapSelections` command it will produce overlapped plots for each selection of the `selections` dict. If it is used instead with the option `-o [selection_name]`, it will produce a plot with the `[selection_name]` selection modified (changes are given in the input file) and overlaps it to the real `[selection_name]`.

### bash

- [**debug.sh**](https://github.com/JustWhit3/my-scripts/blob/main/bash/debugging/debug.sh): script used to debug C++ code with Valgrind and cppcheck.
    > More information about how to use this script can be found [here](https://github.com/JustWhit3/osmanip/blob/main/doc/Download%20and%20install.md#:~:text=repository%20home%20directory.-,debug.sh,./scripts/debug.sh%20cppcheck%20%5Bfile.cpp%5D,-%C2%A9%202022%20GitHub%2C%20Inc)

- [**install.sh**](https://github.com/JustWhit3/my-scripts/blob/main/bash/installation/install.sh): script used to install headers and libraries into the system.

- [**uninstall.sh**](https://github.com/JustWhit3/my-scripts/blob/main/bash/installation/install.sh): script used to uninstall headers and libraries into the system.

- [**update.sh**](https://github.com/JustWhit3/my-scripts/blob/main/bash/installation/install.sh): script used to update a repository.
