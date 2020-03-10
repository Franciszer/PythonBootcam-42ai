import sys

try:
	for n in sys.argv[1:]:
		print("I'm Zero" if int(n) == 0 else "I'm odd"\
		if int(n)%2 == 1 else "I'm even")
except:
	print("ERROR")
