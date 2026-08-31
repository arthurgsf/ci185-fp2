def recebe_mat(m, n):
    mat = []
    for i in range(m):
        linha = []
        for j in range(n):
            x = int(input(f"insira o elemento [{i}][{j}]"))
            linha.append(x)
        mat.append(linha)
    return mat

m = int(input("m:"))
n = int(input("n:"))

mat = recebe_mat(m, n)

print(mat)