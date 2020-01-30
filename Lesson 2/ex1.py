def squ(x):
    a = []
    for i in range(x//2):
        k = 2*i+1
        a.append(k*k)
    return a, x//2


print(squ(x=6))
