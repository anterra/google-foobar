import numpy as np

def solution(x, y):
    """ Takes 2 integer inputs, x and y. Returns the ID of the prisoner located at
    the input coordinates (x, y) within a triangle shaped prison, as a string.

    In its current form, solution is failing hidden test cases 3 and 4. Had I had
    more time, I would have turned the lists into generators to conserve memory, as I
    would guess its failing due to taking too long to execute for larger inputs.
    Just not sure how to implement that yet. But hey, I only learned to code 2 months ago.
    Thanks for the fun challenge!

    "(Large datasets shouldn't be a problem unless) naive use makes many small appends" """

    # determining size of prison to create based on input
    if x > y:
        n = x * 2
    else:
        n = y * 2

    # defining a function which generates the triangular numbers, using it to create a list of triangular numbers
    # and then initializing the prison with the triangular number list as the first row (y = 1)
    def triangles(i):
        return (i ** 2 + i) // 2

    first_row = np.array([triangles(ix) for ix in range(1, n)])
    prison_triangle = np.array([first_row])

    # generating the additional rows in the prison up to the specified size
    for row_add_value in range(1, n):
        next_row = np.array([val + np.where(first_row == val) + row_add_value for val in first_row])
        first_row = next_row
        prison_triangle.append(next_row)

    return str(prison_triangle[y - 1][x - 1])

print(solution(2, 3))

# def solution(x, y):
#    """ Alternate version using only dictionaries. Also failed hidden
#    test cases 3 and 4. """

# generating Floyd triangle
#    (n defined as above.)
#    num = 1
#    rows = {}
#    for row in range(1, n + 1):
#        cols = {}
#        for col in range(1, row + 1):
#            cols[col] = num
#            num += 1
#        rows[row] = cols

# generating prison triangle
#    id_list = {}
#    for x_id in range(1, n + 1):
#        y_id = 1
#        y_list = {}
#        for row in range(1, n + 1):
#            if len(rows[row]) >= x_id:
#                y_list[y_id] = rows[row][x_id]
#                y_id += 1
#            else:
#                pass
#        id_list[x_id] = y_list

#    return str(id_list[x][y])
