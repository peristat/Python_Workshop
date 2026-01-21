#Write script to read the all_user.json file and print details of the user.
import json

file_name = "all_users.json"

with open(file_name,"r") as f:
    all_users = json.load(f)

for user_profile in all_users:
    print(f"Name: {user_profile['name']}")    
    print(f"Age: {user_profile['age']}")
