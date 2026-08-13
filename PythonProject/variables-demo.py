import  sys
x = 10

print(x)
print(type(x))

name='Baba'
print(name)
print(type(name))

#Assigning same value to multiple variables
var_1=var_2=var_3=100
print("variable-1", var_1)
print("variable-2",var_2)
print("variable_3" , var_3)

#Assigning different value to multiple variables
var_4,var_5,var_6 =50,60,70

print("variable-4", var_4)
print("variable-5",var_5)
print("variable_6" , var_6)

#Variable swapping
a=10
b=20
a,b=b,a
print(a)
print(b)

# memory information
my_age=25
print(my_age,type(my_age))
print("my_age variable size :",sys.getsizeof(my_age))

my_name = 'Baba Bhai'
print("my_name varaibale size in bytes:",sys.getsizeof(my_name))

#float data
price = 997.12
percentage = 1.5

print(price,percentage,sys.getsizeof(price),sys.getsizeof(percentage),
      type(price),type(percentage))

#Complex data type
num = 4 + 3j
print(num,type(num))

#list data type(ordered + mutable + duplicates allowed)
#students = ["baba",'bhai',""""chicha how are you"""]
students = ["baba","bhai","john","Abraham","baba"]
print(type(students),students)

#tuple data type (ordered + immutable + duplicates allowed)
courses = ("java","python","java","GenAI","Agentic AI")
print(type(courses),courses)

#set data type(unordered + mutable + no duplicates)
languages = {"german","french","russian","spanish","german"}
print(type(languages),languages)

#dictionary data type(Key-value pair)
student = {
    "Roll Num" : 215,
    "Student_Name" : "Baba",
    "Student_Age" : 30,
    "Student_Gender" : "male"
    }
print(type(student),student)

#student data
student_id = 201
student_name = "john"
course = "python"
free = 5000
is_paid = True
imp_concepts = ["OOPS","DSA","Variables","Fundamentals"]





