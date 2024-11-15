def all_variants(text):
    for name in range(len(text)):
        for x in range(len(text) - name):
            yield text[x:x + name + 1]


a = all_variants("abc")
for i in a:
    print(i)