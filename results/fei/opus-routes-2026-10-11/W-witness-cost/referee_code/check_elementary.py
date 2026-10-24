"""Exhaustive checks of the elementary inequalities used in Theorems 5.1 / 11.1 and Prop 12.1.
(1) Claim A: 4P(1-P)log(1/P) <= 2 I(g) for every Boolean g on n <= 4 variables with 0 < P < 1 (both orientations).
(2) h(v) <= 2I + (log e - 2) v (paper lem:levelentropy) for every Boolean g on n <= 4.
(3) v <= I (Poincare) trivially; (4) s(s+1) <= 3^s and s(s+1) <= 2*3^(s-1), (c+1)(c+2) <= 2*3^c.
(5) Jensen bound E psi_c(Bin(c,1/2)) <= c/2 and E psi_d(1+Bin(d-1,1/2)) <= (d+1)/2, exact sums, c,d <= 200.
(6) x log(1/x) <= log e / e on (0,1]; 1 - ab >= |a-b| on [-1,1]^2 (grid)."""
import math, itertools
from fractions import Fraction
import numpy as np
from rc_common import fwht_int, h2, LOG2E

worstA = 0.0; worstH = -1e9; cnt = 0
for n in range(1, 5):
    N = 1 << n
    idx = np.arange(N)
    for code in range(1 << N):
        f = np.array([1 if (code >> x) & 1 else -1 for x in range(N)], dtype=np.int8)
        P = Fraction(int(np.count_nonzero(f == 1)), N)
        I = Fraction(sum(int(np.count_nonzero(f[idx ^ (1 << i)] != f)) for i in range(n)), N)
        v = 4 * P * (1 - P)
        if 0 < P < 1:
            lhs = 4 * float(P) * (1 - float(P)) * math.log2(1 / float(P))
            worstA = max(worstA, lhs / (2 * float(I)))
            worstH = max(worstH, (h2(v) - (2 * float(I) + (LOG2E - 2) * float(v))))
            assert float(v) <= float(I) + 1e-15
            cnt += 1
print(f'(1) Claim A over {cnt} nonconstant functions n<=4: max LHS/RHS = {worstA:.6f} (must be <= 1)')
print(f'(2) max of h(v) - [2I + (log e - 2)v] = {worstH:.3e} (must be <= 0)')
ok4 = all(s*(s+1) <= 3**s and s*(s+1) <= 2*3**(s-1) for s in range(1, 200)) and all((c+1)*(c+2) <= 2*3**c for c in range(0, 200))
print('(4) size/child-count inequalities:', ok4)
worst5 = 0.0
for c in range(1, 201):
    tot = 0.0
    for t in range(1, c + 1):
        tot += math.comb(c, t) / 2**c * t * math.log2(c / t)
    worst5 = max(worst5, tot / (c / 2))
worst5b = 0.0
for d in range(1, 201):
    tot = 0.0
    for k in range(0, d):
        s = 1 + k
        tot += math.comb(d - 1, k) / 2**(d - 1) * s * math.log2(d / s)
    worst5b = max(worst5b, tot / ((d + 1) / 2))
print(f'(5) max E psi_c(|T|)/(c/2) = {worst5:.6f};  max E psi_d(s)/((d+1)/2) = {worst5b:.6f}  (must be <= 1)')
xs = np.linspace(1e-9, 1, 200001)
print('(6) max x log(1/x) =', float(np.max(xs * np.log2(1 / xs))), ' log e/e =', LOG2E / math.e)
g = np.linspace(-1, 1, 401)
A, B = np.meshgrid(g, g)
print('    min of (1-ab) - |a-b| on grid =', float(np.min(1 - A * B - np.abs(A - B))))
