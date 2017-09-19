#! /bin/env python

import simplex

def main():
    print("Give the coefficients of the objective function being minimized")
    F = list(map(float,input(">").split()))
    print("Give the coefficients of the left hand size of the constraints and the right hand size of the constraints in order")
    A = []
    B = []
    while(True):
        ans = list(map(float, input(">").split()))
        if len(ans) == 0:
            break
        else:
            A.append(ans[:-1])
            B.append(ans[-1])

    assert((len(F) == len(A[0])), "Number of elements of F not equal the number of elements in the constraints")

    problem = simplex.Simplex(F, A, B)
    problem.solve(True)


if __name__ == "__main__":
    main()
