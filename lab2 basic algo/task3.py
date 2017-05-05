list = []
def sqr(i):
    p = i*i
    return p
for x in range(1,21):
       list.append(sqr(x))
       print("Square of ",x," is: ",list[x-1])




