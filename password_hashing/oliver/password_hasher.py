from getpass import getpass
from pprint import pprint
users = {}

counter = 0
while (counter < 2):

    username = input('Enter your username: ')
    password = getpass('Enter your password: ')
    users[username]=password
    counter += 1
with open('usersdata.txt', 'w') as f:
    for user, pw in users.items():
        f.write("{} {}\n".format(user,pw))

pprint(users)
