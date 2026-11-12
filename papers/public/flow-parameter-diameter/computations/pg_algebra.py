"""Symbolic and exact checks for the projective-plane proposition (prop:pg).

Run with python -X utf8 pg_algebra.py (needs sympy).
"""
from fractions import Fraction as Fr
import math
import sympy as sp

s, t, u = sp.symbols('s t u', positive=True)
N = s**2 + s + 1
n = 2 * N
d = s + 1
r = 3
L = (d + 2) * r / (r + d)
b = 2 * L / r
pi_h = 1 / (d + 2)
pi_v = (d + 1) / (n * (d + 2))
pi_B = n * pi_v
twom = n * (d + 2)

# lengths sum to 2m
assert sp.simplify(n * d / 2 * b + n * L - twom) == 0

# V_3 from the distance counts s+1, s^2+s, s^2
S = n * (sp.Rational(1, 3) * (s + 1) + sp.Rational(2, 3) * (s**2 + s) + s**2)
V3_cert = 2 * L * (pi_h * pi_B + pi_v**2 * S)
V3 = (s + 2) * (5 * s**3 + 19 * s**2 + 13 * s + 8) / ((s + 3) * (s + 4) * N)
assert sp.simplify(V3_cert - V3) == 0
print("V3 from lem:cert:", sp.factor(V3))

theta = 3 * (s**2 + 3 * s + 1) / (s * (s + 2) * (s + 4))
assert sp.simplify(1 - theta - (s - 1) * (s + 1) * (s + 3) / (s * (s + 2) * (s + 4))) == 0

spoke = 2 * pi_h * pi_v + 2 * theta * s**2 * pi_v**2
base = pi_v**2 * (2 + 4 * s + 6 * s**2 * (1 - theta) / (s + 1))
assert sp.simplify(spoke - base) == 0
assert sp.simplify(twom * spoke - V3) == 0
print("loads equal and 2m*load = V3")

# the two hand identities quoted in the proof
assert sp.expand((10*s**2 + 6*s + 2)*(s + 2) - 4*(s**2 + s + 1)*(s + 1) - 6*s*(s**2 + 3*s + 1)) == 0
assert sp.expand(2*(s + 4)*(s**2 + s + 1) + 3*s*(s**2 + 3*s + 1) - (5*s**3 + 19*s**2 + 13*s + 8)) == 0
assert sp.simplify(pi_h / pi_v - n / (s + 2)) == 0

# monotonicity of V3: derivative numerator, and the two-point difference
num, den = sp.fraction(sp.together(sp.diff(V3, s)))
print("V3' numerator:", sp.expand(num), " denominator:", sp.factor(den))
p = (s + 2) * (5 * s**3 + 19 * s**2 + 13 * s + 8)
q = (s + 3) * (s + 4) * N
K = sp.cancel((p.subs(s, t) * q - p * q.subs(s, t)) / (t - s))
Kp = sp.Poly(sp.expand(K), s, t)
print("K(s,t) min coefficient:", min(Kp.coeffs()), " terms:", len(Kp.coeffs()))

# ratio and threshold
def V3q(k):
    return Fr((k + 2) * (5 * k**3 + 19 * k**2 + 13 * k + 8), (k + 3) * (k + 4) * (k * k + k + 1))

def ratio_gt_2(k):
    v = V3q(k)
    lhs = (v - 4) * (k + 2)          # R > 2  iff  (V3-4)(s+2) > V3 sqrt(s)
    if lhs <= 0:
        return False
    return lhs * lhs > v * v * k

for k in range(2, 60):
    R = float(V3q(k)) / 2 * (1 - math.sqrt(k) / (k + 2))
    assert ratio_gt_2(k) == (R > 2) == (k >= 38), k
print("exact: ratio > 2 iff s >= 38, checked for 2 <= s < 60")
for k in [2, 3, 4, 5, 7, 37, 38, 41, 49]:
    v = V3q(k)
    tau = (k + 2) / (k + 2 - math.sqrt(k))
    print(f"s={k}: |V(G)|={2*(k*k+k+1)+1} F={v} = {float(v):.9f} tau2={tau:.6f} ratio={float(v)/(2*tau):.5f}")

# root of R = 2
x = sp.symbols('x', positive=True)
Px = sp.expand((5*x**6 + 19*x**4 + 13*x**2 + 8)*(x**2 + 2 - x) - 4*(x**2 + 3)*(x**2 + 4)*(x**4 + x**2 + 1))
print("P(x) =", Px)
roots = [rr for rr in sp.Poly(Px, x).nroots() if abs(sp.im(rr)) < 1e-12 and sp.re(rr) > 0]
print("positive real roots of P (x = sqrt s):", roots, " s =", [sp.re(rr)**2 for rr in roots])
c = sp.Rational(307, 50)
shift = sp.Poly(sp.expand(Px.subs(x, c + u)), u)
print("c =", c, " c^2 =", c**2, " P(c+u) coefficients:", shift.all_coeffs())
print("min coefficient of P(c+u):", min(shift.all_coeffs()))
