age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")

if age >= 18 and nationality.lower() == "indian":
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")