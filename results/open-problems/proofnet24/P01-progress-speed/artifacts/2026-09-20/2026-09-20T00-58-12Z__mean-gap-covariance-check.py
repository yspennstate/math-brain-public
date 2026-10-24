from fractions import Fraction as F


def q_plus(d, L):
    d = F(d, 1)
    return (d - 1) / ((d - L) * (d - L / d))


def q_minus_at_one(D):
    D = F(D, 1)
    return D / (D * D - 1)


def certificate(d, D, L):
    qp = q_plus(d, L)
    qm = q_minus_at_one(D)
    Q = qp - qm
    c = L * Q
    h = F(D - d, 1)
    raw = (F(D + d, 1) - c * h) / 2
    M = min(F(d, 1), raw)
    delta = 2 * M / (F(D, 1) + L) ** 2
    return qp, qm, Q, c, raw, M, delta


expected = {
    (2, 74, F(6, 5)): (
        F(25, 28), F(74, 5475), F(134803, 153300), F(134803, 127750),
        F(796, 63875), F(796, 63875), F(199, 45151960),
    ),
    (2, 12, F(4, 3)): (
        F(9, 8), F(12, 143), F(1191, 1144), F(397, 286),
        F(17, 286), F(17, 286), F(153, 228800),
    ),
    (2, 20, F(5, 4)): (
        F(32, 33), F(20, 399), F(4036, 4389), F(5045, 4389),
        F(958, 1463), F(958, 1463), F(30656, 10570175),
    ),
}

for key, exp in expected.items():
    got = certificate(*key)
    assert got == exp, (key, got, exp)


def condition(d, D, L):
    *_, raw, M, delta = certificate(d, D, L)
    return raw > 0


assert condition(2, 74, F(6, 5))
assert not condition(2, 75, F(6, 5))
assert condition(2, 12, F(4, 3))
assert not condition(2, 13, F(4, 3))

# Exact finite sanity check of the pairwise covariance identity.
pi = {2: F(1, 5), 5: F(3, 10), 12: F(1, 2)}
y = {2: F(7, 8), 5: F(2, 5), 12: F(1, 10)}
r = sum(pi[n] * n for n in pi)
ey = sum(pi[n] * y[n] for n in pi)
cov = sum(pi[n] * (F(n) - r) * (y[n] - ey) for n in pi)
pair = sum(
    pi[n] * pi[m] * (m - n) * (y[n] - y[m])
    for n in pi for m in pi if n < m
)
assert -cov == pair

print("P01 T06 mean-gap covariance exact checker")
for d, D, L in expected:
    qp, qm, Q, c, raw, M, delta = certificate(d, D, L)
    print(f"d={d} D={D} L={L}:")
    print("  q_plus(L) =", qp)
    print("  q_minus(1) =", qm)
    print("  Qstar =", Q)
    print("  c=L*Qstar =", c)
    print("  M =", M)
    print("  derivative_margin =", delta, "=", float(delta))
print("threshold check: D=74 PASS, D=75 FAIL at L=6/5")
print("threshold check: D=12 PASS, D=13 FAIL at L=4/3")
print("pairwise covariance identity exact sanity: PASS")
print("ALL_EXACT_CHECKS_PASS")
