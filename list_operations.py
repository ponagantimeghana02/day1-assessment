employees = [
    "Ajay",
    "Rahul",
    "Priya",
    "Kiran",
    "Sneha"
]

# Perform:
#  Add item 
#  Remove item 
#  Sort list 
#  Reverse list 
#  Find length 
employees.append("meghana")
print("after appending element",employees)
employees.remove("Kiran")
print("after removing a element ",employees)
employees.sort()
print("after sorting list elements",employees)
employees[::-1]
print("after reversing list elements",employees)
print("length of list",len(employees))