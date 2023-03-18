a = input("write your poem here:   ")
a = a.split('-\ ')
b = []

count = 0
for i in range (len(a)):
    list(a[i])

    for j in range (len(a[i])):
        if (a[i])[j] == "a" or "u" or "e" or "i" or "o":
           count = count +1
    b.append(count)       
    count = 0       

if b.count(b[0]) == len(b):
    print ('Парам пам-па')
else:
    print('Пам парам')