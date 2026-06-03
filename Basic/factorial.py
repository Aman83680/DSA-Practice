number=int(input("Enter the number:-"))
if number<0:
    print("not possible")
else:
    factorial=1
    while number > 0:
     factorial = factorial * number
     number = number - 1
    print(factorial)
