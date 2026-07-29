item1 = float(input("Enter price of Item 1: "))
item2 = float(input("Enter price of Item 2: "))
item3 = float(input("Enter price of Item 3: "))

subtotal = item1 + item2 + item3
gst = subtotal * 0.05
service_charge = subtotal * 0.10

final_bill = subtotal + gst + service_charge

print("\n----- Restaurant Bill -----")
print("Subtotal =", subtotal)
print("GST (5%) =", gst)
print("Service Charge (10%) =", service_charge)
print("Final Bill =", final_bill)