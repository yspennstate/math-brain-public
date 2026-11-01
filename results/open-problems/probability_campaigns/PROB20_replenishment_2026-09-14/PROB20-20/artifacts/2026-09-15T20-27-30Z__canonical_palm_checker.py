from fractions import Fraction
from itertools import product, permutations
from collections import defaultdict
import math

# Exact finite product law with mean lambda=1.
P = [Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)]
VALUES = [0, 1, 2]
LAM = sum(Fraction(k) * P[k] for k in VALUES)
N = 6
M = 6
assert LAM == 1 and M == N * LAM


def falling(x, r):
    z = 1
    for j in range(r):
        z *= x - j
    return z

# Product configurations on the exact-sum hyperplane.
configs = []
a = Fraction(0)
for x in product(VALUES, repeat=N):
    pr = Fraction(1)
    for v in x:
        pr *= P[v]
    if sum(x) == M:
        configs.append((x, pr))
        a += pr

ell = -math.log(float(a))
pstar = {k: Fraction(k) * P[k] / LAM for k in VALUES if k > 0}

print('canonical exact-sum atom a =', a, float(a))
print('ell = -log a =', ell)

for r in (1, 2, 3):
    # D_r under Q=P(.|S=M): probability sampled balls occupy distinct boxes.
    distinct_weight = Fraction(0)
    for x, pr in configs:
        qpr = pr / a
        total = 0
        for inds in permutations(range(N), r):
            w = 1
            for i in inds:
                w *= x[i]
            total += w
        distinct_weight += qpr * total
    D = distinct_weight / Fraction(falling(M, r))
    assert D > 0

    # Exact constant density ratio Q_tilde/P_tilde.
    ratio = (Fraction(1, 1) / a) * (
        Fraction(falling(N, r)) * (LAM ** r)
    ) / (Fraction(falling(M, r)) * D)
    K_full = math.log(float(ratio))
    K_formula = ell + math.log(float(
        Fraction(falling(N, r)) * (LAM ** r)
        / (Fraction(falling(M, r)) * D)
    ))
    assert abs(K_full - K_formula) < 1e-14

    # Joint marked-occupancy law under the conditioned distinct-ball Palm measure.
    qjoint = defaultdict(Fraction)
    denom = Fraction(falling(M, r)) * D
    for x, pr in configs:
        qpr = pr / a
        for inds in permutations(range(N), r):
            occ = tuple(x[i] for i in inds)
            w = 1
            for v in occ:
                w *= v
            if w:
                qjoint[occ] += qpr * Fraction(w, 1) / denom
    assert sum(qjoint.values()) == 1

    # Reference marked occupancies are exactly iid size-biased P*.
    KL_joint = 0.0
    for occ, qv in qjoint.items():
        pv = Fraction(1)
        for v in occ:
            pv *= pstar[v]
        assert pv > 0
        KL_joint += float(qv) * math.log(float(qv / pv))
    assert KL_joint <= K_full + 1e-12

    # All marked marginals agree and tensorization gives r D(marginal||P*) <= KL_joint.
    marg = defaultdict(Fraction)
    for occ, qv in qjoint.items():
        marg[occ[0]] += qv
    KL_marg = 0.0
    for v, qv in marg.items():
        KL_marg += float(qv) * math.log(float(qv / pstar[v]))
    assert r * KL_marg <= KL_joint + 1e-12
    assert KL_marg <= K_full / r + 1e-12

    print(
        f'r={r}: D_r={float(D):.12f}, '
        f'full_Palm_KL={K_full:.12f}, '
        f'marked_joint_KL={KL_joint:.12f}, '
        f'marginal_KL={KL_marg:.12f}, '
        f'K/r={K_full/r:.12f}'
    )

print('ALL CANONICAL PALM CHECKS PASSED')
