# 1. Definir se uma lista está ordenada
# Receber uma lista de `float` separados por vírgula e printar `True` caso esteja ordenada em ordem crescente e `False` caso contrário.
def recebe_lista():
    while True:
        try:
            lista_string = input("digite os numeros: ").split(",")
            lista_float = []
            for s in lista_string:
                lista_float.append(float(s))
            return lista_float
        except:
            print("algo deu errado, reinsira a lista")

lista_float = recebe_lista()
ordenada = True

for i in range(len(lista_float) -1):
    if lista_float[i] > lista_float[i + 1]:
        ordenada = False
        break

print(ordenada)
