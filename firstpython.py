# This application stores and uses data with variables

# Variable names are descriptive
//UNOFFICAl CODE    
//REAL CODE on data.py


name = "John Doe"
age = 25
is_student = True

# Decision structure
if is_student:
    print(f"{name} is a student.")
else:
    print(f"{name} is not a student.")

# Repetition structure
for i in range(3):
    print(f"Count: {i}")

# Called function
def greet_person(name):
    print(f"Hello, {name}!")

greet_person(name)

# Collection of data sequences
fruits = ["apple", "banana", "orange"]

# Iterated list with accessed and used elements
for fruit in fruits:
    print(f"Today I ate a {fruit}.")

