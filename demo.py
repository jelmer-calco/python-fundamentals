# ============================================================
# PYTHON TRAINING - REVIEW AND BUILDING TOWARDS FUNCTIONS
# ============================================================

# You can comment by selecting a line and using "ctrl /" or put an # in front of the line of code



# ============================================================
# PART 1 - REVIEW OF PRIOR KNOWLEDGE
# ============================================================

# In this exercise we review:
# - variables
# - strings
# - lists
# - dictionaries
# - if/else
# - operators
# - string methods like .lower()


name = "mila"
age = 20 


# ------------------------------------------------------------
# PART 1 - Demo 1
# ------------------------------------------------------------

# name = "Mila"
# age = 20

# # List
# hobbies = ["coding", "traveling", "cooking"]

# # Dictionary
# student = {
#     # "naam van het vakje": waarde_die_erin_komt
#     # key : value 
#     "name": name,
#     "age": age,
#     "hobbies": hobbies,
# }

# # index starts at 0, so the first item is index 0
# print(hobbies[0])  # print first hobby
# print(student["name"])  # print name from dictionary
# print(student)


# ------------------------------------------------------------
# PART 1 - Assignment 1
# ------------------------------------------------------------

# Create:
# 1. A variable for a name

# 2. A variable for an age

# 3. A list with three hobbies

# 4. A dictionary with name, age and city
# 5. Print the name from the dictionary
# 6. Print the first hobby
# 7. Use if/else to check whether the person is 18 or older


# ============================================================
# PART 2 - NEW TOPIC: FOR LOOPS
# ============================================================

# A for-loop is used when you want to loop over multiple items.
# For example, over all names in a list.


# ------------------------------------------------------------
# PART 2 - Demo 2
# ------------------------------------------------------------

# For-loop with a list


# ------------------------------------------------------------
# PART 2 - Assignment 2
# ------------------------------------------------------------

# Create a list with three favorite foods.
# Use a for-loop to print each food.
# Example:
# My favorite food is pizza


# ============================================================
# PART 3 - FOR LOOPS AND WHILE LOOPS
# ============================================================

# A for-loop is useful when you know what you want to loop over.
# For example:
# - a list of names
# - a list of grades
# - a range of numbers
#
# A while-loop is useful when code should repeat as long as a condition is True.
# For example:
# - keep counting while a number is lower than 5
# - keep asking for a password while the password is wrong
#
# Be careful:
# A while-loop can become an infinite loop if the condition never becomes False.


# ------------------------------------------------------------
# PART 3 - Demo 3A
# ------------------------------------------------------------

# For-loop with grades


# ------------------------------------------------------------
# PART 3 - Demo 3B
# ------------------------------------------------------------

# While-loop that stops


# ------------------------------------------------------------
# PART 3 - Demo 3C
# ------------------------------------------------------------

# Infinite while-loop example
#

# number = 1

# while number <= 5:
#     print(number)

# This loop never stops because number stays 1 forever.


# ------------------------------------------------------------
# PART 3 - Assignment 3
# ------------------------------------------------------------

# Create a list with ages.
# Loop over the ages with a for-loop.
# Print for each age whether the person is an adult or not.
#
# Example:
# 16 is underage
# 21 is an adult
#
# Then create a counter variable.
# Use a while-loop to print the numbers 1 to 3.
# Make sure the while-loop stops.


# ============================================================
# PART 4 - RANGE
# ============================================================

# range() is used when you want to repeat something a number of times.
# range(5) means: 0, 1, 2, 3, 4


# ------------------------------------------------------------
# PART 4 - Demo 4
# ------------------------------------------------------------

# Using range


# ------------------------------------------------------------
# PART 4 - Assignment 4
# ------------------------------------------------------------

# Use range to print the numbers 1 to 10.


# ============================================================
# PART 5 - LOOPING THROUGH A DICTIONARY
# ============================================================

# A dictionary has keys and values.
# With .items() you can loop through both at the same time.


# ------------------------------------------------------------
# PART 5 - Demo 5
# ------------------------------------------------------------

# Dictionary with .items()


# ------------------------------------------------------------
# PART 5 - Common mistake
# ------------------------------------------------------------

# If you ask for a key that does not exist, Python gives an error.
#
# movie = {
#     "title": "Finding Nemo",
#     "year": 2003
# }
#
# print(movie["genre"])
#
# The key "genre" does not exist here.


# ------------------------------------------------------------
# PART 5 - Assignment 5
# ------------------------------------------------------------

# Create a dictionary for a movie.
# Use these keys:
# - title
# - year
# - genre
#
# Then use a for-loop with .items()
# to print all information clearly.


# ============================================================
# PART 6 - FUNCTIONS
# ============================================================

# A function is a piece of code that you can reuse.
# You create a function with def.


# ------------------------------------------------------------
# PART 6 - Demo 6
# ------------------------------------------------------------

# Function without parameter


# ------------------------------------------------------------
# PART 6 - Assignment 6
# ------------------------------------------------------------

# Create a function called say_goodbye.
# The function prints:
# Goodbye and good luck practicing!
#
# Then call the function.


# ============================================================
# PART 7 - FUNCTION WITH PARAMETER
# ============================================================

# A parameter is information that you give to a function.


# ------------------------------------------------------------
# PART 7 - Demo 7
# ------------------------------------------------------------

# Function with parameter


# ------------------------------------------------------------
# PART 7 - Assignment 7
# ------------------------------------------------------------

# Create a function called show_hobby.
# The function gets one parameter: hobby.
# The function prints:
# My hobby is ...
#
# Call the function twice with different hobbies.


# ============================================================
# PART 8 - FUNCTION WITH RETURN
# ============================================================

# With return, a function gives a value back.
# You can store or print that value afterwards.


# ------------------------------------------------------------
# PART 8 - Demo 8
# ------------------------------------------------------------

# Function with return


# ------------------------------------------------------------
# PART 8 - Assignment 8
# ------------------------------------------------------------

# Create a function called multiply_numbers.
# The function gets two parameters.
# The function returns the multiplication.
#
# Call the function with two numbers.
# Then print the result.


# ============================================================
# PART 9 - FUNCTION WITH LIST
# ============================================================

# You can also pass a list to a function.


# ------------------------------------------------------------
# PART 9 - Demo 9
# ------------------------------------------------------------

# Function that loops through a list


# ------------------------------------------------------------
# PART 9 - Common mistake
# ------------------------------------------------------------

# Changing the temporary loop variable does not change the original list.
#
# numbers = [1, 2, 3]
#
# for number in numbers:
#     number = number + 10
#
# print(numbers)
#
# This still prints:
# [1, 2, 3]
#
# number is only a temporary variable inside the loop.


# ------------------------------------------------------------
# PART 9 - Assignment 9
# ------------------------------------------------------------

# Create a function called print_foods.
# The function gets a list with foods.
# The function prints each food.
#
# Then create a list with three foods.
# Call the function with your list.


# ============================================================
# END
# ============================================================

# If you understand this, you can now:
# - use prior knowledge in one exercise
# - loop through lists
# - use for-loops
# - use while-loops
# - understand why infinite loops can happen
# - use range
# - loop through dictionaries
# - create functions
# - use parameters
# - use return
# - recognize common beginner mistakes
