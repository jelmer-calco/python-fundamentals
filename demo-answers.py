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


# A variable stores a value.
# Here, name stores the string "mila".
# A string is text.
name = "mila"

# Here, age stores the number 20.
age = 20 


# ------------------------------------------------------------
# PART 1 - Demo 1
# ------------------------------------------------------------

name = "Mila"
age = 20

# A list stores multiple values in one variable.
# This is useful when several values belong together.
# For example: hobbies, names, foods or grades.
hobbies = ["coding", "traveling", "cooking"]

# A dictionary stores data with keys and values.
#
# The key is the label.
# The value is the information.
#
# Example:
# "name" is the key.
# name is the value, which contains "Mila".
#
# A dictionary is useful when multiple pieces of information
# belong to one thing.
# Here, the name, age and hobbies all belong to one student.
student = {
    # "naam van het vakje": waarde_die_erin_komt
    # key : value 
    "name": name,
    "age": age,
    "hobbies": hobbies,
}

# index starts at 0, so the first item is index 0
print(hobbies[0])  # print first hobby

# With a dictionary, you use the key to get the value.
print(student["name"])  # print name from dictionary

# This prints the complete dictionary.
print(student)


# ------------------------------------------------------------
# PART 1 - Common mistakes
# ------------------------------------------------------------

# Mistake 1: List index does not exist

hobbies = ["coding", "traveling", "cooking"]

# This works:
print(hobbies[0])
print(hobbies[1])
print(hobbies[2])

# This does not work:
# print(hobbies[3])
#
# This gives an error.
# The list has 3 items, but the indexes are 0, 1 and 2.
# Index 3 does not exist.


# Mistake 2: Dictionary key does not exist

student = {
    "name": "Mila",
    "age": 20
}

# This works:
print(student["name"])

# This does not work:
# print(student["city"])
#
# This gives an error.
# The key "city" does not exist in the dictionary.


# Mistake 3: = is not the same as ==

age = 20

# This works:
if age == 20:
    print("Age is 20")

# This does not work:
# if age = 20:
#     print("Age is 20")
#
# = is used to store a value.
# == is used to compare two values.
#
# age = 20 means: put 20 inside age.
# age == 20 means: check if age is equal to 20.


# Mistake 4: Indentation matters

age = 20

# This works:
if age >= 18:
    print("Adult")

# This does not work:
# if age >= 18:
# print("Adult")
#
# This gives an error.
# Python uses indentation to know what belongs inside an if-statement,
# loop or function.


# ------------------------------------------------------------
# PART 1 - Assignment 1
# ------------------------------------------------------------

# Create:
# 1. A variable for a name
person_name = "Sam"

# 2. A variable for an age
person_age = 17

# 3. A list with three hobbies
person_hobbies = ["gaming", "football", "reading"]

# 4. A dictionary with name, age and city
#
# This dictionary stores information about one person.
# The name, age and city belong together.
person = {
    "name": person_name,
    "age": person_age,
    "city": "Utrecht"
}

# 5. Print the name from the dictionary
print(person["name"])

# 6. Print the first hobby
print(person_hobbies[0])

# 7. Use if/else to check whether the person is 18 or older
#
# if/else is used to make a decision.
# If the condition is True, the first print runs.
# Otherwise, the else part runs.
if person_age >= 18:
    print("This person is 18 or older")
else:
    print("This person is under 18")


# ============================================================
# PART 2 - NEW TOPIC: FOR LOOPS
# ============================================================

# A for-loop is used when you want to loop over multiple items.
# For example, over all names in a list.
#
# A for-loop is useful because you do not have to repeat yourself.
# Instead of writing three print statements, you can use one loop.


# ------------------------------------------------------------
# PART 2 - Demo 2
# ------------------------------------------------------------

# For-loop with a list

names = ["Mila", "Sam", "Noah"]

# The loop goes through the list one item at a time.
# First name is "Mila".
# Then name is "Sam".
# Then name is "Noah".
for name in names:
    print("Hello", name)


# ------------------------------------------------------------
# PART 2 - Assignment 2
# ------------------------------------------------------------

