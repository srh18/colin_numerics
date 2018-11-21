`Back to Numerics Course Home Page <http://mpecdt.bitbucket.org/>`_

Numerics Course Part II: Computer Lab
=====================================

You should develop your solutions to these exercises in a git
repository, hosted on BitBucket. During the timetabled laboratory:

- Work through the exercises on your laptop, by forking and checking out
  a copy of the mpcdt git repository. (If you have already forked Hilary's
  repository, it's fine to use that forked version, I will tell you if you
  need to pull any updates from the master repository).

- If you would like help with issues in your code, either:

  - Paste the code into a gist, or
  - Push your code up to your forked git repository on BitBucket.
    Then, share the link to your gist or repository in the IRC channel

This Computer Lab is about the conjugate gradient method for solving
the equation

.. math::

   \begin{equation}
   A\bf{x} = \bf{b}
   \end{equation}

in the case where the matrix :math:`A` is obtained from the following
discretisation of the one-dimensional Poisson equation

.. math::
   2p_i - p_{i-1} - p_{i+1} = h^2 f_i, \quad i=1,\ldots, n-1,

where :math:`p_i` is the approximation for :math:`p(x_i)`, with
:math:`x_i=hi`, and :math:`h=1/n`. We have boundary conditions
:math:`p(0)=p(1)=0`, and hence 
he unknown variables are 
the coefficients :math:`p_1,\ldots,p_{n-1}` which we write as 
a vector :math:`\bf{p}`; hence the above system of equations may
be written in matrix-vector form.

We will work through the steps of constructing and evaluating the
conjugate gradient method for this example.

Exercise 1
----------

Edit the file `colin/cg.py` in the repository, in order to implement
the conjugate gradient algorithm. Currently in this file is a skeleton
describing the inputs and outputs. The script 'colin/test_cg.py',
executable by typing `python test_cg.py` into a terminal whilst in
that directory, is designed to execute without error if the algorithm
is correctly implemented.

This implementation will make use of the Python "numpy" module which
implements a Matlab-style array type, which we use for storing vectors
and matrices. 

You should avoid using loops beyond the loop over CG iterations in the
algorithm description: loops are slow in Python. This means that you
will need to make use of numpy array operations (which are precompiled
in C for speed). Hopefully you are familiar with these by now from the
first part of the course; everything should be implementable using
the numpy function `dot`. For more information on this and other
numpy commands, you can read the documentation by opening an iPython
shell, and typing: ::

  from numpy import *
  help(dot)

The matrix-vector multiplication will require a combination of `dot`
with a loop over the row-index of the matrix. You can access the i-th
row of `A` via `A[i,:]`.

After verifying that test_cg.py passes, answer the following questions.

- On a logarithmic graph, plot the l2-norm of the residual against
  iteration number for problem sizes :math:`n=20,50,100`. 

- What do you notice about the convergence rate of the residual as
  :math:`n` changes?

Exercise 2
----------

Create another function in `test_cg.py` to test the discretisation by
comparing with the exact solution to the boundary value problem

.. math::

   \begin{equation}
   -p_{xx} = \sin(\pi x).
   \end{equation}

Compute the numerical error by comparing with the exact solution
evaluated at each grid point. Plot the infinity-norm of the solution
as a function of :math:`n` on a log-log graph and verify that you
obtain the expected second-order convergence rate.

Exercise 3
----------

- Obtain timings for the solution for a problem size :math:`n=500`,
  using ::
  
    import time

    t0 = time.time()
    CODE TO BE RUN HERE
    t1 = time.time()
  
    total = t1-t0
  
  This method is rather inprecise and much more accurate statistics
  can be obtained using `cProfile`, but we will not do that here.

- Obtain timings for various values of :math:`n`, and plot them.
  Explain the results precisely in terms of asymptotic behaviour 
  for large :math:`n`. Why is this expected?

The Python SciPy module provides an implementation of CG in
`scipy.sparse.linalg.cg`. 

- Compare the timings of your implementation with the SciPy one (which
  has been precompiled in C).

SciPy also supports sparse matrix formats. Creating a sparse version
of `A` is as simple as: ::
  
  from scipy.sparse import csr_matrix
  As = csr_matrix(A)

`As` is in a sparse matrix format called Compressed Sparse Row
(CSR). (Other formats are available). You can see how the data in `A`
has been stored by inspecting `As.data`, `As.ind`, `As.indptr`. This
is how sparse matrices are stored in high performance computing
implementations.

The SciPy CG implementation also allows the matrix to be a CSR matrix.

- Compare the timings for the SciPy CG implementation when a CSR
  matrix is used for `A`.  Explain the results precisely in terms of
  asymptotic behaviour for large :math:`n`. Why is this expected?
