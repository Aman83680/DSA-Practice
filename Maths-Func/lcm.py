def lcm(a,b):
    greatest=max(a,b)
    while True:
         if greatest%a==0 and greatest%b==0:
            return greatest
         greatest+=1
n=int(input())
m=int(input())
print(lcm(m,n))

    