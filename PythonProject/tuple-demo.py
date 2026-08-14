#empty tuple
numbers =()

print(numbers)

print(type(numbers))
############################################################
#list of tuple
courses = ["java", "python", "Gen-AI", "AI"]

print(courses)

print(type(courses))

print(courses[0:2])

print(courses[:2])

print(courses[2:])

# throw an error since it is immutable like tuple obj doesn't
# support item assignment like below
#courses[1] = "AWS"

#find the index
print(courses.index("java")) #0

#tuple packing-storing multiple values into a single tuple
student = "Baba","male",9963175156
print(student)

#tuple unpacking
student = "Baba","male",9963175156
name,gender,phone = student
print(name,gender,phone)

################################################################
#tuple functions
numbers =(10,20,30,40,50)
#len()
print(len(numbers))
#max()
print(max(numbers))
#min()
print(min(numbers))
#sum()
print(sum(numbers))
#sorted()
print(sorted(numbers)) # it returns a new list-ascending order
sorted_nums = sorted(numbers,reverse=True)#descending order
print(sorted_nums)

################################################################
#convert tuple to list
courses = ("java","python",".net")
list_courses = list(courses) #it returns list
list_courses[0] = "AWS"
print(list_courses)

#check value exists in tuple
if "java" in courses:
    print("java is available in courses...")
else:
    print("java is not available in courses...")

#combine the two tuple concatenation
frontend = ("HTML","ReactJS","Angular")
backend = ("java","python","C#")
fullstack = frontend + backend #new tuple got created
print(fullstack)

#conver tuple to list
list_fullstack = list(fullstack)
print(list_fullstack)





####################################################################