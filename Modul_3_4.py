def single_root_words(root_words, *other_words):
    same_words = []
    for i in other_words:
        if root_words.lower() in i.lower():
            same_words.append(i)
        elif i.lower() in root_words.lower():
            same_words.append(i)
    return same_words
print(single_root_words('Ода', 'Года', 'Сода', 'Порода', 'Стекловата', 'ВОДА'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))