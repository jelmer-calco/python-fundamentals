# ============================================================
# PYTHON TRAINING - REVIEW AND BUILDING TOWARDS FUNCTIONS
# ============================================================


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


# ------------------------------------------------------------
# REVIEW EXERCISE - Demo
# ------------------------------------------------------------


name = "Mila"
age = 20

# List
hobbies = ["coding", "traveling", "cooking"]


# Dictionary
student = {
    # "naam van het vakje": waarde_die_erin_komt
    # key : value 
    "name": name,
    "age": age,
    "hobbies": hobbies,
}

# index starts at 0, so the first item is index 0
print(hobbies[0])  # print first hobby
print(student["name"])  # print name from dictionary


# ------------------------------------------------------------
# REVIEW EXERCISE - Assignment
# ------------------------------------------------------------

# Create:
# 1. A variable for a name
# 2. A variable for an age
# 3. A list with three hobbies
# 4. A dictionary with name, age and city
# 5. Print the name from the dictionary
# 6. Print the first hobby
# 7. Use if/else to check whether the person is 18 or older

person_name = "Sam"
person_age = 17
person_hobbies = ["gaming", "football", "reading"]

person = {
    "name": person_name,
    "age": person_age,
    "city": "Utrecht"
}

print(person["name"])
print(person_hobbies[0])

if person_age >= 18:
    print("This person is 18 or older")
else:
    print("This person is under 18")


# ============================================================
# PART 2 - NEW TOPIC: FOR LOOPS
# ============================================================

# A for-loop is used when you want to loop over multiple items.
# For example, over all names in a list.


# ------------------------------------------------------------
# Demo 1 - For-loop with a list
# ------------------------------------------------------------

names = ["Mila", "Sam", "Noah"]

for name in names:
    print("Hello", name)


# ------------------------------------------------------------
# Assignment 1
# ------------------------------------------------------------

# Create a list with three favorite foods.
# Use a for-loop to print each food.
# Example:
# My favorite food is pizza

favorite_foods = ["pizza", "sushi", "pasta"]

for food in favorite_foods:
    print("My favorite food is", food)


# ============================================================
# PART 3 - FOR LOOP WITH IF/ELSE
# ============================================================

# You can combine a for-loop with if/else.
# This lets you check each item in a list.


# ------------------------------------------------------------
# Demo 2 - For-loop with grades
# ------------------------------------------------------------

grades = [4, 7, 8, 5, 10]

for grade in grades:
    if grade >= 6:
        print(grade, "is a pass")
    else:
        print(grade, "is a fail")


# ------------------------------------------------------------
# Assignment 2
# ------------------------------------------------------------

# Create a list with ages.
# Loop over the ages.
# Print for each age whether the person is an adult or not.
#
# Example:
# 16 is underage
# 21 is an adult

ages = [12, 16, 18, 21, 35]

for age in ages:
    if age >= 18:
        print(age, "is an adult")
    else:
        print(age, "is underage")


# ============================================================
# PART 4 - RANGE
# ============================================================

# range() is used when you want to repeat something a number of times.
# range(5) means: 0, 1, 2, 3, 4


# ------------------------------------------------------------
# Demo 3 - Using range
# ------------------------------------------------------------

for number in range(5):
    print(number)


# ------------------------------------------------------------
# Demo 4 - Range with start and stop
# ------------------------------------------------------------

for number in range(1, 6):
    print(number)


# ------------------------------------------------------------
# Assignment 3
# ------------------------------------------------------------

# Use range to print the numbers 1 to 10.

for number in range(1, 11):
    print(number)


# ============================================================
# PART 5 - LOOPING THROUGH A DICTIONARY
# ============================================================

# A dictionary has keys and values.
# With .items() you can loop through both at the same time.


# ------------------------------------------------------------
# Demo 5 - Dictionary with .items()
# ------------------------------------------------------------

student = {
    "name": "Mila",
    "age": 20,
    "city": "Amsterdam"
}

for key, value in student.items():
    print(key, ":", value)


# ------------------------------------------------------------
# Assignment 4
# ------------------------------------------------------------

# Create a dictionary for a movie.
# Use these keys:
# - title
# - year
# - genre
#
# Then use a for-loop with .items()
# to print all information clearly.

movie = {
    "title": "Finding Nemo",
    "year": 2003,
    "genre": "Animation"
}

for key, value in movie.items():
    print(key, ":", value)


# ============================================================
# PART 6 - FUNCTIONS
# ============================================================

# A function is a piece of code that you can reuse.
# You create a function with def.


# ------------------------------------------------------------
# Demo 6 - Function without parameter
# ------------------------------------------------------------

def say_hello():
    print("Hello!")
    print("Welcome to Python training!")

say_hello()


# ------------------------------------------------------------
# Assignment 5
# ------------------------------------------------------------

# Create a function called say_goodbye.
# The function prints:
# Goodbye and good luck practicing!
#
# Then call the function.

def say_goodbye():
    print("Goodbye and good luck practicing!")

say_goodbye()


# ============================================================
# PART 7 - FUNCTION WITH PARAMETER
# ============================================================

# A parameter is information that you give to a function.


# ------------------------------------------------------------
# Demo 7 - Function with parameter
# ------------------------------------------------------------

def greet_person(name):
    print("Hello", name)

greet_person("Mila")
greet_person("Sam")


# ------------------------------------------------------------
# Assignment 6
# ------------------------------------------------------------

# Create a function called show_hobby.
# The function gets one parameter: hobby.
# The function prints:
# My hobby is ...
#
# Call the function twice with different hobbies.

def show_hobby(hobby):
    print("My hobby is", hobby)

show_hobby("coding")
show_hobby("football")


# ============================================================
# PART 8 - FUNCTION WITH RETURN
# ============================================================

# With return, a function gives a value back.
# You can store or print that value afterwards.


# ------------------------------------------------------------
# Demo 8 - Function with return
# ------------------------------------------------------------

def add_numbers(number1, number2):
    result = number1 + number2
    return result

answer = add_numbers(3, 5)
print(answer)


# ------------------------------------------------------------
# Assignment 7
# ------------------------------------------------------------

# Create a function called multiply_numbers.
# The function gets two parameters.
# The function returns the multiplication.
#
# Call the function with two numbers.
# Then print the result.

def multiply_numbers(number1, number2):
    result = number1 * number2
    return result

multiplication_result = multiply_numbers(4, 6)
print(multiplication_result)


# ============================================================
# PART 9 - FUNCTION WITH LIST
# ============================================================

# You can also pass a list to a function.


# ------------------------------------------------------------
# Demo 9 - Function that loops through a list
# ------------------------------------------------------------

def print_names(names):
    for name in names:
        print("Name:", name)

students = ["Mila", "Sam", "Noah"]
print_names(students)


# ------------------------------------------------------------
# Assignment 8
# ------------------------------------------------------------

# Create a function called print_foods.
# The function gets a list with foods.
# The function prints each food.
#
# Then create a list with three foods.
# Call the function with your list.

def print_foods(foods):
    for food in foods:
        print("Food:", food)

foods = ["pizza", "sushi", "pasta"]
print_foods(foods)


# ============================================================
# END
# ============================================================

# If you understand this, you can now:
# - use prior knowledge in one exercise
# - loop through lists
# - use range
# - loop through dictionaries
# - create functions
# - use parameters
# - use return