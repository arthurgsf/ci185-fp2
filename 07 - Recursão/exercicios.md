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

# Exercícios (Recursão)

---
# Fibonacci
Implemente uma função recursiva para calcular fib(n).
$$
\begin{cases}
fib(n) = fib(n - 1) + fib(n - 2) \text{ , se } n > 1 \\ \\
fib(1) = 1 \\ \\
fib(0) = 0
\end{cases}
$$
---
# Fibonacci
```python
def fib(n):
    ...
```

---
# Fatorial
Implemente uma função recursiva para calcular $n!$

$$
\begin{cases}
n! = n \cdot (n -1)! \text{ , se } n > 0 \\ \\
0! = 1
\end{cases}
$$

---
# Fatorial
```python
def fact(n):
    ...
```

---
# Fatorial Iterativo
Implemente a versão iterativa da função fatorial do exercício 2.

---
# Fibonacci Iterativo
Implemente a versão iterativa da função fibonacci do exercício 1.