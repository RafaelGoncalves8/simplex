# Simplex
Linear programming solving algorithm. Project for EA044 course.
Implemented in Python 3.

## Usage:

This package can be used for solving simple linear programming problems that don't need to be solved as fast as possible..

### For solving an LP optimization problem:

Type in the terminal in the same folder where the file main.py is:  
`python -m main`.  
Then give the coefficients of the function being minimized and type enter. Then on each line give the constraints coefficients and value separeted by spaces and type enter 2 times. Each constraint must be separated pressing enter once.  
Make sure to give the constraints in the standard minimization format.
The program should return the steps it took to solve the problem as well as the solution if any.    

The standard format is when the objective function is of minimization and the constraints are equalities with additional variables added for representing inequalities    

Obs: If you want to type the problem in a text file you can use it by typing:  
`python -m main < <file>`  
Where <file> is the file with the coefficients of the objective function in the first line and each constraint in the subsequent lines. Don't forget to put 2 blank lines in the end of the file.  

### For using the tableau or simplex class in lib folder:
You can import simplex in python by typing `import lib.simplex` if you are in the same folder as main.
 - Create simplex model: `<model> = lib.Simplex(<F>, <A>, <B>)`
 - Solve model: `<model>.solve(<True|False>)` - default is False for verbosity.
 - See last tableau and solutions: `print(<model>)`

## Examples:
test/optimal
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

test/multiple
```
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

test/unbounded
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
