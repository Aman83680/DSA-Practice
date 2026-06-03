def count(n):
    c=0
    for i in n:
        if i=='a'or i=='e'or i=='i' or i=='o'or i=='u':
            c+=1
    return c
        
n=str(input())
print(count(n))