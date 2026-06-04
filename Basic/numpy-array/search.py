#working on linear search
import numpy as np
arr = list(map(int, input("Enter numbers: ").split()))
print(arr)
search= int(input("Enter the number you want to search: "))
found = False
for i in range(len(arr)):
    if search==arr[i]:
        print(f"Number found at index {i}")
        found = True
        break
if found == False:
        print("Number not found")

