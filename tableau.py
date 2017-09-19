class Tableau(object):
    def __init__(self, F, A, B):
        """F is a list with (self.vars_num + 1) elements.
        A is an array with self.const_num elements and each
        element of A has self.vars_num elements.
        B is a list with self.const_num elements."""

        # objective function
        self.obj_func = F

        # constraints
        self.const_func = A
        self.const_vals = B
        self.const_nums = len(B)

        # variables
        self.vars = [0]*(len(F)-1)
        self.vars_num = len(F)
        self.num_vars_f = 0
        self.basis = [0]*self.const_nums # variables in base
        self.basis_num = self.const_nums # num of vars in basis

        #tableau
        self.columns = self.vars_num+1
        self.lines   = self.const_nums+1
        self.m = self.create_tab()
        self.set_vars()


    def __str__(self):
        """Print the function being minimized/maximized, a dashed line
        and the expressions for the variables in the base."""
        s = "  1 |"
        for e in self.m[0]:
            s += (" %8.2f |" % e)
        s += ("\n")
        s += ("-"*len(s))
        s += ("\n")
        k = 0
        for l in self.m[1:]:
            s += (" x%d |" % self.basis[k])
            k += 1
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

        self.set_vars()

        return m

    def set_vars(self):
        k = 0
        # set variables out of basis
        for j in len(self.columns):
            if [self.[i][j] != 0 for i in range(1,self.lines)]\
                    .count(True) == 1:
                        self.basis[k] = j
                        k += 1
                        self.val[j] = self.m[i][-1]
            else:
                self.val[j] = 0

        self.num_vars_f = [True for e != 0 in m[0]].count(True)



    def mult_line_by(self, lin, num):
        """Multiply line lin by num."""
        ans = [0]*self.columns
        for i in range(self.columns):
            ans[i] = self.m[lin][i] * num
        return ans


    def mult_column_by(self, col, num):
        """Multiply column col by num."""
        ans = [0]*self.lines
        for j in range(self.lines):
            ans[j] = self.m[j][col] * num
        return ans

    def sum_to_line(self, l_tab, l_sum):
        """Sum line l_sum to l_tab."""
        ans = [0]*self.columns
        for i in range(self.columns):
            ans[i] = self.m[l_tab][i] + l_sum[i]
        return ans

