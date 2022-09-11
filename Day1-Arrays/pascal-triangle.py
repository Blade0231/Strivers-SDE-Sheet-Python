def printPascal(n:int):
    res = []

    for i in range(n):
        z = [1]*(i+1)
        res.append(z)
        if i>1:
            for j in range(1,i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
    return res

res = printPascal(5)