import random
n = int(input("write a number n:"))
a = []
for k in range(1,n+1):
    a.append(random.randint(1,n))
print(a)

x = int(input("write a number x:"))
b = []
for i in range (len(a)):
    b.append(x - a[i])

tmp = min(b)
index = b.index(tmp)
print(a[index])