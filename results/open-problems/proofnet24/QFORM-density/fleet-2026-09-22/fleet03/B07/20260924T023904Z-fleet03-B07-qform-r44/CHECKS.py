from __future__ import annotations

import itertools
import math
import random

random.seed(20260924)

# Exact-integer regression of the rank-two tail lemma and the E2 inclusion law.
tail_cases = 0
heavy_cases = 0
min_tail_slack = None
max_heavy = 0

for _ in range(5000):
    r = random.randint(3, 12)
    x = sorted((random.randint(0, 1000) for _ in range(r)), reverse=True)

    tau = sum(x[2:])
    e3 = sum(x[i] * x[j] * x[k]
             for i, j, k in itertools.combinations(range(r), 3))
    slack = 6 * e3 - tau ** 3
    assert slack >= 0
    min_tail_slack = slack if min_tail_slack is None else min(min_tail_slack, slack)
    tail_cases += 1

    Z = sum(x[i] * x[j] for i, j in itertools.combinations(range(r), 2))
    if Z:
        S = sum(x)
        nums = [xi * (S - xi) for xi in x]
        assert sum(nums) == 2 * Z
        # f(x)=x(S-x) is ordered on the finite spectrum because
        # f(x_i)-f(x_j)=(x_i-x_j)(S-x_i-x_j)>=0 for i<j.
        assert all(nums[i] >= nums[i + 1] for i in range(r - 1))
        heavy = [i for i, num in enumerate(nums) if 3 * num > 2 * Z]
        assert len(heavy) <= 2
        assert all(i < 2 for i in heavy)
        max_heavy = max(max_heavy, len(heavy))
        heavy_cases += 1

C3 = 3 * 2 ** (4 / 3) * math.e ** (1 / 3)
eta = 2 ** -30
zeta = 2 ** -12
rho0 = 2 * C3 * eta ** (-1 / 6)
inside = 2 * 6 ** (1 / 3) + (18 / zeta) * (1 / 32) ** 4
carrier_constant = 2 * C3 * math.sqrt(inside)
partner_constant = 2 * math.sqrt(18 * math.pi) / (3 / 256)

assert abs(C3 - 10.550168831164775) < 1e-12
assert abs(rho0 - 675.2108051945455) < 1e-9
assert abs(carrier_constant - 40.61227812251081) < 1e-9
assert abs(partner_constant - 1283.3936766110721) < 1e-9

print(f"tail_cases={tail_cases}")
print(f"min_exact_tail_slack={min_tail_slack}")
print(f"heavy_cases={heavy_cases}")
print(f"max_heavy_count={max_heavy}")
print(f"C3={C3:.15f}")
print(f"rho0={rho0:.15f}")
print(f"rank6_high_ratio_constant={carrier_constant:.15f}")
print(f"partner_core_constant={partner_constant:.15f}")
print("STATUS=PASS")
