#octal to decimal
#binary to decimal
def dec(n):
    power=0
    total=0
    while n>0:
        dig=n%10
        while dig>7:
            return "It is not octal"
        total=total+dig*(8**power)
        power+=1
        n=n//10
    return total
        
a=int(input())
print(dec(a))