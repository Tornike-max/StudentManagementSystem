from abc import ABC, abstractmethod

class Person(ABC):
    
    @abstractmethod
    def display_details(self):
        pass

class Student(Person):
    def __init__(self, student_id, name):
        self._student_id = student_id
        self.name = name
        self.grades = {}

    def add_grade(self, grade, subject):
        if grade < 0:
            print(f"You can't add a grade below zero. {grade}")
        else:
            self.grades[subject] = grade

    def average_grade(self):
        if not self.grades:
            return 0
        
        average = sum(self.grades.values()) / len(self.grades)
        return average

    def display_details(self):
        print(f"Student ID: {self._student_id}, Name: {self.name}, Average Grade: {self.average_grade()}")

class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        
    def add_student(self, student_id, name, age):
        if age >= 18:
            student = Student(student_id, name)
            self.students[student_id] = student
        else:
            print("Student must be at least 18 years old to be added")
    
    def show_student_details(self, student_id):
        student = self.students.get(student_id)
        if student:
            student.display_details()
        else:
            print("Student not found.")
    
    def show_student_average_grade(self, student_id):
        student = self.students.get(student_id)
        if student:
            print("Average Grade:", student.average_grade())
        else:
            print("Student not found.")

student_management = StudentManagementSystem()
student_management.add_student(1234, 'Tornike', 22)

student_management2 = StudentManagementSystem()
student_management2.add_student(5678, 'Giorgi', 34)

student_management.students[1234].add_grade(8, 'Math')
student_management2.students[5678].add_grade(7, 'Science')

student_management.show_student_details(1234)
student_management2.show_student_details(5678)

student_management.show_student_average_grade(1234)
