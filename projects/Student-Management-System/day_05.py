# Student Management System
# Day 5 - Type Conversion

student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_course = input("Enter course: ")
student_percentage = float(input("Enter percentage: "))

print("\n===== STUDENT INFORMATION =====")
print("Name:", student_name)
print("Age:", student_age)
print("Course:", student_course)
print("Percentage:", student_percentage)

print("\n===== DATA TYPE CHECK =====")
print("Name:", type(student_name))
print("Age:", type(student_age))
print("Course:", type(student_course))
print("Percentage:", type(student_percentage))