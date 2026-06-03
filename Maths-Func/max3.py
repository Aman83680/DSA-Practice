def max(max1,max2,max3):
    if max1>max2 and max1>max3:
        return max1
    elif max2>max1 and max2>max3:
        return max2
    else:
        return max3
max1=input("Enter the first number:")
max2=input("Enter the second number:")
max3=input("Enter the third number:")
print(max(max1,max2,max3))