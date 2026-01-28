import json
class Student: 
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
    
    def is_pass(self):
        return self.marks >= 40


students = []

# Get input from the user
name = input("Enter student name: ")
marks = int(input("Enter student marks: "))

# Create a new Student object
s = Student(name, marks)

# Add the student object to our list
students.append(s)

with open("user_profile.json",'w') as f:
    json.dump(
        [student.__dict__ for student in students],f , indent =4
    )