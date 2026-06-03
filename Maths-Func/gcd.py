def gcd(a,b):
    smaller=min(a,b)
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf
m=int(input())
n=int(input())
print(gcd(m,n))