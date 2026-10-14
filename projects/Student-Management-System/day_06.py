# Student Management System
# Day 6 - Python Operators

student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_percentage = float(input("Enter percentage: "))

print("\n===== STUDENT INFORMATION =====")
print("Name:", student_name)
print("Age:", student_age)
print("Percentage:", student_percentage)

print("\n===== ELIGIBILITY CHECK =====")
print("Age is 18 or above:", student_age >= 18)
print("Passed with 40% or above:", student_percentage >= 40)

print("\n===== DATA CHECKS =====")
print("Age is positive:", student_age > 0)
print("Percentage is valid:", 0 <= student_percentage <= 100)