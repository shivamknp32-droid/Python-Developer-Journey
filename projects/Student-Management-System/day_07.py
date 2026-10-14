# Day 7 - Student Grade Management

student_name = input("Enter student name: ")
marks = float(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks! Enter marks between 0 and 100.")

else:
    print("\n--- Student Result ---")
    print("Student Name:", student_name)
    print("Marks:", marks)

    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 40:
        print("Grade: D")
    else:
        print("Grade: F")

    if marks >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")
        