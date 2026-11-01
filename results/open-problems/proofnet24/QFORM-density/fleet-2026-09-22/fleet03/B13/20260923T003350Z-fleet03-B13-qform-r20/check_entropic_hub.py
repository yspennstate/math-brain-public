from __future__ import annotations

import itertools
import math

L = math.log(64.0)
assert abs(math.exp(L / 6.0) - 2.0) < 1e-14
paid_constant = 6.0 * math.sqrt(math.e) * math.exp(L / 6.0)
assert abs(paid_constant - 12.0 * math.sqrt(math.e)) < 1e-13

# Infeasible support example: every 3-edge contains row 0, so any
# probability measure on the edges has row-0 load exactly one.
vertices = range(7)
star_edges = [e for e in itertools.combinations(vertices, 3) if 0 in e]
assert star_edges
assert all(0 in e for e in star_edges)

# Feasible extremal support: two disjoint triples at half-half weight.
edges = [(0, 1, 2), (3, 4, 5)]
mu = [0.5, 0.5]
loads = [sum(mu[j] for j, e in enumerate(edges) if i in e) for i in range(6)]
assert all(abs(x - 0.5) < 1e-15 for x in loads)

# Entropy-currency identity K = Z exp(-D(mu||w)).
w = [0.7, 0.3]
mu = [0.5, 0.5]
Z = 11.0
d2 = [Z * x for x in w]
D = sum(m * math.log(m / ww) for m, ww in zip(mu, w))
H = -sum(m * math.log(m) for m in mu)
logK = H + sum(m * math.log(x) for m, x in zip(mu, d2))
err = abs(math.exp(logK) - Z * math.exp(-D))
assert err < 1e-12

print(f"L=log64={L:.15f}")
print(f"exp(L/6)={math.exp(L/6):.15f}")
print(f"paid_constant={paid_constant:.15f}")
print(f"infeasible_star_edges={len(star_edges)} row0_load_for_any_mu=1")
print(f"disjoint_two_edge_loads={loads}")
print(f"kl_identity_error={err:.16e}")
print("QFORM_B13_R20_ENTROPIC_HUB_CHECK_PASS")
