import tableau

class Simplex(object):
    """Object that represents a linear programming problem that can be
    solved by the simplex algorithm."""
    def __init__(self, F, A, B):
        """F is the objective funcion, A is the restriction functions
        and B is the value of the restriction functions"""
        self.tab = tableau.Tableau(F, A, B) # main tableau
        self.iter = 0  # initial iteration for the methods next, prev
        self.hist = [] # historico de (tableaus, solutions)
        self.v    = 0  # best value for F til now
        self.sol  = [0]*len(F) # list of variables values
        self.basis = [] # variables states (1 = basis, 0 = non-basis)
        self.set_vars() # set variables initial values and states


    def __str__(self):
        """Print the iterations of the simplex steps."""
        i = 0
        s = ""
        for t, s in self.hist:
            s += ("Iteration %2d\n" % i)
            s += ("============\n\n")
            s += t.__str__()
            s += ("\n")
            s += s[0]
            s += (", " + str(e) for e in s[1])
            s += ("\n\n")
            i += 1
        return s


    def set_vars(self):
        """Set value and state (basis or not) of the vars."""
        self.v = self.tab.m[0][-1]
        for i in range(self.tab.columns -1):
            count = 0
            for j in range(self.tab.lines):
                if self.tab.m[j][i] != 0:
                    val = self.tab.m[j][-1]
                    count += 1
            if count > 1:
                self.basis.append(0) # not in basis
                self.sol[i] = 0    # initial guess
            else:
                self.basis.append(1) # in basis
                self.sol[i] = val  # value of RHS


    def solve(self, verbose = True):
        if not self.is_possible():
            if verbose:
                print("Initializing phase 1")
            self.phase1()
            if verbose:
                print("...phase 1 OK.")
        else:
            if verbose:
                print("All non-basic variables in 0 is possible",)
                print("solution.")
                print("...skipping phase 1.\n")
        print("Initializing phase 2.")
        s = self.phase2(verbose)
        if verbose:
            print("...phase 2 OK.\n")
        if s == 0:
            print("Optimal solution:")
            print("v = %f" % self.v, end="")
            for i in range(len(self.sol)):
                print(", x%d = %f" % (i+1, self.sol[i]), end="")
            return 0
        elif s == 1:
            print("Unlimited solution")
            return 1
        else:
            print("Impossible to solve")
            return 2


    def phase1(self, verbose):
        """First phase of the simplex algorithm."""
        # new = Simplex()
        new.solve()
        return 0


    def phase2(self, verbose):
        """Second phase of the simplex algorithm."""
        i = 0
        if verbose:
            print("Iteration %d" % i)
            print(self.tab)
            print("v = %f" % self.v,end="")
            for i in range(len(self.sol)):
                print(", x%d = %f" % (i+1, self.sol[i]),end="")
        while(not self.is_best()):
            i += 1
            self.hist.append((self.tab.m, self.sol))
            self.tab.m = self.iterate(verbose)
            self.set_vars()
            if verbose:
                print("Iteration %d" % i)
                print(self.tab.m)
                print("v = %f" % self.v),
                for i in range(len(s.sol)):
                    print(", x%d = %f" % (i+1, self.sol[i]))
        return 0


    def iterate(self, verbose):
        """Iteration of the simplex algorithm. One variable leaves
        the basis and another enter in its place."""
        M = self.tab.m
        X = self.sol

        # min coefficient enters basis

        min_coef = 0 # minimum coefficient in the objective func
        enter = None # index in the list self.sol of the variable
                     # with minimum coefficient

        for i in range(len(M[0][:-1])):
            if (M[0][i] < min_coef):
                enter = i
                min_coef = M[0][i]

        if verbose:
            print("Enter: x%d" % enter)

        # min value leaves basis

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

        # tableau

        M[drop] = M[drop].mult_line_by(1/float(M[drop][enter]))
        for i in range(M):
            if i != drop:
                M[i] = M.sum_to_line(i, M.mult_line_by(i, \
                        (-1*M[i][enter])*float(M[drop][enter])))

        return M


    def is_possible(self):
        """Return True if it has solution, return False otherwise."""
        for l in self.tab.m:
            val = 0
            for i in range(len(l[:-1])):
                val += (self.sol[i])*l[i]
            if val != l[-1]:
                return False
        return True


    def is_best(self):
        """Return True if is optimal solution,
        otherwise return False"""
        return any([e < 0 for e in self.tab.m[0][:-1]])


