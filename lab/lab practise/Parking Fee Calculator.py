vehicle = input("Enter vehicle type (bike/car): ").lower()
hours = int(input("Enter parking hours: "))

if vehicle == "bike":
    rate = 20
elif vehicle == "car":
    rate = 50
else:
    print("Invalid vehicle type")
    exit()

fee = rate * hours

print("Parking Fee: ₹", fee)