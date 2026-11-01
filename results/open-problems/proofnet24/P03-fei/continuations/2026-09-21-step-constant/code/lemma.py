"""Two things worth writing down, checked against every function computed today.

LEMMA (ceiling). Delta_i H <= JS(p_0,p_1) + h(Inf_i) <= 1 + h(Inf_i), so with
delta = max_i Inf_i, and (1+h(x))/x decreasing,
        rho_0(f) <= (1 + h(delta)) / delta.
Corollary: rho_0(f) >= 6.4547837 forces delta <= delta*, computed below.

IMPLICATION. For a restriction-closed class C, if rho_0(f) <= K for all f in C then
H <= K*I on C by induction, so   sup_C rho_0 >= C_FEI(C).
On read-once C_RO = 6.4547837 (numerically; <= 6.4573 proved), so the read-once class
itself must contain functions with rho_0 >= 6.4548.
"""
import random, sys
import ro, control
from fast import rho0_fast, ceiling

def delta_star():
    lo, hi = 1e-9, 0.5
    for _ in range(200):
        mid = (lo+hi)/2
        if ceiling(mid) >= 6.4547837: lo = mid
        else: hi = mid
    return lo

if __name__ == '__main__':
    print("delta* (max influence allowed if rho_0 can reach beta(1/2)) = %.6f" % delta_star())
    print("  ceiling(0.28) = %.4f   ceiling(0.30) = %.4f   ceiling(0.5) = %.4f"
          % (ceiling(0.28), ceiling(0.30), ceiling(0.5)))
    print()
    random.seed(5)
    worst_gap = 1e9; viol = 0; tested = 0
    for n in range(2, 13):
        for _ in range(60):
            t = control.rand_tree(list(range(n)))
            r, rows, _ = rho0_fast(t)
            if r is None: continue
            d = max(x[0] for x in rows)
            gap = ceiling(d) - r
            worst_gap = min(worst_gap, gap)
            if gap < -1e-12: viol += 1
            tested += 1
    print("CEILING checked on %d random read-once trees (n=2..12):" % tested)
    print("  violations: %d      tightest slack ceiling-rho_0: %.6f" % (viol, worst_gap))
    # the same check against BRUTE FORCE values, not the recursion, on small n
    viol2 = 0; t2 = 0
    for n in range(2, 8):
        for _ in range(40):
            t = control.rand_tree(list(range(n)))
            r, rows, _ = control.brute_rho0(t, n)
            if r is None: continue
            d = max(x[1] for x in rows)
            if ceiling(d) - r < -1e-12: viol2 += 1
            t2 += 1
    print("  same check on %d brute-force evaluations: %d violations" % (t2, viol2))
    # negative control: a fake 'rho_0' above the ceiling must be flagged
    fake = ceiling(0.4) + 1.0
    print("  negative control (fake rho_0 = ceiling+1 at delta=0.4): flagged = %s"
          % (ceiling(0.4) - fake < -1e-12))
