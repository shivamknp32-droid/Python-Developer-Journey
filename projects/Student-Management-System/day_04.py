
# Student Management System
# Day 4 - User Input

# Take student details from the user
student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_course = input("Enter course: ")
student_city = input("Enter city: ")
student_percentage = float(input("Enter percentage: "))

# Display student information
print()
print("================================")
print("       STUDENT MANAGEMENT")
print("================================")
print()
print("Name:", student_name)
print("Age:", student_age)
print("Course:", student_course)
print("City:", student_city)
print("Percentage:", student_percentage)
print()
print("================================")

# Display data types
print()
print("--------- DATA TYPES ---------")
print("Name Type:", type(student_name))
print("Age Type:", type(student_age))
print("Course Type:", type(student_course))
print("City Type:", type(student_city))
print("Percentage Type:", type(student_percentage))

