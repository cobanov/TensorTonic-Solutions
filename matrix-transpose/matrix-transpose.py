import numpy as np

def matrix_transpose(A):

    rows = len(A)

    cols = len(A[0])

    AT = []

    for j in range(cols):

        new_row = []

        for i in range(rows):

            new_row.append(A[i][j])

        AT.append(new_row)

    return np.array(AT)