#right aligned right angled triangle
n=int(input("Enter the  number:-"))
for i in range(n):
    for j in range(i):#row print
        print(" ",end=" ")#space print
    for j in range(n-i):
        print("*",end=" ")#number print
    print()