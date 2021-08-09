def expanded_form(num):
    counter = len(str(num))
    number_str = []
    for number in str(num):
        if number != '0':
            number_str.append(number + '0' * (counter - 1))
            counter -= 1
        else:
            counter -= 1
            continue

    result = " + ".join(number_str)
    return result


expanded_form(70304)