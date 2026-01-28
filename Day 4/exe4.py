class Student: 
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
    
    def is_pass(self):
        return self.marks >= 40
    
students = []
s1 = Student("milan",50)
s2 = Student("suboid", 60)

students.append(s1)
students.append(s2)

print(students[0].name)