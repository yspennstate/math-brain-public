#!/usr/bin/env python3
from fractions import Fraction as F
import sympy as sp

# Exact/symbolic self-check for the finite algebra in the R09 G0013
# two-sided [0,1] moment-projection improvement.  The analytic transport,
# projection, smoothing, and Jacobi arguments are proved in the companion
# immutable report.  This file is a self-check, not an independent audit.

m, a, u, L, y = sp.symbols("m a u L y", positive=True)
kq = sp.Rational(112, 13)
rq = sp.simplify(kq / (1 + kq))
assert rq == sp.Rational(112, 125)

# Regime II (lower clipping only): verify the ramp has the prescribed moments.
Ls = (6*m - a)/(4*m)
alpha = 1 - Ls
beta = 2*m/Ls**2
p = beta*(y-alpha)
mass = sp.simplify(sp.integrate(p, (y, alpha, 1)))
first = sp.simplify(12*sp.integrate((y-sp.Rational(1,2))*p, (y, alpha, 1)))
p2 = sp.simplify(sp.integrate(p**2, (y, alpha, 1)))
assert sp.simplify(mass-m) == 0
assert sp.simplify(first-a) == 0
assert sp.simplify(p2 - 4*m**2/(3*Ls)) == 0

# Regime III (both clips active): verify the clipped affine ramp identities.
alpha3 = 1-m-L/2
beta3 = 1-m+L/2
p3 = (y-alpha3)/L
mass3 = sp.simplify(
    sp.integrate(p3, (y, alpha3, beta3)) + sp.integrate(1, (y, beta3, 1))
)
first3 = sp.simplify(12*(
    sp.integrate((y-sp.Rational(1,2))*p3, (y, alpha3, beta3))
    + sp.integrate(y-sp.Rational(1,2), (y, beta3, 1))
))
p23 = sp.simplify(
    sp.integrate(p3**2, (y, alpha3, beta3)) + sp.integrate(1, (y, beta3, 1))
)
a3 = 6*m*(1-m) - L**2/2
assert sp.simplify(mass3-m) == 0
assert sp.simplify(first3-a3) == 0
assert sp.simplify(p23-(m-L/6)) == 0

# Lower-ramp penalty factorization.
G = (u**2-kq*(u-1)**3/(3-u))/3
assert sp.simplify(
    G-sp.Rational(7,13)
    - (5*u-7)**2*(5*u-1)/(39*(u-3))
) == 0

# Transition point.
m0 = F(2,5)
k = F(112,13)
r = k/(1+k)
assert r == F(112,125)
assert 4*m0*m0*(3-4*m0) == r

# Tail maximization at m=1/2.
Fl = (
    sp.Rational(125,624)*L**4
    - sp.Rational(125,104)*L**2
    + sp.Rational(56,39)*L
    - sp.Rational(73,208)
)
Fpl = sp.diff(Fl, L)
assert sp.simplify(sp.diff(Fl,L,2) - sp.Rational(125,52)*(L**2-1)) == 0

def eval_frac(expr, x):
    val = sp.cancel(expr.subs(L, sp.Rational(x.numerator, x.denominator)))
    num, den = sp.fraction(val)
    return F(int(num), int(den))

lo = F(1809,2500)
hi = F(7237,10000)
flo = eval_frac(Fl, lo)
fplo = eval_frac(Fpl, lo)
fphi = eval_frac(Fpl, hi)
assert fplo > 0
assert fphi < 0

tangent_ub = flo + fplo*(hi-lo)
tail_cap = F(2273,20000)
tail_margin = tail_cap - tangent_ub
assert tail_margin > 0

# Integrated linear penalty and the resulting global intersection.
B = 2*(F(7,13)*(m0**3)/3 + tail_cap*(F(1,2)-m0))
assert B == F(178247,3900000)

c = 1+k
assert c == F(125,13)
H = (F(1,9)-2*B)/(c+F(4,3))
U = 2*B + c*H
assert H == F(115259,64050000)
assert U == F(580249,5337500)
assert U > F(1,10)

# Compare against the certified lower bracket for the preceding algebraic U_MP.
zlo = F(27010941,10**9)
prior_lo = F(17,171) + F(8,19)*zlo
improvement_lower = prior_lo-U
assert improvement_lower > 0

print("R09 G0013 TWO-SIDED BOX-PROJECTION EXACT SELF-CHECK")
print("k = 112/13")
print("r = k/(1+k) = 112/125")
print("transition m0 = 2/5; 4 m0^2 (3-4m0) = 112/125")
print("lower-ramp identity: G(u)-7/13 = (5u-7)^2(5u-1)/(39(u-3)) [symbolically verified]")
print("tail F''(L) = 125(L^2-1)/52 [symbolically verified]")
print("F'(1809/2500) =", fplo, "> 0")
print("F'(7237/10000) =", fphi, "< 0")
print("concavity tangent upper bound =", tangent_ub, "=", float(tangent_ub))
print("tail cap =", tail_cap, "=", float(tail_cap))
print("tail cap margin =", tail_margin, "=", float(tail_margin))
print("integrated B =", B, "=", float(B))
print("intersection H =", H, "=", float(H))
print("U_new =", U, "=", float(U))
print("gap U_new - 1/10 =", U-F(1,10), "=", float(U-F(1,10)))
print("prior U_MP certified lower bracket =", prior_lo, "=", float(prior_lo))
print("certified strict improvement over prior lower bracket =", improvement_lower, "=", float(improvement_lower))
print("SELF_CHECK_ONLY / PASS")
