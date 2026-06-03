#hexadecimal to decimal
def decimal(n):
    hex_digits = "0123456789ABCDEF"

    power = 0
    total = 0

    while len(n) > 0:

        dig = n[-1]

        value = hex_digits.index(dig)

        total = total + value * (16 ** power)

        power += 1

        n = n[:-1]

    return total

a = input().upper()

print(decimal(a))