import math

def receber_e_validar_angulo():
    graus = float(input("graus: "))
    
    if graus < 0 or graus > 360:
        raise ValueError("graus precisa estar entre [0, 360]")

    return graus

while True:
    try:
        graus = receber_e_validar_angulo()

        # converter de graus para rad
        rad = math.radians(graus)
        print(rad)
        break
            
    except Exception as ex:
        print(ex)
        # além de printar podemos:
        # salvar no banco de dados
        # salvar no arquivo de logs
        # add para uma estatística
        # etc ...