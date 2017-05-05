def rev(st):
    if(st==""):
        return ""
    else:
        return rev(st[1:])+st[0]
str = input("enter the String")
a = rev(str)
print(a)
