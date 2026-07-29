fare = float(input("Enter Base Fare: "))
age = int(input("Enter Age: "))
travel_class = input("Enter Class (Sleeper/AC): ")

if age < 5:
    discount = 1.00      # 100%
elif age >= 60:
    discount = 0.50      # 50%
else:
    discount = 0.00

final_fare = fare - (fare * discount)

print("\nTravel Class:", travel_class)
print("Final Ticket Fare = ₹", final_fare)