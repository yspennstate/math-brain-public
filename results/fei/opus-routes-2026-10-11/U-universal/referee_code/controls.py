"""Negative controls: the checks in thmC_check.py and ex_n4.py must be able to fail.

(1) Theorem C(iii) Delta_i H >= c Inf_i and C(viii) lower bound beta(t) >= (c - 2/ln2) I, evaluated on NON
    ratio-critical functions at n = 4 (with c = H(f)/I(f)): violations are expected.
(2) U-Han with the channel constant 2/ln2 replaced by a smaller constant: violations are expected if the
    constant matters.
(3) Theorem G with the factor 2 on (I - Var) replaced by 1.9, and with U replaced by 0.9 U: violations expected.
"""
import math, json, itertools
import numpy as np
from rlib import Spec, all_tables, popcounts, plogq

C2 = 2 / math.log(2)
n = 4
T = all_tables(n); M, N = T.shape
sp = Spec.from_tables(T)
H = sp.H(); I = sp.I(); inf = sp.infl(); U = sp.U(); Var = sp.Var(); p0 = sp.p[:, 0]
nc = I > 1e-15
c = np.where(nc, H / np.where(nc, I, 1), 0.0)
idx = np.arange(N)
dH = np.zeros((M, n))
for i in range(n):
    lo = idx[((idx >> i) & 1) == 0]; hi = lo | (1 << i)
    dH[:, i] = H - 0.5 * (Spec.from_tables(T[:, lo]).H() + Spec.from_tables(T[:, hi]).H())
# ratio-criticality (same definition as thmC_check.py)
maxr = np.zeros(M)
EH = {}
for J in range(N):
    live = [i for i in range(n) if (J >> i) & 1]; fixed = [i for i in range(n) if not (J >> i) & 1]
    for X in itertools.product([0, 1], repeat=len(fixed)):
        base = sum(b << i for b, i in zip(X, fixed))
        keep = [base | sum((((y >> k) & 1) << i) for k, i in enumerate(live)) for y in range(1 << len(live))]
        if len(live) == 0:
            Hg = np.zeros(M); Ig = np.zeros(M)
        else:
            sg = Spec.from_tables(T[:, keep]); Hg = sg.H(); Ig = sg.I()
        if fixed:
            with np.errstate(divide='ignore', invalid='ignore'):
                maxr = np.maximum(maxr, np.where(Ig > 1e-15, Hg / np.where(Ig > 1e-15, Ig, 1), 0))
        for t in [0.25, 0.5, 0.75]:
            w = t ** len(live) * (1 - t) ** len(fixed) / 2 ** len(fixed)
            EH[t] = EH.get(t, 0) + w * Hg
crit = nc & (maxr <= c + 1e-12)
noncrit = nc & ~crit
out = {}
out['noncritical_count'] = int(noncrit.sum())
out['iii_violations_on_noncritical'] = int((noncrit[:, None] & (dH < c[:, None] * inf - 1e-12)).sum())
out['iii_violations_on_critical'] = int((crit[:, None] & (dH < c[:, None] * inf - 1e-12)).sum())
for cst in [C2, 0.5 * C2, 0.25 * C2]:
    worst = max(float((H - (EH[t] / t + cst * ((1 - t) / t) * I)).max()) for t in EH)
    out[f'Han_worst_with_channel_const_{cst:.3f}'] = worst
G_19 = 1.9 * (I - Var) + 2 * U - plogq(p0, np.where(p0 > 0, 1 / np.where(p0 > 0, p0, 1), 1))
G_09 = 2 * (I - Var) + 1.8 * U - plogq(p0, np.where(p0 > 0, 1 / np.where(p0 > 0, p0, 1), 1))
out['thmG_with_1.9(I-Var)_violations'] = int((nc & (H > G_19 + 1e-12)).sum())
out['thmG_with_1.8U_violations'] = int((nc & (H > G_09 + 1e-12)).sum())
print(json.dumps(out, indent=1))
with open('controls_results.json', 'w', encoding='utf-8') as fh:
    json.dump(out, fh, indent=1)
