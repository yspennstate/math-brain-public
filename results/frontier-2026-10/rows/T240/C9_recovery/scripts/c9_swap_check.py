"""Exact checks for the minus branch by teacher swap tau: R_i1 <-> R_i2, i.e. (Q11,Q12,Q22,R11,R12,R21,R22) -> (Q11,Q12,Q22,R12,R11,R22,R21)."""
import sys; sys.path[:0] = ['.']
from fractions import Fraction as F
import c9_cone
from c9_flow import f_point, N
tau = lambda x: [x[0], x[1], x[2], x[4], x[3], x[6], x[5]]
xs = c9_cone.plateau_float()
P, Pinv, par, w = c9_cone.adapted_frame(xs)
cols_ok = all(tau([P[i][j] for i in range(N)]) == [par[j] * P[i][j] for i in range(N)] for j in range(N))
print('frame columns exactly tau-even/odd:', cols_ok, 'parities', par)
import random; random.seed(1)
worst = 0
for _ in range(5):
    x = [F(random.randint(300, 900), 1000) for _ in range(3)] + [F(random.randint(0, 900), 1000) for _ in range(4)]
    a = f_point(tau(x)); b = tau(f_point(x))
    for u, v in zip(a, b):
        assert u.lo <= v.hi and v.lo <= u.hi, 'enclosures disjoint'
        worst = max(worst, max(u.hi - u.lo, v.hi - v.lo))
print('F(tau x) and tau F(x) enclosures overlap at 5 rational points (equivariance consistent); max width', worst / 2**160)
print('teacher <-> swap:', tau([1,0,1,1,0,0,1]) == [1,0,1,0,1,1,0])
