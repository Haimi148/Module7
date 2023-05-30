# This application allows users to search for student names, view their breakfast choices,
# and search for food to get nutrient information

# Student data
students = [
    ["name", "John Doe", "breakfast", "cereal"],
    ["name", "Jane Smith", "breakfast", "toast"],
    ["name", "Alex Johnson", "breakfast", "eggs"],
    ["name", "Sarah Davis", "breakfast", "yogurt"]
]

# Function to search for student names
def search_student(name):
    for student in students:
        if student[1].lower() == name.lower():
            return student
    return None

# Function to search for food and get nutrient information
def search_food(food):
    nutrients = {
        "cereal": ["calories", 120, "carbs", 25, "protein", 2, "fat", 1],
        "toast": ["calories", 80, "carbs", 15, "protein", 3, "fat", 1],
        "eggs": ["calories", 140, "carbs", 1, "protein", 13, "fat", 9],
        "yogurt": ["calories", 150, "carbs", 27, "protein", 6, "fat", 2]
    }
    food = food.lower()
    if food in nutrients:
        return nutrients[food]
    else:
        return None

# User input for student name
student_name = input("Enter student name: ")

# Search for student and display breakfast choice
student = search_student(student_name)
if student:
    print(f"{student[1]} had {student[3]} for breakfast.")
else:
    print("Student not found.")

# User input for food
food_name = input("Enter food name: ")

# Search for food and display nutrient information
food_info = search_food(food_name)
if food_info:
    print("Nutrient Information:")
    print(f"Calories: {food_info[1]}")
    print(f"Carbs: {food_info[3]}g")
    print(f"Protein: {food_info[5]}g")
    print(f"Fat: {food_info[7]}g")
else:
    print("Food not found.")