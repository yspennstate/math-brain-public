#!/usr/bin/env python3
"""Exact symbolic checker for PROB20-07 run 2026-09-16T071410Z.

Checks the new weak-endpoint theorem excluding every nonreal fixed-point
tangent multiplier with nonnegative real part from the closed unit disk.
The proof uses the archived harmonic/skew bounds plus new exact algebra:
  * harmonic-instability localization q <= 2/27;
  * quantitative circulation drop away from the barycentre;
  * crossover factorization;
  * endpoint Bernstein-polynomial positivity;
  * improved residual circulation lower bound sqrt(35)/54.
"""

import sympy as sp

H, s = sp.symbols('H s', positive=True)
u = sp.symbols('u', nonnegative=True)
r = sp.symbols('r', nonnegative=True)
q = r**2

# 1) Harmonic-instability localization q <= 2/27.
pplus = sp.Rational(1, 27) - r**2 / 6 + r**3 / (3 * sp.sqrt(6))
s_r = sp.Rational(1, 3) - r**2 / 2
u_sub = sp.sqrt(6) * u / 9
loc_expr = sp.simplify((5 * s_r - 54 * pplus).subs(r, u_sub))
assert sp.simplify(loc_expr + (u - 3) * (u - 1) * (4 * u + 3) / 27) == 0

# 2) Crossover bound factorization.
A = (27 - H) / 24
d0 = (H + 9) / (24 * H)
cross_upper_minus_432 = sp.expand((27 - H)**2 + H * (H + 9)**2 / 27 - 432)
assert sp.factor(cross_upper_minus_432) == (H - 9) * (H**2 + 54 * H - 891) / 27

# 3) Quantitative circulation centered cyclic identities.
y1, y2 = sp.symbols('y1 y2', real=True)
y3 = -y1 - y2
q_y = sp.expand(y1**2 + y2**2 + y3**2)
ell1 = 10 * y1 + 8 * y2
ell2 = 10 * y2 + 8 * y3
ell3 = 10 * y3 + 8 * y1
assert sp.expand(ell1 + ell2 + ell3) == 0
assert sp.expand(ell1**2 + ell2**2 + ell3**2 - 84 * q_y) == 0

# 4) Endpoint C(r) certificate.
C = sp.Rational(1, 6) - sp.sqrt(14) * r / 24 + r**2 / 4
pminus = sp.Rational(1, 27) - r**2 / 6 - r**3 / (3 * sp.sqrt(6))
tC = sp.Rational(3, 2) - 9 * C
E = sp.expand(C**2 - pminus * (1 - tC**2))
E_u = sp.simplify(E.subs(r, sp.sqrt(6) * u / 9))
Q = -sp.expand(E_u * 104976)
Q_expected = (
    8 * u**7
    + (36 - 8 * sp.sqrt(21)) * u**6
    + (42 - 36 * sp.sqrt(21)) * u**5
    + 45 * u**4
    + (144 * sp.sqrt(21) - 288) * u**3
    - 2700 * u**2
    + 324 * sp.sqrt(21) * u
    + 972
)
assert sp.expand(Q - Q_expected) == 0

# Bernstein coefficients of degree 7 on [0,1].
poly = sp.Poly(Q, u)
power = [poly.coeff_monomial(u**i) for i in range(8)]
bern = []
for k in range(8):
    bk = sum(
        power[i] * sp.Rational(sp.binomial(k, i), sp.binomial(7, i))
        for i in range(k + 1)
    )
    bern.append(sp.simplify(bk))

bern_expected = [
    972,
    972 + 324 * sp.sqrt(21) / 7,
    sp.Rational(5904, 7) + 648 * sp.sqrt(21) / 7,
    sp.Rational(20232, 35) + 5004 * sp.sqrt(21) / 35,
    sp.Rational(5913, 35) + 1008 * sp.sqrt(21) / 5,
    (-2713 + 1896 * sp.sqrt(21)) / 7,
    (-7593 + 2440 * sp.sqrt(21)) / 7,
    -1885 + 424 * sp.sqrt(21),
]
for got, want in zip(bern, bern_expected):
    assert sp.simplify(got - want) == 0

# First five are manifestly positive. For the last three, sqrt(21)>9/2 suffices.
for bk in bern[:5]:
    assert float(bk.evalf()) > 0
assert sp.simplify((-2713 + 1896 * sp.Rational(9, 2)) / 7) > 0
assert sp.simplify((-7593 + 2440 * sp.Rational(9, 2)) / 7) > 0
assert sp.simplify(-1885 + 424 * sp.Rational(9, 2)) > 0

# 5) Improved product/circulation lower bound in any residual unstable chamber.
p_lower = sp.Rational(5, 54) * sp.Rational(8, 27)
assert sp.simplify(p_lower - sp.Rational(20, 729)) == 0
d_lower_sq = sp.Rational(7, 16) * p_lower
assert sp.simplify(d_lower_sq - sp.Rational(35, 2916)) == 0

print('ALL EXACT POSITIVE-REAL COMPLEX-SPECTRUM CHECKS PASSED')
print('Bernstein coefficients:')
for i, bk in enumerate(bern):
    print(i, sp.simplify(bk))
