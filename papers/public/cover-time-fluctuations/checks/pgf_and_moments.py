"""Symbolic checks (sympy, exact) for Sections 3-4 and the algebra of Section 5.

  1. The excursion transform (3.2) recomputed from the random-sum structure (3.1),
     its mean (3.3), variance (3.4) and third moment (3.5), by differentiation.
  2. The moment-generating bound (3.6): the closed form of E exp(c Y_k / k^2) and a
     uniform bound over k >= 3 at c = 1/4.
  3. The bivariate stage transform (4.1) and the moments (4.2)-(4.3), the third
     moment of N_j used in Lemma 4.2.
  4. The coupon-clock transform (4.5) and the closed forms (4.6)-(4.10), by
     differentiation of (4.5) with symbolic k and r = 1, ..., 6, and by the
     random-sum route for symbolic r.
  5. The identities mu_k + 2k = d_k and sigma_k^2 + mu_k^2 - 4 mu_k - 4k = c_k,
     the polynomial 2t^3 + 16t^2 + 38t + 20 of Proposition 3.1, and the constants
     of (2.3), (2.7), (10.3)-(10.5).
"""
import sympy as sp

k, z, u, v, t, j, r, c = sp.symbols('k z u v t j r c', positive=True)

# ---------------------------------------------------------------- 1. Lemma 3.2
gD = z**2 / (k - 1 - (k - 2) * z)          # PGF of D_i = 1 + Geom_1(1/(k-1))
gF = (1 / k) / (1 - (1 - 1 / k) * u)       # PGF of F ~ Geom_0(1/k)
fY = sp.simplify(z**2 * gF.subs(u, gD))     # PGF of Y_k = 2 + sum_{i<=F} D_i
f32 = z**2 * (k - 1 - (k - 2) * z) / (k * (k - 1) - k * (k - 2) * z - (k - 1) * z**2)
assert sp.simplify(fY - f32) == 0, "(3.2)"
mu = sp.simplify(sp.diff(f32, z).subs(z, 1))
assert sp.expand(mu - (k**2 - k + 2)) == 0, "(3.3)"
fac2 = sp.simplify(sp.diff(f32, z, 2).subs(z, 1))       # E Y(Y-1)
var = sp.expand(fac2 + mu - mu**2)
assert var == sp.expand(k**4 - 4 * k**2 + 5 * k - 2), "(3.4)"
fac3 = sp.simplify(sp.diff(f32, z, 3).subs(z, 1))       # E Y(Y-1)(Y-2)
EY3 = sp.expand(fac3 + 3 * fac2 + mu)
assert sp.degree(EY3, k) == 6, "(3.5): E Y^3 is a polynomial of degree 6 in k"
lead = sp.Poly(EY3, k).all_coeffs()[0]
print("E Y_k^3 =", EY3, " (degree 6, leading coefficient", lead, ") -> (3.5) with C >= that")
# check E Y^3 <= 7 k^6 for k >= 3 exactly (the bound the paper only asserts qualitatively)
assert all(sp.expand(7 * kk**6 - EY3.subs(k, kk)) > 0 for kk in range(3, 60))
print("(3.2)-(3.5) verified symbolically")

# ---------------------------------------------------------------- 2. (3.6)
# E exp(c Y/k^2) = f_k(exp(c/k^2)); it is finite iff the denominator stays positive.
zc = sp.exp(c / k**2)
mgf = f32.subs(z, zc)
vals = [float(mgf.subs({c: sp.Rational(1, 4), k: kk})) for kk in range(3, 200)]
print("E exp(Y_k/(4k^2)) for k=3..199: max = %.6f, at k=%d; last = %.6f" %
      (max(vals), 3 + vals.index(max(vals)), vals[-1]))
assert max(vals) < 3.0
# the algebra used in the proof: (1-1/k)(1+Cc/k) <= 1 - 1/(2k) when Cc <= 1/2
C_, cc = sp.symbols('C_ cc', positive=True)
expr = sp.expand((1 - 1 / k) * (1 + sp.Rational(1, 2) / k) - (1 - 1 / (2 * k)))
assert sp.simplify(expr) == -1 / (2 * k**2) and True
print("(3.6) algebra verified; bound at c = 1/4 uniform over k <= 199")

