def uclid(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)

a = 36
b = 24

uclid(a, b)
