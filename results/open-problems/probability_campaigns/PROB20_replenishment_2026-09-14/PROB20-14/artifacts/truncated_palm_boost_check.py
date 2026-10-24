from fractions import Fraction
from math import exp, log
from collections import defaultdict

# Consistency certificate only; not proof of the universal theorem.
# Critical finite-support law: E xi = 1.
pi = {
    0: Fraction(11, 20),
    1: Fraction(1, 5),
    2: Fraction(3, 20),
    5: Fraction(1, 10),
}
assert sum(pi.values()) == 1
assert sum(x * p for x, p in pi.items()) == 1

# Y=(xi-1)_+, so criticality predicts E Y = pi_0 exactly.
y_dist = defaultdict(Fraction)
for x, p in pi.items():
    y_dist[max(x - 1, 0)] += p
mu = sum(y * p for y, p in y_dist.items())
assert mu == pi[0]

# Natural-scale-sized sanity parameters for q=3/2.
q = 1.5
N = 200
d = 40
eta = 0.2
kappa = 0.2
b = kappa * d

# Exact rational DP for sum_{i=1}^N Y_i.
dist = {0: Fraction(1)}
for _ in range(N):
    nxt = defaultdict(Fraction)
    for s, ps in dist.items():
        for y, py in y_dist.items():
            nxt[s + y] += ps * py
    dist = nxt

threshold = float(mu * N) - eta * d
lower_tail_exact = sum(float(p) for s, p in dist.items() if s <= threshold)

# Lemma 4.1's truncated one-sided Chernoff calculation.
EZ = sum(float(y * p) for y, p in y_dist.items() if y <= b)
EZ2 = sum(float(y * y * p) for y, p in y_dist.items() if y <= b)
m_tail = float(mu) - EZ
x = eta * d - N * m_tail
assert x > 0 and EZ2 > 0
truncated_bound = exp(-(x * x) / (2 * N * EZ2))
assert lower_tail_exact <= truncated_bound + 1e-15

# Theorem 5.1 falling-factorial boost on the lower edge of the good event.
pi0 = float(pi[0])
z = d + (float(mu) * N - eta * d)
s = d
log_product = 0.0
for j in range(s - 1):
    numerator = z - j
    denominator = pi0 * (N - j)
    assert numerator > 0 and denominator > 0
    log_product += log(numerator / denominator)

boost_scale = d * d / N
assert log_product > 0

print(f"E[Y]={float(mu):.12g}, pi0={pi0:.12g}")
print(f"exact lower-tail probability={lower_tail_exact:.16g}")
print(f"truncated Chernoff upper bound={truncated_bound:.16g}")
print(f"bound valid={lower_tail_exact <= truncated_bound + 1e-15}")
print(f"log falling-factor product={log_product:.16g}")
print(f"d^2/N={boost_scale:.16g}")
print(f"log-product/(d^2/N)={log_product / boost_scale:.16g}")
