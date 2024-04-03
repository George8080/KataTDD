import os
import datetime

def greetings(name):
	if 'MYDATE' in os.environ:
		x = datetime.datetime.strptime(os.getenv('MYDATE'), '%m-%d-%Y %H:%M:%S')
	else:
		x = datetime.datetime.now()
	y = int(x.strftime('%H'))
	if (y >= 6 and y < 12):
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