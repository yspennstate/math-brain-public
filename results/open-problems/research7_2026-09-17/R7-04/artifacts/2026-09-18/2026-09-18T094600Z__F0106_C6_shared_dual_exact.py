#!/usr/bin/env python3
from fractions import Fraction as Q

N = 6
FULL = (1 << N) - 1
alpha = Q(37, 50)
p = Q(73, 100)
r = alpha * p
edges = tuple((i, (i + 1) % N) for i in range(N))

def pc(x):
    return x.bit_count()

def independent(mask):
    return all(not ((mask >> a) & 1 and (mask >> b) & 1) for a, b in edges)

def event_prob(J, t):
    """Probability that t-thinning of deterministic J contains a C6 edge."""
    q = 1 - t
    total_no = Q(0)
    K = J
    j = pc(J)
    while True:
        if independent(K):
            k = pc(K)
            total_no += (t ** k) * (q ** (j - k))
        if K == 0:
            break
        K = (K - 1) & J
    return 1 - total_no

def rot(mask, k):
    out = 0
    for i in range(N):
        if (mask >> i) & 1:
            out |= 1 << ((i + k) % N)
    return out

def refl(mask):
    out = 0
    for i in range(N):
        if (mask >> i) & 1:
            out |= 1 << ((-i) % N)
    return out

def orbit(mask):
    s = set()
    for k in range(N):
        s.add(rot(mask, k))
        s.add(rot(refl(mask), k))
    return tuple(sorted(s))

seen = set()
orbits = []
for mask in range(1 << N):
    if mask not in seen:
        o = orbit(mask)
        seen.update(o)
        orbits.append(o)
reps = [o[0] for o in orbits]
assert len(orbits) == 13

# The three opposite-edge unions used by the shared-mass certificate.
Qsets = {
    (1 << 0) | (1 << 1) | (1 << 3) | (1 << 4),
    (1 << 1) | (1 << 2) | (1 << 4) | (1 << 5),
    (1 << 2) | (1 << 3) | (1 << 5) | (1 << 0),
}
edge_masks = {(1 << a) | (1 << b) for a, b in edges}
assert Qsets == set(orbits[10])
assert edge_masks == set(orbits[2])

mA = event_prob(FULL, p)
assert mA == Q(476262636611, 500000000000)

# Primal/shared-mass certificate.
x0 = alpha**3 / mA
x2 = alpha**4 * p**2 * (1-alpha) / mA
x4 = alpha**7 * p**4 * (1-alpha) / mA
weights = {0: x0}
for E in edge_masks:
    weights[E] = x2
for B in Qsets:
    weights[B] = x4

primal_obj = sum(weights.values())
assert primal_obj == Q(2661818171668307599067, 3720801848523437500000)
assert primal_obj < 1

# Check all 64 Talagrand-dual inequalities exactly.
min_slack = None
tight = []
for J in range(1 << N):
    lhs = Q(0)
    for I, w in weights.items():
        if I & ~J == 0:
            lhs += (r ** (-pc(I))) * w
    rhs = event_prob(J, alpha) / mA
    slack = lhs - rhs
    assert slack >= 0, (J, lhs, rhs, slack)
    if min_slack is None or slack < min_slack:
        min_slack = slack
    if slack == 0:
        tight.append(J)

# Exact reduced dual certificate proving the stress-point LP optimum.
# Nonzero reduced dual variables live on subset-orbits:
# 2 = adjacent pair, 4 = consecutive triple, 10 = union of opposite edges.
y = {
    2: 2 - 6*r**2,
    4: 6*r**2 - 3*r**4 - 1,
    10: 3*r**4,
}
assert y[2] == Q(3113797, 12500000)
assert y[4] == Q(309641522747597, 625000000000000)
assert y[10] == Q(159668627252403, 625000000000000)
assert all(v >= 0 for v in y.values())
assert sum(y.values()) == 1

# Reduced dual feasibility: each primal orbit variable has cost |orbit|.
dual_slacks = []
for i, oi in enumerate(orbits):
    k = pc(oi[0])
    lhs = Q(0)
    for j, yj in y.items():
        J = reps[j]
        count = sum(1 for I in oi if I & ~J == 0)
        lhs += Q(count) * (r ** (-k)) * yj
    slack = Q(len(oi)) - lhs
    assert slack >= 0, (i, slack)
    dual_slacks.append(slack)

dual_obj = sum((event_prob(reps[j], alpha) / mA) * yj for j, yj in y.items())
assert dual_obj == primal_obj

# Exact constants used in the all-parameter C6 theorem.
def M(t):
    return Q(6) - 6*t - 3*t*t + 6*t**3 - 2*t**4

assert M(Q(7,10)) == Q(9539, 5000)
assert Q(6) * Q(3,4)**4 == Q(243,128)
assert M(Q(7,10)) - Q(243,128) == Q(749,80000)

mu_07 = Q(7,10)**2 * M(Q(7,10))
g_075 = Q(3,4)**3 + 6*Q(3,4)**6*(1-Q(3,4)) + 3*Q(3,4)**11*(1-Q(3,4))
assert mu_07 == Q(467411,500000)
assert g_075 == Q(12088305,16777216)
assert mu_07 - g_075 == Q(56178212743,262144000000) > 0

print("C6_ORBITS =", len(orbits))
print("mA =", mA, "=", float(mA))
print("primal_opt =", primal_obj, "=", float(primal_obj))
print("stress_margin_to_1 =", 1-primal_obj, "=", float(1-primal_obj))
print("tight_primal_constraints =", len(tight), "/", 64)
print("min_primal_slack =", min_slack)
print("dual_y_adjacent =", y[2])
print("dual_y_triple =", y[4])
print("dual_y_opposite_edge_union =", y[10])
print("min_reduced_dual_slack =", min(dual_slacks))
print("cover_failure_threshold_constant_gap =", Q(749,80000))
print("shared_certificate_constant_gap =", Q(56178212743,262144000000))
print("ALL_EXACT_CHECKS_PASS")
