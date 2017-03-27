from getpass import getpass
import pickle
import os.path
from pathlib import Path


UserData = Path('/home/newuser/Dokumente/programming_project/materials_2017/password_hashing/claudia_eric/UsersPasswords.p')

if UserData.is_file():
    users_and_passwords = pickle.load( open( "UsersPasswords.p", "rb" ) )
    print(users_and_passwords)
else:
    users_and_passwords = {}

username = input('Enter your username: ')
password = getpass('Enter your password: ')

users_and_passwords[username] = password
print(users_and_passwords)

pickle.dump(users_and_passwords, open( "UsersPasswords.p", "wb" ))

