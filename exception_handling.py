# Task 7:
# Exceptional Handling

#ZeroDivisionError
try:
    num1=int(input("enter num1: "))
    num2=int(input("enter num2: "))
    print("dividing num1 by num2: ",num1/num2)
except ZeroDivisionError:
    print("Zero Division Error Occurred")
finally:
    print("Program Executed Successfully")

#ValueError
try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)

except ValueError:
    print("Value Error: Please enter a valid integer.")
finally:
    print("Program Executed Successfully")

#FileNotFoundError
try:
    with open("employee.txt","r" ) as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("File Not Found Error Occurred")
finally:
    print("Program Executed Successfully")




    


