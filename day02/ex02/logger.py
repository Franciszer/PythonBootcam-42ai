import time
from getpass import getuser
from random import randint
from copy import copy

class log(object):
	def __init__(self, func):
		self.func = func
	def __call__(self, *args, **kwargs):
		time_start = time.time()
		func_ret = self.func(self.instance, *args, **kwargs)
		with open("machine.log", 'a+') as file:
			file.write(f"({getuser()})Running: {self.func.__name__:<15} \
				[ exec-time = {int(round((time.time() - time_start) * 1000)):.3f} ms ]\n")
		return func_ret
	def	__get__(self, instance, owner):
		if instance is None:
			return self
		self.instance = instance
		return self

class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
      if self.water_level > 20:
          return True
      else:
          print("Please add water!")
          return False
    
    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)