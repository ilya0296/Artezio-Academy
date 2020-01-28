name = input("Input full name ")
if 0 < len(name) < 1000:
    words = name.split()
    capitalized_words = []
    for word in words:
        title_case_word = word[0].upper() + word[1:]
        capitalized_words.append(title_case_word)
    output = ' '.join(capitalized_words)
    print(output)
else:
    print('Превышен лимит символов')
