"""P0292 (Leskela Problem 4, the characterisation) restricted to the star family on values 1 < 2 < 3:
1 -> 2 at rate a2, 1 -> 3 at rate a3, 2 -> 1 at rate b2, 3 -> 1 at rate b3 (always reversible, a tree).
For each parameter point: (i) the n = 2 test = is P_s(1,3) nondecreasing in s (the only non-trivial concordance
condition, see memo), (ii) the LP dual test of >=_sm at n = 3 and n = 4 over several layouts and speed pairs.
Output: a table; the hypothesis to test is "(2) holds iff b2 >= b3" (and a2, a3 free).
"""
import numpy as np
from scipy.linalg import expm
from p0291_star_sm_lp import fdd, sm_gap

def star4(a2, a3, b2, b3):
    return np.array([[-(a2+a3), a2, a3], [b2, -b2, 0.0], [b3, 0.0, -b3]])

def p13_monotone(Q):
    s = np.linspace(0, 12, 1201); vals = np.array([expm(Q*t)[0, 2] for t in s])
    return float(np.min(np.diff(vals)))   # >= 0 (up to fp) means nondecreasing

def lp_test(Q):
    worst = -1
    for times in ([0.0, 1.0, 2.0], [0.0, 0.3, 1.0], [0.0, 0.5, 1.0, 1.5], [0.0, 1.0, 1.5, 3.0]):
        for c1, c2 in ((0.5, 1.0), (1.0, 2.0), (2.0, 4.0)):
            g, _, _ = sm_gap(fdd(Q, times, c1), fdd(Q, times, c2)); worst = max(worst, g)
    return worst

if __name__ == "__main__":
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    grid = [(1,1,1,1), (1,1,2,1), (1,1,1,2), (1,1,1.2,1), (1,1,1,1.2), (1,1,4,1), (1,1,1,4),
            (2,1,1,1), (1,2,1,1), (3,1,1,1), (1,3,1,1), (1,2,2,1), (2,1,2,1), (1,2,1,2), (2,1,1,2),
            (0.5,2,1,1), (2,0.5,1,1), (1,1,0.5,0.6), (1,1,0.6,0.5), (3,1,1,3), (1,3,3,1), (0.3,3,1,1.1), (3,0.3,1.1,1)]
    print(f"{'a2':>5} {'a3':>5} {'b2':>5} {'b3':>5} | {'min dP13/ds':>12} | {'LP worst':>10} | verdict")
    for (a2, a3, b2, b3) in grid:
        Q = star4(a2, a3, b2, b3); m = p13_monotone(Q); w = lp_test(Q)
        print(f"{a2:5g} {a3:5g} {b2:5g} {b3:5g} | {m:+12.2e} | {w:+10.2e} | {'holds' if w <= 1e-9 else 'FAILS'}  n2:{'ok' if m >= -1e-12 else 'fail'}", flush=True)
