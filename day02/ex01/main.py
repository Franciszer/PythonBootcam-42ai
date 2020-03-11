def what_are_the_vars(*args, **kwargs):
	index = 0
	expected_len = len(args) + len(kwargs)
	for i in args:
		kwargs["var_" + str(index)] = i
		index += 1
	return ObjectC(**kwargs) if expected_len == len(kwargs) else None


class ObjectC(object):
	def __init__(self, **kwargs):
		self.__dict__.update(**kwargs)

def doom_printer(obj):
	if obj is None:
		print("ERROR")
		print("end")
		return
	for attr in dir(obj):
		if attr[0] != '_':
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print("end")