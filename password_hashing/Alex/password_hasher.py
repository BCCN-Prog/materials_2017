from getpass import getpass

username = input('Enter your username: ')
password = getpass('Enter your password: ')


dictionary = {username:password}
d=open("password_dictionary","a+")
for i in dictionary:
    d.write("{0:s},{1:s}\n".format(i,dictionary[i]))
