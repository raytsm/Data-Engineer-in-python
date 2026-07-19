print("Hello, world!")
# Hello, world!
print('Hello, world!')
# Hello, world!

# This is a code comment
# The below is a print function
print("Hello, world!")

ingredient_name = "Tomatoes"
ingredient_quantity = 2

print(ingredient_name)
# Tomatoes
print(ingredient_quantity)
# 2
ingredient_quantity = 1
print(ingredient_quantity)
# 1

new_ingredient_quantity = 1.5

is_in_stock = True
is_in_stock = False

type()
print(type(is_in_stock))
# <class 'bool'>

print(2 + 1.5)
# 3.5

print("Hi" + "There")
# "HiThere"
print("Hi" * 3)
# "HiHiHi"

# Create a string variable over multiple lines
recipe_instructions = """1. Bring a large pot of salted water to boil and cook pasta
2. Heat olive oil in a pan and sauté minced garlic until fragrant
3. Add chopped tomatoes and simmer for 10 minutes
4. Toss cooked pasta with tomato sauce and fresh basil leaves
"""

# Calling a string method
string_variable.method()

welcome_message = "Welcome to the recipe scaler, George"

welcome_message = welcome_message.replace("George", "John")
print(welcome_message)
# Welcome to the recipe scaler, John

ingredient_name = "Basil Leaves"
#Convert to lowercase
ingredient_name = ingredient_name.lower()
print(ingredient_name)
# basil leaves

#Change to uppercase
ingredient_name = ingredient_name.upper()
print(ingredient_name)
# BASIL LEAVES

ingredient_one = "pasta"
ingredient_two = "tomatoes"
ingredient_three = "garlic"
ingredient_four = "basil"
ingredient_five = "olive oil"
ingredient_six = "salt"

# List of ingredients
ingredients = ["pasta", "tomatoes", "garlic", "basil", "olive oil", "salt"]

# List of ingredients using variables as values
ingredients = [ingredient_one, ingredient_two, ingredient_three, ingredient_four, ingredient_five, ingredient_size]

# Check the data type of a list
print(type(ingredients))
# <class 'list'>

print(ingredients)
# ['pasta', 'tomatoes', 'garlic', 'basil', 'olive oil', 'salt']

# Get the value of the first index
print(ingredients[0])
# pasta

# Get the fourth element
print(ingredients[3])
# basil

# Get the last element of a list
print(ingredients[5])
# salt

# Get the last element of a list for unknown length
print(ingredient[-1])
# salt