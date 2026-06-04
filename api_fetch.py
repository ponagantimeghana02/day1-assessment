#Task 8:

# Fetch data using requests library.

import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")

userDetails = response.json()

for userInfo in userDetails:
    print("Name:", userInfo["name"])
    print("Email:", userInfo["email"])
    print("Company:", userInfo["company"]["name"])
    print("_"*30)
    