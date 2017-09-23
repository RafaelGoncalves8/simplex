# Simplex
Linear programming solving algorithm. Project for EA044 course.
Implemented in Python 3.

## Usage:

This package can be used for solving simple linear programming problems that don't need to be solved as fast as possible..

### For solving an LP optimization problem:

Type in the folder where the file is: `python -m main`.  
Then give the coefficients of the function being minimized and type enter. Then on each line give the constraints coefficients and value separeted by spaces and type enter 2 times. Each constraint must be separated pressing enter once.  
The program should return the steps it took to solve the problem as well as the solution.    

Obs: If you want to type the problem in a text file you can use it by typing: `python -m main < <file>`  
Where <file> is the file with the coefficients of the objective function in the first line and each constraint in the subsequent lines. Don't forget to put 2 blank lines in the end of the file.  

### For using the tableau or simplex class in lib folder:

You can import simplex in python by typing

## Examples:
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
