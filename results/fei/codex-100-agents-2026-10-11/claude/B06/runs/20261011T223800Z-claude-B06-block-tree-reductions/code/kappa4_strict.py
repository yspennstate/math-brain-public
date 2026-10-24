# Rigorous strict separation at n=4: every squared-spectrum class other than the four dummy extensions of the 3-bit point
# defect has min_i B_i/Inf_i < 267/100 < (5/2)h2(1/10)+3/2. Exclusion by the exact rational proxy (B_i <= A_i) when possible,
# otherwise by an mpmath interval upper bound.
import json, sys
from fractions import Fraction
import numpy as np
from mpmath import iv
iv.dps = 40
n, N = 4, 16
Hd = np.array([[1 - 2 * (bin(S & x).count('1') & 1) for x in range(N)] for S in range(N)], dtype=np.int64)
t = np.arange(1 << N, dtype=np.int64)[:, None]
F = 1 - 2 * ((t >> np.arange(N, dtype=np.int64)[None, :]) & 1)
W2 = (F @ Hd.T) ** 2
u2 = np.unique(W2, axis=0)
THR = Fraction(267, 100)
pd3 = sorted([144] + [16] * 7)
excluded_proxy = excluded_interval = pd3_dummy = constants = 0
worst_interval_hi = None
for r in u2:
    if not any(int(r[S]) for S in range(1, N)):
        constants += 1
        continue
    dummy = [i for i in range(n) if all(int(r[S]) == 0 for S in range(N) if S >> i & 1)]
    if len(dummy) == 1 and int(r[0]) == 144 and sorted(int(r[S]) for S in range(N) if int(r[S])) == pd3:
        pd3_dummy += 1
        continue
    a = [abs(int(round(int(v) ** 0.5))) for v in r]
    assert all(x * x == int(v) for x, v in zip(a, r))
    prox = []
    for i in range(n):
        den = sum(int(r[T | 1 << i]) for T in range(N) if not T >> i & 1)
        if den:
            prox.append(Fraction(2 * sum(a[T] * a[T | 1 << i] for T in range(N) if not T >> i & 1), den))
    if min(prox) < THR:
        excluded_proxy += 1
        continue
    vals = []
    for i in range(n):
        Ii = sum(int(r[S]) for S in range(N) if S >> i & 1)
        if Ii == 0:
            continue
        tot = iv.mpf(0)
        for T in range(N):
            if T >> i & 1:
                continue
            P, Q = int(r[T]), int(r[T | 1 << i])
            if P and Q:
                s = iv.mpf(P + Q)
                tot += -(iv.mpf(P) * iv.log(iv.mpf(P) / s) + iv.mpf(Q) * iv.log(iv.mpf(Q) / s)) / iv.log(2)
        vals.append(tot / iv.mpf(Ii))
    hi = min(x.b for x in vals)
    assert hi < iv.mpf(THR.numerator) / THR.denominator, ('NOT SEPARATED', [int(v) for v in r], str(hi))
    excluded_interval += 1
    worst_interval_hi = hi if worst_interval_hi is None or hi > worst_interval_hi else worst_interval_hi
lo_exact = (iv.mpf(5) / 2) * (-(iv.mpf(1) / 10 * iv.log(iv.mpf(1) / 10) + iv.mpf(9) / 10 * iv.log(iv.mpf(9) / 10)) / iv.log(2)) + iv.mpf(3) / 2
res = {'classes_total': int(u2.shape[0]), 'constants': constants, 'pd3_dummy_classes': pd3_dummy,
       'excluded_by_exact_proxy_below_267_100': excluded_proxy, 'excluded_by_interval_below_267_100': excluded_interval,
       'worst_interval_upper': str(worst_interval_hi), 'exact_value_enclosure': str(lo_exact),
       'threshold_below_exact': bool(iv.mpf(THR.numerator) / THR.denominator < lo_exact)}
json.dump(res, open(sys.argv[1], 'w', encoding='utf-8'), indent=1)
print(json.dumps(res, indent=1))
