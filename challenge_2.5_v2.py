#def solution(x, y):


def floyd(rowcount):
    rows = [[1]]
    while len(rows) < rowcount:
        n = rows[-1][-1] + 1
        rows.append(list(range(n, n + len(rows[-1]) + 1)))
    return rows


def pfloyd(rows):
    colspace = [len(str(n)) for n in rows[-1]]
    for row in rows:
        print(" ".join("%*i" % space_n for space_n in zip(colspace, row)))


print(floyd(4))


def floyd2(rowcount):
    the_list = [list(range(i * (i - 1) // 2 + 1, i * (i + 1) // 2 + 1))
                for i in range(1, rowcount + 1)]

    the_dict = {i: list(range(i * (i - 1) // 2 + 1, i * (i + 1) // 2 + 1))
                for i in range(1, rowcount + 1)}

    print(the_list)
    print(the_dict)


print(floyd2(5))
