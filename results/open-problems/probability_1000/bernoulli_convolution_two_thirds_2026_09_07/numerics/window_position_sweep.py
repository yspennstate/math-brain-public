"""Is Err <= CL a UNIFORM statement, or does it need the octave's arithmetic position?

F_K has period P = 3^(K+1).  For a window W = [k0, k0+L) of length L = R = (3/2)^K,
    sum_{k in W} F_K(k) = 2^-(K+1) (L + Err(k0)).
What the L^2 target needs is Err(k0) <= C L at the ONE position k0 = R.  If the same bound holds
uniformly over every k0, the statement is a general one about the window length and much more likely
to be provable by soft means.  If sup_k0 Err(k0)/L grows geometrically while Err(R)/L stays near -0.94,
then the position matters and the problem is genuinely arithmetic.

Computed exactly: tabulate F_K over one full period, then every window sum by a prefix sum.
"""
import numpy as np, sys

for K in (6, 8, 10, 12, 14):
    P = 3 ** (K + 1)
    L = max(1, int(round(1.5 ** K)))
    k = np.arange(P, dtype=np.float64)
    F = np.ones(P)
    for i in range(K + 1):
        F *= np.cos(np.pi * k * (2.0 ** i) / (3.0 ** (i + 1))) ** 2
    pre = np.concatenate(([0.0], np.cumsum(F)))
    # wrap: window sums for every start k0 in [0, P)
    Fd = np.concatenate((F, F[:L]))
    pre2 = np.concatenate(([0.0], np.cumsum(Fd)))
    ws = pre2[L:L + P] - pre2[0:P]
    err = (2.0 ** (K + 1)) * ws - L
    k0 = int(round(1.5 ** K)) % P
    print(f"K={K:>3}  P={P:>10}  L={L:>7}   mean Err = {err.mean():+.6f} (must be 0: {err.mean():.2e})")
    print(f"      Err/L at the octave position k0=R : {err[k0]/L:+.5f}")
    print(f"      max Err/L over ALL k0             : {err.max()/L:+.5f}   at k0={int(err.argmax())}")
    print(f"      min Err/L over ALL k0             : {err.min()/L:+.5f}")
    print(f"      fraction of k0 with Err/L > 1     : {(err > L).mean():.4f}")
    sys.stdout.flush()
    del F, pre, Fd, pre2, ws, err, k
