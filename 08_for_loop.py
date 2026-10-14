
# Day 8 - Python for Loop Practice

print("===== TASK 1: NUMBERS FROM 1 TO 10 =====")

for number in range(1, 11):
    print(number)


print("\n===== TASK 2: EVEN NUMBERS FROM 1 TO 10 =====")

for number in range(1, 11):
    if number % 2 == 0:
        print(number)


print("\n===== TASK 3: MULTIPLICATION TABLE =====")

number = int(input("Enter a number for multiplication table: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


print("\n===== TASK 4: SUM FROM 1 TO 10 =====")

total = 0

for number in range(1, 11):
    total = total + number

print("Total:", total)
