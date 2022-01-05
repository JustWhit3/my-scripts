# my-scripts

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
├── README.mc
├── LICENSE/
```

## List of scripts

### python

- [**impact_parameters_1D.py**](https://github.com/JustWhit3/my-scripts/blob/main/python/data%20analysis/impact%20parameters/impact_parameters_1D.py): script used to produce 1D impact parameters plots, using the pyROOT framework, for some of my [master thesis](https://www.researchgate.net/publication/348806406_Study_of_the_quantum_interference_between_singly_and_doubly_resonant_top-quark_production_in_proton-proton_collisions_at_the_LHC_with_the_ATLAS_detector) studies (see Appendix A).

- [**impact_parameters_2D.py**](https://github.com/JustWhit3/my-scripts/blob/main/python/data%20analysis/impact%20parameters/impact_parameters_2D.py): script used to produce 2D impact parameters plots, using the pyROOT framework, for some of my [master thesis](https://www.researchgate.net/publication/348806406_Study_of_the_quantum_interference_between_singly_and_doubly_resonant_top-quark_production_in_proton-proton_collisions_at_the_LHC_with_the_ATLAS_detector) studies (see Appendix A).

- [**compare_plots.py**](https://github.com/JustWhit3/my-scripts/blob/main/python/data%20analysis/impact%20parameters/compare_plots.py): script used to compare impact parameters plots produced with [**impact_parameters_2D.py**](https://github.com/JustWhit3/my-scripts/blob/main/python/data%20analysis/impact%20parameters/impact_parameters_2D.py) and [**impact_parameters_1D.py**](https://github.com/JustWhit3/my-scripts/blob/main/Python/data%20analysis/Impact%20parameters/impact_parameters_1D.py) scripts, using the pyROOT framework.

- [**OverlapSelections.py**](https://github.com/JustWhit3/my-scripts/blob/main/python/data%20analysis/WbWb/OverlapSelections.py): script used to produce unfolding plots with overlapped b-tagging selections for each systematic. This script is produced with the pyROOT framework and is used in ATLAS WbWb analysis.

### bash

- [**debug.sh**](https://github.com/JustWhit3/my-scripts/blob/main/bash/debugging/debug.sh): script used to debug C++ code with Valgrind and cppcheck.

- [**install.sh**](https://github.com/JustWhit3/my-scripts/blob/main/bash/installation/install.sh): script used to install headers and libraries into the system.

- [**uninstall.sh**](https://github.com/JustWhit3/my-scripts/blob/main/bash/installation/install.sh): script used to uninstall headers and libraries into the system.

- [**update.sh**](https://github.com/JustWhit3/my-scripts/blob/main/bash/installation/install.sh): script used to update a repository.
