# Maximal flow through thin boxes with heavy-tailed capacities

Yitzchak Shmalo

Paper: [paper/main.pdf](paper/main.pdf) (source `paper/main.tex`).

Kesten's law of large numbers for the maximal flow from the bottom to the top of a box [0,k] x [0,l] x [0,m] in Z^3
with i.i.d. capacities assumes a finite exponential moment. Auffinger, Damron and Hanson (*50 Years of First-Passage
Percolation*, Question 36) ask whether the limit of Phi/(kl) exists without that assumption.

The paper shows that, with no replacement moment condition, it need not. For every height function m(N) with
liminf m(N)/log N = 0 there is a capacity law with no atom at 0 (and infinite mean) such that the maximal flow through
[0,N]^(d-1) x [0,m(N)] in Z^d, d >= 2, satisfies limsup Phi/N^(d-1) = +infinity almost surely, and Phi/N^(d-1) exceeds
N^(1/2)/2 with probability tending to one along a sequence of N. The heights may grow, for example like
(log N)^(1/2), which is inside Kesten's range. For heights with m(N)/log N -> infinity, Rossignol and Theret
(Electron. J. Probab. 23 (2018), paper 99) proved convergence to a finite flow constant for every capacity law, so for
these laws the limit depends on how fast the height grows. The argument counts vertical columns whose edges all carry
a very large capacity. Finite-mean and finite-second-moment laws are not addressed.

## Contents

- `paper/` - the paper.
- `code/check.py` - exact rational checks of the explicit example (masses, tails, column probability, Chebyshev
  bound, final lower bound, r <= 12, d = 2, 3), and exact integer max-flow computations (scipy) on 300 random small
  boxes confirming that the flow is at least a times the number of columns with all capacities >= a, with a control
  box. Output in `code/check_output.txt`. Needs Python 3 with numpy and scipy.
