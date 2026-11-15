#!/usr/bin/env python3
"""Small arithmetic checks for the Green regularization limit.

No PDE discretization or proof certification is performed.
"""
import math
import os
import resource
import signal
from decimal import Decimal, localcontext
from fractions import Fraction as F

signal.alarm(60)
assert os.environ.get("OMP_NUM_THREADS") == "1"
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15

# Coefficients after factoring out pi**(1-p). The two computations use
# different integration variables: radial t=log(2/r) and Green level u.
for p in range(1, 9):
    radial_integral = F(1, 2)
    for j in range(1, p + 1):
        radial_integral *= F(j, 2)
    polar_coefficient = F(8, 2**p) * radial_integral
    level_integral = F(1, 4)
    for j in range(1, p):
        level_integral *= F(j, 4)
    level_coefficient = 4 * p * level_integral
    target = F(math.factorial(p), 4**(p - 1))
    assert polar_coefficient == level_coefficient == target
assert F(math.factorial(2), 4) == F(1, 2)
assert F(math.factorial(4), 4**3) == F(3, 8)
assert 4 * F(3, 8) == F(3, 2)  # (2*pi)^2 times the fourth moment
print("moment coefficients: p=1..8 agree exactly by polar and level-set recurrences")
print("L2 coefficient=1/2; L4 coefficient=3/8; source-error-squared coefficient=3/2")

scalar_cases = 0
with localcontext() as ctx:
    ctx.prec = 110
    tolerance = Decimal("1e-70")
    largest_ratio = Decimal(0)
    for hstr in ["1e-50", "1e-12", "1e-3", "1", "100", "1e12", "1e30"]:
        h = Decimal(hstr)
        s = (1 + 1 / h).ln()  # s=4*pi*G
        lmean = 1 / s
        correction = h + Decimal("0.5") - lmean
        assert 0 <= correction <= Decimal("0.5")
        last_c = Decimal(0)
        for estr in ["1", "1e-1", "1e-4", "1e-12"]:
            epsilon = Decimal(estr)
            c = 1 / (lmean + epsilon * correction)  # c=4*pi*C
            # The second denominator uses the original convex-combination form.
            alternative = 1 / ((1 - epsilon) * lmean + epsilon * (h + Decimal("0.5")))
            assert abs(c - alternative) <= tolerance * max(1, c)
            assert last_c <= c <= s
            last_c = c
            difference = s - c
            identity = epsilon * correction * s * c
            bound = epsilon * s * s / 2
            assert abs(difference - identity) <= tolerance * max(1, bound)
            assert 0 <= difference <= bound + tolerance
            largest_ratio = max(largest_ratio, difference / bound)
            scalar_cases += 1
    for estr in ["1", "1e-1", "1e-4", "1e-12"]:
        epsilon = Decimal(estr)
        c_diagonal = 1 / (epsilon / 2)
        assert c_diagonal == 2 / epsilon
    print(f"regularization identities: {scalar_cases} high-precision off-diagonal cases; 4 diagonal cases")
    print(f"largest (G-C)/(2*pi*epsilon*G^2) in fixtures={largest_ratio:.12f}")

# Independent exact scalar checks of the correction estimate with a shared
# contraction bound; includes a spectral gap of 1/100.
resolvent_cases = 0
for d in [F(1, 5), F(1, 2), F(99, 100)]:
    alpha = 1 - d
    for delta in [F(0), F(1, 100), F(1, 2)]:
        for eta in [F(0), d / 2]:
            b = F(1)
            c = b - delta
            actual = b*b/alpha - c*c/(alpha + eta)
            bound = 2*b*delta/alpha + b*b*eta/(alpha*alpha)
            assert 0 <= actual <= bound
            resolvent_cases += 1
assert resolvent_cases == 18
print(f"correction error: {resolvent_cases} exact-rational scalar checks")
print("PASS (arithmetic checks only)")
print(f"priority={os.getpriority(os.PRIO_PROCESS, 0)}, "
      f"peak_rss_bytes={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}")
