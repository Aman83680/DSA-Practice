def palindrome(n):

    temp = n
    rev = 0

    while n > 0:

        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    if temp == rev:
        return "Palindrome"

    else:
        return "Not Palindrome"

n=int(input())
print(palindrome(n))