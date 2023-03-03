a = list(input('write numbers: '))
b = list(input('write numbers: '))
temp = []
for i in a: 
    for j in b: 
        if i == j: 
            temp.append(i) 
print (sorted(temp))