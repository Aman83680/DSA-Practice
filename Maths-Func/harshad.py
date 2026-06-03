#harshad number
def harshad(n):
    temp = n
    total = 0

    while n > 0:
        dig = n % 10
        total += dig
        n = n // 10

    if temp % total == 0:
        return "Harshad Number"
    else:
        return "Not Harshad Number"

a = int(input())
print(harshad(a))