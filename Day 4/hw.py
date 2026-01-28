class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    
users = []
for _i in range(3):
    u = User(input("Enter your name: "), input("Enter your email: "))
    users.append(u)

#To display user
for user in users:
    print("Name: ",user.name)
    print("email: ",user.email)