recharge = float(input("Enter recharge amount: "))
discount = float(input("Enter cashback/discount (%): "))

cashback = recharge * discount / 100
final_amount = recharge - cashback

print("Cashback: ₹", cashback)
print("Final Recharge Amount: ₹", final_amount)