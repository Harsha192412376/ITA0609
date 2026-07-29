product = input("Enter product name: ")
stock = int(input("Enter current stock: "))
minimum = int(input("Enter minimum stock level: "))

print("Product:", product)
print("Current Stock:", stock)

if stock < minimum:
    print("Stock is Low! Reorder Required.")
else:
    print("Stock Level is Sufficient.")