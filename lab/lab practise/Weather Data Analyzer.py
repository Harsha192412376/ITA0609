temperatures = []

for i in range(7):
    temp = float(input(f"Enter temperature for Day {i+1}: "))
    temperatures.append(temp)

maximum = max(temperatures)
minimum = min(temperatures)
average = sum(temperatures) / len(temperatures)

print("\nMaximum Temperature:", maximum)
print("Minimum Temperature:", minimum)
print("Average Temperature:", round(average, 2))