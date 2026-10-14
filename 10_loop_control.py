
# Day 10 - break, continue and pass

print("===== TASK 1: BREAK =====")

for number in range(1, 11):
    if number == 5:
        break
    print(number)


print("\n===== TASK 2: CONTINUE =====")

for number in range(1, 11):
    if number == 3:
        continue
    print(number)


print("\n===== TASK 3: PASS =====")

for number in range(1, 6):
    if number == 3:
        pass
    print(number)


print("\n===== TASK 4: WHILE LOOP WITH CONTINUE =====")

number = 1

while number <= 10:
    if number == 7:
        number += 1
        continue

    print(number)
    number += 1
