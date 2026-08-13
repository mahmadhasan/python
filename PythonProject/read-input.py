name = input("Enter your name")

print("my name is -",name)

age = input("Enter your age")
print("my age is-", age)

salary = input("Enter your salary")

print("my salary is -",salary)

a,b = input("Enter two numbers").split(" ")
print("first num-",a)
print("second num-",b)

#sum
result = a +b #concatination
print("sum of two numbers before type casting-", result)# from the above result get the
# result get 1020 since whenever input function take the data as string
# then it concatenated so # need to do typecasting

a = int(a)
b=int(b)
result = a+b # addition
print("sum of two numbers after type casting-", result)




