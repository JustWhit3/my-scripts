<p align="center"><img src="https://github.com/JustWhit3/my-scripts/blob/main/img/logo.svg" height=220></p>

<h3 align="center">A collection of personal Python and Bash scripts</h3>
<p align="center">
    <img title="v1.1" alt="v1.1" src="https://img.shields.io/badge/version-v1.1-informational?style=flat-square"
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
  - [size_of_dir.py](#sizeofdirpy)
  - [dirs_remover.py](#dirsremoverpy)
  - [send_whatsapp.py](#sendwhatsapppy)
- [Bash](#bash)
  - [debug.sh](#debugsh)
  - [update.sh](#updatesh)
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

### [dirs_remover.py](https://github.com/JustWhit3/my-scripts/tree/main/python/dirs_remover)

**Description**: script used to efficiently remove directories in parallel.

**Arguments**:

- `--dirs`: contains path to dirs to be removed in parallel. Example: `"dir_1 dir_2 dir_3"`.

### [send_whatsapp.py](https://github.com/JustWhit3/my-scripts/tree/main/python/send_whatsapp)

**Description**: script used to send whatsapp messages using [Twilio API](https://www.twilio.com/go/twilio-brand-sales-it-1?utm_source=google&utm_medium=cpc&utm_term=twilio&utm_campaign=G_S_EMEA_Brand_Mature_ITA_IT_NV&cq_plac=&cq_net=g&cq_pos=&cq_med=&cq_plt=gp&gclid=Cj0KCQjw1bqZBhDXARIsANTjCPJl_as8WIkOJAThL-NlAH7ZpkR94dFMUdvH64ISyvYz-e6N0HK5iroaAvQ2EALw_wcB). It can be easily used for bots.

**Arguments**:

- `--number`: your personal telephone number (with prefix and +).
- `--message`: the message to be sent.

## Bash

### [debug.sh](https://github.com/JustWhit3/my-scripts/blob/main/bash/debug.sh)

**Description**: script used to debug C/C++ code with Valgrind and cppcheck.

**Requirements**:

- [cppcheck](https://cppcheck.sourceforge.io/).
- [Valgrind](https://valgrind.org/).

**Arguments**:

- `$1`: debug option (cppcheck, memcheck, helgrind etc...).
- `$2`: source file to be debugged.

### [update.sh](https://github.com/JustWhit3/my-scripts/blob/main/bash/update.sh)

**Description**: script used to update a repository without using git.

**Requirements**:

- [wget](https://www.gnu.org/software/wget/).
- [unzip](https://linuxhint.com/unzip_command_-linux/).
