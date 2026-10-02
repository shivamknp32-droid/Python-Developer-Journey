# Day 2 - Python Variables

# Basic variables
name = "Shivam"
age = 20
course = "BCA"
city = "Kanpur"

print(name)
print(age)
print(course)
print(city)


# Student introduction using variables
print("My name is", name)
print("I am", age, "years old")
print("I am studying", course)
print("I live in", city)


# Reassigning a variable
age = 21

print("Updated age:", age)


# Multiple assignment
student_name, student_age, student_city = "Shivam", 20, "Kanpur"

print("Student Name:", student_name)
print("Student Age:", student_age)
print("Student City:", student_city)


# Same value assigned to multiple variables
x = y = z = 100

print(x)
print(y)
print(z)


# Swapping two variables
a = 10
b = 20

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)


# Checking data types using type()
name = "Shivam"
age = 20
percentage = 82.5
is_student = True

print(type(name))
print(type(age))
print(type(percentage))
print(type(is_student))


# Dynamic typing
value = 10

print(value)
print(type(value))

value = "Python"

print(value)
print(type(value))


# Constant convention
MAX_MARKS = 100
PI = 3.14159

print("Maximum Marks:", MAX_MARKS)
print("PI:", PI)


# Final Student Information
student_name = "Shivam Singh"
student_age = 20
student_course = "BCA"
student_city = "Kanpur"
student_percentage = 82
student_goal = "Python Developer"

print()
print("================================")
print("       STUDENT INFORMATION")
print("================================")
print()
print("Name:", student_name)
print("Age:", student_age)
print("Course:", student_course)
print("City:", student_city)
print("Percentage:", student_percentage)
print("Goal:", student_goal)
print()
print("================================")
