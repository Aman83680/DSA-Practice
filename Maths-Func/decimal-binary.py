#decimal to binary
def binary(n):
    b=0
    place=1
    while n>0:
        dig=n%2 #n=10 to pahla remainder 0
        b=b+dig*place #0+0*1 =0
        place=place*10 #place=10
        n=n//2 #n=10//2=5
    return b #same loop again work krega 
a=int(input())
print(binary(a))