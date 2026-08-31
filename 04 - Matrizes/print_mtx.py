def recebe_mat(m, n):
    mat = []
    for i in range(m):
        linha = []
        for j in range(n):
            x = int(input(f"insira o elemento [{i}][{j}]"))
            linha.append(x)
        mat.append(linha)
    return mat

m = 4
n = 4
mat = recebe_mat(m, n)

for i in range(m):
    linha = ""
    for j in range(n):
        print(mat[i][j], end = "")
    print(linha)