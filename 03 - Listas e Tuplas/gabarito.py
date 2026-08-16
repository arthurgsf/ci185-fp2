gabarito = input("Gabarito: ")
resposta = input("Resposta: ")

gabarito = list(gabarito)
resposta = list(resposta)

count = 0
for i in range(len(gabarito)):
    if(gabarito[i] == resposta[i]):
        count += 1

print(f"{count}/{len(gabarito)}")