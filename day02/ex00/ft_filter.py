def	ft_filter(func, iterable):
	return [i for i in iterable if func(i) == True]
