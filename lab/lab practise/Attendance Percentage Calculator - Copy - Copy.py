total_classes = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

percentage = (attended / total_classes) * 100

print("Attendance Percentage:", round(percentage, 2), "%")

if percentage >= 75:
    print("Eligible for Examination")
else:
    print("Not Eligible for Examination")