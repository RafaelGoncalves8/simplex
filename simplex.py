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


class Simplex(object):
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
        self.t_hist = [] # history of tableaus of each iteration
        self.s_hist = [] # hisory of solutions for each iteration
        self.sol = None  # solution of the problem
        self.offset = 0  # offset for where ends phase1 and begins pase2

        for i in range(len(A)+1):
            self.m[0][i] = [F[i] if len(F) > i else 0]
            self.m[i] = [e for e in [B[i] if (i == len(A)) else A[i]]]


    def __str__(self):
        """Prints the tableau of each iteration and the solution."""
    i = 0
    for t, s in zip(self.t_hist, self.s_hist):
        print("Iteration %2d" % i)
        print("============\n")
        print_tab(t)
        print("\n")
        print_sol(s)
        print("\n")
        i += 1


    def phase1(self, verbose):
        """First phase of the simplex algorithm."""
        if verbose:
            print("Phase 1:\n")
        self.iter += 1

        self.offset = self.iter


    def phase2(self, init, verbose):
        """Second phase of the simplex algorithm."""
        while (any(n < 0 for n in M[:-1])):
            if verbose:
                print("Phase 2:\n")
            self.iter += 1

            # min coefficient enters base

            min_coef = 0 # minimum coefficient in the objective function
            enter = None # index in the list self.sol of the variable with
                         # minimum coefficient

            for i in len(M[0][:-1]):
                if (e = M[0][i] < min_coef):
                    enter = i
                    min_coef = e

            # min value drops base

            min_val = 0  # minimum value in RHS/(enter colum)
            drop = None  # index in the list self.sol of the variable with
                         # minimum positive value

            for i in len(M[:-1]):
                if (M[i][enter] != 0 and e = M[i][-1]/M[i][enter] and a > 0):
                    drop = i
                    min_val = e

            # escalonate matrix M

            [M[drop][i] = M[drop][i]/M[drop][enter] for i in range(len(M))] 

            for l in M:
                if l != M[drop]:
                    [l[i] = l[i] - M[drop][i] for i in range(len(M))]


    def solve(self, verbose = False):
        """Solves the problem and print its solutions."""
        return self.sol


    def next(self, verbose = False):
        """Prints the next tableau from the index self.iter."""
        self.iter += 1
        if verbose:
            print_tab(self.t_hist[self.iter])
            print_sol(self.s_hist[self.iter])
        return self.t_hist[self.iter], self.s_hist[self.iter]


    def prev(self, verbose = False):
        """Prints the previous tableau from the index self.iter."""
        self.iter -= 1
        if verbose:
            print_tab(self.t_hist[self.iter])
            print_sol(self.s_hist[self.iter])
        return self.t_hist[self.iter], self.s_hist[self.iter]
