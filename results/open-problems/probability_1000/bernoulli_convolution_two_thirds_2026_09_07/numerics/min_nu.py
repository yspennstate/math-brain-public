# DECISIVE QUESTION.  With a Selberg/Fejer majorant of the window one gets
#     sum_{k in W} F_K(k)  <=  (|W| + P/Q) 2^{-(K+1)}     provided NO nonzero eps has |nu_eps| <= Q,
# where P = 3^{K+1}, nu_eps = sum_{i=0}^K eps_i 2^i 3^{K-i}, eps in {0,+-1}.
# The target needs Q >~ 3 (3/2)^K.  So: is  min_{eps != 0} |nu_eps|  >=  c (3/2)^K ?
# Meet in the middle over the two halves of the index range.
import numpy as np, sys, math
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 22
def half(coeffs):
    v = np.array([0], dtype=np.int64)
    for c in coeffs:
        v = np.concatenate([v - c, v, v + c])
    return v
print(" K |   min |nu_eps| over eps != 0 |   (3/2)^K   | ratio min/(3/2)^K | 2^K for scale")
for K in range(1, KMAX+1):
    co = [2**i * 3**(K-i) for i in range(K+1)]
    if max(co) > 2**60: print(f"K={K}: overflow risk, stop"); break
    m = (K+1)//2
    A = half(co[:m]); B = half(co[m:])
    if A.size*1.0*B.size > 4e12: print(f"K={K}: too big"); break
    B.sort()
    best = None
    # for each a, the closest b to -a
    idx = np.searchsorted(B, -A)
    for shift in (-1, 0):
        j = np.clip(idx + shift, 0, B.size-1)
        s = A + B[j]
        s = np.abs(s)
        s = s[s > 0]
        if s.size:
            v = int(s.min())
            best = v if best is None else min(best, v)
    r = best/(1.5**K)
    print(f"{K:2d} | {best:>28d} | {1.5**K:11.1f} | {r:16.4f} | {2**K}", flush=True)
