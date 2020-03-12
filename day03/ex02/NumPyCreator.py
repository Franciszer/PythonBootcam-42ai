import numpy as np

class	NumPyCreator:
	@staticmethod
	def	from_list(lst, dtype = None):
		return np.array(lst, dtype)
	@staticmethod
	def	from_tuple(tpl, dtype = None):
		return np.array(tpl, dtype)
	@staticmethod
	def	from_iterable(itr, dtype = None):
		return np.array(itr, dtype)
	@staticmethod
	def	from_shape(shape, value = 0, dtype = None):
		return np.full(shape, value, dtype)
	@staticmethod
	def	random(*shape):
		return np.random.rand(*shape)
	@staticmethod
	def	identity(size, dtype = None):
		return np.identity(size, dtype)
