courses ={"Java","Python"}
print(courses)

###########Set Operations######################

# add() : it is used add one value to set
courses.add("AWS")
print(courses)

#update():it is used add multiple elements to set
courses.update(["HTML","CSS","JS"])
print(courses)
#remove():it is used remove specified element from the set,if the element not available throw an exception
courses.remove("HTML")
print(courses)
#discard():it is also used to remove element from set but doesn't throw an exception
courses.discard("JS")
print(courses)
#pop():it is used to remove random element from set
courses.pop()
print(courses)

#clear():it is used to remove all elements from set the return empty set{}
courses.clear()
print(courses)

#del():it is used to delete entire set from memory
del courses
#print(courses) after del courses trying to print the elements throw
#an error like NameError: name 'courses' is not defined because deleted from the memory


