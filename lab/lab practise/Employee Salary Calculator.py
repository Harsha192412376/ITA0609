basic_salary=float(input("enter basic salary:"))
hra=0.20*basic_salary
da=0.10*basic_salary
gross_salary=basic_salary+hra+da
pf=0.12*basic_salary
tax=0.10*gross_salary
net_salary=gross_salary-(pf-tax)
print("------salary details-----")
print("Basic salary=",basic_salary)
print("gross salary=",gross_salary)
print("pf=",pf)
print("tax=",tax)
print("net salary=",net_salary)