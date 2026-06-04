#finding second largest element in array
import numpy as np
arr=list(map(int,input("Enter the number: ").split()))
print(arr)
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
#print(arr)
print(arr[-2])