# class Simplex(object):
#     """Object that represents a linear programming problem, that can be
#     solved by the simplex algorithm."""
#     def __init__(self, F, A, B):
#         """F is the objective funcion, A is the restriction functions
#         and B is the value of the restriction functions"""
#         self.iter = 0 # initial iteration for the functions next, prev
#         self.f = F    # objective function
#         self.a = A    # LHS of restriction equations
#         self.b = B    # RHS of restriction equations
#         self.m = []   # initial tableau
#         self.t_hist = [] # history of tableaus of each iteration
#         self.s_hist = [] # hisory of solutions for each iteration
#         self.sol = None  # solution of the problem
#         self.offset = 0  # offset for where end phase1 and begin pase2
#
#         self.m = [[0]*(len(A[0])+1) for i in range(len(A)+1)]
#
#         # creating tableau M
#         for i in range(len(A)+1):
#             self.m[0][i] = F[i] if len(F) > i else 0
#             if i != 0:
#                 self.m[i] = [e for e in A[i-1]+[B[i-1]]]
#
#
#     def __str__(self):
#         """Prints the tableau of each iteration and the solution."""
#         i = 0
#         th = self.t_hist
#         sh = self.s_hist
#         s = ""
#         for t, s in zip(th, sh):
#             s.join("Iteration %2d\n" % i)
#             s.join("============\n\n")
#             string_tab(t)
#             s.join("\n\n")
#             string_sol(s)
#             s.join("\n\n")
#             i += 1
#         return s
#
#
#     def phase1(self, verbose):
#         """First phase of the simplex algorithm."""
#         if verbose:
#             print("Phase 1:\n")
#         self.iter += 1
#
#         self.offset = self.iter
#
#
    # def phase2(self, init, verbose):
    #     """Second phase of the simplex algorithm."""
    #     M = self.m
    #     while (any(n < 0 for n in M[0][:-1])):
    #         if verbose:
    #             print("Phase 2:\n")
    #         self.iter += 1
    #
    #         # min coefficient enters base
    #
    #         min_coef = 0 # minimum coefficient in the objective func
    #         enter = None # index in the list self.sol of the variable
    #                      # with minimum coefficient
    #
    #         for i in range(len(M[0][:-1])):
    #             if (M[0][i] < min_coef):
    #                 enter = i
    #                 min_coef = M[0][i]
    #
    #         if verbose:
    #             print("Enter: x%d" % enter)
    #
    #         # min value drops base
    #
    #         min_val = 0  # minimum value in RHS/(enter colum)
    #         drop = None  # index in the list self.sol of the variable
    #                      # with minimum positive value
    #
    #         for i in range(len(M[:-1])):
    #             if (M[i][enter] != 0 and M[i][-1]/float(M[i][enter])\
    #                     and M[i][-1]/float(M[i][enter]) > 0):
    #                 drop = i
    #                 min_val = M[i][-1]/float(M[i][enter])
    #
    #         if verbose:
    #             print("Leave: x%d" % drop)
    #
    #         # escalonate matrix M
    #
    #         M[drop] = [M[drop][i]/M[drop][enter] for i in range(len(M))]
    #         for l in M:
    #             if l != M[drop]:
    #                 l = [l[i] - M[drop][i] for i in range(len(M))]
    #
    #         print(string_tab(M))
#
#
#     def solve(self, verbose = False):
#         """Solves the problem and print its solutions."""
#         return self.sol
#
#
#     def next(self, verbose = False):
#         """Prints the next tableau from the index self.iter."""
#         self.iter += 1
#         if verbose:
#             print_tab(self.t_hist[self.iter])
#             print_sol(self.s_hist[self.iter])
#         return self.t_hist[self.iter], self.s_hist[self.iter]
#
#
#     def prev(self, verbose = False):
#         """Prints the previous tableau from the index self.iter."""
#         self.iter -= 1
#         if verbose:
#             print_tab(self.t_hist[self.iter])
#             print_sol(self.s_hist[self.iter])
#         return self.t_hist[self.iter], self.s_hist[self.iter]
