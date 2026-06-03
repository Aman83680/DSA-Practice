#reverse triangle
n=int(input("Enter the number:-"))
for i in range(n):
    for j in range(1,2*i):
        if i>=j-n+1 and i<=j+n-1:
            print("*",end=" ")
        else:
            print(" ",end="")
    print()