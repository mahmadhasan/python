#range(stop)
for  i in range(6):
    print(i)

#range(start,stop)
for i in range(1,15):
    print(i)

#range(start,stop,step)
for i in range(1,11,2):
    print(i)

#for loop with string
#print  each char
name = "baba bhai"
for ch in name:
    print(ch)


#for loop for list of students
students = ["baba","john","bab","marsh"]
for names in students:
    print(names)


#for loop with tuple
courses = ("java","python","C#","C++","GenAI")
for course in courses:
    print(course)

#for loop with set
cities = ["Hyd","Pune","Blr","sydney","Hyd"]
for city in cities:
    print(city)

#for loop with dictionary
student ={
    "id" : 100,
    "name" : "baba",
    "gender" : "male"
}
for key in student:
    print(key,"--",student[key])

#cart prices for items find total price
cart_prices =[200,300,500,900,150,220]
total_price =0
for price in cart_prices:
    total_price = total_price + price
print("Total cart Price-",total_price)
