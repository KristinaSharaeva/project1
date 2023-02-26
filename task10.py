import numpy
number=input("write a number of coins:  ") 
b = numpy.random.randint(2, size=int(number))
c=[]
d = []
for i in range (len(b)):
        if b[i]==0:
           c.append(b[i])
           i = i+1
        else:
            d.append(b[i])
            i = i+1
if len(c)<=len(d):
    print(len(c))
else:
    print(len(d))