def solution(x, y):
    """"""
    # defining size of triangle based on largest input value
    if x > y:
        n = 2 * x
    else:
        n = 2 * y

    # generating Floyd triangle
    num = 1
    rows = {}
    for row in range(1, n + 1):
        cols = {}
        for col in range(1, row + 1):
            cols[col] = str(num)
            num += 1
        rows[row] = cols

    # generating prison triangle
    id_list = {}
    for x_id in range(1, n + 1):
        y_id = 1
        y_list = {}
        for row in range(1, n + 1):
            if len(rows[row]) >= x_id:
                y_list[y_id] = rows[row][x_id]
                y_id += 1
            else:
                pass
        id_list[x_id] = y_list

    return str(id_list[x][y])

print(solution(1000, 1000))