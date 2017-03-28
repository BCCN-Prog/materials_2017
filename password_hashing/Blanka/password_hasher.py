#Blanka Version 27032017
from getpass import getpass

username = input('Enter your username: ')
password = getpass('Enter your password: ')

print(username)
print(password)

# Try to create a dictionary of user/pass
# combinations and save it to disk
#Declare dictionary
dict = {}
#Assign values
dict["username"] = username
dict["password"] = password
#Save
import pickle
with open('dict.p', 'wb') as fp:
    pickle.dump(dict, fp)

    
