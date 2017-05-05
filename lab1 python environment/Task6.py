x = input("enter the String\n")
y=z=0

for s in x:
     if s.isdigit():
         y=y+1
     elif s.isalpha():
         z=z+1

print("letter and digit",z,y)


