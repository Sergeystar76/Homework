def all_variants(text):
    for i in range(len(text)):
        for y in range(len(text) - i):
            yield text[y:y + i + 1]

a = all_variants("abc")
for i in a:
    print(i)