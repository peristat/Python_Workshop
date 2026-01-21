#Modify the mini-program to store 3 user in a list of disctonaries 
# and save to a json file "all_users.json"

import json

all_users = []

for _i in range(3):
    name = input("Enter the name: ")
    age = input("Enter the age: ")

    user_profile = {
        "name": name,
        "age" : age
    }

    all_users.append(user_profile)

file_name = "all_users.json"
with open(file_name,"w") as f:
    json.dump(all_users,f,indent=4)
print(f"The Record are save to {file_name}")