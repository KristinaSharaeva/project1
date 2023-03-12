count = 0
a  = int(input("please write number a:  "))
b = int(input("please write number b:  "))

def sum(a,b):
    global count
    if a ==0:
        return(b)
    if b ==0:
        return(a)
    a = a+1
    count = count+1
    if count==b:
        return a
    else:
        return sum(a,b);
    
    
print(sum(a,b))