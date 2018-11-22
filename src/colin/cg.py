from numpy import *

def solve_cg(A,b,x0,rtol,maxits):
    r0 = b
    p0 = r0
    while dot(r0,  r0)**0.5 - rtol > 0:
        a = dot(r0,r0)/dot(p0, A @ p0)
        x = x0 + a * p0
        r = r0 - a * (A @ p0)
        p = r + dot(r , r)/dot(r0,  r0) * p0
        r0 = r
        x0 = x
        p0 = p
        

    """
    Function to use the conjugate gradient algorithm to
    solve the equation Ax = b for symmetric positive definite A.
    Inputs:
    A -- An nxn matrix stored as a rank-2 numpy array
    b -- A length n vector stored as a rank-1 numpy array
    x0 -- The initial guess, length n vector stored as a rank-1 numpy array
    rtol -- a tolerance, algorithm should stop if l2-norm of
    the residual r=Ax-b drops below this value.
    maxits -- Stop if the tolerance has not been reached after this number
    of iterations

    Outputs:
    x -- the approximate solution
    rvals -- a numpy array containing the l2 norms of the residuals
    r=Ax-b at each iteration
    """
    rvals = (r0 @ r0)**0.5 - rtol

    return x, rvals
