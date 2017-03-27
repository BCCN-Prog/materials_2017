from getpass import getpass
import json

try:
    with open('users.json', 'r') as f:
        users = json.load(f)
except EnvironmentError:
    users = {}

username = input('Enter your username: ')
password = getpass('Enter your password: ')

if username in users:
    print("Modified password for exisiting user:", username)
else:
    print("Created new user:", username)

users[username] = password

with open('users.json', 'w') as f:
    json.dump(users, f, sort_keys=True, indent=4)
