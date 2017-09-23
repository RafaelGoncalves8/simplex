# Simplex
__Nome__: Rafael Gonçalves --- __RA__: 186062  

Algoritimo para calculo de problema de programação linear desenvolvido para a matéria EA044 e implementado usando Python 3.

## Uso:

No terminal, na mesma pasta que o arquivo main.py digite:  
`python -m main`.  
Dê os coeficientes da função objetivo a ser minizada, em seguida os coeficientes das restrições e seu valor rhs na mesma linha, separada por espaços. Cada restrição deve estar em uma linha e separada por um Enter. Feito isso aperte Enter 2 vezes e o algoritimo deve resolver o problema.
O problema deve estar na forma padrão para ser minizado.  
**Obs:** Para usar com um arquivo de texto, digite:  
`python -m main < <file>`  
Onde <file> é o arquivo de texto como descrito acima, com a função objetivo na primeira linha e cada restrição nas linhas subsequentes. Não esqueça de adicionar 2 linhas vazias no fim do arquivo.

_Exemplo_:  

[lib/zero_not_feasible]
```
1 2 0 0 0
1 1 -1 0 0 2
-1 1 0 -1 0 1
0 1 0 0 -1 3

```

### Examplos:

### Teste 1:

Minimizar  $v = -3x_0 -2x_1$  
Sujeito a:  
$2x_0 + 1x_1 +1x_2 \quad \quad \quad \quad \quad \quad = 18$  
$2x_0 + 3x_1 \quad \quad \quad+ 1x_3 \quad \quad \quad = 42$  
$3x_0 + 1x_1 \quad \quad \quad \quad \quad \quad +1x_4 = 24$  

Solução:

[test/optimal]
```
Give the coefficients of the objective function being minimized
>-3 -2 0 0 0 
Give the coefficients of the left hand size of the constraints and the right hand size of the constraints in order
>2 1 1 0 0 18
>2 3 0 1 0 42
>3 1 0 0 1 24
>
All non-basic variables in 0 is possible
solution.

...skipping phase 1.

Initializing phase 2.
Iteration 0
  1 |    -3.00 |    -2.00 |     0.00 |     0.00 |     0.00 |     0.00 |
------------------------------------------------------------------------
 x2 |     2.00 |     1.00 |     1.00 |     0.00 |     0.00 |    18.00 |
 x3 |     2.00 |     3.00 |     0.00 |     1.00 |     0.00 |    42.00 |
 x4 |     3.00 |     1.00 |     0.00 |     0.00 |     1.00 |    24.00 |

v = 0.00, x1 = 0.00, x2 = 0.00, x3 = 18.00, x4 = 42.00, x5 = 24.00

Enter: x0
Leave: x4


Iteration 1
  1 |     0.00 |    -1.00 |     0.00 |     0.00 |     1.00 |    24.00 |
------------------------------------------------------------------------
 x2 |     0.00 |     0.33 |     1.00 |     0.00 |    -0.67 |     2.00 |
 x3 |     0.00 |     2.33 |     0.00 |     1.00 |    -0.67 |    26.00 |
 x0 |     1.00 |     0.33 |     0.00 |     0.00 |     0.33 |     8.00 |

v = -24.00, x0 = 8.00, x1 = 0.00, x2 = 2.00, x3 = 26.00, x4 = 0.00

Enter: x1
Leave: x2


Iteration 2
  1 |     0.00 |     0.00 |     3.00 |     0.00 |    -1.00 |    30.00 |
------------------------------------------------------------------------
 x1 |     0.00 |     1.00 |     3.00 |     0.00 |    -2.00 |     6.00 |
 x3 |     0.00 |     0.00 |    -7.00 |     1.00 |     4.00 |    12.00 |
 x0 |     1.00 |     0.00 |    -1.00 |     0.00 |     1.00 |     6.00 |

v = -30.00, x0 = 6.00, x1 = 6.00, x2 = 0.00, x3 = 12.00, x4 = 0.00

Enter: x4
Leave: x3


Iteration 3
  1 |     0.00 |     0.00 |     1.25 |     0.25 |     0.00 |    33.00 |
------------------------------------------------------------------------
 x1 |     0.00 |     1.00 |    -0.50 |     0.50 |     0.00 |    12.00 |
 x4 |     0.00 |     0.00 |    -1.75 |     0.25 |     1.00 |     3.00 |
 x0 |     1.00 |     0.00 |     0.75 |    -0.25 |     0.00 |     3.00 |

v = -33.00, x0 = 3.00, x1 = 12.00, x2 = 0.00, x3 = 0.00, x4 = 3.00

...phase 2 done.

Optimal solution:
Iterations: 0 (phase 1) + 3 (phase 2) = 3
v = -33.00, x0 = 3.00, x1 = 12.00, x2 = 0.00, x3 = 0.00, x4 = 3.00

Done.

```

