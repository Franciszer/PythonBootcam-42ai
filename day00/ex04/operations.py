import sys

def	do_op(a, b):
	print(
		" Sum:			{}\n".format(a + b),\
		"Difference:	{}\n".format(a - b),\
		"Product:		{}\n".format(a * b),\
		"Quotient:		{}\n".format(a / b if b != 0 else "ERROR (div by zero)"),\
		"Remainder:		{}".format(a % b if b != 0 else "ERROR (modulo by zero)"))

try:
	do_op(int(sys.argv[1]), int(sys.argv[2]))\
	if len(sys.argv) == 3 else\
	print("Error: Too ", "many" if len(sys.argv) > 3 else "few", " arguments")
except:
	print("Error: only numbers")