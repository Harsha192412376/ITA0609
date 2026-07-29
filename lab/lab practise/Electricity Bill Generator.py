units=int(input("enter units:"))
if units<=100:
    bill=100*1.5
elif units<=200:
    bill=(100*1.5)+(units-100*2.5)
elif units<=300:
    bill=(100*1.5)+(100*2.5)+(units-300*4)
else:
    bill=(100*1.5)+(100*2.5)+(100*4)+(100*6)
print("-----electric bill------")
print("total units consumed=",units)
print("total bill=Rs.",bill)