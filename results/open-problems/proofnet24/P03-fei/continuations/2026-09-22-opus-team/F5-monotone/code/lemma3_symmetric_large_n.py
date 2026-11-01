"""Lemma 3 for symmetric thresholds at large n (exact, Krawtchouk).  For f = [#(-1) < k] every coordinate has
U_i = all others, N_i = n, and the Lemma 3 quantity equals sum_k k W_k ln(n/k) / I.  Bound: L1 = 4.1511."""
import math, sys
from symthresh import kraw_all

def lemma3_ratio(n, k):
    N = n - 1
    K = kraw_all(N, k - 1)
    L2 = 2 * (n - 1)
    lWs = []
    for j in range(1, n + 1):
        a = K[j - 1]
        if a == 0: continue
        lw = 2 * (math.log2(abs(a)) + math.log2(math.comb(N, k - 1)) - math.log2(math.comb(N, j - 1))) - L2
        lWs.append((j, math.log2(math.comb(n, j)) + lw))
    top = max(l for _, l in lWs)          # common scale factor cancels in the ratio
    num = 0.0; I = 0.0
    for j, l in lWs:
        Wj = 2.0 ** (l - top)
        num += j * Wj * math.log(n / j); I += j * Wj
    return num / I

L1 = 2 * math.log(3 * math.sqrt(3 / math.pi)) + 2
for n in [21, 101, 401, 1001, 2001, 4001]:
    ks = sorted(set([1, 2, 3, n // 10, n // 4, n // 3, (n + 1) // 2]))
    vals = [(k, lemma3_ratio(n, k)) for k in ks if k >= 1]
    worst = max(v for _, v in vals)
    print("n=%d  E ln(n/|T|+1) by k: %s   max/L1 = %.4f" % (n, ", ".join("%d:%.3f" % kv for kv in vals), worst / L1), flush=True)
