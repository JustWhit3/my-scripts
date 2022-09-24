#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:13:00 2022
Author: Gianluca Bianco
"""

#############################################################
#    Import libraries
#############################################################
import shutil as sh
import os
import argparse as ap
import multiprocessing as multi
import numpy as np

#############################################################
#    RemoveSingleDir
#############################################################
def RemoveSingleDir( path_to_dir ):
    """
    Function used to remove a directory from the system.

    Args:
        path_to_dir (string): the path to the directory ro be removed.
    """
    
    os.path.join( path_to_dir )
    sh.rmtree( path_to_dir )

#############################################################
#    Main program
#############################################################
def main():
    
    # Variables
    jobs = np.array( [] )
    
    # Removing directories in parallel
    for dir in args.dirs.split( " " ):
        process = multi.Process( target = RemoveSingleDir, args = ( dir, ) )
        jobs = np.append( jobs, process )
        process.start()
    for job in jobs:
        job.join()

if __name__ == "__main__":

    # Parser settings
    parser = ap.ArgumentParser( description = "Parsing input file names." ) 
    parser.add_argument( "--dirs", default = "", help = "Path to dirs to be removed." ) 
    args = parser.parse_args()

    # Main commands
    main()