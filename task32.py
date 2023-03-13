import numpy
import random
l = numpy.random.randint(0, 100, 10)
a = int(input("write the initial number:..."))
b = int(input("write another number:..."))
for i in range (len(l)):
    if a<=l[i]<=b:
        print(l[i])
        print(i)
print(l)