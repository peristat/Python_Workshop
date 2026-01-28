from storage import save_users, load_users
from colorama import Fore, Back, Style

def add_user(username, email):
    users = load_users()
    users.append({"username": username, "email": email})
    save_users(users)
    print(f"User {username} added.")

def list_users():
    users = load_users()
    if not users:
        print("No users found.")
        return
    for user in users:
        print(Fore.RED+Back.GREEN+Style.DIM+f"- {user['username']} ({user['email']})")

if __name__ == "__main__":
    add_user("Alice", "alice@example.com")
    add_user("Bob", "bob@example.com")
    list_users()
    print(Style.RESET_ALL)