balance = int(input("Enter the amount..."))

deposit_amount = int(input("Enter the Deposit_amount..."))

withdraw_amount = int(input("Enter the withdraw_amount..."))

if  balance <= deposit_amount:
    balance =  balance + deposit_amount
    print("balance before deposit",balance)
elif balance >= withdraw_amount:
    balance = balance-withdraw_amount
    print("balance after withdraw",balance)
else:
    print("Exit from the machine")