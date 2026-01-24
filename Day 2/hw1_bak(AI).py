#Build a CLI User Manager:
#Add user(name, age)
#List all user
#Persist data to users.json
#Load existing users on start

import json
import os
import argparse
USER_DATA_FILE = 'users.json'
users = []
def load_users():
    global users
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            users = json.load(f)
def save_users():
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(users, f)
def add_user(name, age):
    users.append({'name': name, 'age': age})
    save_users()
    print(f"User {name} added.")
def list_users():
    if not users:
        print("No users found.")
    else:
        for user in users:
            print(f"Name: {user['name']}, Age: {user['age']}")
def main():
    parser = argparse.ArgumentParser(description="User Manager CLI")
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new user')
    add_parser.add_argument('name', type=str, help='Name of the user')
    add_parser.add_argument('age', type=int, help='Age of the user')

    list_parser = subparsers.add_parser('list', help='List all users')

    args = parser.parse_args()
    load_users()

    if args.command == 'add':
        add_user(args.name, args.age)
    elif args.command == 'list':
        list_users()
    else:
        parser.print_help()
if __name__ == "__main__":
    main()
# CLI User Manager
# Add user(name, age)
# List all users
# Persist data to users.json
# Load existing users on start
# Usage:
# python hw1.py add John 30
# python hw1.py list
