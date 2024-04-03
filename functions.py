import os
import datetime

def greetings(name):
	if 'MYDATE' in os.environ:
		x = int(datetime.datetime.strptime(os.getenv('MYDATE'), '%m-%d-%Y %H:%M:%S').strftime('%H'))
	else:
		x = int(datetime.datetime.now().strftime('%H'))
	if (x >= 6 and x < 12):
		return ("¡Buenos días " + name + "!")
	else:
		return ("Hola " + name)
	pass

def palindrome(text):
	pass

def reverse(txt):
	pass

def stop():
	pass