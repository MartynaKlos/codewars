# Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.
# Assumptions:
#
#     A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII. (No need to handle fancy punctuation.)
#     Matches should be case-insensitive, and the words in the result should be lowercased.
#     Ties may be broken arbitrarily.
#     If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
import string


def top_3_words(text):
    list_text = text.split()
    final_list = [item.split("\n") for item in list_text if item != ' ']
    result = [item.strip('.').strip(',').lower() for i in final_list for item in i]
    result_set = set(result)
    unique_words = list(result_set)
    for word in unique_words:
        count = text.count(word)
        unique_words[unique_words.index(word)] = (word, count)
    sorted_words = sorted(unique_words, key=lambda x: x[1])
    if len(sorted_words) >= 3:
        most_freq_words = sorted_words[-3:]
    else:
        most_freq_words = sorted_words
    top_3 = [word[0] for word in most_freq_words[::-1]]
    return top_3


print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""))