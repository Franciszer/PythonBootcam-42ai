import random

nb = random.randint(1, 99)
count = 0
print("Find the secret number between 1 and 99\n"\
		"Type exit to exit the game")
while 1:
	guess = input("What is the secret number?\n")
	if guess == 'exit':
		break
	count += 1
	try:
		guess = int(guess)
		if guess == nb:
			print("Right number! {} tries".format(count))
			break
		else:
			print("Too low" if guess < nb else "Too high")
	except:
		print("Error: input must be an integer")