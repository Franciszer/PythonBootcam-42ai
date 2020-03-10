from random import shuffle

def	generator(text, sep = " ", option=None):
	if type(text) != str or (option != None and option != "shuffle" and option != "unique" and option != "ordered"):
		yield "ERROR"
		exit()
	split_text = text.split(sep)
	if option == "shuffle":
		shuffle(split_text)
	elif option == "unique":
		split_text = list(set(split_text))
	elif option == "ordered":
		split_text = sorted(split_text)
	for substring in split_text:
		yield(substring)

#for i in generator("world hello", " ", 'ordered'):
#	print(i)