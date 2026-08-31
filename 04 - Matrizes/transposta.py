m = 3
n = 3

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(m):
    for j in range(n):
        if i > j:
            aux = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = aux
print(mat)