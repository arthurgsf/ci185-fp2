import math

def receber_ponto(n):
    coordenadas = []
    for i in range(n):
        while True:
            print(f"insira a coordenada {i + 1}: ")
            try:
                c = float(input(f"c{i}: "))
                coordenadas.append(c)
                break
            except:
                print("algo deu errado! re-insira as coordenadas.")
    return coordenadas

n = int(input("insira a qtd. de dimensões (n): "))

print("========== ponto 1 ==========")
p1 = receber_ponto(n)

print("========== ponto 2 ==========")
p2 = receber_ponto(n)

distance = math.dist(p1, p2)

print(distance)