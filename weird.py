def in_array(array1, array2):
    x = []
    for item in array1:
        for item2 in array2:
            if item in item2:
                if item in x:
                    continue
                else:
                    x.append(item)
            else:
                continue
    sorted_x = sorted(x)
    return sorted_x


a1 = ["arp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
in_array(a1, a2)