class Student: 
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
    
    def is_pass(self):
        return self.marks >= 40
    
s = Student(input("Enter the name: "),int(input("Enter the marks: ")))

if s.is_pass():
    print(s.name,"is passed")
else:
    print(s.name," is failed")