---

### Teste 2:

Minimizar  $v = -0.3x_0 -0.2x_1 -0.1x_2$  
Sujeito a:  
$\quad 3x_0 + 2x_1 +1x_2 +1x_3 \quad \quad \quad \quad \quad \quad= 2$  
$-1x_0 + 1x_1 \quad \quad \quad\quad \quad \quad+ 1x_4 \quad \quad \quad = 5$  
$10x_0 \quad \quad \quad + 30x_2 \quad \quad \quad \quad \quad \quad -1x_5 = 10$  

Solução:

[test/multiple]
```
Give the coefficients of the objective function being minimized
>-0.3 -0.2 -0.1 0 0 0
Give the coefficients of the left hand size of the constraints and the right hand size of the constraints in order
>3 2 1 1 0 0 2
>-1 1 0 0 1 0 5
>10 0 30 0 0 -1 10
>
Initializing phase 1.

Iteration 0
  1 |   -10.00 |     0.00 |   -30.00 |     0.00 |     0.00 |     1.00 |     0.00 |     0.00 |
----------------------------------------------------------------------------------------------
 x3 |     3.00 |     2.00 |     1.00 |     1.00 |     0.00 |     0.00 |     0.00 |     2.00 |
 x4 |    -1.00 |     1.00 |     0.00 |     0.00 |     1.00 |     0.00 |     0.00 |     5.00 |
 x6 |    10.00 |     0.00 |    30.00 |     0.00 |     0.00 |    -1.00 |     1.00 |    10.00 |



Enter: x2
Leave: x6


Iteration 1
  1 |     0.00 |     0.00 |     0.00 |     0.00 |     0.00 |     0.00 |     1.00 |    10.00 |
----------------------------------------------------------------------------------------------
 x3 |     2.67 |     2.00 |     0.00 |     1.00 |     0.00 |     0.03 |    -0.03 |     1.67 |
 x4 |    -1.00 |     1.00 |     0.00 |     0.00 |     1.00 |     0.00 |     0.00 |     5.00 |
 x2 |     0.33 |     0.00 |     1.00 |     0.00 |     0.00 |    -0.03 |     0.03 |     0.33 |



...phase 1 done.

Initializing phase 2.
Iteration 0
  1 |    -0.27 |    -0.20 |     0.00 |     0.00 |     0.00 |    -0.00 |     0.03 |
-----------------------------------------------------------------------------------
 x3 |     2.67 |     2.00 |     0.00 |     1.00 |     0.00 |     0.03 |     1.67 |
 x4 |    -1.00 |     1.00 |     0.00 |     0.00 |     1.00 |     0.00 |     5.00 |
 x2 |     0.33 |     0.00 |     1.00 |     0.00 |     0.00 |    -0.03 |     0.33 |

v = -0.03, x1 = 0.00, x2 = 0.00, x3 = 0.33, x4 = 1.67, x5 = 5.00, x6 = 0.00

Enter: x0
Leave: x3


Iteration 1
  1 |     0.00 |     0.00 |     0.00 |     0.10 |     0.00 |     0.00 |     0.20 |
-----------------------------------------------------------------------------------
 x0 |     1.00 |     0.75 |     0.00 |     0.38 |     0.00 |     0.01 |     0.62 |
 x4 |     0.00 |     1.75 |     0.00 |     0.38 |     1.00 |     0.01 |     5.62 |
 x2 |     0.00 |    -0.25 |     1.00 |    -0.12 |     0.00 |    -0.04 |     0.12 |

v = -0.20, x0 = 0.62, x1 = 0.00, x2 = 0.12, x3 = 0.00, x4 = 5.62, x5 = 0.00

...phase 2 done.

Multiple solutions
Showing one optimal solution:
Iterations: 1 (phase 1) + 1 (phase 2) = 2
v = -0.20, x0 = 0.62, x1 = 0.00, x2 = 0.12, x3 = 0.00, x4 = 5.62, x5 = 0.00

Done.
```

