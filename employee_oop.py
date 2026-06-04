#Task 5:
#OOPs Basics

class Employee:
    def __init__(self,id,name,department,salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary

    def display_details(self):
        print(f"Id: {self.id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

    def annual_salary(self):
        return self.salary * 12

emp1 = Employee(1, "Meghana", "FullStack", 50000)
emp2 = Employee(2, "Priya", "HR", 45000)
emp3 = Employee(3, "Ajay", "AI", 60000)

for emp in [emp1, emp2, emp3]:
    emp.display_details()
    print("Annual Salary:", emp.annual_salary())

         
