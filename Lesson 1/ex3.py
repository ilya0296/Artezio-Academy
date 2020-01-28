text = input("Input text")
if len(text) >= 2:
    dl = len(text)
    a = text[0:2]
    b = text[dl-2:dl]
    output = a+b
    print(output)
else:
    print('')
