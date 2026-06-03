#To reverse number(string) 
def reverse_string(n):

    rev = ""

    for i in range(len(n)-1, -1, -1):
        rev = rev + n[i]

    return rev

n=str(input())
print(reverse_string(n))