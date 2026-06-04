a=int(input("Enter the first:-"))
b=int(input("Enter the second:-"))
print("what you want to perform with these two:")
print("1. Sum")
print("2. Sub")
print("3. Multiply")
print("4. Division")
print("5. Floor")
print("6. Modulo")
print("7. power of number")
print("8. not")
c=int(input("you choose..."))
if c==1:
    print("sum of these ",a+b)
elif c==2:
    print("Subtraction is :-",a-b)
elif c==3:
    print("Multiplication is:-",a*b)
elif c==4:
    print("Division is:-",a/b)
elif c==5:
    print("Floor number is:-",a//b)
elif c==6:
    print("modulos/remainder is:-",a%b)
elif c==7:
    print("power of the first number",a**b)
elif c==8:
    print("not value of number:-",a^b)
else:
    print("you choose wrong operation.")