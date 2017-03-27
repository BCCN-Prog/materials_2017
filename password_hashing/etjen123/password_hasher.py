import getpass

username = input('Enter your username: ')
password = getpass.getpass(prompt='Enter your password: ', stream=None)

#Declare dictionary 
dict = {}
#Assign values
dict["username"] = username
dict["password"] = password
#Save
import pickle
with open('dict.p', 'wb') as fp:
    pickle.dump(dict, fp)


