# Exact restriction step for a perfect matching gate G = OR_{i<=k} (y_a(i) AND y_b(i)) under i.i.d. bias q, via the
# product structure: with s = sqrt(q(1-q)), g_i = 1 - AND_i has biased coefficients 1-q^2 (empty), -q s ({a}), -q s ({b}),
# -s^2 ({a,b}), and 1 - 2G = 2 prod g_i - 1. At an endpoint a of edge 1:
#   B~_a  = erasure term H(1[a in S] | S - a) of the biased spectral sample,
#   Inf~_a = sigma^2 Pr[a pivotal],  sigma^2 = 4q(1-q),
#   rho_a = (B~_a - Inf~_a log2(1/sigma^2)) / Inf~_a    (credited erasure per unit influence).
# If rho_a grows without bound along balanced matchings (k ~ ln2/q^2), no single-coordinate step can prove the biased
# strengthened inequality for this gate, although the gate satisfies it by composition of AND and OR.
import math
def E(X, Y):
    def phi(t): return 0.0 if t <= 0 else -t * math.log2(t)
    return phi(X) + phi(Y) - phi(X + Y)
def step(q, k):
    s2 = q * (1 - q); g0 = 1 - q * q
    A = g0 ** 2; B1 = q * q * s2; B2 = s2 * s2          # squared coefficients on edge 1: {}, {a} or {b}, {a,b}
    rest_all = g0 ** (k - 1)                             # prod_{i>=2} E[g_i^2] = (1-q^2)^{k-1}
    rest_empty = g0 ** (2 * (k - 1))                     # prod_{i>=2} g_i(empty)^2
    Wne = 4 * (rest_all - rest_empty)                    # total of 4 R(T') over nonempty T'
    Fe = 2 * g0 ** k - 1                                 # Fhat(empty)
    Bt = Wne * (E(A, B1) + E(B1, B2))                    # pairs with the other edges not all empty (homogeneity)
    Bt += E(Fe * Fe, 4 * rest_empty * B1) + E(4 * rest_empty * B1, 4 * rest_empty * B2)
    inf = 4 * q * (1 - q) * q * g0 ** (k - 1)
    sig2 = 4 * q * (1 - q)
    return (Bt - inf * math.log2(1 / sig2)) / inf, 1 - g0 ** k
print('balanced perfect matchings, k = round(ln 2 / q^2) edges:')
for q in (0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001):
    k = max(1, round(math.log(2) / q ** 2))
    rho, p1 = step(q, k)
    print('  q=%-6g k=%-8d Pr[G=1]=%.3f  rho_a = %.3f   log2(1/q) = %.2f' % (q, k, p1, rho, math.log2(1 / q)))
# cross-check against brute force for small k
import numpy as np
from biased_gate import biased_transform
for q, k in ((0.3, 3), (0.2, 4), (0.1, 5)):
    m = 2 * k; N = 1 << m; x = np.arange(N); G = np.zeros(N, dtype=bool)
    for i in range(k): G |= ((x >> (2 * i)) & 1).astype(bool) & ((x >> (2 * i + 1)) & 1).astype(bool)
    c = biased_transform(np.where(G, -1.0, 1.0), [q] * m); P = c * c
    low = x[(x & 1) == 0]; X = P[low]; Y = P[low | 1]
    Bb = sum(E(a, b) for a, b in zip(X, Y)); infb = Y.sum(); sig2 = 4 * q * (1 - q)
    print('  brute force q=%g k=%d: rho %.6f  vs product formula %.6f' % (q, k, (Bb - infb * math.log2(1 / sig2)) / infb, step(q, k)[0]))
