amount = float(input("Enter purchase amount: "))
if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0

amount_after_discount = amount - discount
gst = amount_after_discount * 0.18

final_bill = amount_after_discount + gst

print("\n----- Bill Details -----")
print("Purchase Amount =", amount)
print("Discount =", discount)
print("Amount After Discount =", amount_after_discount)
print("GST (18%) =", gst)
print("Final Bill =", final_bill)