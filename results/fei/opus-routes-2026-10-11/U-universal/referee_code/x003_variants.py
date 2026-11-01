"""X003 selector ratios for both activation sizes: the campaign's r = 2k and the author's r = k.
F = G spliced with H' at a physical selector y, G = 1 + A_r (b - 1), H' = 1 + A_r (b' - 1), b' = b - 2*1_{x=0}.
Prints Delta_y U / Inf_y and Delta_y H / Inf_y (direct physical restriction, float logs)."""
import sys, json
import numpy as np
from rlib import Spec, restrict_tables


def table(k, r):
    n = 1 + r + k; N = 1 << n
    xs = np.arange(N, dtype=np.int64)
    xb = xs & ((1 << k) - 1)
    zb = (xs >> k) & ((1 << r) - 1)
    yb = (xs >> (k + r)) & 1
    q = np.zeros(N, dtype=np.int64)
    for a in range(k // 2):
        q += ((xb >> (2 * a)) & 1) * ((xb >> (2 * a + 1)) & 1)
    b = 1 - 2 * (q & 1)
    f = np.where(zb == 0, b, 1)
    f = np.where((yb == 1) & (zb == 0) & (xb == 0), -f, f)
    return f.astype(np.int8), n, k + r


def ratios(k, r):
    f, n, iy = table(k, r)
    sp = Spec.from_tables(f)
    H = float(sp.H()[0]); U = float(sp.U()[0]); inf = sp.infl()[0]; I = float(inf.sum())
    a = Spec.from_tables(restrict_tables(f, iy, 1)); b = Spec.from_tables(restrict_tables(f, iy, -1))
    dH = H - 0.5 * float(a.H()[0] + b.H()[0]); dU = U - 0.5 * float(a.U()[0] + b.U()[0])
    return dict(k=k, r=r, n=n, Inf_y=float(inf[iy]), dU_over_Inf=dU / float(inf[iy]), dH_over_Inf=dH / float(inf[iy]), U_over_I=U / I, H_over_I=H / I)


if __name__ == "__main__":
    res = []
    for (k, r) in [(4, 4), (6, 6), (8, 8), (4, 8), (6, 12), (10, 10)]:
        d = ratios(k, r); res.append(d); print(json.dumps(d), flush=True)
    with open('x003_variants_results.json', 'w', encoding='utf-8') as fh:
        json.dump(res, fh, indent=1)
