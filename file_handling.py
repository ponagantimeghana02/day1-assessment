#Task 6:
#  10 employee records to employees.txt is added and displayed.

with open("employees.txt", "w") as file:
    file.write("1, Ajay, AI, 50000\n")
    file.write("2, Priya, HR, 45000\n")
    file.write("3, Rahul, IT, 60000\n")
    file.write("4, Sneha, Finance, 55000\n")
    file.write("5, Kiran, Marketing, 48000\n")
    file.write("6, Meghana, FullStack, 50000\n")
    file.write("7, Arjun, DevOps, 62000\n")
    file.write("8, Anjali, Testing, 47000\n")
    file.write("9, Rohan, AI, 58000\n")
    file.write("10, Pooja, Support, 42000\n")

with open("employees.txt", "r") as file:
    content = file.read()
    print(content)