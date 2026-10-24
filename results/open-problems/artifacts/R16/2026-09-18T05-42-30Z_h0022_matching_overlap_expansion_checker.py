#!/usr/bin/env python3
# Exact symbolic self-check for R16 H0022 matching-overlap expansion.
# Uses SymPy exact rationals/symbolics only.

import sympy as sp

x,b,c = sp.symbols("x b c", positive=True)
r = b*x

def F(a):
    return a*sp.log(a)-a

# Exact n-scale Stirling-rate part of E[Y_j], after the -r log n term is separated.
g = r*sp.log(2) - F(r) + 2*F(1-r) - F(1-2*r) - F(1)

# After combining -r log n from E[Y_j] with +r log n in log W,
# and writing L=1/x, the remaining logarithmic term is -r log(c L) = -r log(c/x).
base = sp.expand(g - r*sp.log(c/x))

# Fixed-M falling-factorial corrections, retaining q=1,2,3,4 leading power-sum terms.
wcorr = 0
for q in range(1,5):
    wcorr += (2-(2-r)**(q+1))*sp.Integer(2)**q / (
        sp.Integer(q)*(q+1)*c**q
    ) * x**q

series = sp.series(base + wcorr, x, 0, 5).removeO().expand()
coeff = [sp.simplify(series.coeff(x,i)) for i in range(1,5)]

expected1 = b*(1 + sp.log(2/(b*c))) - 2/c
expected2 = -(b-2/c)**2
expected3 = -b**3 - b**2/c + 8*b/c**2 - sp.Rational(28,3)/c**3

assert sp.simplify(coeff[0]-expected1) == 0
assert sp.simplify(coeff[1]-expected2) == 0
assert sp.simplify(coeff[2]-expected3) == 0

at_saddle = [sp.simplify(z.subs(b,2/c)) for z in coeff[:4]]
assert at_saddle[0] == 0
assert at_saddle[1] == 0
assert at_saddle[2] == -sp.Rational(16,3)/c**3
assert at_saddle[3] == -sp.Integer(16)/c**4

# Exact cycle/path matching polynomials for small finite checks.
z = sp.symbols("z")
lam_plus = (1 + sp.sqrt(1+4*z))/2
lam_minus = (1 - sp.sqrt(1+4*z))/2

def path_poly(k):
    # P_k path on k vertices: sum_s C(k-s,s) z^s
    return sp.expand(sum(sp.binomial(k-s,s)*z**s for s in range(k//2+1)))

def cycle_poly(k):
    # C_k matching polynomial: sum_s k/(k-s) C(k-s,s) z^s
    out = 0
    for s in range(k//2+1):
        if s == 0:
            out += 1
        else:
            out += sp.Rational(k,k-s)*sp.binomial(k-s,s)*z**s
    return sp.expand(out)

for k in range(3,13):
    cp = cycle_poly(k)
    closed = sp.expand(lam_plus**k + lam_minus**k)
    assert sp.simplify(cp-closed) == 0
    pp = path_poly(k)
    # recurrence check
    if k >= 2:
        assert sp.expand(pp - path_poly(k-1) - z*path_poly(k-2)) == 0

print("combined coefficients:")
for i,q in enumerate(coeff[:4], start=1):
    print(f"x^{i}: {sp.simplify(q)}")
print("at saddle b=2/c:")
for i,q in enumerate(at_saddle, start=1):
    print(f"x^{i}: {q}")
print("cycle/path matching-polynomial identities checked for k=3..12")
print("ALL_EXACT_CHECKS_PASS")
