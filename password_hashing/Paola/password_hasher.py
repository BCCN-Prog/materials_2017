# Avoid see the pwd
from getpass import getpass

username = input('Enter your username: ')
password = getpass('Enter your password: ')

print(username)
print(password)

# Try to create a dictionary of user/pass
# combinations and save it to disk
