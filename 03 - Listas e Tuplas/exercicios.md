# 1. Definir se uma lista está ordenada
Receber uma lista de `float` separados por vírgula e printar `True` caso esteja ordenada em ordem crescente e `False` caso contrário.
Exemplo de input:
```bash
$ 1.2,3.4,5,6.4,5
```

> **OBS1**: deverá realizar validação de input via loop de validação.

> **OBS2**: deverá receber os números em `um input só`. 

> Para isso utilize : `input().split(",")`.


# 2. Inverter String
Receber uma string `s` e invertê-la.

1. Proibido utilizar `s.reverse()`.
2. Proibido iterar por `s` utilizando `for`.
3. Proibido utilizar indexação `s[i]`.


# 3. Interpolar duas strings
Receber uma string `s1` e outra `s2` e construir uma string `s3` que seja uma **interpolação das duas**. Exemplo:
```bash
$ s1: abcdefg
$ s2: 123
$ s3 -> a1b2c3defg
```
> **OBS**: deve permitir strings de tamanhos diferentes.

# [Extra] Calcular o ângulo entre dois vetores v1 e v2
Faça um algoritmo que:
* Receba o número de dimensões dos vetores `n_dim`. **(10 pts)**

* Receba dois vetores de entrada, com **n dimensões** no formato $c_1, c_2, c_3, c_4 ... c_n$. Com as coordendas separadas por vírgula, utilize `input("vetor: ").split(",")` para receber o vetor em um input só. **(30 pts)**

* **Modularize** o recebimento de vetor criando uma função que recebe `n_dim` como parâmetro e **devolve um vetor de n dimensões**. **(20pts)**

* Faça a validação da entrada utilizando loop de validação. Não serão aceitos vetores de tamanho diferente de `n_dim`. **(20pts)**

* Calcule o **produto escalar** $\vec{v_1} \cdot \vec{v_2}$ **sem usar biblioteca** e exiba na tela. **(20 pts)**

* Calcule o ângulo entre os dois vetores utilizando `math.arccos` em conjunto com as fórmulas abaixo, e imprima na tela. **Dica**: utilize `math.hypot(v1)` para calcular o **módulo** de um vetor. **(20pts)**

$$
\vec{v_1} \cdot \vec{v_2} = |v_1| |v_2| cos(\theta)
$$

$$
\theta = arccos(\frac{\vec{v_1} \cdot \vec{v_2}}{|v_1| |v_2|})
$$