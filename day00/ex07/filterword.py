import sys

try:
	wordlist = ",".join(sys.argv[1].split()).split(',')
	max = int(sys.argv[2])
	new = [word for word in wordlist if len(word) >= max]
	print(new)
except:
	print("Error: arguments must be str and int")