# T354 next-order term under random reshuffling, beta1 = 0, eps = 0 (agent B, 20 Oct 2026 04:0x).
# Claim: with g_i = x + b_i (mean b = 0), B_k = E b^k, Z = b^2 - B2, T = E[b Z^2], K = K_rr(n, 0, beta2) and x0 = d K B3/(2 B2),
#   x*/x0 = 1 + d (K - T/(8 K B2 B3)) + O(d^2)  ->  1 + d (1/2 - T/(4 B2 B3)),   fixed n, d = 1 - beta2 -> 0.
# Derivation (the remainder lemma of remainder_rr.py): 0 = x - (d K/2) C/V + (3/8) Q2 + (3/8) X + E[g r], C = 2 x B2 + B3, V = x^2 + B2.
# x = O(d), so C/V = B3/B2 + 2x + O(d^2); X = O(x d^2) and E[g r] = O(d^3). In Q2 = (d^2/V^2) avg_p [M00 + 2 s1 M0l + s2 Mjj +
# (s1^2 - s2) Mjl] take x = 0 and beta = 1 (s1 = s2 = p), errors O(d^3): sum_b Z_b = 0 gives M0l = Mjj = -T/(n-1),
# Mjl = 2T/((n-1)(n-2)), and with avg p = (n-1)/2, avg p(p-1) = (n-1)(n-2)/3 the bracket averages to T (1 - 3/2 + 2/3) = T/6.
# So x (1 - d K) = d K B3/(2 B2) - (3/8) d^2 T/(6 B2^2). Under iid sampling the same bracket is T (not T/6), and the long
# lag sum adds the S term; under RR the earlier epochs cancel (each sums Z to 0), so no S term at this order.
# Part 1 checks the bracket identity by brute force over all permutations; part 2 compares with exact roots from
# audit_A/rr_exact.py (run here at more beta2 values).
import itertools, numpy as np, sys, runpy
from kfactor import K_rr
rng = np.random.default_rng(7)
for n in (5, 6, 7):
    b = rng.normal(size=n); b -= b.mean(); B2 = np.mean(b * b); Z = b * b - B2; T = np.mean(b * Z * Z)
    tot = 0.0
    perms = list(itertools.permutations(range(n)))
    for p in range(n):          # current sample at position p; lags 0..p in this epoch, weights beta = 1
        acc = 0.0
        for pm in perms:
            k = pm[p]; s = sum(Z[pm[p - j]] for j in range(p + 1))
            acc += b[k] * s * s
        tot += acc / len(perms)
    print("n %d bracket avg %.12f  T/6 %.12f  diff %.1e" % (n, tot / n, T / 6, tot / n - T / 6))
n = 10; b = np.array([9.0] + [-1.0] * 9); B2 = np.mean(b ** 2); B3 = np.mean(b ** 3); Z = b * b - B2; T = np.mean(b * Z * Z)
print("test model B2 %g B3 %g T %g  limit coefficient 1/2 - T/(4 B2 B3) = %.6f" % (B2, B3, T, 0.5 - T / (4 * B2 * B3)))
for b2 in sys.argv[1:]:
    argv = sys.argv; sys.argv = ["rr_exact.py", b2, "300"]
    xs = runpy.run_path("../audit_A/rr_exact.py")["xs"]; sys.argv = argv; d = 1 - float(b2); K = K_rr(n, 0.0, float(b2)); x0 = d * K * B3 / (2 * B2)
    c_ex = (xs / x0 - 1) / d; c_pr = K - T / (8 * K * B2 * B3)
    print("beta2 %s K %.6f exact x*/x0 %.8f  (x*/x0 - 1)/d %.5f  predicted %.5f  gap/d %.3f" % (b2, K, xs / x0, c_ex, c_pr, (c_ex - c_pr) / d))
