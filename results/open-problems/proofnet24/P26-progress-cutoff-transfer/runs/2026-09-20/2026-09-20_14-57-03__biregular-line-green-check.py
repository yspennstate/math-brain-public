from fractions import Fraction
import sympy as sp

K = sp.Integer(8)
k = sp.Integer(2)
D = K + k
S = K * k

# Biregular line-graph spectrum.
s2 = sp.symbols("s2", nonnegative=True)
a, b = K + 1, k + 1
theta_plus = (a + b + sp.sqrt((a - b)**2 + 4*s2)) / 2
theta_minus = (a + b - sp.sqrt((a - b)**2 + 4*s2)) / 2
qplus = sp.simplify((theta_plus - 2) / D)
qminus = sp.simplify((theta_minus - 2) / D)
qtop = sp.simplify(qplus.subs(s2, 18))
gap = sp.simplify(1 - qtop)
assert qtop == sp.Rational(2, 5) + 3*sp.sqrt(3)/10
assert gap == sp.Rational(3, 5) - 3*sp.sqrt(3)/10
assert sp.simplify(sp.diff(qplus, s2)) > 0
assert sp.simplify(sp.diff(qminus, s2)) < 0
assert sp.simplify(qplus.subs(s2, 0)) == sp.Rational(7, 10)
assert sp.simplify(qminus.subs(s2, 0)) == sp.Rational(1, 10)
assert sp.Rational(-2, 10) < qtop

# Radial Markov-additive clock.
# Type A: far endpoint is R, type B: far endpoint is L.
counts_A = {-1: 1, 0: int(K - 1), 1: int(k)}
counts_B = {-1: 1, 0: int(k - 1), 1: int(K)}
assert sum(counts_A.values()) == D
assert sum(counts_B.values()) == D

pi_A = sp.Rational(K + 1, D + 2)
pi_B = sp.Rational(k + 1, D + 2)
assert sp.simplify(pi_A + pi_B) == 1
drift_A = sp.Rational(k - 1, D)
drift_B = sp.Rational(K - 1, D)
v = sp.simplify(pi_A*drift_A + pi_B*drift_B)
assert v == sp.Rational(1, 4)

# Continuous-time variance rate from the principal eigenvalue of the tilted one-jump matrix.
z = sp.symbols("z", real=True)
M = sp.Matrix([
    [sp.Rational(K - 1, D), (sp.exp(-z) + k*sp.exp(z))/D],
    [(sp.exp(-z) + K*sp.exp(z))/D, sp.Rational(k - 1, D)]
])
tr = sp.trace(M)
det = sp.det(M)
lam = sp.simplify((tr + sp.sqrt(tr**2 - 4*det))/2)
assert sp.simplify(lam.subs(z, 0)) == 1
v_tilt = sp.simplify(sp.diff(lam, z).subs(z, 0))
sigma2 = sp.simplify(sp.diff(lam, z, 2).subs(z, 0))
assert v_tilt == sp.Rational(1, 4)
assert sigma2 == sp.Rational(37, 80)
tau2 = sp.simplify(sigma2 / v**3)
assert tau2 == sp.Rational(148, 5)

# General formulas.
Kg, kg = sp.symbols("K k", positive=True)
Dg = Kg + kg
Sg = Kg * kg
vg = sp.simplify(2*(Sg - 1)/(Dg*(Dg + 2)))
sigmag = sp.simplify(
    4*((Sg + 1)*(Dg + 2)**2 - 2*(Sg - 1)**2)/(Dg*(Dg + 2)**3)
)
assert sp.simplify(vg.subs({Kg: 8, kg: 2}) - v) == 0
assert sp.simplify(sigmag.subs({Kg: 8, kg: 2}) - sigma2) == 0

# Sphere growth and long-range mismatch.
# For the (9,3) tree line graph, |S_{2m}|=2*16^m and
# |S_{2m+1}|=10*16^m, hence exponential growth base 4 per line step.
assert int(sp.sqrt(S)) == 4
assert D - 1 == 9
assert sp.sqrt(S) < D - 1

print("degree =", D)
print("Ramanujan bulk line eigenvalue top =", qtop)
print("one-sided spectral gap lower bound =", gap, "~", float(gap))
print("type A counts =", counts_A)
print("type B counts =", counts_B)
print("stationary type law =", (pi_A, pi_B))
print("radial speed v =", v)
print("continuous-time variance rate sigma^2 =", sigma2)
print("profile tau^2 =", tau2)
print("entropic radius base =", sp.sqrt(S))
print("cutoff center = 4 log_4 n = 2 log_2 n")
print("LRE branching mismatch: cover growth base 4 < output tree base 9")
print("P26_T08_BIGRAPH_LINE_GREEN_EXACT_PASS")
