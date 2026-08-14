import math

def receber_e_validar_ponto():
    while True:
        try:
            x = float(input("x: "))
            y = float(input("y: "))
            z = float(input("z: "))

            ponto = (x, y, z)

            return ponto
        except:
            print("algo deu errado! re-insira as coordenadas.")

print("========== ponto 1 ==========")
p1 = receber_e_validar_ponto()

print("========== ponto 2 ==========")
p2 = receber_e_validar_ponto()

distance = math.dist(p1, p2)

print(distance)