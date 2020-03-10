def	ft_map(func, *args):
	shortest_len = 0
	for arg in args:
		shortest_len = len(arg) if shortest_len == 0 or len(arg) < shortest_len else shortest_len
	output = []
	for i in range(0, shortest_len):
		func_args = [arg[i] for arg in args]
		output.append(func(*func_args))
	return (output)

