def recebe_mat(m, n):
    mat = []
    for i in range(m):
        linha = []
        for j in range(n):
            x = int(input(f"insira o elemento [{i}][{j}]"))
            linha.append(x)
        mat.append(linha)
    return mat

m = 2
n = 2
mat = recebe_mat(m, n)

triangular_sup = True
triangular_inf = True
for i in range(m):
    for j in range(n):
        # triangular superior
        if j > i and mat[i][j] != 0:
            triangular_sup = False
            break
        if j < i and mat[i][j] != 0:
            triangular_inf = False
            break
print(triangular_inf or triangular_sup)