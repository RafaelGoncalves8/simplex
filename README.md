# Simplex
Linear programming solving algorithm. Project for EA044 course.
Implemented in Python 3.

## Usage:

### For solving an LP optimization problem:

Type in the folder where the file is:  
`python -m main`
Then give the coefficients of the function being minimized and type enter. Then on each line give the constraints coefficients and value separeted by spaces and type enter 2 times. Each constraint must be separated pressing enter once.  
The program should return the steps it took to solve the problem as well as the solution.    

Obs: If you want to type the problem in a text file you can use it by typing:  
`python -m main < <file>`
Where <file> is the file with the coefficients of the objective function in the first line and each constraint in the subsequent lines. Don't forget to put 2 blank lines in the end of the file.  

## For using the tableau or simplex class in lib file:

## Examples:
