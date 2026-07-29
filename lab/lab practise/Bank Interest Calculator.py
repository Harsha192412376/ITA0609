principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Annual Interest Rate (%): "))
time = float(input("Enter Time (in years): "))
si = (principal * rate * time) / 100
amount = principal * (1 + rate / 100) ** time
ci = amount - principal
print("\n----- Interest Details -----")
print("Simple Interest =", si)
print("Compound Interest =", ci)
print("Total Amount (CI) =", amount)