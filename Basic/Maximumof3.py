a=int(input("Enter the number:-"))
b=int(input("Enter the number:-"))
c=int(input("Enter the number:-"))
if a>=b and a>=c:
    print("Max:-",a)
elif b>=c and b>=a:
    print("Max:-",b)
elif c>=b and c>=a:
    print("Max:-",c)
else:
    print("Equal")