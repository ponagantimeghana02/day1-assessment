Task 4:
# Perform:
#  Add key 
#  Update key 
#  Delete key 
#  Iterate all values

employee = {
    "id":1,
    "name":"Ajay",
    "department":"AI",
    "salary":50000
}

employee["age"]=30
print("after adding key",employee)
employee["salary"]=60000
print("after updating element",employee)
del employee["department"]
print("after deleting key",employee)
print("all values are")
for value in employee.values():
    print(value)
