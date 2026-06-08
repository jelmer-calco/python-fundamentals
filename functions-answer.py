# Startlijst met studenten.
# Elke student is een dictionary met een naam, leeftijd en active-status.
students = [
    {"name": "Anna", "age": 20, "active": True},
    {"name": "Bram", "age": 22, "active": True},
    {"name": "Carlos", "age": 21, "active": False},
]


# Deze functie toont alle studenten netjes onder elkaar.
# De functie krijgt de studentenlijst mee als parameter.
def show_students(student_list):
    print("----- STUDENTS -----")

    # Loop door alle studenten heen.
    # enumerate geeft zowel het indexnummer als de student zelf.
    for index, student in enumerate(student_list):
        name = student["name"]
        age = student["age"]
        active = student["active"]

        # Zet de boolean True/False om naar leesbare tekst.
        if active:
            status = "active"
        else:
            status = "inactive"

        # Maak één nette regel per student.
        row = f"{index + 1}. {name} - {age} years old - {status}"
        print(row)

    print("--------------------")


# Deze functie vraagt om een studentnummer.
# Omdat lijsten bij 0 beginnen, halen we er 1 vanaf.
def get_student_index():
    number = int(input("Student number: "))
    index = number - 1
    return index


# Hoofdprogramma.
# Deze loop blijft draaien totdat de gebruiker exit typt.
while True:
    user_action = input("Type show, add, edit, deactivate or exit: ")
    user_action = user_action.strip()

    # Toon de studentenlijst.
    if user_action.startswith("show"):
        show_students(students)

    # Voeg een nieuwe student toe aan de lijst.
    elif user_action.startswith("add"):
        name = input("Name: ")
        age = int(input("Age: "))

        student = {
            "name": name,
            "age": age,
            "active": True,
        }

        students.append(student)

        # Toon de aangepaste lijst.
        show_students(students)

    # Pas de naam en leeftijd van een bestaande student aan.
    elif user_action.startswith("edit"):
        index = get_student_index()

        name = input("New name: ")
        age = int(input("New age: "))

        students[index]["name"] = name
        students[index]["age"] = age

        # Toon de aangepaste lijst.
        show_students(students)

    # Zet een student op inactive.
    elif user_action.startswith("deactivate"):
        index = get_student_index()

        students[index]["active"] = False

        # Toon de aangepaste lijst.
        show_students(students)

    # Stop het programma.
    elif user_action.startswith("exit"):
        break

    # Als de gebruiker iets anders typt.
    else:
        print("Command is not valid.")

print("Bye!")