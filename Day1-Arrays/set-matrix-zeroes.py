from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    r = len(matrix)
    c = len(matrix[0])

    r_ = set()
    c_ = set()

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                r_.add(i)
                c_.add(j)

    for i in range(r):
        for j in range(c):
            if i in r_ or j in c_:
                matrix[i][j] = 0

    return matrix

matrix = [[0,2,3,0],[1,2,3,4], [1,2,3,4]]
res = setZeros(matrix)