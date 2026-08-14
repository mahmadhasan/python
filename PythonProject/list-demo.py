#list creation
courses = ["Java","Python","DevOps","GenAI"]

#access list elements
print(courses[0])
print(courses[1])
print(courses[3])

#list with for loop
for course in courses:
    print(course)

#length of the list
print(len(courses))

items =["Laptop","Computer","Monitor","Keyboard","Mouse"]
#positive Indexing (from right to left)
print(items[1])

#negative Indexing (from left to right)
print(items[-1])

#List slicing - used to a part of list
#syntax:: list_name

numbers = [10,20,30,40,50,60]

print(numbers)#print all the numbers

print(numbers[1:4]) #start index inclusive,end index exclusive

print(numbers[:3])#start from 0th index to 2 index.

print(numbers[2:])#print from 2nd to last

print(numbers[::2])#step by 2

print(numbers[::-1])#print in reverse order

print(len(numbers))

print(max(numbers))

print(min(numbers))

print(sum(numbers))

print(sorted(numbers)) #ascending order natural sorting

#print(numbers.sort()) #ascending order natural sorting

numbers.sort(reverse=True)#descending ordering custom sorting
print(numbers)






##################################################
#list operations
##################################################

course = ["Java", "AgenticAI", "Python"]

#append operation
print(course)

#insert operation
course.insert(1,"GenAI")
print(course)

#remove operation
course.remove("Java")
print(course)

#extend operation
frontend = ["Angular","React"]
backend = ["Java","Python"]
frontend.extend(backend)
print(frontend)

#pop operation
course.pop()
print(course)

#delete operation
del course[0]
print(course)

#clear operation
course.clear()
print(course)




