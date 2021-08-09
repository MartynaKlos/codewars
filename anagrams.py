def anagrams(word, words):
    split_word = sorted(list(word))
    list_anagrams = []

    for item in words:
        if sorted(list(item)) == split_word:
            list_anagrams.append(item)
        else:
            pass

    return list_anagrams


# word = "abba"
# split_word = sorted(list(word))
# print(split_word)