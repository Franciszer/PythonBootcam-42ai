import string

def text_analyzer(s = ""):
	"""This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text."""

	if s == "":
		s = input("What is the text to analyze?\n")
	print("The text contains {} characters:\n".format(len(s)),\
	"- {} upper letters\n".format(sum(1 for c in s if c.isupper())),
	"- {} lower letters\n".format(sum(1 for c in s if c.islower())),
	"- {} punctuation marks\n".format(sum(map(lambda x: x in string.punctuation , s))),\
	"- {} spaces".format(sum(map(lambda x: x in " ", s))))