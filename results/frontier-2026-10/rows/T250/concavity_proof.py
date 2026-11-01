"""(sign conditions used on [0, D]: p' >= qL >= 0 because sL >= t - t^3/6 >= 0; p'' >= rL > 0 checked by intervals; 2 pi - pU > 0 checked.)
T250 lemma (i) (agent A, 18 Oct): F(t) = arccos k(t), k = (sin t + (pi - t) cos t)/pi, is concave on (0, pi/2].
With p = pi (1 - k): p' = (pi - t) sin t, p'' = (pi - t) cos t - sin t, and F' = p' / sqrt(p (2 pi - p)). F'' <= 0 iff
    H(t) = p'^2 - 2 p p'' - p p'^2 / (2 pi - p) >= 0   (multiply (log F')' <= 0 by 2 p p' > 0).
Proof of H > 0 on (0, pi/2], computer-assisted and rigorous:
  [0, D]: sin and cos lie between consecutive partial sums of their alternating series (t <= 1), which gives polynomial bounds
          p in [pL, pU], p' in [qL, qU], p'' in [rL, rU] (all >= 0 there). Then H >= qL^2 - 2 pU rU - pU qU^2 / (2 pi - pU) =: P(t),
          a polynomial with P(t) = t^3 (2 pi/3 + O(t)); P/t^3 is checked > 0 on [0, D] by interval arithmetic on the exact quotient.
  [D, pi/2]: H itself by mpmath interval arithmetic with adaptive bisection."""
import sympy as sp
from mpmath import iv, mp
t = sp.symbols('t', nonnegative=True); PI = sp.pi
def enc(c):
    """An enclosure of an exact coefficient in Q[pi]: each rational part enters as an interval quotient of two integers and
    pi as iv.pi, so nothing is rounded to a decimal string (review by agent C, 18 Oct)."""
    P = sp.Poly(sp.expand(c), PI); out = iv.mpf(0)
    for (k,), q in P.terms():
        q = sp.Rational(q); out += iv.mpf(int(q.p)) / iv.mpf(int(q.q)) * iv.pi ** k
    return out
N = 9
def sin_bounds():
    terms = [(-1) ** j * t ** (2 * j + 1) / sp.factorial(2 * j + 1) for j in range(N + 2)]
    s_lo = sum(terms[:N + 1]) if N % 2 == 1 else sum(terms[:N + 2])   # partial sum ending on a negative term
    s_hi = sum(terms[:N + 2]) if N % 2 == 1 else sum(terms[:N + 1])
    return sp.expand(s_lo), sp.expand(s_hi)
def cos_bounds():
    terms = [(-1) ** j * t ** (2 * j) / sp.factorial(2 * j) for j in range(N + 2)]
    c_lo = sum(terms[:N + 1]) if N % 2 == 1 else sum(terms[:N + 2])
    c_hi = sum(terms[:N + 2]) if N % 2 == 1 else sum(terms[:N + 1])
    return sp.expand(c_lo), sp.expand(c_hi)
sL, sU = sin_bounds(); cL, cU = cos_bounds()
# sanity: lo <= true <= hi at a few points in (0, 1]
for v in ('0.01', '0.3', '0.7', '1'):
    vv = sp.Rational(v)
    assert sp.N(sL.subs(t, vv) - sp.sin(vv), 60) <= 0 <= sp.N(sU.subs(t, vv) - sp.sin(vv), 60)
    assert sp.N(cL.subs(t, vv) - sp.cos(vv), 60) <= 0 <= sp.N(cU.subs(t, vv) - sp.cos(vv), 60)
# p = pi (1 - cos) - sin + t cos = pi - sin - (pi - t) cos ; on [0, 1] pi - t > 0
pL = sp.expand(PI - sU - (PI - t) * cU); pU = sp.expand(PI - sL - (PI - t) * cL)
qL = sp.expand((PI - t) * sL); qU = sp.expand((PI - t) * sU)
rL = sp.expand((PI - t) * cL - sU); rU = sp.expand((PI - t) * cU - sL)
D = sp.Rational(1, 4)
# H >= qL^2 - 2 pU rU - pU qU^2/(2pi - pU); clear the positive denominator (2 pi - pU > 0 checked below)
num = sp.expand((qL ** 2 - 2 * pU * rU) * (2 * PI - pU) - pU * qU ** 2)
poly = sp.Poly(num, t)
low = min(m[0] for m in poly.monoms())
print('lowest power of t in the bound numerator:', low)
quot = sp.Poly(sp.expand(num / t ** low), t)
mp.prec = 200; iv.prec = 200
coeffs = [enc(c) for c in quot.all_coeffs()]
def ev(cs, x):
    acc = iv.mpf(0)
    for c in cs: acc = acc * x + c
    return acc
def denom_ok(x):
    pu = ev([enc(c) for c in sp.Poly(pU, t).all_coeffs()], x)
    return (2 * iv.pi - pu).a > 0
import math
K = 2000; worst = None
for i in range(K):
    x = iv.mpf([float(D) * i / K, float(D) * (i + 1) / K])
    v = ev(coeffs, x)
    rl = ev([enc(c) for c in sp.Poly(rL, t).all_coeffs()], x)   # p'' >= rL > 0 needed for -2 p p'' >= -2 pU rU
    if not (v.a > 0 and denom_ok(x) and rl.a > 0):
        print('FAIL on small-t piece at', x); raise SystemExit(1)
    worst = v.a if worst is None or v.a < worst else worst
print(f'[0, {float(D)}]: num/t^{low} > 0 on all {K} subintervals; min lower bound {float(worst):.4g} (2pi/3 * (2pi)... leading)')
def H(x):
    p = iv.pi - iv.sin(x) - (iv.pi - x) * iv.cos(x); q = (iv.pi - x) * iv.sin(x); r = (iv.pi - x) * iv.cos(x) - iv.sin(x)
    return q * q - 2 * p * r - p * q * q / (2 * iv.pi - p)
stack = [(float(D), math.pi / 2)]; boxes = 0; minlow = None
while stack:
    a, b = stack.pop()
    x = iv.mpf([a, b]); x = iv.mpf([a, b if b < math.pi / 2 else iv.pi.b / 2]) if b >= math.pi / 2 else x
    h = H(x); boxes += 1
    if h.a > 0:
        minlow = h.a if minlow is None or h.a < minlow else minlow; continue
    if b - a < 1e-9: print('FAIL near', a, b, h); raise SystemExit(1)
    m = (a + b) / 2; stack += [(a, m), (m, b)]
print(f'[{float(D)}, pi/2]: H > 0 on {boxes} boxes, min lower bound {float(minlow):.4g}')
print('F is concave on (0, pi/2]: PROVED (computer-assisted)')
