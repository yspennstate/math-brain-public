#!/usr/bin/env python3
import math

C0 = math.log2(32.0 / 31.0)


def phi(delta):
    return 4.0 * delta / math.log2(1.0 / (2.0 * delta))


def defect_threshold_from_s(s):
    """Solve phi(delta)=1/(16s+1) by monotone bisection on (0,1/4)."""
    target = 1.0 / (16.0 * s + 1.0)
    lo, hi = 0.0, 0.249999999999
    for _ in range(180):
        mid = (lo + hi) / 2.0
        if phi(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def defect_threshold_r(r):
    return defect_threshold_from_s(float(r))


def defect_threshold_L(L):
    return defect_threshold_from_s(float(L) + C0)


prev = None
max_resid = 0.0
for r in range(1, 4097):
    d = defect_threshold_r(r)
    resid = abs(phi(d) - 1.0 / (16.0 * r + 1.0))
    max_resid = max(max_resid, resid)
    if prev is not None:
        assert d < prev
    prev = d

print("c0=log2(32/31) =", format(C0, ".15f"))
print("max_bisection_residual_r_1_to_4096 =", format(max_resid, ".3e"))
print("r delta_star(r)")
for r in [1, 2, 3, 4, 8, 16, 32, 64, 128, 256]:
    print(r, format(defect_threshold_r(r), ".15f"))
print("L delta_star(L+c0)")
for L in [1, 2, 3, 4, 8, 16, 32, 64, 128]:
    print(L, format(defect_threshold_L(L), ".15f"))

eta = 1.0 / 32.0
print("eta0_upper_cap_1/32 =", format(eta, ".15f"))
print("codim_1_low_defect_terminal_impossible =", defect_threshold_r(1) > eta)

worst = 0.0
for r in range(1, 4097):
    a = 1.0 / (16.0 * r + 1.0)
    lhs = 16.0 * r * a
    rhs = 1.0 - a
    worst = max(worst, lhs - rhs)
print("max_[16r*a-(1-a)]_at_a=1/(16r+1) =", format(worst, ".3e"))
