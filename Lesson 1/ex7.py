def merge(d1, d2):
    d1.update(d2)
    return d1


dt1 = {'a': 1, 'b': 2}
dt2 = {'c': 3, 'd': 4}
print(merge(dt1, dt2))
