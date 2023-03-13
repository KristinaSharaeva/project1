a = int(input("write the initial number:..."))
b = int(input("write another number:..."))
n = int(input("write the number of elements:..."))

l = [a]*n

for i in range(len(l)):
    l[i] = l[i] + i*b
    i = i +1
    
print(l)