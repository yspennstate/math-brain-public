"""The three-atom case of Problem 3.3.

An extreme point of the set of probability measures on a compact interval satisfying one linear
equality and one linear inequality has at most three atoms, and carries three only when the inequality
is tight.  So the remaining case is atoms d1 < 0 < d3 (and d2 between the extremes), spread at most
one, with BOTH xi'(0) = 0 and xi''(0) = 0.  Those two equations plus normalisation determine the three
weights; where they are all nonnegative the configuration is admissible and xi(0) is computed.
"""
import numpy as np, itertools

def F_of(d, R2):
    d = np.asarray(d, float)
    den = d * d + R2
    M = np.array([np.ones(3), d / den ** 2, (3 * d * d - R2) / den ** 3])
    try: w = np.linalg.solve(M, np.array([1.0, 0.0, 0.0]))
    except np.linalg.LinAlgError: return None
    if w.min() < -1e-12: return None
    return float((w / den).sum()), w

best = (np.inf, None); tested = 0
grid = np.linspace(0.0, 1.0, 41)
for lo in np.linspace(-1.0, -0.02, 40):
    hi_max = min(1.0, lo + 1.0)
    for hi in np.linspace(0.02, hi_max, 40):
        if hi <= 0 or hi - lo > 1.0 + 1e-12: continue
        for mid in lo + (hi - lo) * grid[1:-1]:
            for R2 in np.linspace(1e-5, 3.0, 120):
                r = F_of([lo, mid, hi], R2)
                if r is None: continue
                tested += 1
                if r[0] < best[0]: best = (r[0], (lo, mid, hi, R2, r[1]))
print(f"admissible three-atom configurations tested: {tested}")
print(f"minimum of xi(0): {best[0]:.8f}")
lo, mid, hi, R2, w = best[1]
print(f"  atoms {lo:+.4f} {mid:+.4f} {hi:+.4f}   R^2 = {R2:.4f}   weights {np.round(w,4)}")
