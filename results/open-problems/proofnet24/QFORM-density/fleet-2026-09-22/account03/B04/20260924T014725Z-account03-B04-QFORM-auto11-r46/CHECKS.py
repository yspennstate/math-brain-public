from fractions import Fraction
import itertools
import math
import sympy as sp

# Exact deterministic verification for account03/B04 r46.
# No Monte Carlo is used.

# Sylvester H_8 and five normalized dense orthogonal directions.
H = sp.Matrix([[1]])
for _ in range(3):
    old = H
    H = sp.Matrix.vstack(sp.Matrix.hstack(old, old),
                         sp.Matrix.hstack(old, -old))
assert H * H.T == 8 * sp.eye(8)
w = [sp.Matrix([H[i, j] for j in range(8)]) / sp.sqrt(8)
     for i in range(5)]

L = sp.Integer(16)
eps = sp.Rational(1, 16)
rows = [L * w[0]]
for g in (1, 2, 3):
    rows += [w[g] / sp.sqrt(2), w[g] / sp.sqrt(2)]
rows += [eps * w[4] / sp.sqrt(2), eps * w[4] / sp.sqrt(2)]
M = sp.Matrix.hstack(*rows).T
assert M.shape == (9, 8)
assert all(x != 0 for x in M)

# Singular-value squares are 256,1,1,1,1/256 plus three zeros.
ev = (M.T * M).eigenvals()
assert ev == {sp.Integer(256): 1, sp.Integer(1): 3,
              sp.Rational(1, 256): 1, sp.Integer(0): 3}

# Exact row-Gram fourth-volume enumeration.
def gramdet(indices):
    R = M[list(indices), :]
    return sp.simplify((R * R.T).det())

E4 = sp.Integer(0)
H0 = sp.Integer(0)
positive = {}
for S in itertools.combinations(range(9), 4):
    d = gramdet(S)
    E4 += d
    if d != 0:
        positive[S] = d
    if 0 in S:
        H0 += d
assert sp.simplify(E4) == sp.Rational(66305, 256)
assert H0 == 259
assert len(positive) == 48
rho = sp.simplify(H0 / E4)
assert rho == sp.Rational(66304, 66305)

# Anchored residual triple law; projected determinant is d/||m_0||^2=d/256.
beta = [sp.Rational(0) for _ in range(9)]
sum_w_log_D = 0.0
for S, d in positive.items():
    if 0 not in S:
        continue
    ww = sp.simplify(d / H0)
    D = sp.simplify(d / 256)
    sum_w_log_D += float(ww) * math.log(float(D))
    for j in S:
        if j != 0:
            beta[j] += ww
betas = [sp.simplify(beta[j]) for j in range(1, 9)]
assert betas[:6] == [sp.Rational(129, 259)] * 6
assert betas[6:] == [sp.Rational(3, 518)] * 2
assert max(betas) < sp.Rational(1, 2)
assert sum(betas) == 3

sum_a_log_a = sum(float(a) * math.log(float(a)) for a in betas if a > 0)
Gamma = math.exp(sum_w_log_D - sum_a_log_a)
Omega = 256.0 * Gamma
assert abs(Gamma - 0.9989708620178627) < 1e-12
assert abs(Omega - 255.73654067657284) < 1e-10

# Constants and equation-level comparisons.
C4 = 2 * math.sqrt(2) * math.exp(0.25) * 3 ** 0.75
C_hub = 2 ** (17 / 8) * 3 ** 0.25
new_exact = 2 ** (9 / 4) * Omega ** (-1 / 8)
new_coarse = C_hub * float(H0) ** (-1 / 8)
partner = 3 * math.e * (259 / 256) ** (-1 / 6)
pair = C4 * 129 ** (-1 / 8)
high_carrier_hub = C_hub * 25 ** (1 / 8)
high_carrier_pair = C4 * 50 ** (1 / 8)
high_carrier = max(high_carrier_hub, high_carrier_pair)

assert abs(new_exact - 2.378720371807186) < 1e-12
assert abs(new_coarse - 2.8662006090751166) < 1e-12
assert abs(partner - 8.13902601868726) < 1e-12
assert abs(pair - 4.509577357402878) < 1e-12
assert abs(high_carrier_hub - 8.58443181728124) < 1e-12
assert abs(high_carrier_pair - 13.499907897578499) < 1e-12
assert new_exact < pair < partner
assert high_carrier < 13.5

print("QFORM_B04_R46_ANCHORED_E4_HUB_CHECK_PASS")
print("E4", E4)
print("H0", H0)
print("rho", rho)
print("betas", betas)
print("Gamma", repr(Gamma))
print("Omega", repr(Omega))
print("new_exact", repr(new_exact))
print("new_coarse", repr(new_coarse))
print("partner", repr(partner))
print("pair", repr(pair))
print("high_carrier_coeff", repr(high_carrier))
