class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        permission = input("Do you want to display student details? (yes/no): ").strip().lower()
        if permission == 'yes':
            print(f"Name: {self.name}")
            print(f"Roll No: {self.roll_no}")
            print(f"Marks: {self.marks}")
        else:
            print("Permission denied. Details not displayed.")

if __name__ == "__main__":
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = input("Enter marks: ")
    student = Student(name, roll_no, marks)
    student.display_details()