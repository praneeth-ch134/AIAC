
class Student:
    def __init__(self,name,age,student_id,marks):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.marks = marks
    def display_details(self):
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"ID     : {self.student_id}")
        print(f"Grade  : {self.calculate_grade()}")
    def calculate_grade(self):
        if(self.marks >= 90):
            return 'A'
        elif(self.marks >= 80):
            return 'B'
        elif(self.marks >= 70):
            return 'C'
        elif(self.marks >= 60):
            return 'D'
        else:
            return 'F'
name = input("Enter the student name :")
age = int(input("Enter age of the student :"))
student_id = input("Enter the Roll No :")
marks = int(input("Enter the marks of the student :"))

student1 = Student(name,age,student_id,marks)
student1.display_details()