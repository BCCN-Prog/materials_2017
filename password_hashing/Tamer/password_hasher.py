from getpass import getpass
import pickle
quit = True
while quit==True:
	username = raw_input("Enter your username: ")
	password = getpass("Enter your password: ")

	print (username)
	print (password)




	pass_dictionary = {}
	pass_dictionary[username] = password
	test=raw_input("Enter Q to quit: ")
	if test=="q": quit =False
output = open('myfile.pkl', 'wb')
pickle.dump(pass_dictionary, output)
output.close()

