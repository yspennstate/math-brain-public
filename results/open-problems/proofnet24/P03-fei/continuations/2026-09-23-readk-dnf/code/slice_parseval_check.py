# Parseval check for the all-slice scans that ran at a fixed 60 digits (slice_highbias.py, slice_highbias2.py):
# psi_ratio returns (Psi/Var, relative Parseval error, rho); a small error certifies the coefficients in aggregate.
import mpmath as mp
from slice_scaling import psi_ratio
mp.mp.dps = 60
for q, m in [('0.9', 64), ('0.95', 64), ('0.98', 64), ('0.99', 64), ('0.8', 64), ('0.5', 64)]:
    worst = mp.mpf(0); worst_s = None; top = 0.0
    for s in range(0, m + 1):
        r, perr, rho = psi_ratio(m, q, s)
        if rho < 1e-300: continue
        if abs(perr) > worst: worst, worst_s = abs(perr), s
        top = max(top, float(r))
    print('q %s m %d: max |Parseval rel err| over all s = %s (at s=%s); max Psi/Var %.4f' % (q, m, mp.nstr(worst, 3), worst_s, top), flush=True)
