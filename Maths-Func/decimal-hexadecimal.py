#decimal to hexadecimal
def hexa(n):
    hex_digits = "0123456789ABCDEF"
    b = ""

    while n > 0:
        dig = n % 16
        b = hex_digits[dig] + b
        n = n // 16

    return b

a = int(input())
print(hexa(a))