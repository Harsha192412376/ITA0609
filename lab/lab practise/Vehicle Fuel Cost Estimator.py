distance = float(input("Enter distance (km): "))
mileage = float(input("Enter vehicle mileage (km/l): "))
fuel_price = float(input("Enter fuel price per litre: "))

fuel_needed = distance / mileage
total_cost = fuel_needed * fuel_price

print("Fuel Needed:", round(fuel_needed, 2), "litres")
print("Total Fuel Cost: ₹", round(total_cost, 2))