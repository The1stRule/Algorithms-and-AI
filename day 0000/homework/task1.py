
def multiple_of_c(a,b,c):
    if a > b:
        if b % c == 0:
            return (a // c) - (b // c - 1)
        else:
            return (a // c) - (b // c)
    else:
        if a % c == 0:
            return (b // c) - (a // c - 1)
        else:
            return (b // c) - (a // c)

print(multiple_of_c(12, 21, 3))