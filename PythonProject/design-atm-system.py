# balance = int(input("Enter the amount..."))
#
# deposit_amount = int(input("Enter the Deposit_amount..."))
#
# withdraw_amount = int(input("Enter the withdraw_amount..."))
#
# if  balance <= deposit_amount:
#     balance =  balance + deposit_amount
#     print("balance before deposit",balance)
# elif balance >= withdraw_amount:
#     balance = balance-withdraw_amount
#     print("balance after withdraw",balance)
# else:
#     print("Exit from the machine")

balance = 1000
while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("Deposit successful!")
            print("Your new balance is:", balance)
        else:
            print("Please enter a valid amount.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance = balance - amount
            print("Withdrawal successful!")
            print("Your remaining balance is:", balance)

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Please try again.")