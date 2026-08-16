# Descubra se um dado é viciado: lance-o n vezes e **determine o número de ocorrências de cada face**.
import random

n = int(input("n: "))
faces = [0] * 6 # a lista irá conter 6 espaços (um para contar as ocorrências de cada face)

for i in range(n):
    lancamento = random.randint(0, 5) # simula lançamento de dado com 6 possibilidades
    faces[lancamento] += 1

print("===== resultados =====")
for i in range(len(faces)):
    print(f"{i} - {faces[i]}")
print(f"diferenca max: {max(faces) - min(faces)}")