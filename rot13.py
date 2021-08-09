uppercase_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']


def rot13(message):
    list_message = list(message)
    coded_message = []

    for letter in list_message:
        if letter in uppercase_list:
            index = uppercase_list.index(letter) + 13
            if uppercase_list.index(letter) > 12:
                index = 13 - (len(uppercase_list) - uppercase_list.index(letter))
            coded_message.append(uppercase_list[index])
        elif letter in lowercase_list:
            index = lowercase_list.index(letter) + 13
            if lowercase_list.index(letter) > 12:
                index = 13 - (len(lowercase_list) - lowercase_list.index(letter))
            coded_message.append(lowercase_list[index])
        else:
            pass

    message2 = "".join(coded_message)

    return coded_message


# rot13("Test")


