#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 11:44:00 2022
Author: Gianluca Bianco
"""

#############################################################
#    Modules
#############################################################
import platform
from termcolor import colored as cl
import socket
import re, uuid
import psutil
import cpuinfo
from datetime import datetime
from tabulate import tabulate
import GPUtil

#############################################################
#    Decoration functions
#############################################################
def TITLE( title ):
    return [ "", ( cl( "{}".format( title ), "green" ) ) ]
    
def ENTRY( second ):
    return ( cl( second, "yellow" ) )

#############################################################
#    Helper functions
#############################################################
def bt():
    """
    Get boot information.
    """
    
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp( boot_time_timestamp )
    return bt

def get_size( bytes, suffix = "B" ):
    """
    Scale bytes to its proper format
    """
    
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
        
def get_gpus():
    return ["", ""], ["", ""]

#############################################################
#    Main
#############################################################
def main():
    
    # Main container
    platform_data = [
        
        # Platform
        TITLE( "PLATFORM" ),
        [ "Platform", ENTRY( platform.system() ) ],
        [ "Platform node", ENTRY( platform.node() ) ],
        [ "Platform release", ENTRY( platform.release() ) ],
        [ "Platform version", ENTRY( platform.version() ) ],
        [ "Architecture", ENTRY( platform.machine() ) ],
        
        # Network
        [ "", "" ],
        TITLE( "NETWORK" ),
        [ "Hostname", ENTRY( socket.gethostname() ) ],
        [ "IP-address", ENTRY( socket.gethostbyname( socket.gethostname() ) ) ],
        [ "MAC-address", ENTRY( ':'.join( re.findall( '..', '%012x' % uuid.getnode() ) ) ) ],
        
        # Hardware
        [ "", "" ],
        TITLE( "HARDWARE" ),
        [ "Processor architecture", ENTRY( platform.processor() ) ],
        [ "Processor type", ENTRY( cpuinfo.get_cpu_info()['brand_raw'] ) ],
        [ "RAM memory", ENTRY( get_size( psutil.virtual_memory().total ) ) ],
        [ "SWAP memory", ENTRY( get_size( psutil.swap_memory().total ) ) ],
        [ "Disk size", ENTRY( get_size( psutil.disk_usage('/').total ) ) ],
        
        # CPU info
        [ "", "" ],
        TITLE( "CPU" ),
        [ "Physical cores", ENTRY( psutil.cpu_count( logical = False ) ) ],
        [ "Total cores", ENTRY( psutil.cpu_count( logical = True ) ) ],
        [ "Max frequency", ENTRY( f"{psutil.cpu_freq().max:.2f}Mhz" ) ],
        [ "Min frequency", ENTRY( f"{psutil.cpu_freq().min:.2f}Mhz" ) ],
        
        # System
        [ "", "" ],
        TITLE( "SYSTEM" ),
        [ "Boot time", ENTRY( f"{bt().year}/{bt().month}/{bt().day} {bt().hour}:{bt().minute}:{bt().second}" ) ],
        
        # GPU
        [ "", "" ],
        TITLE( "GPUs" ),
    ]
    
    # Insert GPUs
    for gpu, idx in zip( GPUtil.getGPUs(), range( 0, len( GPUtil.getGPUs() ) ) ):
        platform_data.append( [ str( idx + 1 ), ENTRY( gpu.name ) ] )
    
    # Print table
    print( tabulate( platform_data, headers = "firstrow", tablefmt = "fancy_grid" ) )
    print()

if __name__ == "__main__":
    main()