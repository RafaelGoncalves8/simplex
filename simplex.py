import tableau

class Simplex(object):
    """Object that represents a linear programming problem that can be
    solved by the simplex algorithm."""
    def __init__(self, F, A, B):
        """F is the objective funcion, A is the restriction functions
        and B is the value of the restriction functions"""

        assert len(F) == len(A[0])
        assert len(A) == len(B)

        self.tab = tableau.Tableau(F, A, B) # main tableau
        self.iter = 0  # initial iteration for the methods next, prev
        self.hist = [] # historico de (tableaus, solutions)
        self.v    = 0  # best value for F til now
        self.sol  = [0]*len(F) # list of variables values
        self.basis = [] # variables states (1 = basis, 0 = non-basis)
        self.set_vars() # set variables initial values and states
        self.mult = None # used in multiple solutions
        self.y = []


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
        self.v = -1*self.tab.m[0][-1]
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
                print("Initializing phase 1.")
            self.phase1()
            if verbose:
                print("...phase 1 OK.\n")
        else:
            if verbose:
                print("All non-basic variables in 0 is possible",)
                print("solution.\n")
                print("...skipping phase 1.\n")
        print("Initializing phase 2.")
        s = self.phase2(verbose)
        if verbose:
            print("...phase 2 OK.\n")
        if s == 0:
            print("Optimal solution:")
            print("Iterations: %d" % self.iter)
            print("v = %.2f" % self.v, end="")
            for i in range(len(self.sol)):
                print(", x%d = %.2f" % (i+1, self.sol[i]), end="")
            return 0
        elif s == 1:
            print("Multiple solutions for %s:" % self.mult)
            print("Iterations: %d" % self.iter)
            print("v = %.2f" % self.v, end="")
            for i in range(len(self.sol)):
                print(", x%d = %.2f" % (i+1, self.sol[i]), end="")
            return 1
        elif s == 2:
            print("Unlimited solution")
            print("Iterations: %d" % self.iter)
            print("v and solutions tend to infinity")
            return 2
        else:
            print("Impossible to solve")
            return 3


    def phase1(self, verbose = True):
        """First phase of the simplex algorithm."""
        for i in range(len(self.tab.obj_func)):
            if (self.tab.obj_func[i]) == 0 and\
                    any([self.tab.const_func[j][i] < 0 for j in\
                    range(self.tab.lines -1)]):
                        self.y.append(i)

        le = len(self.y)
        F = self.tab.obj_func + [0]*len(self.y)
        A = []
        k = 0

        for i in range(len(self.tab.const_func)):
            if i in self.y:
                A.append(self.tab.const_func[i] + [1 if (j == k)\
                        else 0 for j in range(le)])
                k += 1
            else:
                A.append(self.tab.const_func[i] + [0]*le)

        B = self.tab.const_vals

        print("Inserted %d new variables...\n" % le)
        print("Trying to solve new tableau...\n")

        new = Simplex(F, A, B)
        new.solve(verbose)
        return 0


    def phase2(self, verbose):
        """Second phase of the simplex algorithm."""
        i = 0
        if verbose:
            print("Iteration %d" % i)
            print(self.tab)
            print("v = %.2f" % self.v,end="")
            for j in range(len(self.sol)):
                print(", x%d = %.2f" % (j+1, self.sol[j]),end="")
            print("\n")
        while(not self.is_best()):
            i += 1
            self.hist.append((self.tab.m, self.sol))
            state = self.iterate(verbose)
            self.set_vars()
            if verbose:
                print("Iteration %d" % i)
                print(self.tab)
                print("v = %.2f" % self.v, end=""),
                for j in range(len(self.sol)):
                    print(", x%d = %.2f" % (j+1, self.sol[j]), end="")
                print("\n")

        self.iter = i

        return state


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

        min_val = None  # minimum value in RHS/(enter colum)
        drop = None  # index in the list self.sol of the variable
                     # with minimum positive value

        for i in range(1, len(M)):
            if (M[i][enter] > 0 or\
                    (min_val == None)):
                drop = i
                min_val = M[i][-1]/float(M[i][enter])

        if drop == None:
            return 2

        if verbose:
            print("Leave: x%d" % drop)
            print("\n")

        # tableau

        M[drop] = self.tab.mult_line_by(drop, 1/float(M[drop][enter]))
        for i in range(len(M)):
            if i != drop:
                M[i] = self.tab.sum_to_line(i, self.tab.mult_line_by(\
                        drop, -1*M[i][enter]))

        self.tab.m = M

        if [e < 0 for e in M[0][:-1]].count(True) == 1:
            self.mult = drop
            return 1

        return 0


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
        return not any([e < 0 for e in self.tab.m[0][:-1]])
