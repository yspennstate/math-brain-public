#!/usr/bin/env python3
"""
Finite algebra checker for PROB20-20 record-band inequalities.

This is NOT a proof of any asymptotic theorem. It checks, on a finite toy
probability mass function, the identities/inequalities used in the report:
  * definition of the lower record envelope r(x);
  * uniform band gap Gamma;
  * pointwise bound -log(c0 q_k) >= k h_R + Gamma;
  * integrated geometric bound for Q(L,U);
  * raw fragment-product comparison against a record.
"""
import math

N = 6000
c0 = 0.1

raw = [0.0] + [1.0 / (k + 1) ** 2 for k in range(1, N + 1)]
Z = sum(raw)
q = [x / Z for x in raw]  # toy qbar; nu is set to 1 in this checker

r = [float("inf")] * (N + 1)
best = float("inf")
records = []
for k in range(1, N + 1):
    rate = -math.log(c0 * q[k]) / k
    if rate < best:
        best = rate
        records.append(k)
    r[k] = best

def check_case(R, L, U):
    h = r[R]
    gamma = min(x * (r[x] - h) for x in range(L, U + 1))

    min_pointwise_slack = float("inf")
    for k in range(L, U + 1):
        lhs = -math.log(c0 * q[k])
        rhs = k * h + gamma
        min_pointwise_slack = min(min_pointwise_slack, lhs - rhs)

    Q = sum(q[L + 1 : U + 1])
    geom_bound = (1.0 / c0) * math.exp(-gamma) * math.exp(-h * L) / (1.0 - math.exp(-h))
    integrated_slack = geom_bound - Q
    if min_pointwise_slack < -1e-10:
        raise AssertionError(("pointwise", R, L, U, min_pointwise_slack))
    if integrated_slack < -1e-10:
        raise AssertionError(("integrated", R, L, U, integrated_slack))
    return {
        "R": R,
        "L": L,
        "U": U,
        "h": h,
        "Gamma": gamma,
        "Q": Q,
        "geom_bound": geom_bound,
        "min_pointwise_slack": min_pointwise_slack,
        "integrated_slack": integrated_slack,
    }

cases = [
    (500, 10, 22),
    (1000, 15, 31),
    (2000, 20, 44),
    (5000, 30, 70),
]
checked = [check_case(*case) for case in cases]

# Exact-mass fragment comparison at R=5000 using twenty fragments of size 250.
R = 5000
L = 50
U = 250
h = r[R]
gamma = min(x * (r[x] - h) for x in range(L, U + 1))
frags = [250] * 20
assert sum(frags) == R
log_ratio = math.log(q[R]) - sum(math.log(q[k]) for k in frags)
lower = len(frags) * gamma + (len(frags) - 1) * math.log(c0)
fragment_slack = log_ratio - lower
if fragment_slack < -1e-10:
    raise AssertionError(("fragment", fragment_slack))

print(f"toy_support_max={N}")
print(f"record_count={len(records)}")
for row in checked:
    print(
        "case "
        f"R={row['R']} L={row['L']} U={row['U']} "
        f"h={row['h']:.12g} Gamma={row['Gamma']:.12g} "
        f"Q={row['Q']:.12g} geom_bound={row['geom_bound']:.12g} "
        f"pointwise_slack={row['min_pointwise_slack']:.3e} "
        f"integrated_slack={row['integrated_slack']:.3e}"
    )
print(
    "fragment "
    f"R={R} t={len(frags)} size={frags[0]} "
    f"Gamma={gamma:.12g} log_ratio={log_ratio:.12g} "
    f"lower_bound={lower:.12g} slack={fragment_slack:.12g}"
)
print("PASS")
