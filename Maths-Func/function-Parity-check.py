#Parity checking by function
def eod(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
n=int(input("Enter a number:-"))
print(eod(n))