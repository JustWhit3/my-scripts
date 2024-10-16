<p align="center"><img src="https://github.com/JustWhit3/my-scripts/blob/main/img/logo.svg" height=220></p>

<h3 align="center">A collection of personal scripts</h3>
<p align="center">
    <img title="v1.4" alt="v1.4" src="https://img.shields.io/badge/version-v1.4-informational?style=flat-square"
    <a href="LICENSE">
        <img title="MIT License" alt="license" src="https://img.shields.io/badge/license-MIT-informational?style=flat-square">
    </a>
	<img title="Python" alt="Python" src="https://img.shields.io/badge/Python--informational?style=flat-square">
	<img title="Bash" alt="Bash" src="https://img.shields.io/badge/Bash--informational?style=flat-square">
    </a><br>
	<img title="Code size" alt="code size" src="https://img.shields.io/github/languages/code-size/JustWhit3/my-scripts?color=red">
	<img title="Repo size" alt="repo size" src="https://img.shields.io/github/repo-size/JustWhit3/my-scripts?color=red">
	<img title="Total lines" alt="total lines" src="https://img.shields.io/tokei/lines/github/JustWhit3/my-scripts?color=red">
</p>

## Table of contents

- [Introduction](#introduction)
- [Python](#python)
  - [size_of_dir.py](#size_of_dirpy)
  - [dirs_remover.py](#dirs_removerpy)
  - [send_whatsapp.py](#send_whatsapppy)
  - [system_info.py](#system_infopy)
  - [compute_lines.py](#compute_lines)
- [Bash](#bash)
  - [debug.sh](#debugsh)
  - [update.sh](#updatesh)
  - [setup_env.sh](#setup_envsh)
  - [include_tests.sh](#include_testssh)
  - [benchmarking.sh](#benchmarkingsh)
- [CMake](#cmake)
  - [Qt installer](#qt-installer)
- [Stargazers over time](#stargazers-over-time)

## Introduction

This repository contains some scripts I write for other personal and working projects. I keep them here for two reasons: first, to keep them easily accessible to me in case of the needing to retrieve some parts of code; secondly, to let everybody accessing them freely.

For each script folder there is a `requirements.txt` file which contains prerequisites for correct usage.

If you want to use one of my scripts please cite them with this [template citation file](https://github.com/JustWhit3/my-scripts/blob/main/CITATION.cff).

## Python

### [size_of_dir.py](https://github.com/JustWhit3/my-scripts/tree/main/python/size_of_dir)

**Description**: script used to compute the size of a single or more directories in a precise way, by considering also all the subdirectories and files.

**Arguments**:

- `--paths`: directory path, or paths. Example: `"path_1 path_2 path_n"`.
- `--message`: a flag to turn on/off the final message.
- `--exception`: exclude a particular file from the final count.

### [dirs_remover.py](https://github.com/JustWhit3/my-scripts/tree/main/scripts/python/dirs_remover)

**Description**: script used to efficiently remove directories in parallel.

**Arguments**:

- `--dirs`: contains path to dirs to be removed in parallel. Example: `"dir_1 dir_2 dir_3"`.

### [send_whatsapp.py](https://github.com/JustWhit3/my-scripts/tree/main/scripts/python/send_whatsapp)

**Description**: script used to send whatsapp messages using [Twilio API](https://www.twilio.com/go/twilio-brand-sales-it-1?utm_source=google&utm_medium=cpc&utm_term=twilio&utm_campaign=G_S_EMEA_Brand_Mature_ITA_IT_NV&cq_plac=&cq_net=g&cq_pos=&cq_med=&cq_plt=gp&gclid=Cj0KCQjw1bqZBhDXARIsANTjCPJl_as8WIkOJAThL-NlAH7ZpkR94dFMUdvH64ISyvYz-e6N0HK5iroaAvQ2EALw_wcB). It can be easily used for bots.

**Arguments**:

- `--number`: your personal telephone number (with prefix and +).
- `--message`: the message to be sent.

### [system_info.py](https://github.com/JustWhit3/my-scripts/tree/main/scripts/python/system_info)

**Description**: script used to get current device information (RAM, CPU, etc...).

### [compute_lines.py](https://github.com/JustWhit3/my-scripts/tree/main/scripts/python/compute_lines)

**Description**: Script used to count lines of code in files with specific extensions (`.cpp`, `.hpp`, `.py`, `.sh`, or custom extensions) within one or more directories, recursively.

**Arguments**:
- `directories`: a list of directories to scan. Example: `"dir_1 dir_2 dir_n"`.
- `-e`, `--extensions`: file extensions to include in the count (optional). If not specified, the default is `['.cpp', '.hpp', '.py', '.sh']`. Example: `-e .cpp .py`.

## Bash

### [debug.sh](https://github.com/JustWhit3/my-scripts/blob/main/scripts/bash/debug.sh)

**Description**: script used to debug C/C++ code with Valgrind and cppcheck.

**Requirements**:

- [cppcheck](https://cppcheck.sourceforge.io/).
- [Valgrind](https://valgrind.org/).

**Arguments**:

- `$1`: debug option (cppcheck, memcheck, helgrind etc...).
- `$2`: source file to be debugged.

### [update.sh](https://github.com/JustWhit3/my-scripts/blob/main/scripts/bash/update.sh)

**Description**: script used to update a repository without using git.

**Requirements**:

- [wget](https://www.gnu.org/software/wget/).
- [unzip](https://linuxhint.com/unzip_command_-linux/).

### [setup_env.sh](https://github.com/JustWhit3/my-scripts/blob/main/scripts/bash/setup_env.sh)

**Description**: script used to create a virtual environment specifying Python version, environment name and requirements file. If it is the first time you run it, a virtual environment will be created and activated and prerequisites Python modules will be installed. From the second time on, the script will simply activate the virtual environment.
> :warning: Launch it with `source setup_env.sh` since `source` command is used into the script.

**Requirements**:

- [virtualenv](https://mannimal.blog/2019/07/04/creating-a-virtualenv-with-python-3-7-3/).

**Arguments**:

- `$1`: Python version.
- `$2`: Virtual environment name.
- `$3`: Requirements file.

### [include_tests.sh](https://github.com/JustWhit3/my-scripts/blob/main/scripts/bash/include_tests.sh)

**Description**: script used to launch include tests of a .h/.hpp c++ file. Basically it tests if the file can be included correctly in a generic program and if there are no inline errors in case of multiple inclusion from different files.

**Requirements**:

- [g++](https://gcc.gnu.org/) compiler.

**Arguments**:

- `$1`: the input .h/.hpp file to be tested for include. Use complete path in string format.

### [benchmarking.sh](https://github.com/JustWhit3/my-scripts/blob/main/scripts/bash/benchmarking.sh)

**Description**: script used to optimize benchmark result precision. To use it open the script and add your benchmark command in the respective line, doesn't matter which command you prefer, it is not relevant. The script allows to set scaling governor to "precision", to disable Turboboost, to drop file cache and to disable address space randomization. All these operations will improve the precision of the result. At the end all the settings will be restored.

**Arguments**:

- `$1`: the number of benchmarking iterations.

## CMake

### [Qt installer](https://github.com/JustWhit3/my-scripts/blob/main/scripts/cmake/Qt_installer/CMakeLists.txt)

**Description**: script used to install Qt. Default is Qt6 but the version can be changed from the script.

## Stargazers over time

[![Stargazers over time](https://starchart.cc/JustWhit3/my-scripts.svg)](https://starchart.cc/JustWhit3/my-scripts)