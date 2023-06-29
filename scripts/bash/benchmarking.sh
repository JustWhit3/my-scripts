#!/bin/bash

# Setting-up environment
sudo cpupower frequency-set --governor performance > /dev/null 2>&1                  # Set scaling_governor to "performance"
echo "1" | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo > /dev/null 2>&1   # Disable Turboboost
echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null 2>&1                          # Drop file system cache
sync
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space > /dev/null 2>&1               # Disable address space randomization

# Benchmark command here...

# Setting-up environment back to old settings
sudo cpupower frequency-set --governor powersave > /dev/null 2>&1
echo "0" | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo > /dev/null 2>&1
echo "" | sudo tee /proc/sys/vm/drop_caches > /dev/null 2>&1
sync
echo 2 | sudo tee /proc/sys/kernel/randomize_va_space > /dev/null 2>&1
