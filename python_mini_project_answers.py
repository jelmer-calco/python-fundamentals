# ============================================================
# PYTHON MINI PROJECT - STUDENT MANAGER - ANSWERS
# ============================================================


# ============================================================
# PART 1 - CREATE ONE STUDENT
# ============================================================

# This is the simple version for assignment 1.
# You can comment this part out when you continue with the full project.

# student = {}
#
# name = input("What is the student's name? ")
# age = int(input("What is the student's age? "))
# city = input("What city does the student live in? ")
#
# student["name"] = name
# student["age"] = age
# student["city"] = city
#
# print(student)


# ============================================================
# PART 2 - CREATE A FUNCTION
# ============================================================

def create_student():
    student = {}

    name = input("What is the student's name? ")
    age = int(input("What is the student's age? "))
    city = input("What city does the student live in? ")

    student["name"] = name
    student["age"] = age
    student["city"] = city

    return student


# ============================================================
# PART 3 - STORE MULTIPLE STUDENTS
# ============================================================

students = []

student_1 = create_student()
students.append(student_1)

student_2 = create_student()
students.append(student_2)

student_3 = create_student()
students.append(student_3)


# ============================================================
# PART 4 - SHOW STUDENTS CLEARLY
# ============================================================

def show_students(students):
    for student in students:
        print("Name: " + student["name"])
        print("Age: " + str(student["age"]))
        print("City: " + student["city"])
        print("----------")


show_students(students)


# ============================================================
# PART 5 - CHECK ADULT OR UNDERAGE
# ============================================================

def check_age(student):
    if student["age"] >= 18:
        print(student["name"] + " is an adult")
    else:
        print(student["name"] + " is underage")


for student in students:
    check_age(student)


# ============================================================
# PART 6 - EXTRA CHALLENGE
# ============================================================

def count_adults(students):
    total = 0

    for student in students:
        if student["age"] >= 18:
            total = total + 1

    return total


number_of_adults = count_adults(students)
print("Number of adult students: " + str(number_of_adults))
