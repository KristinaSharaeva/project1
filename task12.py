import math

numberA =input("write a number a:  ")
numberB =input("write a number b:  ")

x = (int(numberA) + math.sqrt(int(numberA)**2 - 4*int(numberB))) / 2
y = int(numberA) - x
print(int(x),int(y))