
# Day 9 - Python while Loop Practice

print("===== TASK 1: NUMBERS FROM 1 TO 10 =====")

count = 1
while count <= 10:
    print(count)
    count += 1


print("\n===== TASK 2: COUNTDOWN FROM 10 TO 1 =====")

count = 10
while count >= 1:
    print(count)
    count -= 1


print("\n===== TASK 3: EVEN NUMBERS FROM 1 TO 10 =====")

number = 1
while number <= 10:
    if number % 2 == 0:
        print(number)
    number += 1


print("\n===== TASK 4: VALIDATE MARKS =====")

marks = int(input("Enter marks (0-100): "))

while marks < 0 or marks > 100:
    print("Invalid marks! Please try again.")
    marks = int(input("Enter marks (0-100): "))

print("Valid marks:", marks)
