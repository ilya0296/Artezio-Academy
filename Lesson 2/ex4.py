def range2(a):
    s = []
    i = 0
    while i < a:
        s.append(i)
        i = i+1
    return s


def range3(a, b):
    s = []
    i = a
    while i < b:
        s.append(i)
        i = i + 1
    return s


def range4(a, b, c):
    s = []
    i = a
    while i < b:
        s.append(i)
        i = i + c
    return s


print(range2(5))
print(range3(-1, 4))
print(range4(-4, 6, 2))
