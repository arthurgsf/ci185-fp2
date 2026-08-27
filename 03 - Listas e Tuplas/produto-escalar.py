import math

def recebe_vetor(n_dim):
    while True:
        try:
            lista_string = input("vetor: ").split(",")
            lista_float = []
            if (len(lista_string) != n_dim):
                continue
            for s in lista_string:
                lista_float.append(float(s))
            
            return lista_float
        except:
            print("algo deu errado, reinsira o vetor.")

n_dim = int(input("n_dim"))
v1 = recebe_vetor(n_dim)
v2 = recebe_vetor(n_dim)

pe = 0
for i in range(n_dim):
    pe += v1[i] * v2[i]

print(f"PE : {pe}")

mod_v1 = math.hypot(v1)
mod_v2 = math.hypot(v2)
frac = pe/(mod_v1 * mod_v2)
theta = math.arccos(frac)

print(f"theta: {theta}")