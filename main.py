from functions import greetings
from functions import reverse
from functions import palindrome
from functions import stop


while True:
	start = [str(x) for x in input().split()]
	if len(start) >= 2:
		if start[0] == 'ohce':
			name = start[1]
			for i in range(len(start) - 2):
				name = name + ' ' + start[i+2]
				pass
			print(greetings(name))
			break
		pass
	pass

while True:
	txt = input()
	if txt == "Stop!":
		print(stop(name))
		break
		pass
	print(reverse(txt))
	if palindrome(txt) != "":
		print(palindrome(txt))
		pass
	pass