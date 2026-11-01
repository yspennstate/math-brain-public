#!/usr/bin/env python3
"""
P05 binary LCS: deterministic calculator for the limiting Green-layer kernel.

This is not a Monte Carlo experiment.  It evaluates the closed forms proved in
the accompanying report:

  g(x) = sqrt(3/pi) exp(-3 x^2/4)
         - (3/2)|x| erfc(sqrt(3)|x|/2),

and, for c>=0,

  Tail(c) = P_mu(|X|>c)
          = (1 + 3 c^2/2) erfc(sqrt(3)c/2)
            - sqrt(3/pi)c exp(-3c^2/4).

It also converts a permitted Green-tail error epsilon into the central
pivotal-density threshold Q needed to improve the public and repository-
internal upper endpoints, and the corresponding threshold for the published
lower endpoint.
"""
import math

PUBLIC_UPPER = 0.826280
INTERNAL_UPPER_CANDIDATE = 0.826275942762282626
PUBLISHED_LOWER = 0.792665992

def density(x: float) -> float:
    a = abs(x)
    return (
        math.sqrt(3.0 / math.pi) * math.exp(-3.0 * a * a / 4.0)
        - 1.5 * a * math.erfc(math.sqrt(3.0) * a / 2.0)
    )

def tail(c: float) -> float:
    if c < 0:
        raise ValueError("c must be nonnegative")
    a = math.sqrt(3.0) * c / 2.0
    return (
        (1.0 + 1.5 * c * c) * math.erfc(a)
        - math.sqrt(3.0 / math.pi) * c * math.exp(-3.0 * c * c / 4.0)
    )

def root_for_tail(eps: float) -> float:
    lo, hi = 0.0, 10.0
    for _ in range(120):
        mid = (lo + hi) / 2.0
        if tail(mid) > eps:
            lo = mid
        else:
            hi = mid
    return hi

# Elementary self-checks of the closed forms.
assert abs(tail(0.0) - 1.0) < 1e-15
assert abs(density(0.0) - math.sqrt(3.0 / math.pi)) < 1e-15
grid = [j / 100.0 for j in range(0, 801)]
assert all(density(x) >= -1e-14 for x in grid)
assert all(tail(grid[j+1]) <= tail(grid[j]) + 1e-14 for j in range(len(grid)-1))
assert tail(8.0) < 1e-20

p_public = 3.0 * PUBLIC_UPPER - 2.0
p_internal = 3.0 * INTERNAL_UPPER_CANDIDATE - 2.0
p_lower = 3.0 * PUBLISHED_LOWER - 2.0

print("limit_density_at_zero =", format(density(0.0), ".15f"))
print("limit_second_moment = 1/3")
print("public_upper_pivotal_threshold =", format(p_public, ".15f"))
print("internal_upper_pivotal_threshold =", format(p_internal, ".15f"))
print("published_lower_pivotal_threshold =", format(p_lower, ".15f"))
print()

for eps in (1e-2, 1e-3, 1e-6):
    c = root_for_tail(eps)
    q_public = (p_public - eps) / (1.0 - eps)
    q_internal = (p_internal - eps) / (1.0 - eps)
    q_lower = p_lower / (1.0 - eps)
    print("epsilon =", format(eps, ".0e"))
    print("  c_epsilon =", format(c, ".15f"))
    print("  tail(c_epsilon) =", format(tail(c), ".15f"))
    print("  upper_Q_needed_public <", format(q_public, ".15f"))
    print("  upper_Q_needed_internal <", format(q_internal, ".15f"))
    print("  lower_Q_needed_published >", format(q_lower, ".15f"))

print()
print("TAIL_AT_C_2_25 =", format(tail(2.25), ".15f"))
print("GREEN_LAYER_LIMIT_KERNEL_CALCULATOR_PASS")
