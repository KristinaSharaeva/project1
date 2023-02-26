number =input("write a number:  ") 
number = int(number) 
i = 0 
n = 0 
while n <= number: 
    n = 2**i 
    if n<= number: 
        print (n) 
        i = i + 1