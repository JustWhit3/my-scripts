#!/bin/bash

# $1: the input .h/.hpp file to be tested for include. Use complete path in string format.

#====================================================
#     Metadata
#====================================================
# File name:  include_tests.sh
# Author:     Gianluca Bianco (biancogianluca9@gmail.com)
# Date:       2022-09-27
# Copyright:  (c) 2022 Gianluca Bianco under the MIT license.

# Creating the first file
touch include_one.hpp
echo "#ifndef INCLUDE_ONE" >> include_one.hpp
echo "#define INCLUDE_ONE" >> include_one.hpp
echo "#include <${1}>" >> include_one.hpp
echo "#endif" >> include_one.hpp

# Creating the second file
touch include_two.hpp
echo "#ifndef INCLUDE_TWO" >> include_two.hpp
echo "#define INCLUDE_TWO" >> include_two.hpp
echo "#include <${1}>" >> include_two.hpp
echo "#endif" >> include_two.hpp

# Creating the multiple include file
touch multiple_include.cpp
echo "#include \"include_one.hpp\"" >> multiple_include.cpp
echo "#include \"include_two.hpp\"" >> multiple_include.cpp
echo "int main() {}" >> multiple_include.cpp

# Compiling
g++ -std=c++17 multiple_include.cpp

# Removing all
rm include_one.hpp
rm include_two.hpp
rm multiple_include.cpp
rm a.out