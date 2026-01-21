import json

name = input("Enter your name:  ")
age = input("Enter your age: ")

user_profile = {
    "name": name,
    "age": int(age)
}

file_name = "user_profiles.json"
with open(file_name,"w") as f:
    json.dump(user_profile, f, indent=4)


print(f"User data for {name} saved successfully to {file_name}")