import random
n = int(input("write a number n:"))
a = []
for k in range(1,n+1):
    a.append(random.randint(1,n))
print(a)

x = int(input("write a number x:"))
print(a.count(x))