import numpy as np


def gausse_jordan(matrix):
    a = np.delete(matrix, matrix.shape[1]-1, 1)
    b = np.array(matrix[:, matrix.shape[1]-1], float)
    b = b.reshape(len(b), 1)
    print(a.shape)
    n = len(b)
    for k in range(n):
        a_kk = a[k][k]
        b[k] = b[k] / a_kk
        for j in range(k, len(a[k])):
            a[k][j] = a[k][j] / a_kk  # transformacja wiersza, gdzie na przekątnej ma być 1
        for i in range(n):  # k+1 bo i != k
            if a[i][k] != 0 and i != k:  # jeżeli 0 to skipuje wiersz
                a_i_k = a[i][k]
                b[i] = b[i] - a_i_k * b[k]
                for j in range(k, len(a[k])):
                    a[i][j] = a[i][j] - a_i_k * a[k][j]

    return a, b


"""
układ równiań:
__
| x + y + 2z = -1
| 2x - y + 2z = -4
| 4x + y + 4z = -2
|--
"""
# matrix = np.array([
#     [1, 1, 2, -1],
#     [2, -1, 2, -4],
#     [4, 1, 4, -2],
# ], float)
matrix = np.array([
    [1, 1, -2, 1, 2],
    [0, 2, -1, 2, -1],
    [2, -3, 0, -2, 0],
    [4, 1, -2, -1, 1],
],float)
a_new, b_new = gausse_jordan(matrix)
print(a_new)
print(b_new)