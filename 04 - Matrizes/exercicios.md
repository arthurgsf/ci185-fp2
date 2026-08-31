# 1. Receber uma matriz como input
Crie uma função que receba uma matriz de inteiros a partir do input.

> OBS: Não precisa ser tudo em um input só =D

# 2. Printar a matriz de maneira formatada
$$
\begin{matrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{matrix}
$$

# 3. Calcular a soma da diagonal principal
>OBS: Aceitar apenas matriz quadrada
$$
\begin{matrix}
\textbf{1} & 2 & 3\\
4 & \textbf{5} & 6\\
7 & 8 & \textbf{9}
\end{matrix}
$$

# 4. Verificar se é triangular
Uma matriz triangular possui todos os elementos acima ou abaixo da diagonal principal iguais à zero.

$$
\begin{bmatrix}
\textbf{1} & 0 & 0\\
4 & \textbf{5} & 0\\
7 & 8 & \textbf{9}
\end{bmatrix}
\qquad
\begin{bmatrix}
\textbf{1} & 2 & 3\\
0 & \textbf{5} & 6\\
0 & 0 & \textbf{9}
\end{bmatrix}
$$

# 5. Calcular a transposta de uma matriz
$$
M= 
\begin{bmatrix}
\textbf{1} & 2 & 3\\
4 & \textbf{5} & 6\\
7 & 8 & \textbf{9}
\end{bmatrix}
,
\qquad
M^T =
\begin{bmatrix}
\textbf{1} & 4 & 7\\
2 & \textbf{5} & 8\\
3 & 6 & \textbf{9}
\end{bmatrix}
$$

# 6. Multiplicar matrizes de tamanho arbitrário
Receba duas matrizes `mat1` e `mat2` como entrada e (se for possível) calcule o resultado da sua multiplicação. Caso não seja possível informe ao usuário.
> OBS : duas matrizes só podem ser multiplicadas se o número de colunas de `mat1` for igual ao número de linhas de `mat2`.

> OBS: Se, por exemplo, `mat1` for de tamanho $3 \times 2$ e `mat2` for de tamanho $2 \times 3$ A matriz resultante terá tamanho $3 \times 3$.

Exemplo: 
$$
T_{2 \times 3} \times S_{3 \times 2} = R_{2 \times 2}
$$

$$
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6
\end{bmatrix}

\times

\begin{bmatrix}
1 & 2 \\
3 & 4 \\
5 & 6
\end{bmatrix}

=

\begin{bmatrix}
22 & 28 \\
49 & 64
\end{bmatrix}
$$