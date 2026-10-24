# A definite rank-two form with a small diagonal twist

The degenerate hub itself is now proved for every hub law without this statement (degenerate_hub/). M-D2 below is
recorded for its own interest.

The degenerate hub

    Q = 4 X_h L + 2L^2 + 2V^2 + X'^T D X' + <b, X>,   L = <w, X'>,  V = <v, X'>,

with w, v orthonormal and D diagonal and small, is bounded for hub laws supported in an interval
(real_variable_hub/, Theorem A). Conditioning on X_h = x instead of on X' gives

    Q = Y_{b' + 4xw} + c(x),   Y_beta = 2L^2 + 2V^2 + X'^T D X' + <beta, X'>,

where b' is the part of b on the leaves and c(x) does not depend on X'. So the degenerate hub is bounded for every
hub law and every hub diagonal as soon as the following holds.

**(M-D2).** There are absolute constants delta_0 > 0 and C_2 such that sup_beta ||p_{Y_beta}||_inf <= C_2 whenever
||D|| <= delta_0, for all n, all orthonormal w, v and all product laws with densities at most 1.

M-D2 concerns two large eigenvalues, so the conjecture does not cover it, and it needs definiteness: 2LV has a
logarithmic singularity. It is not proved here. Its hardest part may be the linear term: already
2L^2 + 2V^2 + beta U with U orthogonal to L and V is a two-eigenvalue form, and Fresnel linearisation with the
three-dimensional Brascamp-Lieb bound (for a spread frame (w, v, u)) only gives ||p|| <= C(1 + log_+ 1/|beta|): the
two-dimensional bound |phi(t)| <= 2 pi/|t| below |t| = 1/|beta| and the three-dimensional one above it. For small beta the bound has to come
from the circle geometry of the limit beta = 0, and no such argument is written. The degenerate hub needs M-D2 only
for beta = b' + 4xw, with b' the fixed linear term of Q.

md2_scan.py evaluates the density of Y_beta exactly (the fibre identity of real_variable_hub/fibre_density.py) on a
grid around its peak. It uses random orthonormal w, v; six diagonals D (zero, minus twice the leverages, which removes
the diagonal of both squares, minus the leverages, random +-0.1, -0.1 I, +0.1 I); three linear terms (zero, 4w, which
is the hub shift at x = 1, and a random vector of norm one); and three laws (uniform on an interval, uniform on two
intervals of length 1/2 at distance 2.3, three narrow Gaussian bumps). The outputs for n = 60 and n = 120 are the two
text files. Peak densities at beta = 0:

| law | n | D = 0 | the five twisted D |
|---|---|---|---|
| uniform | 60 | 2.82 | 2.10 - 2.48 |
| uniform | 120 | 2.84 | 1.92 - 2.65 |
| two intervals | 60 | 0.168 | 0.131 - 0.153 |
| two intervals | 120 | 0.159 | 0.128 - 0.160 |
| three bumps | 60 | 0.119 | 0.089 - 0.103 |
| three bumps | 120 | 0.124 | 0.086 - 0.119 |

Nonzero beta lowers every value. The twist never raises the peak beyond the Monte Carlo error, and nothing grows
from n = 60 to n = 120. The laws are not optimised, so this is evidence for M-D2, not a test of its extremal cases.
