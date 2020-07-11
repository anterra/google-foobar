from collections import deque


def solution(x, y):
    """"""

    # defining size of triangle based on largest input value
    if x > y:
        n = 2 * x
    else:
        n = 2 * y

    my_num = 1

    def increment(number):
        number += 1
        return number

    # generating Floyd triangle
    num = 1
    rows = {}
    for row in range(1, n + 1):
        cols = {}
        for col in range(1, row + 1):
            cols[col] = num
            num += 1
        rows[row] = cols

    rows2 = {row_2: {col_2: increment(my_num) for col_2 in range(1, row_2 + 1) for my_num in range(col_2)} for row_2 in range(1, n+1)}


    print(rows2)

    # generating prison triangle
    # id_list = {}
    # for x_id in range(1, n + 1):
    #    y_id = 1
    #    y_list = {}
    #    for row in range(1, n + 1):
    #        if len(rows[row]) >= x_id:
    #            y_list[y_id] = rows[row][x_id]
    #            y_id += 1
    #        else:
    #            pass
    #    id_list[x_id] = y_list


    id_list_2 = {x_id_2: {increment(y_id_2): rows[row_2][x_id_2] if len(rows[row_2]) >= x_id_2
                    else None for y_id_2 in range(0, n + 1) for row_2 in range(1, n + 1)} for x_id_2 in range(1, n + 1)}

    print(rows)
    # print(id_list)
    print(id_list_2)

    # return str(id_list[x][y])


print(solution(2, 2))
