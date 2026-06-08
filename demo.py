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

student_name = "Lina"
student_age = 28
student_education = "Calco"

# List
subjects = ["Python", "Data cruncher", "Ask like a detective"]

# Dictionary
student = {
    "name": student_name,
    "age": student_age,
    "education": student_education
}

print("Student:", student["name"])
print("Education:", student["education"])
# index starts at 0, so the first item is index 0
print("First subject:", subjects[0])

if student_age >= 18:
    print(student_name, "is an adult")
else:
    print(student_name, "is not 18 yet")



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


# ============================================================
# PART 2 - NEW TOPIC: FOR LOOPS
# ============================================================

# A for-loop is used when you want to loop over multiple items.
# For example, over all names in a list.


# ------------------------------------------------------------
# Demo 1 - For-loop with a list
# ------------------------------------------------------------

student_names = ["Ali", "Sara", "Noah", "Emma"]

for student_name in student_names:
    print("Welcome", student_name)


# ------------------------------------------------------------
# Assignment 1
# ------------------------------------------------------------

# Create a list with three favorite foods.
# Use a for-loop to print each food.
# Example:
# My favorite food is pizza


# ============================================================
# PART 3 - FOR LOOP WITH IF/ELSE
# ============================================================

# You can combine a for-loop with if/else.
# This lets you check each item in a list.


# ------------------------------------------------------------
# Demo 2 - For-loop with grades
# ------------------------------------------------------------

grades = [4, 7, 8, 5, 9]

for grade in grades:
    if grade >= 6:
        print(grade, "is a passing grade")
    else:
        print(grade, "is a failing grade")


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


# ============================================================
# PART 4 - RANGE
# ============================================================

# range() is used when you want to repeat something a number of times.
# range(5) means: 0, 1, 2, 3, 4


# ------------------------------------------------------------
# Demo 3 - Using range
# ------------------------------------------------------------

for number in range(5):
    print("This is round", number)


# ------------------------------------------------------------
# Demo 4 - Range with start and stop
# ------------------------------------------------------------

for number in range(1, 6):
    print("This is round", number)


# ------------------------------------------------------------
# Assignment 3
# ------------------------------------------------------------

# Use range to print the numbers 1 to 10.


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
    "education": "ICT"
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


# ============================================================
# PART 6 - FUNCTIONS
# ============================================================

# A function is a piece of code that you can reuse.
# You create a function with def.


# ------------------------------------------------------------
# Demo 6 - Function without parameter
# ------------------------------------------------------------

def say_hello():
    print("Hello, welcome to the lesson!")


say_hello()


# ------------------------------------------------------------
# Assignment 5
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
# Demo 7 - Function with parameter
# ------------------------------------------------------------

def greet_student(student_name):
    print("Welcome", student_name)


greet_student("Ali")
greet_student("Sara")


# ------------------------------------------------------------
# Assignment 6
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
# Demo 8 - Function with return
# ------------------------------------------------------------

def add_numbers(number_1, number_2):
    result = number_1 + number_2
    return result


answer = add_numbers(4, 6)

print("The answer is:", answer)


# ------------------------------------------------------------
# Assignment 7
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
# Demo 9 - Function that loops through a list
# ------------------------------------------------------------

def print_student_names(student_names):
    for student_name in student_names:
        print("Student:", student_name)


student_names = ["Lina", "Mo", "Sven"]

print_student_names(student_names)


# ------------------------------------------------------------
# Assignment 8
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
# - use range
# - loop through dictionaries
# - create functions
# - use parameters
# - use return