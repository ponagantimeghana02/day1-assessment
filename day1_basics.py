#Task1

# Printed in formatted output.

name="meghana"
age=21
email="meghana@gmail.com"
salary=25000.00

print(f"name is {name}")
print(f"age is {age}")
print(f"email is {email}")
print(f"salary is {salary}")

#printing DataTypes

boolean=False
firstNames=["Megha","Srivya","Niha"]
lastNames=("Ponaganti","Guntha","Adapa")
students={"Sanjana":2,"Thrisha":5}
salaries={10000,2000,4000}

print(type(name))
print(type(age))
print(type(salary))
print(type(boolean))
print(type(firstNames))
print(type(lastNames))
print(type(students))
print(type(salaries))

# Operators
num1=5
num2=2

print(f"sum of num1 and num2 is {num1+num2}")
print(f"subtraction of num1 and num2 is {num1-num2}")
print(f"multiplication of num1 and num2 is {num1*num2}")
print(f"division of num1 and num2 is {num1/num2}")
print(f"modulus of num1 and num2 is {num1%num2}")

# Take user age input and classify the age.

userAge=int(input("enter age of user:"))

if(userAge<18):
    print("Minor")
elif(userAge<60):
    print("Adult")
else:
    print("Senior Citizen")

#display 1 to 50 using for and while loops 

for i in range(1,51):
    print(i)

i=1
while(i<=50):
    print(i)
    i=i+1



