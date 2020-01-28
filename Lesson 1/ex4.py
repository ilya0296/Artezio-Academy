a = ['abc', 'xyz', 'aba', '1221']
n = 0
for x in a:
    if len(x) > 2 and x[0] == x[-1]:
        n = n+1
print(n)
