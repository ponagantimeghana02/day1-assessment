# Task 1

# Formatted Output
user_name = "Meghana"
user_age = 21
user_email = "meghana@gmail.com"
monthly_salary = 25000.00

print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"Email: {user_email}")
print(f"Salary: {monthly_salary}")

# Data Types
is_active = False
first_names = ["Megha", "Srivya", "Niha"]
last_names = ("Ponaganti", "Guntha", "Adapa")
student_marks = {"Sanjana": 2, "Thrisha": 5}
salary_set = {10000, 2000, 4000}

print(type(user_name))
print(type(user_age))
print(type(monthly_salary))
print(type(is_active))
print(type(first_names))
print(type(last_names))
print(type(student_marks))
print(type(salary_set))

# Operators
first_number = 5
second_number = 2

print(f"Addition: {first_number + second_number}")
print(f"Subtraction: {first_number - second_number}")
print(f"Multiplication: {first_number * second_number}")
print(f"Division: {first_number / second_number}")
print(f"Modulus: {first_number % second_number}")

# Age Classification
try:
    entered_age = int(input("Enter age of user: "))
    if entered_age < 18:
        print("Minor")
    elif entered_age < 60:
        print("Adult")
    else:
        print("Senior Citizen")
except ValueError:
    print("ValueError Occurred provide valid age")

    
# Display 1 to 50 using for loop
for number in range(1, 51):
    print(number)

# Display 1 to 50 using while loop
current_number = 1
while current_number <= 50:
    print(current_number)
    current_number += 1