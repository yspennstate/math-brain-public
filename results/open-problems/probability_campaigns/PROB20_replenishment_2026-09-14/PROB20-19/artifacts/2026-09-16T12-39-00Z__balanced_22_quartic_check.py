#!/usr/bin/env python3
"""
PROB20-19 reproducibility/self-review checker.

Builds the exact two-scale top-two half-normal expectation G(s,t), uses Gaussian
scale-score operators to construct the balanced p=4,d=2 2+2 fourth directional
derivative q4(s), and certifies q4>0 on the previously certified first Hessian
root bracket s in [0.50461,0.50462] with outward mpmath interval arithmetic.

This is a reproducibility aid, not independent verification.
"""
import sympy as sp
import mpmath as mp

s, t = sp.symbols("s t", positive=True)
pi = sp.pi
R = sp.sqrt(s**2*t**2 + s**2 + t**2)
rs = sp.sqrt(1 + 2*s**2)
rt = sp.sqrt(1 + 2*t**2)

G = 4/pi**2 * (
    2*R*sp.atan(s*t/R)
    + rs*sp.atan(s/(t*rs))
    + rt*sp.atan(t/(s*rt))
)

# Exact one-scale formula from the preceding balanced-score checkpoint.
r = sp.sqrt(1 + 2*s**2)
g_prev = 12/pi**2 * (
    sp.atan(1/(sp.sqrt(3)*s))/sp.sqrt(3)
    + r*sp.atan(s/r)
)
residual = sp.simplify(sp.trigsimp(G.subs(t, 1) - g_prev))
print("G(s,1)-g_previous residual:", residual)
assert residual == 0


def Ls(expr):
    return s * sp.diff(expr, s)


def Lt(expr):
    return t * sp.diff(expr, t)


def P1s(expr):
    return Ls(expr) + expr


def P1t(expr):
    return Lt(expr) + expr


def P2s(expr):
    le = Ls(expr)
    return Ls(le) + 4*le + 3*expr  # (Ls+1)(Ls+3)


def P2t(expr):
    le = Lt(expr)
    return Lt(le) + 4*le + 3*expr  # (Lt+1)(Lt+3)


# Exact even moments E[T D^a A^b], t set to 1 only after differentiation.
M20 = s**2 * P1s(G)
M02 = P1t(G)
M40 = s**4 * P2s(G)
M04 = P2t(G)
M22 = s**2 * P1t(P1s(G))
M24 = s**2 * P2t(P1s(G))
M42 = s**4 * P1t(P2s(G))
M44 = s**4 * P2t(P2s(G))

alpha = (1 - s**2) / s**2
q4 = (
    4*alpha*(M02 - M20)
    + 3*alpha**2*(M04 + M40)
    - 22*alpha**2*M22
    - 6*alpha**3*(M24 - M42)
    + alpha**4*M44
).subs(t, 1)

print("q4 operation count:", sp.count_ops(q4))

# High-precision point diagnostic only.
mp.mp.dps = 60
q4_num = sp.lambdify(s, q4, "mpmath")
s_locator = mp.mpf("0.5046113125617359603")
print("diagnostic s locator:", mp.nstr(s_locator, 25))
print("diagnostic q4(s locator):", mp.nstr(q4_num(s_locator), 30))

# Outward interval evaluation. The root bracket itself was certified in the
# preceding checkpoint; this run certifies q4 on the entire bracket.
mp.iv.dps = 60
iv = mp.iv
ONE = iv.mpf([1, 1])
mods = {
    "sqrt": iv.sqrt,
    "atan": lambda x: iv.atan2(x, ONE),
    "pi": iv.pi,
}
q4_iv = sp.lambdify(s, q4, modules=[mods])
root_lo = mp.mpf("0.50461")
root_hi = mp.mpf("0.50462")
whole = q4_iv(iv.mpf([str(root_lo), str(root_hi)]))
print("one-shot q4 interval on root bracket:", whole)
assert bool(whole.a > 0)

vals = []
N = 100
for k in range(N):
    a = root_lo + (root_hi-root_lo) * k / N
    b = root_lo + (root_hi-root_lo) * (k+1) / N
    v = q4_iv(iv.mpf([str(a), str(b)]))
    vals.append(v)
    assert bool(v.a > 0)

# Conservative decimal enclosure verified against every outward interval.
LOW_CERT = iv.mpf(["1.30136", "1.30136"])
HIGH_CERT = iv.mpf(["1.30473", "1.30473"])
assert all(bool(v.a > LOW_CERT) for v in vals)
assert all(bool(v.b < HIGH_CERT) for v in vals)
print("100-subinterval certified global enclosure: 1.30136 < q4(s) < 1.30473")

# Exact S4 cubic-tensor transverse splitting for h22.
sq2 = sp.sqrt(2)
sq3 = sp.sqrt(3)
h31 = [sp.Rational(3,2)/sq3] + [-sp.Rational(1,2)/sq3]*3
h22 = [sp.Rational(1,2), sp.Rational(1,2), -sp.Rational(1,2), -sp.Rational(1,2)]
eplus = [1/sq2, -1/sq2, 0, 0]
eminus = [0, 0, 1/sq2, -1/sq2]
I3h31 = sp.simplify(sum(x**3 for x in h31))
plus_ratio = sp.simplify(sum(h22[i]*eplus[i]**2 for i in range(4)) / I3h31)
minus_ratio = sp.simplify(sum(h22[i]*eminus[i]**2 for i in range(4)) / I3h31)
print("I3(h31):", I3h31)
print("D3(h22,e+,e+)/c3 ratio:", plus_ratio)
print("D3(h22,e-,e-)/c3 ratio:", minus_ratio)
assert sp.simplify(I3h31 - 1/sq3) == 0
assert sp.simplify(plus_ratio - sq3/2) == 0
assert sp.simplify(minus_ratio + sq3/2) == 0

print("ALL CHECKS PASSED")
