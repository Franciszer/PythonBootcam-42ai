import time
from recipe import Recipe

class	Book:
	def	__init__(self, name):
		self.name = name
		self.creation_date = time.time()
		self.last_update = time.time()
		self.recipe_list = {"starter":[], "lunch":[], "desert":[]}
	def	add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		if (isinstance(recipe, Recipe) == False):
				print("Error: not a Recipe")
				exit()
		self.recipe_list[recipe.recipe_type].append(recipe)
		self.last_update = time.time()
	def	get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		try:
			for category in self.recipe_list:
				for recipe in self.recipe_list[category]:
					print(str(recipe)) 
			return
		except:
			print(f"{name} is not in the book")
			return None
	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		for category in self.recipe_list:
			for recipe in self.recipe_list[category]:
				print(str(recipe))
