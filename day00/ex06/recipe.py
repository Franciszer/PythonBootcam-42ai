
def	add_recipe(cookbook, name, r_ingredients, r_meal, r_prep_time):
	for key, value in cookbook.items():
		if key == name:
			print("Error: recipe already exists")
	else:
		cookbook[name] = {}
		cookbook[name]["ingredients"] = r_ingredients
		cookbook[name]["meal"] = r_meal
		cookbook[name]["prep_time"] = r_prep_time

def	delete_recipe(cookbook, name):
	cookbook.pop(name, None)

def	print_recipe(cookbook, name):
	print("Recipe for ", name)
	print("Ingredients: ", " ,".join(i for i in cookbook[name]["ingredients"]))
	print("Type of meal: ",cookbook[name]["meal"])
	print("Prep_time: {} minutes".format(cookbook[name]["prep_time"]))

def	print_allrecipes(cookbook):
	for key, value in cookbook.items():
		print_recipe(cookbook, key)
		print()

cookbook = {}
while (1):
	try:
		print ("Please select an option by typing the corresponding number:")
		print("1: Add a recipe")
		print("2: Delete a recipe")
		print("3: Print a recipe")
		print("4: Print the cookbook")
		print("5: Quit")
		a = input()
		if int(a) == 1:
			name = input("Enter the recipe name: ")
			r_ingredients = input("Enter the recipe ingredients: ").split()
			r_meal= input("Enter the type of meal for this recipe: ")
			r_prep_time = int(input("Enter the recipe prep_time: "))
			add_recipe(cookbook, name, r_ingredients, r_meal, 0)
		elif int(a) == 2:
			name = input("Enter the recipe to delete: ")
			delete_recipe(cookbook, name)
		elif int(a) == 3:
			name = input("Enter the recipe to print: ")
			print_recipe(cookbook, name)
		elif int(a) == 4:
			print_allrecipes(cookbook)
		elif int(a) == 5:
			break
		else:
			print("Incorrect input")
	except:
		print("Incorrect input")
