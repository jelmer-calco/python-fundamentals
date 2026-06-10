# ============================================================
# PYTHON TRAINING - PRACTICE AFTER FUNCTIONS - ANSWERS
# ============================================================


# ============================================================
# PART 1 - EDITING LISTS
# ============================================================

# Assignment 1

animals = ["dog", "cat"]
animals.append("rabbit")
print(animals)


# Assignment 2

cities = ["Utrecht", "Amsterdam", "Rotterdam"]
cities.remove("Amsterdam")
print(cities)


# Assignment 3

shopping_list = ["bread", "milk", "eggs", "apples"]
print("You have " + str(len(shopping_list)) + " items on your shopping list.")


# Assignment 4

friends = ["Mila", "Noah", "Sara"]
friends.append("Liam")
friends.remove("Noah")

print(friends)
print("You have " + str(len(friends)) + " friends in the list.")


# ============================================================
# PART 2 - EXPANDING AND UPDATING DICTIONARIES
# ============================================================

# Assignment 5

book = {
    "title": "Harry Potter",
    "author": "J.K. Rowling",
    "pages": 320
}

print(book["title"])


# Assignment 6

phone = {
    "brand": "Apple",
    "model": "iPhone 15",
    "price": 899
}

phone["price"] = 799
print(phone)


# Assignment 7

movie = {
    "title": "Finding Nemo",
    "year": 2003
}

movie["genre"] = "animation"
print(movie)


# Assignment 8

profile = {
    "name": "Mila",
    "age": 20,
    "city": "Utrecht"
}

profile["city"] = "Amsterdam"
profile["hobbies"] = ["coding", "cooking"]

print(profile)


# ============================================================
# PART 3 - FUNCTIONS WITH LISTS
# ============================================================

# Assignment 9

def print_animals(animals):
    for animal in animals:
        print(animal)

animals = ["dog", "cat", "rabbit"]
print_animals(animals)


# Assignment 10

def count_items(items):
    return len(items)

items = ["pen", "book", "laptop", "phone"]
result = count_items(items)

print(result)


# Assignment 11

def show_passed_grades(grades):
    for grade in grades:
        if grade >= 6:
            print("Passed: " + str(grade))

grades = [4, 6, 8, 5, 9]
show_passed_grades(grades)


# ============================================================
# PART 4 - FUNCTIONS WITH DICTIONARIES
# ============================================================

# Assignment 12

def show_movie(movie):
    print("Title: " + movie["title"])
    print("Year: " + str(movie["year"]))
    print("Genre: " + movie["genre"])

movie = {
    "title": "The Lion King",
    "year": 1994,
    "genre": "animation"
}

show_movie(movie)


# Assignment 13

def update_score(player):
    player["score"] = player["score"] + 10

player = {
    "name": "Mila",
    "score": 50
}

update_score(player)
print(player)


# Assignment 14

def print_profile(profile):
    print("Name: " + profile["name"])
    print("Age: " + str(profile["age"]))

    for hobby in profile["hobbies"]:
        print("Hobby: " + hobby)

profile = {
    "name": "Noah",
    "age": 22,
    "hobbies": ["gaming", "running", "coding"]
}

print_profile(profile)


# ============================================================
# PART 5 - INPUT
# ============================================================

# Assignment 15

name = input("What is your name? ")
print("Welcome, " + name)


# Assignment 16

age = int(input("What is your age? "))

if age >= 18:
    print("You are an adult")
else:
    print("You are underage")


# Assignment 17

hobbies = []
hobby = input("What is your hobby? ")

hobbies.append(hobby)
print(hobbies)


# Assignment 18

def greet_user(name):
    print("Hello, " + name)

name = input("What is your name? ")
greet_user(name)


# Assignment 19

user = {}

name = input("What is your name? ")
city = input("Where do you live? ")

user["name"] = name
user["city"] = city

print(user)


# ============================================================
# EXTRA CHALLENGE
# ============================================================

tasks = []

task_1 = input("Enter task 1: ")
task_2 = input("Enter task 2: ")
task_3 = input("Enter task 3: ")

tasks.append(task_1)
tasks.append(task_2)
tasks.append(task_3)

print("You have " + str(len(tasks)) + " tasks:")

for task in tasks:
    print(task)
