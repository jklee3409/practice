def sum(a, b, n):
    result = 0
    a, b, n = int(a), int(b), int(n)

    for i in range(1, n + 1):
        result += (a ** n) * (b ** (n - 1))
        result += (a ** n) * (a ** n)
    return result

a, b, n = input().split()
print(sum(a,b,n))
