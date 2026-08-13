#Numeric literals
from unittest import result

age = 35
student_id=123456

print(age)
print(student_id)

#floating literals
price=99.9
percentage=15.5

print(price)
print(percentage)

#String literals
name='Baba'
city="Hyd"
msg="""
I Joined GenAi and Agentic Course
"""
print(name)
print(city)
print(msg)


#Boolean literals
is_activated = True
is_completed= False

print(is_activated)
print(is_completed)

#None literals
result = None
print(result)

#List literals(mutable and insertion order)
students =['Baba','javeed','Baba','Raj','Ramesh']
print(students)

#Tuple literals(immutable and insertion order)
cities=('hyd','pune','hyd','delhi','Bangalore')
print(cities)

#set literals(duplicates not allowed)
courses={'java','python','java','C++','C#','java'}
print(courses)

#Dictionary literals
student = {
        "student_Id" : 101,
        "student_Age": 25,
        "student_Name": 'John',
        "student_Gender":'Male'
}
print(student)

books =[ {
    "book_id" : 100,
    "book_name" :"Biography",
    "book_price":104.23

},
    {
        "book_id": 101,
        "book_name": "Geography",
        "book_price": 105.23

    },
    {
        "book_id": 102,
        "book_name": "History",
        "book_price": 105.23

    },
    {
        "book_id": 103,
        "book_name": "Chemistry",
        "book_price": 106.23

    }
]
print(books)
