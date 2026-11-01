"""Certify n<=4 maxima: interval arithmetic (mpmath.iv, 120 bits) for the point-defect values,
and float64 runner-up gaps from the exhaustive scan (gap >> float error bound 1e-11)."""
import sys, json, numpy as np, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from descent_scan import analyze, all_tables, descent
from mpmath import iv
iv.prec = 120
def H_pd(m):
    if m <= 0: return iv.mpf(0)
    e = iv.mpf(2) ** (1 - m); c = (1 - e) ** 2
    t0 = -c * iv.log(c) / iv.log(2) if m >= 2 else iv.mpf(0)
    return t0 + (iv.mpf(2) ** m - 1) * iv.mpf(4) ** (1 - m) * 2 * (m - 1)
out = {}
for n in (2, 3, 4):
    Hn = H_pd(n); In = n * iv.mpf(2) ** (1 - n)
    Mn = Hn / In
    phis = [(Hn - iv.mpf(2) ** (-k) * H_pd(n - k)) / (k * iv.mpf(2) ** (1 - n)) for k in range(1, n)]
    F = all_tables(n); res = analyze(F, n); H, I = res['H'], res['I']; nc = I > 1e-12
    ratio = np.where(nc, H / np.where(nc, I, 1), -np.inf)
    phi, phi1, argA = descent(res, n); phi = np.where(nc & np.isfinite(phi), phi, -np.inf)
    pd_mask = np.array([bin(t).count('1') in (1, (1 << n) - 1) for t in range(F.shape[0])])
    out[n] = dict(M_interval=[str(Mn.a), str(Mn.b)],
                  phi_pd_by_blocksize={k + 1: [str(p.a), str(p.b)] for k, p in enumerate(phis)},
                  ratio_runnerup=float(ratio[~pd_mask].max()), phi_runnerup=float(phi[~pd_mask].max()),
                  ratio_pd_float=float(ratio[pd_mask].max()), phi_pd_float=float(phi[pd_mask].max()))
    print(n, json.dumps(out[n]))
json.dump(out, open(sys.argv[1], 'w'), indent=1)
