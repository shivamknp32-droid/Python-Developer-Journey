# Day 7 - Conditional Statements

marks = float(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks! Enter marks between 0 and 100.")

elif marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 40:
    print("Pass - Grade D")

else:
    print("Fail")
    