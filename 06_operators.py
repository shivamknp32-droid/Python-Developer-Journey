# Day 6 - Python Operators Practice

price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("\n===== BILL SUMMARY =====")
print("Price:", price)
print("Quantity:", quantity)
print("Total:", total)

print("\n===== CHECKS =====")
print("Total greater than 500:", total > 500)
print("Quantity is positive:", quantity > 0)
print("Quantity is even:", quantity % 2 == 0)