

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height * height)

print("\nBMI =", round(bmi, 2))

if bmi < 18.5:
    print("Health Status: Underweight")
elif bmi < 25:
    print("Health Status: Normal")
elif bmi < 30:
    print("Health Status: Overweight")
else:
    print("Health Status: Obese")