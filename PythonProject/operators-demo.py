#assignment operator

a=10
b=20

#comparison operator
print(a == b)

#addition operator
i=15
j=15
sum = a+b
print(sum)

result = a-b
print(result)

result = a*b
print(result)

result = a/b
print(result)

#floor division operator (return quotient w/o decimal value)
result = a//b
print(result)

# it returns remainder
result = a % b
print(result)

#additional assignment
balance = 1000
deposit_amount = 500
#balance = balance + deposit_amount
balance+=deposit_amount
print("final balance--",balance)


withdraw_amount = 200
#balance = balance-withdraw_amount
balance-=withdraw_amount
print("final amount-",balance)

user_name ="admin"
pwd="bhai@123456"
print(user_name=="admin" and pwd=="bhai@123456")
print(user_name=="admin" or pwd=="bhai@1234")

is_logged_in=True
print(not is_logged_in)

#membership operators
students=["baba","john","raj"]
print("baba" in students) # true
print("don" in students) #false
print("kiran" not in students) # true

#identity operators
a=10
b=10
print(a is b) # true
print(a is not b) # false












