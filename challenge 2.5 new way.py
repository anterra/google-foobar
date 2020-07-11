def all_triangle_numbers(n):
    for i in range(1, n + 1):
        print("n = {0}, triangle = {1}".format(i, (i ** 2 + i) // 2))


def triangles(i):
    return (i ** 2 + i) // 2


def solution1(x, y):
    n = x * 2
    id_triangle = [[triangles(x) + m for x in range(1, n)] for m in range(0, n)]
    print(id_triangle)

#print(solution1(4, 4))

def solution4(x, y):
    n = x * 2
    id_triangle = [[triangles(x) + y * x for x in range(1, n)] for y in range(0, n)]
    print(id_triangle)


def solution(x, y):
    """ Takes 2 integer inputs, x and y. Returns the ID of the prisoner located at
    the input coordinates (x, y) within a triangle shaped prison, as a string """

    # determining size of prison to create based on input
    if x > y:
        n = x * 2
    else:
        n = y * 2

    # defining a function which generates the triangular numbers, using it to create a list of triangular numbers
    # and then initializing the prison with the triangular number list as the first row (y = 1)
    def triangles(i):
        return (i ** 2 + i) // 2

    triangular_nums = [triangles(ix) for ix in range(1, n)]
    prison_triangle = [triangular_nums]

    # generating the additional rows in the prison up to the specified size
    for row_add_value in range(1, n):
        next_row = [val + triangular_nums.index(val) + row_add_value for val in triangular_nums]
        triangular_nums = next_row
        prison_triangle.append(next_row)

    print(prison_triangle)
    return str(prison_triangle[y-1][x-1])


print(solution(3, 2))


def different_way(x, y):

    def triangles(i):
        return (i ** 2 + i) // 2

    if x > y:
        n = x * 2
    else:
        n = y * 2

    orig_triangles = [triangles(m) for m in range(1, n)]

    def iterate(a_triangle):
        new_triangle = [val + a_triangle.index(val) + 1 for val in a_triangle]
        a_triangle = new_triangle
        return a_triangle

    for z in range(1, n):
        new_row = [val + orig_triangles.index(val) + 1 for val in orig_triangles]
        orig_triangles = new_row


    id_triangle = [orig_triangles] + [new_row] + [[val + new_row.index(val) + iterator for val in new_row] for iterator in range(1, n)]
    print(id_triangle)


#print(different_way(4, 4))