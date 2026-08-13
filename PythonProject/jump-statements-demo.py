for i in range(1,10):
    if i == 5:
        break
    print(i)

for i in range(1,10):
    if i == 5:
        continue
    print(i)

#search name
students =["baba","john","javeed","hasan","gangadhar"]
search_name="javeed"
for student in students:
    print("Checking..",student)
    if search_name == student:
        print("student found..",student)
        break



students = [
    {"name":"baba","marks":80},
    {"name":"john","marks":30},
    {"name":"Hasan","marks":90}
]

for student in students:
    if student["marks"] < 35:
        continue
    print("certificate sent to ",student["name"])

