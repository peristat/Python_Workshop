#! /usr/bin python3.12

#Build a CLI User Manager:
#Add user(name, age)
#List all user
#Persist data to users.json
#Load existing users on start

import json 
import sys as s
import os as o

file_name = "all_user_data.json"
all_user_profile = []

def load_user():
    global all_user_profile
    if o.path.exists(file_name):
        with open(file_name,"r") as f:
            all_user_profile = json.load(f)


def add(user_profile):

    all_user_profile.append(user_profile)
    with open(file_name,"w") as f:
        json.dump(all_user_profile,f,indent=4)

def list():

    if not all_user_profile:
        print("No users found.")
        return
    for  user_profile in all_user_profile:
        print(f"Name:{user_profile["name"]}")
        print(f"Age: {user_profile["age"]}")

def usage():
    print("Usage Information")
    print("To Add User: python hw1.py add <name> <age>")
    print("To List Users: python hw1.py list")


def main():

    load_user()
    try:    
        if s.argv[1] == "add":
            user_profile ={
                "name": s.argv[2] ,
                "age" : int(s.argv[3])
            }
            add(user_profile)
            print(f"{user_profile["name"]} Added Successfully")
        elif s.argv[1] == "list":
            list()
        elif s.argv[1] == "help" or s.argv[1] == "-h":
            usage()
        else:
            usage()
    except ValueError:
        usage()
        print("Age must be a number")
    except IndexError:
        usage()
        print("Missing Arguments")
    except Exception as e:
        print(f"Exception Occurred:{e}")


if __name__ == "__main__":
    main()
