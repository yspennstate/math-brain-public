"""
PROB20-07 exact checker for run 2026-09-15T181044Z.

Checks:
1. sharp barycentric residual example and determinant;
2. exhaustive 3^6 deterministic residual enumeration at the barycentre,
   restricted to residual kernels that fix the barycentre;
3. symbolic Cauchy--Binet determinant-ratio identity;
4. endpoint complex-instability coordinate polynomial and numerical roots;
5. exact rational central-neighbourhood determinant inequality.

This is a finite algebra/certificate checker, not a proof of the unrestricted
global QSO threshold.
"""
from itertools import product
from fractions import Fraction
import sympy as sp

# ---------------------------------------------------------------------
# 1. Sharp barycentric residual example
# ---------------------------------------------------------------------
R = sp.Matrix([
    [sp.Rational(2,3), 0, sp.Rational(1,3)],
    [sp.Rational(1,3), sp.Rational(2,3), 0],
    [0, sp.Rational(1,3), sp.Rational(2,3)],
])
lam = sp.symbols("lam")
assert R.det() == sp.Rational(1,3)
assert sp.factor(R.charpoly(lam).as_expr()) == (lam - 1)*(3*lam**2 - 3*lam + 1)/3

# ---------------------------------------------------------------------
# 2. Exhaustive deterministic symmetric residual kernels at u=(1/3)^3
# ---------------------------------------------------------------------
pairs = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
u = [sp.Rational(1,3)]*3
max_det = None
max_assignment = None
fixed_count = 0

for assignment in product(range(3), repeat=6):
    Q = {}
    for pair, child in zip(pairs, assignment):
        row = [sp.Integer(0)]*3
        row[child] = sp.Integer(1)
        Q[pair] = row

    W = [sp.Integer(0)]*3
    for i in range(3):
        for j in range(3):
            row = Q[tuple(sorted((i,j)))]
            for k in range(3):
                W[k] += u[i]*u[j]*row[k]
    if W != u:
        continue
    fixed_count += 1

    RR = sp.zeros(3,3)
    for j in range(3):
        for k in range(3):
            RR[j,k] = sum(u[i]*Q[tuple(sorted((i,j)))][k] for i in range(3))
    d = sp.factor(RR.det())
    if max_det is None or d > max_det:
        max_det = d
        max_assignment = assignment

assert fixed_count == 36
assert max_det == sp.Rational(1,3)

# ---------------------------------------------------------------------
# 3. Cauchy--Binet determinant ratio
# ---------------------------------------------------------------------
x1,x2,x3,a,b = sp.symbols("x1 x2 x3 a b", positive=True)
l1 = x1**2/(b*(x1-a))
l2 = x2**2/(b*(x2-a))
l3 = x3**2/(b*(x3-a))

detG = sp.factor(
    x1*x2
    + x1*x3*(x2**2/x3**2)
    + x2*x3*(x1**2/x3**2)
)
detL = sp.factor(
    l1*l2
    + l1*l3*(x2**2/x3**2)
    + l2*l3*(x1**2/x3**2)
)
ratio = sp.factor(detL/detG)
ratio_reduced = sp.factor(
    ratio.subs(x3, 1-x1-x2).subs(b, 1-3*a)
)
target_reduced = sp.factor(
    (x1*x2*(1-x1-x2)) /
    ((1-3*a)*(x1-a)*(x2-a)*(1-x1-x2-a))
)
assert sp.simplify(ratio_reduced-target_reduced) == 0

# ---------------------------------------------------------------------
# 4. Endpoint coordinate localization polynomial
# ---------------------------------------------------------------------
t = sp.symbols("t", positive=True)
a0 = sp.Rational(1,12)
F = sp.factor(
    (1-a0/t) *
    (1-a0/((1-t)/2))**2
    - sp.Rational(1,3)
)
num, den = sp.together(F).as_numer_denom()
assert sp.factor(num) == 288*t**3 - 468*t**2 + 216*t - 25
roots = sorted([float(sp.re(r)) for r in sp.nroots(num) if abs(float(sp.im(r))) < 1e-12])
assert len(roots) == 3
assert abs(roots[0] - 0.174860236322416) < 1e-12
assert abs(roots[1] - 0.553902959429950) < 1e-12

# ---------------------------------------------------------------------
# 5. Exact central-neighbourhood bound
# ---------------------------------------------------------------------
eps = Fraction(1,120)
lo = Fraction(1,3) - eps
hi = Fraction(1,3) + eps
b0 = Fraction(3,4)
q_hi = (hi - Fraction(1,12))/b0
c = hi/Fraction(2,1) + q_hi/(2*lo)
assert c == Fraction(6559,9360)

row_norm_sq_bound = c*c + (1-c)*(1-c)
assert row_norm_sq_bound**3 < Fraction(16,81)

print("ALL EXACT CHECKS PASSED")
print("barycentric deterministic fixed kernels:", fixed_count)
print("max deterministic det(R):", max_det)
print("one maximizing assignment:", max_assignment)
print("coordinate roots:", roots)
print("central cap c:", c, float(c))
print("central determinant-square margin:",
      float(Fraction(16,81) - row_norm_sq_bound**3))
