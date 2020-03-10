from book import Book
from recipe import Recipe

steak = Recipe("steak", 2, 7.23423, ["meat", "bernaise"], "lunch", "a very good steak")
burger = Recipe("burger", 3, 10, ["meat", "bread"], "lunch", "la qualidad mon ami")
book = Book("book of recipe")
book.add_recipe("helo")
book.add_recipe(burger)
book.get_recipes_by_types("lunch")