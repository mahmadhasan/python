for i in range(1,10):
    if i == 5:
        break
    print(i)

for i in range(1,10):
    if i == 5:
        break
    print(i)

#search name
students =["baba","john","javeed","hasan","gangadhar"]
search_name="javeed"
for student in students:
    print("Checking..",student)
    if search_name == student:
        print("student found..",student)
        break
