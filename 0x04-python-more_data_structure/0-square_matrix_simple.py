#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
<<<<<<< HEAD
    return list(map(lambda submat: list(map(lambda e: e**2, submat ), matrix)))
=======
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (new_matrix)
>>>>>>> 4a6734a88484bfa721cb9dd7f61c3db83a267411
