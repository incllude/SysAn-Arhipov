import numpy as np


def calc_matrix(A):
    rankings = {elem: idx for idx, val in enumerate(A) 
               for elem in (val if isinstance(val, list) else [val])}
    
    return [[1 if rankings[k] >= rankings[i] else 0 
            for k in rankings] for i in range(1, len(rankings) + 1)]

def calc_uhoh(X, Y):
    X, Y = np.array(X), np.array(Y)
    print(np.logical_or(X * Y, X.T * Y.T))


A = [1, [2, 3], 4, [5, 6, 7], 8, 9, 10]
B = [[1, 2], [3, 4, 5], 6, 7, 9, [8, 10]]

A = calc_matrix(A)
B = calc_matrix(B)

calc_uhoh(A, B)
