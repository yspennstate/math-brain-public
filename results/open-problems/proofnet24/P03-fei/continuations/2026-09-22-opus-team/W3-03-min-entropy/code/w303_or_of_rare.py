"""OR-of-copies mechanism (tribes generalised), exhaustive over the inner function f on n <= 4 variables.

F = OR_s(f_1..f_s), f_i disjoint copies of f with Pr[f true] = p.  With q = (1-p)^s = Pr[F false]:
  Fhat(empty) = 2q-1,  max_{S nonempty}|Fhat(S)| = (1-p)^(s-1) max_{S nonempty}|fhat(S)|,
  I(F) = s (1-p)^(s-1) I(f).
At exact balance q = 1/2 (s = ln2 / -ln(1-p), real s; the empty coefficient then vanishes):
  ratio_OR(f) = (2 + 2 log2(1-p) + Hstar(f)) (1-p) (2 (-ln(1-p))) / (ln2 * I(f)),
  Hstar(f) = min over nonempty S of log2(1/fhat(S)^2).
For f = AND_w this tends to 2/ln 2 as w -> infinity (tribes).  Reports max over all f (true = minority value).
"""
import sys, json
import numpy as np
import psutil
_p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 10, 11, 12, 13, 14, 15])
sys.path.insert(0, __file__.rsplit("/", 1)[0].rsplit("\\", 1)[0])
from fmei_lib import coeffs, popcounts, bits_to_pm
LN2 = np.log(2.0)
res = {}
for n in range(1, 5):
    N = 1 << n
    masks = np.arange(1 << N, dtype=np.uint64)
    tt = bits_to_pm(masks, n)
    c = coeffs(tt)
    p_true = (1 - c[:, 0]) / 2
    keep = (p_true > 0) & (p_true <= 0.5)
    c = c[keep]; p = p_true[keep]; m = masks[keep]
    pc = popcounts(n).astype(np.float64)
    I = (c * c) @ pc
    Hs = -np.log2((c[:, 1:] ** 2).max(axis=1))
    r = (2 + 2 * np.log2(1 - p) + Hs) * (1 - p) * 2 * (-np.log(1 - p)) / (LN2 * I)
    k = int(np.argmax(r))
    res[n] = dict(max_ratio_OR=float(r[k]), mask=hex(int(m[k])), p=float(p[k]), Hstar=float(Hs[k]), I=float(I[k]))
    print(n, json.dumps(res[n]), flush=True)
# AND_w family for reference
for w in (2, 4, 8, 16, 32):
    p = 2.0 ** -w; Hs = 2 * (w - 1); I = w * 2.0 ** (1 - w)
    print("AND", w, (2 + 2 * np.log2(1 - p) + Hs) * (1 - p) * 2 * (-np.log(1 - p)) / (LN2 * I))
