list = []
list.append(5)
print("this is in list ",list[0])

x = int(input("Enter the number of students"))

row = []
for y in range (1,x+1):
    print("Enter the Name of student ",y)
    j = input()
    row.append(j)

for n in range(1,x+1):
    print(row[n-1])




