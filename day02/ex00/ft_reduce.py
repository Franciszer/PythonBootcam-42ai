def	ft_reduce(func, iterable):
	output = iterable[0]
	for i in iterable[1:]:
		output = func(output, i)
	return output
