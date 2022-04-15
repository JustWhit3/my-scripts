#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:44:00 2022
Author: Gianluca Bianco
"""

#############################################################
#    Import libraries
#############################################################
from twilio.rest import Client
import argparse as ap

#############################################################
#    SendWhatsapp
#############################################################
def SendWhatsapp( my_number, message ):

    # Credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN environment variables
    client = Client()

    # Numbers
    twilio_sandbox_testing_number = "whatsapp:+14155238886"
    number = my_number

    client.messages.create( body = message, from_ = twilio_sandbox_testing_number, to = number )
    
#############################################################
#    Main function
#############################################################
def main():
    
    # Sending the whatsapp message
    SendWhatsapp( "whatsapp:{}".format( args.number ), args.message )

if __name__ == "__main__":
    
    # Parser settings
    parser = ap.ArgumentParser( description = "Parses the folder path." )
    parser.add_argument( "--number", default = 0, help = "Your personal whatsapp number (with prefix and +)." )
    parser.add_argument( "--message", default = "", help = "The message to be sent." )
    args = parser.parse_args()
    
    # Main commands
    main()