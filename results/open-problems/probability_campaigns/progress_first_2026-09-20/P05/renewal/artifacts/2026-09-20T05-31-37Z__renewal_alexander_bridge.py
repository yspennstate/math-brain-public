#!/usr/bin/env python3
"""
P05 binary LCS: numerical sanity checks for the explicit renewal/Alexander bridge.

The proof itself is in the accompanying immutable report.  This script only
checks the numerical margins for the fixed Alexander Proposition 2.4
parameters A=theta=8/5 at n=8, evaluates the resulting explicit error
function, and locates the first even r for which the bridge error at M=20 is
smaller than the current internal repository interval width.

No Monte Carlo is used.
"""

import math

A = 8.0 / 5.0
THETA = 8.0 / 5.0


def alexander_condition_rhs_A(n: int) -> float:
    L = math.log(2.0 * n)
    return (
        1.0
        + 1.0 / (2.0 * n * L)
        + 2.0 * A / math.sqrt(2.0 * n * L)
        + math.log(5.1 * A) / L
        + math.log(L) / (2.0 * L)
    )


def alexander_condition_rhs_theta(n: int) -> float:
    return 2.0 + math.log(4.0) / math.log(2.0 * n)


def bridge_error(r: int, M: int) -> float:
    """Explicit proved error epsilon_{r,M}, valid for even r>=8."""
    return (
        (24.0 / 5.0) * math.sqrt(math.log(2.0 * r) / (2.0 * r))
        + math.sqrt(2.0 * math.log(2.0) / r)
        + math.sqrt(2.0 / r)
        + 1.0 / r
        + 2.0 ** (-(M - 1))
    )


n0 = 8
rhs_A = alexander_condition_rhs_A(n0)
rhs_theta = alexander_condition_rhs_theta(n0)
assert A * A > rhs_A
assert THETA * THETA >= rhs_theta

# For n>=8 every positive term in rhs_A is decreasing: log(2n)>e makes
# log(log(2n))/(2 log(2n)) decreasing as well. rhs_theta is also decreasing.
# The report supplies this derivative argument; checking n=8 is therefore the
# only endpoint numerical evaluation needed.

internal_lower = 0.792665992
internal_upper = 0.826275942762282625
interval_width = internal_upper - internal_lower

M = 20
lo = 8
hi = 8
while bridge_error(hi, M) >= interval_width:
    hi *= 2
while hi - lo > 2:
    mid = ((lo + hi) // 4) * 2
    if mid <= lo:
        mid = lo + 2
    if bridge_error(mid, M) < interval_width:
        hi = mid
    else:
        lo = mid

print(f"A = {A:.17g}")
print(f"theta = {THETA:.17g}")
print(f"A^2 = {A*A:.17g}")
print(f"Alexander_A_rhs_n8 = {rhs_A:.17g}")
print(f"Alexander_A_margin_n8 = {A*A-rhs_A:.17g}")
print(f"theta^2 = {THETA*THETA:.17g}")
print(f"Alexander_theta_rhs_n8 = {rhs_theta:.17g}")
print(f"Alexander_theta_margin_n8 = {THETA*THETA-rhs_theta:.17g}")
print(f"current_internal_interval_width = {interval_width:.17g}")
for r in (10_000, 100_000, 193_072, 1_000_000, 10_000_000):
    print(f"epsilon_r{r}_M20 = {bridge_error(r, 20):.17g}")
print(f"first_even_r_found_with_epsilon_below_current_width_M20 = {hi}")
print(f"epsilon_at_that_r = {bridge_error(hi, M):.17g}")
print("RENEWAL_ALEXANDER_BRIDGE_NUMERICAL_CHECK_PASS")
