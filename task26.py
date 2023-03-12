def stepen(A, B):
    if B == 0:
        return 1
    else:
        return A * stepen(A, B-1)
        
print(stepen(2,4))