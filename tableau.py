class Tableau(object):
    def __init__(self, F, A, B):
        """F is a list with (self.vars_num + 1) elements.
        A is an array with self.const_num elements and each
        element of A has self.vars_num elements.
        B is a list with self.const_num elements."""

        # objective function
        self.obj_func = F

        # variables
        self.vars = [0]*(len(F)-1)
        self.vars_num = len(F)

        # constraints
        self.const_func = A
        self.const_vals = B
        self.const_nums = len(B)

        #tableau
        self.columns = self.vars_num+1
        self.lines   = self.const_nums+1
        self.m = self.create_tab()


    def __str__(self):
        """Print the function being minimized/maximized, a dashed line
        and the expressions for the variables in the base."""
        s = ""
        for e in self.m[0]:
            s += (" %8.2f |" % e)
        s += ("\n")
        s += ("-"*len(s))
        s += ("\n")
        for l in self.m[1:]:
            for e in l:
                s += (" %8.2f |" % e)
            s += ("\n")
        return s


    def create_tab(self):
        """Create the tableau array with self.lines x self.columns"""
        A = self.const_func
        B = self.const_vals

        # initialize the tableau lines
        m = [0]*self.lines

        # first line is the objective function
        m[0] = [self.obj_func[i] for i in range(self.columns-1)]
        m[0].append(0)

        # other lines are constraints of base variables
        for i in range(1,self.lines):
            m[i] = [ A[i-1][j] for j in range(self.columns-1)]
            m[i].append(B[i-1])

        return m


    def mult_line_by(self, lin, num):
        """Multiply line lin by num."""
        for i in range(self.columns):
            self.m[lin][i] *= num


    def mult_column_by(self, col, num):
        """Multiply column col by num."""
        for j in range(self.lines):
            self.m[j][col] *= num