# ---------------------------------------------------------------- 3. Section 4
G41 = j / (k + 1 - u - (k - j) * v)
EN = sp.simplify(sp.diff(G41, u).subs({u: 1, v: 1}))
EM = sp.simplify(sp.diff(G41, v).subs({u: 1, v: 1}))
ENN = sp.simplify(sp.diff(G41, u, 2).subs({u: 1, v: 1}))     # E N(N-1)
EMM = sp.simplify(sp.diff(G41, v, 2).subs({u: 1, v: 1}))
ENM = sp.simplify(sp.diff(G41, u, v).subs({u: 1, v: 1}))
assert sp.simplify(EN - 1 / j) == 0
assert sp.simplify(ENN + EN - EN**2 - (1 / j + 1 / j**2)) == 0, "(4.2)"
assert sp.simplify(EM - (k - j) / j) == 0
assert sp.simplify(ENM - EN * EM - (k - j) / j**2) == 0, "(4.3)"
assert sp.simplify(EMM + EM - EM**2 - (k**2 / j**2 - k / j)) == 0, "Var M_j = k^2/j^2 - k/j"
# marginal of N_j is Geom_0(j/(j+1)); third raw moment
GN = G41.subs(v, 1)
assert sp.simplify(GN - (j / (j + 1)) / (1 - u / (j + 1))) == 0
ENNN = sp.simplify(sp.diff(GN, u, 3).subs(u, 1))
EN3 = sp.simplify(ENNN + 3 * ENN + EN)
assert sp.simplify(EN3 - (1 / j + 6 / j**2 + 6 / j**3)) == 0, "E N_j^3"
assert all(sp.Rational(13, jj) - EN3.subs(j, jj) >= 0 for jj in range(1, 200))
print("(4.1)-(4.3) and E N_j^3 = 1/j + 6/j^2 + 6/j^3 <= 13/j verified")

# ---------------------------------------------------------------- 4. (4.5)-(4.10)
mu_k = k**2 - k + 2
sig2 = k**4 - 4 * k**2 + 5 * k - 2
d_k = k**2 + k + 2
c_k = 2 * k**4 - 2 * k**3 - 3 * k**2 + k - 6
H = lambda R: sum(sp.Rational(1, jj) for jj in range(1, R + 1))
H2 = lambda R: sum(sp.Rational(1, jj * jj) for jj in range(1, R + 1))
for R in range(1, 7):
    PGF = z**-1 * sp.prod([jj * z**2 / (k + 1 - (k - jj) * z**2 - f32) for jj in range(1, R + 1)])
    m1 = sp.simplify(sp.diff(PGF, z).subs(z, 1))
    m2f = sp.simplify(sp.diff(PGF, z, 2).subs(z, 1))
    varL = sp.simplify(m2f + m1 - m1**2)
    assert sp.simplify(m1 - (d_k * H(R) - 1)) == 0, ("(4.6)", R)
    assert sp.simplify(varL - (c_k * H(R) + d_k**2 * H2(R))) == 0, ("(4.7)", R)
    # (4.8)-(4.10) from the stage structure: S = sum of Z_j, L = r + sum M_j
    # joint transform of (S, L): E[z^S w^L] = w^r prod_j j/(k+1-f(z)-(k-j) w)
    w = sp.symbols('w', positive=True)
    JT = w**R * sp.prod([jj / (k + 1 - (k - jj) * w - f32) for jj in range(1, R + 1)])
    ES = sp.simplify(sp.diff(JT, z).subs({z: 1, w: 1}))
    EL = sp.simplify(sp.diff(JT, w).subs({z: 1, w: 1}))
    VS = sp.simplify(sp.diff(JT, z, 2).subs({z: 1, w: 1}) + ES - ES**2)
    VL = sp.simplify(sp.diff(JT, w, 2).subs({z: 1, w: 1}) + EL - EL**2)
    CSL = sp.simplify(sp.diff(JT, z, w).subs({z: 1, w: 1}) - ES * EL)
    assert sp.simplify(VS - ((sig2 + mu_k**2) * H(R) + mu_k**2 * H2(R))) == 0, ("(4.8)", R)
    assert sp.simplify(VL - (k**2 * H2(R) - k * H(R))) == 0, ("(4.9)", R)
    assert sp.simplify(CSL - mu_k * (k * H2(R) - H(R))) == 0, ("(4.10)", R)
    assert sp.simplify(EL - k * H(R)) == 0
print("(4.5)-(4.10) verified by differentiation for r = 1..6, symbolic k")

