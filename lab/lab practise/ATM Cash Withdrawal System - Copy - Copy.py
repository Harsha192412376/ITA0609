balance=5553555
pin=1608
user_pin=int(input("enter user_pin="))
if user_pin==pin:
    amount=float(input("enter withdrawal amount:"))
    if amount<=balance:
        balance=balance-amount
        print("withdrawal succesfully ")
        print("balance",balance)
    else:
        print("not sufficient balance")
else:
    print("invalid pin")