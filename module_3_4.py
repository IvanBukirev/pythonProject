def single_root_words(root_word, *other_words):
    same_words = []
    lower_root_word = root_word.lower()
    for word in other_words:
        lower_other_words = word.lower()
        if lower_root_word in lower_other_words or lower_other_words in lower_root_word:
            same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)