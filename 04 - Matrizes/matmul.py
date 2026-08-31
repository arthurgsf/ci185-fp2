mat1 = [
    [1, 2, 3],
    [4, 5, 6]
]
m1 = 2
n1 = 3

mat2 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

m2 = 3
n2 = 2

mat_result = []
for i in range(m1):
    linha = []
    for j in range(n2):
        res = 0
        for k in range(n1):
            res += mat1[i][k] * mat2[k][j]
        linha.append(res)
    mat_result.append(linha)

print(mat_result)