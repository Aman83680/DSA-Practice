n=int(input("Enter the number: "))
if n<0:
    print("Factorial not exist for Negative Numbers.")
elif n==0 or n==1:
    print("Factorial is: 1")
elif n>1:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("Factorial is:",fact)
