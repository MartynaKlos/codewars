def valid_solution(board):
    for row in board:
        for number in row:
            if row.count(number) > 1:
                return False

    index = 0
    numbers = []
    while index < 9:
        for row in board:
            numbers.append(row[index])
        for number in numbers:
            if numbers.count(number) > 1:
                return False
        index += 1
        numbers = []

    index2 = 0
    numbers2 = []
    while index2 < 3:
        for row in board[0:3]:
            numbers2.append(row[index2])
        index2 += 1
    if numbers2 != set(numbers2):
        return False
    numbers2 = []

    index3 = 0
    numbers3 = []
    while 3 < index3 < 7:
        for row in board[4:7]:
            numbers3.append(row[index3])
        index3 += 1
    if numbers3 != set(numbers3):
        return False
    numbers3 = []

    index4 = 0
    numbers4 = []
    while 6 < index4 < 9:
        for row in board[6:9]:
            numbers4.append(row[index4])
        index4 += 1
    if numbers4 != set(numbers4):
        return False
    numbers4 = []

    return True


valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 4, 5, 2, 8, 6, 1, 7, 9]])