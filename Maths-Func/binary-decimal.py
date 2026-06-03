#binary to decimal
def dec(n):
    power=0
    total=0
    while n>0:
        dig=n%10
        if dig!=1 and dig!=0:
            return "It is not Binary"
        total=total+dig*(2**power)
        power+=1
        n=n//10
    return total
        
a=int(input())
print(dec(a))