class	Recipe:
	def	__init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = ""):
		self.check(name, cooking_lvl, cooking_time, ingredients, recipe_type, description)
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients.split() if type(ingredients) == str else ingredients
		self.recipe_type = recipe_type
		self.description = description
	def	check(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description):
		if type(name) != str:
			print("Error: name must be a string")
			exit()
		elif type(cooking_lvl) != int or cooking_lvl < 1 or cooking_lvl > 5:
			print("Error: wrong value cooking_lvl must be an integer between 1 and 5")
			exit()
		elif (type(cooking_time) != int and type(cooking_time) != float) or cooking_time < 0:
			print("Error: wrong value cooking_time must be a positive integer or a floating point")
			exit()
		elif type(description) != str:
			print("Error: description must be a string")
			exit()
		elif type(recipe_type) != str:
			print("Error: recipe_time must be a string")
			exit()
		elif recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "desert":
			print("Error: recipe_type shoulde be either starter, lunch or desert")
			exit()
		elif type(ingredients) != str and type(ingredients) != list:
			print("Error: Ingredients should be either a list of string or a string of ingredients separated by whitespace that will be parsed into a list")
			exit()
	def	__str__(self):
		"""Return the string to print with the recipe info"""
		txt = f"Recipe for {self.name}:\n" + f"- cooking_lvl: {self.cooking_lvl}\n" +\
		f"- cooking_time: {self.cooking_time:.1f}\n" +\
		"- ingredients: {}\n".format(" ".join(ingredient for ingredient in self.ingredients)) +\
		f"- recipe_type: {self.recipe_type}"
		if self.description != "":
			txt += "\n" + self.description
		return (txt)