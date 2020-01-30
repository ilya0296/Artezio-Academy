a = [1, 2, 3, 4, 5, 1]
dup_items = set()
for x in a:
    if x not in dup_items:
        dup_items.add(x)
print(dup_items)
