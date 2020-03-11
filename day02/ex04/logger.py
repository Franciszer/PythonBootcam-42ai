import time
from getpass import getuser
from random import randint
from copy import copy

class logtime(object):
	def __init__(self, func):
		self.func = func
	def __call__(self, *args, **kwargs):
		time_start = time.time()
		func_ret = self.func(self.instance, *args, **kwargs) if hasattr(self, "instance") else self.func(*args, **kwargs)
		with open("machine.log", 'a+') as file:
			file.write(f"({getuser()})Running: {self.func.__name__:<15} \
				[ exec-time = {int(round((time.time() - time_start) * 1000)):.3f} ms ]\n")
		return func_ret
	def	__get__(self, instance, owner):
		if instance is None:
			return self
		self.instance = instance
		return self
