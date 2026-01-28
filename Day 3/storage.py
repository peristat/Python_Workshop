import json

def save_users(users_data, filename="users.json"):
    with open(filename, "w") as f:
        json.dump(users_data, f, indent=4)

def load_users(filename="users.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


