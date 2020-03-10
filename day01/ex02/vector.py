class	Vector:
	def	__init__(self, vals):
		if (type(vals) == list):
			self.values = vals
		elif(type(vals) == int):
			if (vals < 0):
				print("Error: range must be a positve integer")
			self.values = []
			for i in range(vals):
				self.values.append(i)
		elif(type(vals) == tuple and len(vals) == 2 and type(vals[0]) == int and vals[0] <= vals[1]):
			self.values = []
			for i in range(vals[0], vals[1]):
				self.values.append(i)
		else:
			print("Error: bad syntax")
	def	__add__(self, other):
		add_list = []
		if isinstance(other, Vector):
			vector_len = len(self.values)
			if len(other.values) == vector_len:
				for i in range(0, vector_len):
					add_list.append(self.values[i] + other.values[i])
			else:
				print("Error: the two vectors need to have the same number of dimensions")
		elif type(other) == float or type(other) == int:
			for val in self.values:
				add_list.append(val + other)
		else:
			print("Error: other must be Vector, float or integer")
			exit()
		return add_list
	def	__radd__(self, other):
		return(self.__add__(other))
	def	__sub__(self, other):
		add_list = []
		if isinstance(other, Vector):
			vector_len = len(self.values)
			if len(other.values) == vector_len:
				for i in range(0, vector_len):
					add_list.append(self.values[i] - other.values[i])
			else:
				print("Error: the two vectors need to have the same number of dimensions")
		elif type(other) == float or type(other) == int:
			for val in self.values:
				add_list.append(val - other)
		else:
			print("Error: other must be Vector, float or integer")
			exit()
		return add_list
	def	__rsub__(self, other):
		return(self.__sub__(other))
	def	__truediv__(self, other):
		add_list = []
		if other == 0:
			print("Error: division by zero")
			exit()
		if type(other) == float or type(other) == int:
			for val in self.values:
				add_list.append(val / other)
		else:
			print("Error: other must be Vector, float or integer")
			exit()
		return add_list
	def	__rtruediv__(self, other):
		return(self.__truediv__(other))
	def	__mul__(self, other):
		add_list = []
		if isinstance(other, Vector):
			vector_len = len(self.values)
			if len(other.values) == vector_len:
				for i in range(0, vector_len):
					add_list.append(self.values[i] * other.values[i])
			else:
				print("Error: the two vectors need to have the same number of dimensions")
		elif type(other) == float or type(other) == int:
			for val in self.values:
				add_list.append(val * other)
		else:
			print("Error: other must be Vector, float or integer")
			exit()
		return add_list
	def	__rmul__(self, other):
		return(self.__mul__(other))
	def	__str__(self):
		return f"{len(self.values)} dimensions.\n" +\
		"Values: {}".format(", ".join(str(i) for i in self.values))
	def __repr__(self):
		return " ".join(str(i) for i in self.values)