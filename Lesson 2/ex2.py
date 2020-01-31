def delenie(a, b, c):
    i = 0
    for x in range(a,b+1):
        if x % c == 0:
            i = i+1
    return i


print(delenie(5, 10, 2))

