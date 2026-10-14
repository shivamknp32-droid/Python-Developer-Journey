
# Day 8 - Student Management System
# Using for loop

print("===== STUDENT MANAGEMENT SYSTEM =====")

total_students = int(input("How many students do you want to enter? "))

for i in range(1, total_students + 1):
    print(f"\n--- Student {i} ---")

    student_name = input("Enter student name: ")
    marks = float(input("Enter marks (0-100): "))

    print("\nStudent Name:", student_name)
    print("Marks:", marks)

    if marks < 0 or marks > 100:
        print("Invalid marks!")
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 40:
        print("Grade: D")
    else:
        print("Grade: F")

    if 0 <= marks <= 100:
        if marks >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")

print("\nAll student records processed.")

