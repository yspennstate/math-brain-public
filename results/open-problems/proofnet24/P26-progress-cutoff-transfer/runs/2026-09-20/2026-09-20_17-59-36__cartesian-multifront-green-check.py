from fractions import Fraction
import sympy as sp
import numpy as np
from scipy.linalg import expm

# P26 / T08 exact checker for the Cartesian multifront Green transfer.
# This checks the exact constants used in the degree-12 application and
# the central tensor/chi-square identities behind the proof.

v = sp.Rational(2, 3)          # degree-6 tree radial speed
M2 = sp.Rational(1, 1)         # continuous-time second-moment rate
base_tau2 = sp.simplify(M2 / v**3)
assert base_tau2 == sp.Rational(27, 8)

k = 2
natural_tau2 = sp.simplify(k * base_tau2)
assert natural_tau2 == sp.Rational(27, 4)

# If beta <= sqrt(5)/3 is the normalized nontrivial Ramanujan bulk edge,
# then the Cartesian-square second eigenvalue is <= (1+beta)/2.
gap = sp.simplify((1 - sp.sqrt(5) / 3) / 2)
assert sp.simplify(gap - (3 - sp.sqrt(5)) / 6) == 0

# Exact tensor chi-square identity: 1+chi2(mu^xk||pi^xk)=(1+chi2(mu||pi))^k.
mu = [sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 6)]
pi = [sp.Rational(1, 3)] * 3

def chi2(a, b):
    return sp.simplify(sum((x-y)**2 / y for x, y in zip(a, b)))

c = chi2(mu, pi)
prod_mu = [a*b for a in mu for b in mu]
prod_pi = [a*b for a in pi for b in pi]
cp = chi2(prod_mu, prod_pi)
chi2_residual = sp.simplify(1 + cp - (1 + c)**2)
assert chi2_residual == 0

# Exact continuous-time factorization checked numerically on C3 x C3:
# exp(t(P_square-I)) = exp((t/2)(P-I)) tensor exp((t/2)(P-I)).
P = np.array([
    [0.0, 0.5, 0.5],
    [0.5, 0.0, 0.5],
    [0.5, 0.5, 0.0],
])
I3 = np.eye(3)
P_square = 0.5 * (np.kron(P, I3) + np.kron(I3, P))
I9 = np.eye(9)
t = 1.234567
lhs = expm(t * (P_square - I9))
Hhalf = expm((t / 2) * (P - I3))
rhs = np.kron(Hhalf, Hhalf)
semigroup_error = float(np.max(np.abs(lhs - rhs)))
assert semigroup_error < 1e-12

# Multifront profile for k=2 at the entropic center.
D20 = 1 - sp.Rational(1, 2)**2
assert D20 == sp.Rational(3, 4)

# On the sqrt(log_5 N) scale, N=n^2, the profile denominator is
# sqrt(k * base_tau^2) = 3 sqrt(3)/2.
profile_scale = sp.sqrt(natural_tau2)
assert sp.simplify(profile_scale - 3 * sp.sqrt(3) / 2) == 0

print("v =", v)
print("base tau^2 =", base_tau2)
print("cartesian-square natural tau^2 =", natural_tau2)
print("gap lower bound =", gap, "=", float(gap))
print("chi2 base example =", c)
print("chi2 product example =", cp)
print("chi2 product identity residual =", chi2_residual)
print("semigroup tensor identity max error =", f"{semigroup_error:.3e}")
print("D_2(0) =", D20)
print("sqrt(log_5 N) profile scale =", profile_scale, "=", float(profile_scale))
print("branching mismatch: 5 < 11")
print("P26_T08_CARTESIAN_MULTIFRONT_GREEN_EXACT_PASS")
