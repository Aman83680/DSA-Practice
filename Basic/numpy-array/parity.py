#parity checking
import numpy as np
arr=list(map(int,input("Enter the number: ").split()))
odd=0
even=0
for i in range(len(arr)):
    if arr[i]%2==0:
        even+=1
    else:
        odd+=1
print("Even",even)
print("Odd",odd)
        
    
