# Damped slice ratio Psi/Var at high equal bias, where the random tests did not reach: the conjunction (s = m) of m
# inputs of bias q has limit ln 4 + 2 q ln(1/q)/(1 - q) as m (1 - q) -> infinity, which tends to ln 4 + 2 as q -> 1.
# Scans all slices s for several (m, q) with the exact level formula of slice_scaling.py.
import mpmath as mp
from slice_scaling import psi_ratio
mp.mp.dps = 60
best = (0, None)
for q in ['0.5', '0.8', '0.9', '0.95', '0.98', '0.99']:
    for m in [16, 64, 160]:
        qq = float(q)
        row = []
        for s in range(0, m + 1):
            r, perr, rho = psi_ratio(m, q, s)
            if rho < 1e-300: continue
            row.append((float(r), s))
            if float(r) > best[0]: best = (float(r), (m, q, s, float(rho)))
        top = max(row)
        pred = float(mp.log(4) + 2 * qq * mp.log(1 / mp.mpf(q)) / (1 - qq))
        print('q %s m %3d  max_s Psi/Var %.4f at s=%d   conjunction s=m: %.4f   limit ln4+2q ln(1/q)/(1-q) = %.4f'
              % (q, m, top[0], top[1], [r for r, s in row if s == m][0], pred), flush=True)
print('overall max', best)
