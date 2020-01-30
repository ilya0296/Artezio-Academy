def hvalues(d):
    a = list(d.values())
    a.sort(reverse=True)
    b = []
    for x in range(3):
        b.append(a[x])
    return b


dt = {'a': 400, 'b': 500, 'c': 100, 'd': 800, 'e': 200}
print(hvalues(dt))
