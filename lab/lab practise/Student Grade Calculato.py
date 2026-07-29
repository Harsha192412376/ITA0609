m1=float(input("enter mark of subject 1:"))
m2=float(input("enter mark of subject 2:"))
m3=float(input("enter mark of subject 3:"))
m4=float(input("enter mark of subject 4:"))
m5=float(input("enter mark of subject 5:"))
total = m1+m2+m3+m4+m5
average = total/5
if average>=90:
    grade="A"
elif average>=80:
    grade="B"
elif average>=70:
    grade="c"
elif average>=60:
    grade="D"
else:
    grade="F"
print("-----student result-------")
print("total marks",total)
print("average",average)
print("grade",grade)