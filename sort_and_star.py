# You will be given a vector of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.
#
# The returned value must be a string, and have "***" between each of its letters.
#
# You should not remove or add elements from/to the array.


def two_sort(array):
    sorted_array = sorted(array)
    second_array = []
    for word in sorted_array:
        if word[0].isupper():
            second_array.append(word)
    if len(second_array) > 0:
        result = "***".join(list(sorted(second_array)[0]))
    else:
        result = "***".join(list(sorted_array[0]))
    return result
