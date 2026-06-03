#horizontal number printing triangle

n=int(input("Enter the number:-"))
for i in range(1,n+1):
    for j in range(0,i):
        print(i,end=" ")
    print()