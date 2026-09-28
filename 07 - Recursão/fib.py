def fibonacci_recursivo(n):
    if(n == 1):
        return 1
    elif (n == 0):
        return 0
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_iterativo(n):
    penultimo = 0
    ultimo = 1
    for i in range(2, n + 1):
        soma = penultimo + ultimo
        penultimo = ultimo
        ultimo = soma
    return soma