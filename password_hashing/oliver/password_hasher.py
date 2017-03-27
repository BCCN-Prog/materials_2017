from getpass import getpass
from pprint import pprint
import sys

fname = 'usersdata.txt'
users = {}
counter = 0
while (counter < 2):
    username = input('Enter your username: ')
    password = getpass('Enter your password: ')
    users[username]=password
    counter += 1

try:
    f = open(fname, 'w')
except IOError:
    print("Could not write to file: {}".format(fname))
    raise
with f:
    for user, pw in users.items():
        f.write("{} {}\n".format(user,pw))
