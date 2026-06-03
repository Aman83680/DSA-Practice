#pascal triangle
n=int(input("Enter the number:-"))

for i in range(n):
    for j in range(n-i):
        print("",end=" ")
    num=1
    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j)//(j+1)
    print()
        