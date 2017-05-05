import math
x = int(input('Enter the 1st Num'))
y = int(input('Enter the @nd Num'))
op = input('Enter the operator')

def add(x, y):
    z = x + y
    return z

def sub(x, y):
    z = x - y
    return z

def mul(x, y):
    z = x * y
    return z

def div(x, y):
    z = x / y
    return z

if (op=="+"):
       z = add(x,y)
       print(z)
if (op=="-"):
       z = sub(x,y)
       print(z)
if (op=="*"):
       z = mul(x,y)
       print(z)
if (op=="/"):
       z = div(x,y)
       print(z)






