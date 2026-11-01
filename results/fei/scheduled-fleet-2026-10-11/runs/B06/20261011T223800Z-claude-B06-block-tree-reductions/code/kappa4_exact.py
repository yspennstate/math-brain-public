# Identify every n=4 squared-spectrum class whose min_i B_i/Inf_i is within 1e-6 of the maximum, and decide whether each is
# a dummy-variable extension of the 3-variable point defect (exactly equal kappa) or needs a strict certified separation.
import json, math, sys
import numpy as np
from mpmath import iv
iv.dps = 40
n, N = 4, 16
Hd = np.array([[1 - 2 * (bin(S & x).count('1') & 1) for x in range(N)] for S in range(N)], dtype=np.int64)
t = np.arange(1 << N, dtype=np.int64)[:, None]
F = 1 - 2 * ((t >> np.arange(N, dtype=np.int64)[None, :]) & 1)
W = F @ Hd.T
u2 = np.unique(W * W, axis=0)


def h2(p):
    return 0.0 if p <= 0 or p >= 1 else -(p * math.log2(p) + (1 - p) * math.log2(1 - p))


def kappa_f(w2):
    vals = []
    for i in range(n):
        Ii = sum(int(w2[S]) for S in range(N) if S >> i & 1)
        if Ii == 0:
            continue
        B = sum((w2[T] + w2[T | 1 << i]) / 256 * h2(w2[T] / (w2[T] + w2[T | 1 << i])) if (w2[T] + w2[T | 1 << i]) else 0.0
                for T in range(N) if not T >> i & 1)
        vals.append(B / (Ii / 256))
    return min(vals) if vals else None


def kappa_iv(w2):
    out = []
    for i in range(n):
        Ii = sum(int(w2[S]) for S in range(N) if S >> i & 1)
        if Ii == 0:
            continue
        tot = iv.mpf(0)
        for T in range(N):
            if T >> i & 1:
                continue
            P, Q = int(w2[T]), int(w2[T | 1 << i])
            if P and Q:
                s = iv.mpf(P + Q)
                tot += -(iv.mpf(P) * iv.log(iv.mpf(P) / s) + iv.mpf(Q) * iv.log(iv.mpf(Q) / s)) / iv.log(2)
        out.append(tot / iv.mpf(Ii))
    return min(x.a for x in out), min(x.b for x in out)


exact = 2.5 * h2(0.1) + 1.5
pd3 = sorted([36] + [4] * 7)  # 3-bit point defect squared spectrum scaled by 64 -> on 4 bits scaled by 256: 144 and 16
rows = [(kappa_f(r), r) for r in u2 if any(int(r[S]) for S in range(1, N))]
kmax = max(k for k, r in rows)
near = [(k, r) for k, r in rows if k >= kmax - 1e-6]
report = {'exact_value': exact, 'float_max': kmax, 'classes_within_1e-6': len(near), 'classes': []}
for k, r in near:
    dummy = [i for i in range(n) if all(int(r[S]) == 0 for S in range(N) if S >> i & 1)]
    support = sorted(int(r[S]) for S in range(N) if int(r[S]))
    is_pd3_dummy = len(dummy) == 1 and support == sorted([144] + [16] * 7)
    lo, hi = kappa_iv(r)
    report['classes'].append({'kappa_float': k, 'dummy_coords': dummy, 'nonzero_sq_walsh_x256': support,
                              'is_3bit_point_defect_with_dummy': is_pd3_dummy, 'interval': [str(lo), str(hi)]})
second = max(k for k, r in rows if k < kmax - 1e-6)
report['largest_kappa_outside_these_classes_float'] = second
json.dump(report, open(sys.argv[1], 'w', encoding='utf-8'), indent=1)
print(json.dumps(report, indent=1))
