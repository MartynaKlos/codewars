# You are given a table, in which every key is a stringified number, and each corresponding value is an array of characters, e.g.
#
# {
#   "1": ["A", "B", "C"],
#   "2": ["A", "B", "D", "A"],
# }
#
# Create a function that returns a table with the same keys, but each character should appear only once among the value-arrays, e.g.
#
# {
#   "1": ["C"],
#   "2": ["A", "B", "D"],
# }
#
# Rules
#
# Whenever two keys share the same character, they should be compared numerically, and the larger key will keep that character.
# That's why in the example above the array under the key "2" contains "A" and "B", as 2 > 1.
# If duplicate characters are found in the same array, the first occurrence should be kept.

# ISSUE: Kata seems to have an error, by which some solutions in tests are sorted via key in an ascending order and some in an
# descending order. There seems to be no rule to it. I wasn't able to submit my solution because of it.


def remove_duplicate_ids(obj):
    for key, array in obj.items():
        array_uniques = list(dict.fromkeys(array))
        obj[key] = array_uniques

    for array in obj.values():
        for element in array:
            for key in obj:
                if array != obj[key]:
                    if element in obj[key]:
                        if int(key) > int(list(obj.keys())[list(obj.values()).index(array)]):
                            array.remove(element)
                        else:
                            obj[key].remove(element)

    ordered_obj = {}

    for key in sorted(obj):
        ordered_obj[key] = obj[key]

    return ordered_obj




a = {
    "1": ["A", "B", "C"],
    "2": ["A", "B", "D", "A"],
}

b = {
    "1": ["C", "F", "G"],
    "2": ["A", "B", "C"],
    "3": ["A", "B", "D"],
}





