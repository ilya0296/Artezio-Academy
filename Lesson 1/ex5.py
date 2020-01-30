inp = "12 23 2"
a = inp.split()
a1 = set(a[0]).isdisjoint(set(a[2]))
a2 = set(a[1]).isdisjoint(set(a[2]))
if a1 is False and a2 is False:
    print('True')
else:
    print('False')
