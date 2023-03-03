a = list(input('write your numbers here: ')) 
sum = 0
maxSum = 0
index = 0
for i in range (1 , len(a)-1):
    sum = int(a[i]) + int(a[i-1]) + int(a[i+1])
    if maxSum<sum:
        maxSum = sum
    index = index + 1
   
sum = int(a[-1]) + int(a[0]) + int(a[1])   
if maxSum<sum:
    maxSum = sum
        
sum = int(a[-2]) + int(a[-1]) + int(a[0])   
if maxSum<sum:
    maxSum = sum
        
print(maxSum)