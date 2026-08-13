#list type casting
course_name = "python"
chars = list(course_name)
print(chars,type(chars))

#tuple type casting
numbers =[10,20,30,45,58,23]
result = tuple(numbers)
print(type(result),result)

#set type casting
numbers=[10,10,20,20,30,45,58,23]
unique_nums= set(numbers)
print(type(unique_nums),unique_nums)

#dictionary type casting
data = [("name","baba"),("course","python")]
student = dict(data)
print(type(student),student)

#implicit casting
a=15
b=10.5
result = a+b
print(type(result),"Result--",result)

#explicit casting
i = "15"
j="25"
result = int(i) + int(j)
print("result===",result)
