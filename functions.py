import os
import datetime

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

def reverse(text):
	return text[::-1]
	pass

def palindrome(txt):
	if txt == reverse(txt):
		return "¡Bonita palabra!"
	else:
		return ""
	pass

def stop(name):
	pass