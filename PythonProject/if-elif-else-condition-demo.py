age = 12
if age>=18:
    print("Eligible to vote..")

else :
     print("Not eligible for vote")

#Multiple conditions use if-elif-else statements
#marks = 100
marks = int(input("Enter the Marks"))
if marks>=90:
    print("Grade-A")
elif marks>=80:
    print("Grade-B")
elif marks>=70:
    print("Grade-C")
elif marks>=50:
    print("Grade-D")
elif marks>=45:
    print("Grade-E")
elif marks>=35:
    print("pass")
else:
    print("Fail")

#Nested If statement
#username = "admin"
#pwd ="admin123"
#role = "trainer"
username = input("Enter the username")
pwd = input("Enter the password")
role = input("Enter the role")
if username == "admin" and pwd =="admin123":
    if role == "student":
       print("display student dashboard")
    elif role == "trainer":
        print("display trainer dashboard")
    elif role == "admin":
        print("display admin dashboard")
else :
    print("Invalid credentials")

#Nested if for Withdraw_amount
balance = 5000
withdraw_amount = int(input("Enter the amount to withdraw"))
if balance>0:
    if withdraw_amount <= balance:
        balance = balance - withdraw_amount
        print("Withdraw success and remaining balance",balance)
    else :
        print("Insufficient balance")
else :
        print("Funds not available")
