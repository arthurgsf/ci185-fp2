import csv

with open("teste.csv", "r", encoding="utf-8") as file:
    leitor = csv.reader(file)
    for linha in leitor:
        print(linha) # Retorna uma lista por linha