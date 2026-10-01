---
marp: true
theme: uncover
paginate: true
header: Fundamentos de Programação II - Universidade Federal do Paraná
footer: Prof. Arthur Fernandes
style: |
  section {
    font-family: 'Courier Prime', sans-serif;
  }
---
# Exercício

---
# Experimento
Montar um experimento empírico que compare fibonacci recursivo com fibonacci iterativo.

---
## Medir Tempo de Execução
```python
def fib_recursivo(n):
  ...

import time
t_start = time.time()
fib_recursivo(10)
t_end = time.time()

print(t_end)
```

---
## Calcular Média
Executar e medir o algoritmo 10x, e printar o tempo médio dentre as 10 execuções.

---
## Tempo (t) x  Entrada (n)
Iremos plotar um gráfico com uso da biblioteca matplotlib.

```bash
$ pip3 install matplotlib
```

---
## Exemplo de Plot
```python
import matplotlib.pyplot as plt
    
plt.figure(figsize=(8, 5))
plt.title("Exemplo")
plt.xlabel('n')
plt.ylabel('T')
plt.grid(True)

# cores: (r, g, b, c, m, y)
plt.plot([1, 2, 3], [1, 2, 3], marker='o', linestyle='-', color='g')
plt.plot([1, 2, 3], [4, 5, 6], marker='o', linestyle='-', color='y')

plt.show()
```

---
# Exercício
1. Rodar Fib Recursivo com n variando de [0, 30] e guardar os tempos médios (10x) em uma lista.

---
# Exercício
2. Rodar Fib Iterativo com n variando de [0, 30] e guardar os tempos médios (10x) em uma lista.

---
# Exercício
3. Comparar as duas "curvas" em um plot

---
# Memoization
Utilizaremos um dicionário para guardar valores previamente calculados.

---
```python
memo = {
    1: 1,
    0: 0
}

def fib_memo(n):
    if n in memo:
        return memo[n]
    else:
        result = fib_memo(n - 1) + fib_memo(n - 2)
        memo[n] = result
        return result
```
---
# Utilizar Memoization
4. Adicionar memoization ao fib recursivo para comparar o desempenho com o fib iterativo.