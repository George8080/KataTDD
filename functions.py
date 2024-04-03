import os
import datetime

# Function to greet user
def greetings(name):
	if 'MYDATE' in os.environ:
		x = int(datetime.datetime.strptime(os.getenv('MYDATE'), '%m-%d-%Y %H:%M:%S').strftime('%H'))
	else:
		x = int(datetime.datetime.now().strftime('%H'))
	if (x >= 6 and x < 12):
		return ("¡Buenos días " + name + "!")
	elif (x >= 12 and x < 20):
		return ("¡Buenas tardes " + name + "!")
	else:
		return ("¡Buenas noches " + name + "!")
	pass


# Function to return the reverse word
def reverse(text):
	return text[::-1]
	pass


# Function to define if a word is a palindrome
def palindrome(txt):
	if txt == reverse(txt):
		return "¡Bonita palabra!"
	else:
		return ""
	pass


# Function to create the goodbye
def stop(name):
	return ("Adios " + name)
	pass