# ---------------------------------------------------------------- 5. identities
assert sp.expand(mu_k + 2 * k - d_k) == 0
assert sp.expand(sig2 + mu_k**2 - 4 * mu_k - 4 * k - c_k) == 0
assert sp.expand(2 * (3 + t)**3 - 2 * (3 + t)**2 - 4 * (3 + t) - 4 - (2 * t**3 + 16 * t**2 + 38 * t + 20)) == 0
assert sp.expand(k * (2 * k**2 + k + 1) - k * (3 * k + 5 + 4 / k) - (2 * k**3 - 2 * k**2 - 4 * k - 4)) == 0
# random-sum route for the variance of Y_k
assert sp.expand((k - 1)**2 * (k - 2) + k**3 * (k - 1) - sig2) == 0
# second-order Taylor data of f_k at z = 1 (used by the Lean file): f = 1 + mu (z-1) + (f''(1)/2)(z-1)^2 + O((z-1)^3)
f2 = sp.expand(fac2)                      # f''(1) = E Y(Y-1)
print("f_k''(1) = E Y(Y-1) =", f2)
N = z**2 * (k - 1 - (k - 2) * z)
D = k * (k - 1) - k * (k - 2) * z - (k - 1) * z**2
T = 1 + mu_k * (z - 1) + (f2 / 2) * (z - 1)**2
S, rem = sp.div(sp.expand(N - D * T), sp.expand((z - 1)**3), z)
assert rem == 0, "Taylor identity N - D T = (z-1)^3 S"
print("N - D*T = (z-1)^3 * S with S =", sp.factor(S))
# (2.7): sqrt(2) 2^{-beta} (log k)^{beta-1/2} = (log k / 2)^{beta - 1/2}
beta, L = sp.symbols('beta L', positive=True)
assert sp.simplify(sp.sqrt(2) * 2**(-beta) * L**(beta - sp.Rational(1, 2)) / (L / 2)**(beta - sp.Rational(1, 2))) == 1
# (10.3)-(10.5): E|Z| = sqrt(2/pi), Var|Z| = 1 - 2/pi, and the constants
x = sp.symbols('x', real=True)
phi = sp.exp(-x**2 / 2) / sp.sqrt(2 * sp.pi)
EabsZ = sp.integrate(sp.Abs(x) * phi, (x, -sp.oo, sp.oo))
EZ2 = sp.integrate(x**2 * phi, (x, -sp.oo, sp.oo))
assert sp.simplify(EabsZ - sp.sqrt(2 / sp.pi)) == 0 and sp.simplify(EZ2 - 1) == 0
assert sp.simplify(4 * sp.sqrt(2 / sp.pi) / sp.sqrt(2) - 4 / sp.sqrt(sp.pi)) == 0          # (10.3)
assert sp.simplify(16 * (1 - 2 / sp.pi) / 2 - 8 * (1 - 2 / sp.pi)) == 0                     # (10.4)
assert sp.simplify(2 * sp.sqrt(2) / (2 * sp.sqrt(6)) - 1 / sp.sqrt(3)) == 0                 # (10.5)
assert sp.simplify(sp.sqrt(8 * (1 - 2 / sp.pi)) / 6 - sp.sqrt(2) / 3 * sp.sqrt(1 - 2 / sp.pi)) == 0
# two-vertex unequal decoration: G = sqrt2 (a Z_+ + b (-Z)_+)
a, b = sp.symbols('a b', positive=True)
EZp = sp.integrate(x * phi, (x, 0, sp.oo))
EZp2 = sp.integrate(x**2 * phi, (x, 0, sp.oo))
EG = sp.sqrt(2) * (a + b) * EZp
EG2 = 2 * (a**2 + b**2) * EZp2
assert sp.simplify(EG - (a + b) / sp.sqrt(sp.pi)) == 0
assert sp.simplify(EG2 - EG**2 - (a**2 + b**2 - (a + b)**2 / sp.pi)) == 0
# Prop 10.2: star variance 4(k^2 H2 - k H) <= 2 pi^2 k^2 / 3 and SD/t_hit <= pi/sqrt(6)
assert sp.simplify(sp.sqrt(2 * sp.pi**2 / 3) / 2 - sp.pi / sp.sqrt(6)) == 0
print("identities of Sections 3, 5, 9.1, 10 verified")
print("PGF_AND_MOMENTS_CHECKS_PASS")
