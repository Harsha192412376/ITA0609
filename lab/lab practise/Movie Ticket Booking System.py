category = input("Enter seat category (Silver/Gold): ").lower()
tickets = int(input("Enter number of tickets: "))

if category == "silver":
    price = 150
elif category == "gold":
    price = 250
else:
    print("Invalid Seat Category")
    exit()

total = tickets * price

if tickets >= 5:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

print("Total Cost: ₹", total)
print("Discount: ₹", discount)
print("Final Amount: ₹", final_amount)