
# Day 10 - Student Management System
# Using break, continue and pass

print("===== STUDENT MANAGEMENT SYSTEM =====")

total_students = int(input("How many students do you want to process? "))

for i in range(1, total_students + 1):
    print(f"\n--- Student {i} ---")

    student_name = input("Enter student name: ")

    marks = float(input("Enter marks (0-100), or -1 to stop: "))

    if marks == -1:
        print("Student entry stopped.")
        break

    if marks < 0 or marks > 100:
        print("Invalid marks. Student skipped.")
        continue

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

print("\nStudent processing completed.")
