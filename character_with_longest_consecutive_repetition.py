# For a given string s find the character c (or C) with longest consecutive repetition and return:
#
# (c, l)
#
# where l (or L) is the length of the repetition. If there are two or more characters with the same l return
# the first in order of appearance.
#
# For empty string return:
#
# ('', 0)

def longest_repetition(chars):
    counts = []
    start = 0
    chars_list = chars
    for char in chars_list:
        count = 0
        index = chars_list.index(char)
        while index < len(chars_list) and chars_list[index] == char:
            count += 1
            index += 1
        counts.append((char, count))
        start += 1
        chars_list = chars[start:]

    sorted_counts = sorted(counts, key=lambda x: (-x[1], x[0]))

    return sorted_counts[0]


print(longest_repetition("bbbaaabaaaa"))