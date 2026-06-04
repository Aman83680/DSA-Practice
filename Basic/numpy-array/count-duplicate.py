import numpy as np
arr=list(map(int,input("Enter any number: ").split()))
print(arr)
visited = []
for i in range(len(arr)):
    if arr[i] not in visited:
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count > 1:
            print(arr[i], "->", count, "times")
        visited.append(arr[i])