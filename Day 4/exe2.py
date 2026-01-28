class User:
    def __init__(self,name):
        self.name = name 
    
    def greet(self):
        print("Hello,",self.name)

u = User("Sita")
u.greet()
