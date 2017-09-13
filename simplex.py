def string_tab(t):
    """Prints the tableau t."""
    a = ""
    a.join("-"*len(t[0])*11)
    a.join("\n")
    for l in t:
        for e in l[:-1]:
            a.join("%10f " % e)
        a.join("| ")
        a.join("%f" % l[-1])
        a.join("\n")
    a.join("\n")
    return a


def string_sol(s):
    """Prints the solution s."""
    i = 0
    a = ""
    for e in s:
        i += 1
        a.join("x%d = %f " % i, e)
    a.join("\n")
    return a


class Simplex(object):
    """Object that represents a linear programming problem, that can be
    solved by the simplex algorithm."""
    def __init__(self, F, A, B):
        """F is the objective funcion, A is the restriction functions
        and B is the value of the restriction functions"""
        self.iter = 0 # initial iteration for the functions next, prev
        self.f = F    # objective function
        self.a = A    # LHS of restriction equations
        self.b = B    # RHS of restriction equations
        self.m = []   # initial tableau
        self.t_hist = [] # history of tableaus of each iteration
        self.s_hist = [] # hisory of solutions for each iteration
        self.sol = None  # solution of the problem
        self.offset = 0  # offset for where end phase1 and begin pase2

        self.m = [[0]*(len(A[0])+1) for i in range(len(A)+1)]

        # creating tableau M 
        for i in range(len(A)+1):
            self.m[0][i] = F[i] if len(F) > i else 0
            if i != 0:
                self.m[i] = [e for e in A[i-1]+[B[i-1]]]


    def __str__(self):
        """Prints the tableau of each iteration and the solution."""
        i = 0
        th = self.t_hist
        sh = self.s_hist
        s = ""
        for t, s in zip(th, sh):
            s.join("Iteration %2d\n" % i)
            s.join("============\n\n")
            string_tab(t)
            s.join("\n\n")
            string_sol(s)
            s.join("\n\n")
            i += 1
        return s


    def phase1(self, verbose):
        """First phase of the simplex algorithm."""
        if verbose:
            print("Phase 1:\n")
        self.iter += 1

        self.offset = self.iter


    def phase2(self, init, verbose):
        """Second phase of the simplex algorithm."""
        M = self.m
        while (any(n < 0 for n in M[0][:-1])):
            if verbose:
                print("Phase 2:\n")
            self.iter += 1

            # min coefficient enters base

            min_coef = 0 # minimum coefficient in the objective func
            enter = None # index in the list self.sol of the variable
                         # with minimum coefficient

            for i in range(len(M[0][:-1])):
                if (M[0][i] < min_coef):
                    enter = i
                    min_coef = M[0][i]

            if verbose:
                print("Enter: x%d" % enter)

            # min value drops base

            min_val = 0  # minimum value in RHS/(enter colum)
            drop = None  # index in the list self.sol of the variable
                         # with minimum positive value

            for i in range(len(M[:-1])):
                if (M[i][enter] != 0 and M[i][-1]/float(M[i][enter])\
                        and M[i][-1]/float(M[i][enter]) > 0):
                    drop = i
                    min_val = M[i][-1]/float(M[i][enter])

            if verbose:
                print("Leave: x%d" % drop)

            # escalonate matrix M

            M[drop] = [M[drop][i]/M[drop][enter] for i in range(len(M))] 
            for l in M:
                if l != M[drop]:
                    l = [l[i] - M[drop][i] for i in range(len(M))]

            print(string_tab(M))


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
