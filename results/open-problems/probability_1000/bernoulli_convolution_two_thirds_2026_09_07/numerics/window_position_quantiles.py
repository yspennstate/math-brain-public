"""Where does the exponential growth of sup_k0 Err(k0)/L actually live?

The maximum is the window that contains the frequency 0, where F_K = 1: there Err ~ 2^(K+1) - L,
i.e. 2(4/3)^K L, which is the whole observed growth and says nothing.  The question that matters is
whether the growth is confined to a thin set of spike-containing positions or is spread through the
distribution.  So: quantiles of Err(k0)/L over all P positions, as K grows.

If the high quantiles stay bounded and only the extreme tail grows, then Err <= CL holds off a thin
exceptional set and a proof needs only to place the octave away from the spikes.  If the 99th
percentile grows too, the difficulty is everywhere and no position argument helps.
"""
import numpy as np, sys

QS = [0.5, 0.9, 0.99, 0.999, 0.9999]
print(f"{'K':>3} {'P':>10} {'L':>6} {'at k0=R':>9} " + " ".join(f"{'q'+str(q):>9}" for q in QS) + f"{'max':>10} {'>L frac':>9}")
for K in (6, 8, 10, 12, 14, 16):
    P = 3 ** (K + 1)
    if P > 60_000_000:
        print(f"K={K}: period {P} too large for this laptop, skipped")
        continue
    L = max(1, int(round(1.5 ** K)))
    k = np.arange(P, dtype=np.float64)
    F = np.ones(P)
    for i in range(K + 1):
        F *= np.cos(np.pi * k * (2.0 ** i) / (3.0 ** (i + 1))) ** 2
    del k
    Fd = np.concatenate((F, F[:L]))
    del F
    pre = np.concatenate(([0.0], np.cumsum(Fd)))
    del Fd
    ws = pre[L:L + P] - pre[0:P]
    del pre
    err = ((2.0 ** (K + 1)) * ws - L) / L
    del ws
    k0 = int(round(1.5 ** K)) % P
    qs = np.quantile(err, QS)
    print(f"{K:>3} {P:>10} {L:>6} {err[k0]:>+9.4f} " + " ".join(f"{v:>+9.4f}" for v in qs)
          + f"{err.max():>+10.2f} {(err > 1).mean():>9.4f}")
    sys.stdout.flush()
    del err
