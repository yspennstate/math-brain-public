# T354 next-order term under random reshuffling WITH momentum, eps = 0 (agent B, 20 Oct 2026 04:1x). Candidate.
# Claim: with g_i = x + b_i (mean b = 0), B_k = E b^k, Z = b^2 - B2, T = E[b Z^2], K = K_rr(n, beta1, beta2), x0 = d K B3/(2 B2),
#   x*/x0 = 1 + d (K - (3/4) T H/(K B2 B3)) + O(d^2),   fixed n and beta1, d = 1 - beta2 -> 0,
#   H = (1/n) sum_{p=0}^{n-1} (1 - beta1^(p+1)) h(p),   h(p) = 1 - 3p/(n-1) + 2p(p-1)/((n-1)(n-2)),
#   K -> K0 = (1/n) sum_p (1 - beta1^(p+1)) (1 - p/(n-1)).
# Derivation from remainder_rr_mom.py: 0 = x - (d K/2) C/V + (3/8) Q + O(d^3) (the "other epoch" X part is f' = x times O(d^2)).
# In Q set x = 0 and beta2 = 1 (error O(d^3)). A momentum lag i in a FULL earlier epoch has bracket c^2 [M00 + 2(n-1) M0l +
# (n-1) Mjj + (n-1)(n-2) Mjl] = c^2 T (1 - 2 - 1 + 2) = 0 (the epoch sums Z to zero). A lag i <= p in the current epoch has
# bracket c^2 T h(p), whatever i is. Its momentum weight sums to 1 - beta1^(p+1). So Q = (d/B2)^2 T H, and
# x (1 - d K) = d K B3/(2 B2) - (3/8) d^2 T H/B2^2. At beta1 = 0, H = 1/6 and this is next_order_rr.py's formula.
# Part 1 checks H against Q computed by remainder_rr_mom.py's own sum at x = 0, beta2 near 1. Part 2 compares with exact
# roots from audit_A/rr_exact_mom_eps.py (no Taylor step).
import numpy as np, sys, runpy, itertools
from kfactor import K_rr
n = 10; b = np.array([9.0] + [-1.0] * 9); B2 = np.mean(b ** 2); B3 = np.mean(b ** 3); Z = b * b - B2; T = np.mean(b * Z * Z)
P = np.arange(n)
h = 1 - 3 * P / (n - 1) + 2 * P * (P - 1) / ((n - 1) * (n - 2))
def H(b1): return np.mean((1 - b1 ** (P + 1)) * h)
def K0(b1): return np.mean((1 - b1 ** (P + 1)) * (1 - P / (n - 1)))
def coef(b1, K=None): K = K0(b1) if K is None else K; return K - 0.75 * T * H(b1) / (K * B2 * B3)
# part 1: Q from the lemma's lag sum (same code path as remainder_rr_mom.py), x = 0
def Qsum(b1, b2):
    g = b.copy(); V = np.mean(g * g); d = 1 - b2
    M00 = np.mean(g * Z * Z)
    M0l = np.mean([g[a] * Z[a] * Z[c] for a, c in itertools.permutations(range(n), 2)])
    Mjj = np.mean([g[a] * Z[c] * Z[c] for a, c in itertools.permutations(range(n), 2)])
    Mjl = np.mean([g[a] * Z[c] * Z[e] for a, c, e in itertools.permutations(range(n), 3)])
    L = int(np.ceil(60 * max(1 / d, 1 / (1 - b1)) / n)) * n + n; lag = np.arange(L)
    wm = (1 - b1) * b1 ** lag; c = d * b2 ** lag / V; Q = 0.0
    for p in range(n):
        ep = np.where(lag <= p, 0, (lag - p - 1) // n + 1)
        S1 = np.bincount(ep, weights=c); S2 = np.bincount(ep, weights=c * c); s1, s2 = S1[ep], S2[ep]
        Q += np.sum(wm * (c * c * M00 + 2 * c * (s1 - c) * M0l + (s2 - c * c) * Mjj + ((s1 - c) ** 2 - (s2 - c * c)) * Mjl))
    return Q / n
print("test model B2 %g B3 %g T %g" % (B2, B3, T))
for b1 in (0.0, 0.5, 0.9):
    for b2 in (0.999, 0.9999):
        d = 1 - b2; print("beta1 %.1f beta2 %s  Q/(d/B2)^2/T %.6f  H %.6f  ratio %.6f" % (b1, b2, Qsum(b1, b2) / (d / B2) ** 2 / T, H(b1), Qsum(b1, b2) / (d / B2) ** 2 / T / H(b1)))
    print("beta1 %.1f  K0 %.6f  H %.6f  limit coefficient %.6f" % (b1, K0(b1), H(b1), coef(b1)))
# part 2: exact roots
for arg in sys.argv[1:]:
    b1, b2 = (float(v) for v in arg.split(":")); d = 1 - b2
    sv = sys.argv; sys.argv = ["rr_exact_mom_eps.py", str(b1), str(b2), "0"]
    ns = runpy.run_path("../audit_A/rr_exact_mom_eps.py", run_name="rr"); sys.argv = sv
    xs = ns["xs"]; K = K_rr(n, b1, b2); x0 = d * K * B3 / (2 * B2)
    ce = (xs / x0 - 1) / d; cp = coef(b1, K)
    print("beta1 %s beta2 %s K %.6f exact x*/x0 %.9f (x*/x0-1)/d %.5f predicted %.5f gap/d %.3f" % (b1, b2, K, xs / x0, ce, cp, (ce - cp) / d), flush=True)
