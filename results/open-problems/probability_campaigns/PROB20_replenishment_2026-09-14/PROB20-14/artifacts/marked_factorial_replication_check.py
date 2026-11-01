from fractions import Fraction
from math import exp, log

# Finite-support algebraic consistency check only.  This is not evidence for
# the infinite-variance theorem.
pi = {0: Fraction(1, 2), 1: Fraction(1, 4), 3: Fraction(1, 4)}
n = 40
qexp = 1.5


def conv_dist(base, count):
    d = {0: Fraction(1)}
    for _ in range(count):
        nd = {}
        for s, p in d.items():
            for x, px in base.items():
                nd[s + x] = nd.get(s + x, Fraction()) + p * px
        d = nd
    return d


convs = [None] * (n + 1)
convs[0] = {0: Fraction(1)}
for j in range(1, n + 1):
    prev = convs[j - 1]
    nd = {}
    for s, p in prev.items():
        for x, px in pi.items():
            nd[s + x] = nd.get(s + x, Fraction()) + p * px
    convs[j] = nd

a = convs[n].get(n - 1, Fraction())
assert a > 0
lam = -log(float(a))

# A genuinely soft mark, not a hard degree set.
g = {0: Fraction(0), 1: Fraction(1, 5), 3: Fraction(4, 5)}
p_g = sum(pi[x] * g.get(x, 0) for x in pi)
q_g = Fraction(0)
for x, px in pi.items():
    q_g += px * g.get(x, 0) * convs[n - 1].get(n - 1 - x, Fraction()) / a
mu = n * q_g

print("a_n =", float(a))
print("lambda_n =", lam)
print("p_g =", float(p_g))
print("q_g =", float(q_g))
print("n q_g =", float(mu))

# Verify the marked factorial identity/Jensen lower bound and Theorem 3.1
# numerically for several negative-tilt parameters.
for m in range(1, min(5, int(float(mu) // 2) + 1)):
    weighted = {x: pi[x] * g.get(x, 0) for x in pi}
    wm = conv_dist(weighted, m)
    residual = convs[n - m]
    event_weight = Fraction(0)
    for s, p in wm.items():
        event_weight += p * residual.get(n - 1 - s, Fraction())

    falling_n = 1
    for j in range(m):
        falling_n *= n - j
    factorial_moment = Fraction(falling_n) * event_weight / a
    lower = (mu / 2) ** m
    assert factorial_moment >= lower
    print(
        f"m={m}: factorial={float(factorial_moment):.12g} "
        f"lower={float(lower):.12g}"
    )

    for theta in [0.03, 0.08, 0.16, 0.35]:
        Lambda = log(
            sum(float(px) * exp(-theta * (x - 1)) for x, px in pi.items())
        )
        Mg = sum(
            float(pi[x] * g.get(x, 0)) * exp(-theta * (x - 1)) for x in pi
        )
        lhs = log(float(q_g / (2 * p_g)))
        rhs = (
            (lam - theta) / m
            + (n - m) * Lambda / m
            + log(Mg / float(p_g))
        )
        if lhs > rhs + 2e-12:
            raise AssertionError((m, theta, lhs, rhs))
    print("  marked inequality checks passed")

# Check that the soft-mark theorem reduces exactly to the previous hard-set
# formula on a singleton support set, up to the numerical grid optimization.
d = 3
p_h = pi[3]
q_h = pi[3] * convs[n - 1].get(n - 1 - 3, Fraction()) / a
mu_h = n * q_h
if float(mu_h) >= 2:
    m = 1
    x = 1 + m * (d - 1)
    N = n - m
    best_H = 0.0
    best_marked = float("inf")
    for j in range(1, 5000):
        theta = j * 0.001
        Lambda = log(
            sum(float(px) * exp(-theta * (xx - 1)) for xx, px in pi.items())
        )
        Hcand = theta * x / N - Lambda
        best_H = max(best_H, Hcand)
        Mg = float(p_h) * exp(-theta * (d - 1))
        rhs = (
            (lam - theta) / m
            + N * Lambda / m
            + log(Mg / float(p_h))
        )
        best_marked = min(best_marked, rhs)
    hard_rhs = lam / m - N * best_H / m
    assert abs(best_marked - hard_rhs) < 2e-3
    print("hard-set recovery gap =", abs(best_marked - hard_rhs))

# Verify the exact winsorized-mark identities W/D^q = E g.
K, D = 0, 3
WP = sum(
    float(px) * min(float(x) ** qexp, float(D) ** qexp)
    for x, px in pi.items()
    if x > K
)
WQ = 0.0
for x, px in pi.items():
    if x > K:
        qx = float(px * convs[n - 1].get(n - 1 - x, Fraction()) / a)
        WQ += qx * min(float(x) ** qexp, float(D) ** qexp)
pg_win = sum(
    float(px) * (min(1.0, (x / D) ** qexp) if x > K else 0.0)
    for x, px in pi.items()
)
qg_win = sum(
    float(px * convs[n - 1].get(n - 1 - x, Fraction()) / a)
    * (min(1.0, (x / D) ** qexp) if x > K else 0.0)
    for x, px in pi.items()
)
assert abs(pg_win - WP / (D**qexp)) < 1e-13
assert abs(qg_win - WQ / (D**qexp)) < 1e-13
print("winsorized mark identities passed; expected marks =", n * qg_win)
print("ALL CHECKS PASSED")
