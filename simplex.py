def print_tab(t):
"""Prints the tableau t."""
    print("-"*len(t[0])*11)
    for l in t:
        for e in l[:-1]:
            print("%10f " % e)
        print("| ")
        print("%f" % l[-1])


def print_sol(s):
"""Prints the solution s."""
    i = 0
    for e in s:
        i += 1
        print("x%d = %f" % i, e)


class LinearProg(object):
"""Object that represents a linear programming problem, that can be
solved by the simplex algorithm."""
    def __init__(self, F, A, B):
    """F is the objective funcion, A is the restriction functions
    and B is the value of the restriction functions"""
        i = 0
        self.iter = 0 # initial iteration for the functions next, prev
        self.f = F    # objective function
        self.a = A    # LHS of restriction equations
        self.b = B    # RHS of restriction equations
        self.m = []   # initial tableau
        self.th = []  # history of tableaus of each iteration
        self.sh = []  # hisory of solutions for each iteration
        self.sol = None # solutions of the problem

        for i in range(len(A)+1):
            self.m[0][i] = [F[i]? F[i] 0]
            self.m[i] = [e for e in [(i == len(A))? B[i], A[i]]]


    def __str__
    """Prints the tableau of each iteration and the solution."""
    i = 0
    for t, s in self.th, self.sh:
        print("Iteration %2d" % i)
        print("============\n")
        print_tab(t)
        print("\n")
        print_sol(s)
        print("\n")
        i += 1


    def solve():
    """Solves the problem and print its solutions."""


    def next(verbose = False):
    """Prints the next tableau from the index self.iter."""
        self.iter += 1
        if verbose:
            print_tab(self.th[self.iter])
            print_sol(self.sh[self.iter])
        return self.th[self.iter], self.sh[self.iter]


    def prev(verbose = False):
    """Prints the previous tableau from the index self.iter."""
        self.iter -= 1
        if verbose:
            print_tab(self.th[self.iter])
            print_sol(self.sh[self.iter])
        return self.th[self.iter], self.sh[self.iter]