# Create a list with three favorite foods.
# Use a for-loop to print each food.
# Example:
# My favorite food is pizza

favorite_foods = ["pizza", "sushi", "pasta"]

# This loop prints every food in the list.
for food in favorite_foods:
    print("My favorite food is", food)


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

grades = [4, 7, 8, 5, 10]

# This for-loop checks every grade in the list.
# If the grade is 6 or higher, it is a pass.
# Otherwise, it is a fail.
for grade in grades:
    if grade >= 6:
        print(grade, "is a pass")
    else:
        print(grade, "is a fail")


# ------------------------------------------------------------
# PART 3 - Demo 3B
# ------------------------------------------------------------

# While-loop that stops

# A while-loop keeps running while the condition is True.
# Here, the loop runs while number is lower than or equal to 5.
number = 1

while number <= 5:
    print(number)

    # This line is very important.
    # It increases number by 1.
    # Because of this, the condition will eventually become False.
    number = number + 1

# What happens:
# number is 1, print 1
# number becomes 2, print 2
# number becomes 3, print 3
# number becomes 4, print 4
# number becomes 5, print 5
# number becomes 6, condition is False, loop stops


# ------------------------------------------------------------
# PART 3 - Demo 3C
# ------------------------------------------------------------

# Infinite while-loop example
#
# Do not run this code.
# This code is commented out on purpose.
#
# number = 1
#
# while number <= 5:
#     print(number)
#
# This loop never stops because number stays 1 forever.
#
# The condition number <= 5 is always True.
# That is why this becomes an infinite loop.
#
# To fix it, you need to change number inside the loop:
#
# number = 1
#
# while number <= 5:
#     print(number)
#     number = number + 1


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

ages = [12, 16, 18, 21, 35]

# This for-loop checks every age in the list.
for age in ages:
    if age >= 18:
        print(age, "is an adult")
    else:
        print(age, "is underage")

# This while-loop prints the numbers 1 to 3.
counter = 1

while counter <= 3:
    print(counter)

    # This makes sure the loop stops.
    # Without this line, counter would always stay 1.
    counter = counter + 1


# ============================================================
# PART 4 - RANGE
# ============================================================

# range() is used when you want to repeat something a number of times.
# range(5) means: 0, 1, 2, 3, 4
#
# Important:
# The stop number is not included.
#
# So range(5) stops before 5.


# ------------------------------------------------------------
# PART 4 - Demo 4
# ------------------------------------------------------------

# Using range

for number in range(5):
    print(number)

# This prints:
# 0
# 1
# 2
# 3
# 4


# Range with start and stop

for number in range(1, 6):
    print(number)

# This prints:
# 1
# 2
# 3
# 4
# 5
#
# The stop number 6 is not included.


# ------------------------------------------------------------
# PART 4 - Common mistake
# ------------------------------------------------------------

# The stop number is not included.

for number in range(1, 6):
    print(number)

# Many beginners expect this to print 1 to 6.
# But it prints 1 to 5.
#
# range(1, 6) starts at 1 and stops before 6.


# ------------------------------------------------------------
# PART 4 - Assignment 4
# ------------------------------------------------------------

# Use range to print the numbers 1 to 10.

# We use range(1, 11), because the stop number is not included.
for number in range(1, 11):
    print(number)


# ============================================================
# PART 5 - LOOPING THROUGH A DICTIONARY
# ============================================================

# A dictionary has keys and values.
#
# Example:
# "name" is a key.
# "Mila" is a value.
#
# With .items() you can loop through both at the same time.
#
# This is useful when you want to print all information
# from a dictionary without writing every key separately.


# ------------------------------------------------------------
# PART 5 - Demo 5
# ------------------------------------------------------------

# Dictionary with .items()

student = {
    "name": "Mila",
    "age": 20,
    "city": "Amsterdam"
}

# .items() gives us both the key and the value.
for key, value in student.items():
    print(key, ":", value)


# ------------------------------------------------------------
# PART 5 - Common mistake
# ------------------------------------------------------------

# If you ask for a key that does not exist, Python gives an error.

movie = {
    "title": "Finding Nemo",
    "year": 2003
}

# This works:
print(movie["title"])

# This does not work:
# print(movie["genre"])
#
# The key "genre" does not exist here.
# You can only use keys that are inside the dictionary.


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

# This dictionary stores information about one movie.
# The title, year and genre belong together.
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
#
# A function is useful when you want to use the same code
# multiple times without writing it again.


# ------------------------------------------------------------
# PART 6 - Demo 6
# ------------------------------------------------------------

# Function without parameter

def say_hello():
    print("Hello!")
    print("Welcome to Python training!")

# This calls the function.
# The code inside the function now runs.
say_hello()


# ------------------------------------------------------------
# PART 6 - Common mistake
# ------------------------------------------------------------

# Creating a function is not the same as calling a function.

def say_hi():
    print("Hi!")

# If we only create the function, nothing is printed yet.
# To run the function, we must call it.

say_hi()


# ------------------------------------------------------------
# PART 6 - Assignment 6
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
#
# A parameter makes a function more flexible.
# The function can do the same action with different information.


# ------------------------------------------------------------
# PART 7 - Demo 7
# ------------------------------------------------------------

# Function with parameter

# name is a parameter.
def greet_person(name):
    print("Hello", name)

greet_person("Mila")
greet_person("Sam")


# ------------------------------------------------------------
# PART 7 - Common mistake
# ------------------------------------------------------------

# A parameter only exists inside the function.

def greet_student(student_name):
    print("Hello", student_name)

greet_student("Noah")

# This does not work:
# print(student_name)
#
# student_name only exists inside the function.
# Outside the function, Python does not know that variable.


# ------------------------------------------------------------
# PART 7 - Assignment 7
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
#
# print() only shows something on the screen.
# return gives a value back to the rest of your program.
#
# return is useful when you want to use the result later.


# ------------------------------------------------------------
# PART 8 - Demo 8
# ------------------------------------------------------------

# Function with return

def add_numbers(number1, number2):
    result = number1 + number2
    return result

# The returned value is stored in answer.
answer = add_numbers(3, 5)
print(answer)


# ------------------------------------------------------------
# PART 8 - Common mistake
# ------------------------------------------------------------

# print() is not the same as return.

def print_numbers(number1, number2):
    print(number1 + number2)

wrong_answer = print_numbers(3, 5)
print(wrong_answer)

# This prints 8 first.
# But then it prints None.
#
# Why?
# The function prints the answer,
# but it does not return the answer.
#
# If you want to store the result in a variable,
# use return.

def return_numbers(number1, number2):
    return number1 + number2

right_answer = return_numbers(3, 5)
print(right_answer)


# ------------------------------------------------------------
# PART 8 - Assignment 8
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
#
# This is useful when a function needs to work with multiple values.
# For example:
# - a list of names
# - a list of foods
# - a list of grades


# ------------------------------------------------------------
# PART 9 - Demo 9
# ------------------------------------------------------------

# Function that loops through a list

def print_names(names):
    for name in names:
        print("Name:", name)

students = ["Mila", "Sam", "Noah"]
print_names(students)


# ------------------------------------------------------------
# PART 9 - Common mistake
# ------------------------------------------------------------

# Changing the temporary loop variable does not change the original list.

numbers = [1, 2, 3]

for number in numbers:
    number = number + 10

print(numbers)

# This still prints:
# [1, 2, 3]
#
# Why?
# number is only a temporary variable inside the loop.
# Changing number does not change the original list.


# ------------------------------------------------------------
# PART 9 - Assignment 9
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
# - use for-loops
# - use while-loops
# - understand why infinite loops can happen
# - use range
# - loop through dictionaries
# - create functions
# - use parameters
# - use return
# - recognize common beginner mistakes
#
# Most important ideas:
#
# A variable stores one value.
# A list stores multiple values.
# A dictionary stores information with clear labels: keys and values.
# A for-loop repeats code for every item in a list or range.
# A while-loop repeats code as long as a condition is True.
# An infinite loop happens when the condition never becomes False.
# range() stops before the stop number.
# A function stores reusable code.
# A parameter gives information to a function.
# A parameter usually only exists inside the function.
# print() shows something on the screen.
# return gives a value back from a function.
