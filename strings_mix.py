def unique_letters(string):
    all_list = list(string)
    letters_list = [item.lower() for item in all_list if item.isalpha()]
    unique_set = set(letters_list)
    unique_list = sorted(list(unique_set))
    return unique_list


def join_lists(list1, list2):
    joined = list1 + list2
    set_joined = set(joined)
    result = list(set_joined)
    return result


def mix(s1, s2):
    final_pairs = []
    list1 = unique_letters(s1)
    list2 = unique_letters(s2)
    final_letters = sorted(join_lists(list1, list2))

    for letter in final_letters:
        if letter in s1 and letter in s2:
            c1 = s1.count(letter)
            c2 = s2.count(letter)
            if c1 > c2 and c1 > 1:
                final_pairs.append(['1:', letter * c1])
            elif c2 > c1 and c2 > 1:
                final_pairs.append(['2:', letter * c2])
            elif c1 == c2 and c1 > 1:
                final_pairs.append(['=:', letter * c1])
        elif letter in s1 and letter not in s2:
            c1 = s1.count(letter)
            if c1 > 1:
                final_pairs.append(['1:', letter * c1])
        elif letter in s2 and letter not in s1:
            c2 = s2.count(letter)
            if c2 > 2:
                final_pairs.append(['2:', letter * c2])

    sorted_result = sorted(final_pairs, key=lambda i: (-len(i[1]), i[1]))
    result1 = [f'{"".join(item)}/' for item in sorted_result]
    result11 = "".join(result1)
    result = str(result11[:-1])
    print(result)
    return result


s1 = " In many languages"
s2 = " there's a pair of functions"


mix(s1, s2)