---

### Teste 3:

Minimizar  $v = -10x_0 -22x_1 -15x_2$  
Sujeito a:  
$1x_0 + 1x_1 -1x_2 +1x_3 \quad \quad \quad = 200$  
$-1x_0 +1x_1 \quad \quad \quad  \quad \quad \quad + 1x_4 = 10$

Solução:

[test/unbounded]
```
Give the coefficients of the objective function being minimized
>-10 -22 -15 0 0
Give the coefficients of the left hand size of the constraints and the right hand size of the constraints in order
>1 1 -1 1 0 200
>-1 1 0 0 1 10
>
All non-basic variables in 0 is possible
solution.

...skipping phase 1.

Initializing phase 2.
Iteration 0
  1 |   -10.00 |   -22.00 |   -15.00 |     0.00 |     0.00 |     0.00 |
------------------------------------------------------------------------
 x3 |     1.00 |     1.00 |    -1.00 |     1.00 |     0.00 |   200.00 |
 x4 |    -1.00 |     1.00 |     0.00 |     0.00 |     1.00 |    10.00 |

v = 0.00, x1 = 0.00, x2 = 0.00, x3 = 0.00, x4 = 200.00, x5 = 10.00

Enter: x1
Leave: x4


Iteration 1
  1 |   -32.00 |     0.00 |   -15.00 |     0.00 |    22.00 |   220.00 |
------------------------------------------------------------------------
 x3 |     2.00 |     0.00 |    -1.00 |     1.00 |    -1.00 |   190.00 |
 x1 |    -1.00 |     1.00 |     0.00 |     0.00 |     1.00 |    10.00 |

v = -220.00, x0 = 0.00, x1 = 10.00, x2 = 0.00, x3 = 190.00, x4 = 0.00

Enter: x0
Leave: x3


Iteration 2
  1 |     0.00 |     0.00 |   -31.00 |    16.00 |     6.00 |  3260.00 |
------------------------------------------------------------------------
 x0 |     1.00 |     0.00 |    -0.50 |     0.50 |    -0.50 |    95.00 |
 x1 |     0.00 |     1.00 |    -0.50 |     0.50 |     0.50 |   105.00 |

v = -3260.00, x0 = 95.00, x1 = 105.00, x2 = 0.00, x3 = 0.00, x4 = 0.00

Enter: x2
Iteration 3
  1 |     0.00 |     0.00 |   -31.00 |    16.00 |     6.00 |  3260.00 |
------------------------------------------------------------------------
 x0 |     1.00 |     0.00 |    -0.50 |     0.50 |    -0.50 |    95.00 |
 x1 |     0.00 |     1.00 |    -0.50 |     0.50 |     0.50 |   105.00 |

v = -3260.00, x0 = 95.00, x1 = 105.00, x2 = 0.00, x3 = 0.00, x4 = 0.00

...phase 2 done.

Unbounded solution
Iterations: 0 (phase 1) + 3 (phase 2) = 3
v and solutions tend to infinity.
Done.
```
