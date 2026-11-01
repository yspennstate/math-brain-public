#!/usr/bin/env python3
import sympy as sp

# Exact checker for the two endpoint real-neutral normal forms in PROB20-07.
u, v, t = sp.symbols("u v t", real=True)
a = sp.Rational(1, 12)
b = sp.Rational(3, 4)

# Canonical endpoint maps (sigma=+1 and sigma=-1).
up_plus = u * (4 + 3*v) / 4
up_minus = -u * (4 + 3*v) / 4
vp = -sp.Rational(3, 8) * (u**2 - 3*v**2)

# Lyapunov function.
L = u**2 + sp.Rational(3, 2)*u**2*v + v**2
Lp_plus = sp.expand(L.subs({u: up_plus, v: vp}, simultaneous=True))
Lp_minus = sp.expand(L.subs({u: up_minus, v: vp}, simultaneous=True))
assert sp.simplify(Lp_plus - Lp_minus) == 0

Delta = sp.factor(Lp_plus - L)
N = sp.factor(-256 * Delta)

expected_N = (
    81*u**4*v**2 + 216*u**4*v + 108*u**4
    -243*u**2*v**4 -648*u**2*v**3 -360*u**2*v**2
    -324*v**4 +256*v**2
)
assert sp.expand(N - expected_N) == 0

# Regard N as a quadratic in r=u^2.
r = sp.symbols("r", nonnegative=True)
A = 27*(v + 2)*(3*v + 2)
B = -9*v**2*(27*v**2 + 72*v + 40)
C = -4*v**2*(9*v - 8)*(9*v + 8)
Nr = sp.expand(A*r**2 + B*r + C)
assert sp.expand(N.subs(u**4, r**2).subs(u**2, r) - Nr) == 0

disc = sp.factor(B**2 - 4*A*C)
Dpoly = sp.factor(disc/(27*v**2))
expected_D = (
    2187*v**6 + 11664*v**5 + 25920*v**4 + 27648*v**3
    +6912*v**2 -8192*v -4096
)
assert sp.expand(Dpoly - expected_D) == 0

# On the image simplex at a=1/12, v lies in [-1/4,1/2].
# Transform that interval to t in [0,1] and compute degree-6 Bernstein coefficients.
vt = -sp.Rational(1,4) + sp.Rational(3,4)*t
Pt = sp.Poly(sp.expand(Dpoly.subs(v, vt)), t)
n = 6
power = [Pt.coeff_monomial(t**k) for k in range(n+1)]
bern = []
for j in range(n+1):
    bj = sum(
        power[k] * sp.binomial(j,k) / sp.binomial(n,k)
        for k in range(j+1)
    )
    bern.append(sp.factor(bj))

expected_bern = [
    -sp.Rational(8018357,4096),
    -sp.Rational(6023643,2048),
    -sp.Rational(21208553,5120),
    -sp.Rational(2757115,512),
    -sp.Rational(7950153,1280),
    -sp.Rational(710171,128),
    -sp.Rational(63317,64),
]
assert bern == expected_bern
assert all(c < 0 for c in bern)

# A(v)>0 throughout [-1/4,1/2].
assert A.subs(v, -sp.Rational(1,4)) > 0
# A'=162v+270 is positive on the interval, so A is increasing there.
assert sp.diff(A, v).subs(v, -sp.Rational(1,4)) > 0

# At v=0, N=108 u^4 exactly.
assert sp.factor(N.subs(v,0) - 108*u**4) == 0

# Verify the two actual endpoint QSO tensors reduce to the canonical maps.
x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
pairs = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]

def qso_from_residual_assignment(assign, coords):
    out = [sp.Integer(0), sp.Integer(0), sp.Integer(0)]
    for child, (i,j) in zip(assign, pairs):
        row = [a,a,a]
        row[child] += b
        wt = coords[i]*coords[j]*(1 if i==j else 2)
        for k in range(3):
            out[k] += wt*row[k]
    return [sp.expand(z) for z in out]

# +1 exceptional tensor: Q11=Q12=e1, Q13=Q22=e2, Q23=Q33=e3.
assign_plus = (0,0,1,1,2,2)
# Coordinates u=x1-x3, v=x2-1/3.
coords_plus = [
    sp.Rational(1,3)-v/2+u/2,
    sp.Rational(1,3)+v,
    sp.Rational(1,3)-v/2-u/2,
]
Vplus = qso_from_residual_assignment(assign_plus, coords_plus)
assert sp.simplify((Vplus[0]-Vplus[2]) - up_plus) == 0
assert sp.simplify((Vplus[1]-sp.Rational(1,3)) - vp) == 0

# -1 flip tensor: Q11=Q13=e2, Q22=Q23=e1, Q12=Q33=e3.
assign_minus = (1,2,1,0,0,2)
# Coordinates u=x1-x2, v=x3-1/3.
coords_minus = [
    sp.Rational(1,3)-v/2+u/2,
    sp.Rational(1,3)-v/2-u/2,
    sp.Rational(1,3)+v,
]
Vminus = qso_from_residual_assignment(assign_minus, coords_minus)
assert sp.simplify((Vminus[0]-Vminus[1]) - up_minus) == 0
assert sp.simplify((Vminus[2]-sp.Rational(1,3)) - vp) == 0

# Image-strip bounds at the endpoint:
# every output coordinate is in [1/12,5/6], hence the distinguished coordinate
# used in v lies in [1/12,5/6], i.e. v in [-1/4,1/2].
assert sp.Rational(1,12)-sp.Rational(1,3) == -sp.Rational(1,4)
assert sp.Rational(5,6)-sp.Rational(1,3) == sp.Rational(1,2)

print("ALL EXACT ENDPOINT NORMAL-FORM LYAPUNOV CHECKS PASSED")
print("Delta =", Delta)
print("N =", N)
print("discriminant factor =", disc)
print("Dpoly Bernstein coefficients on [-1/4,1/2]:")
for c in bern:
    print(c)
