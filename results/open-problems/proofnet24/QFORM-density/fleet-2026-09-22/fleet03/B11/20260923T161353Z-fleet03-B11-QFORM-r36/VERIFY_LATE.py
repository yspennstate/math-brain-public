import itertools
import math
import numpy as np

rng = np.random.default_rng(3611)
min_gap = float('inf')
nchecks = 0

for n in range(4, 11):
    for _ in range(16):
        X = rng.normal(size=(n, 3))
        R = np.linalg.qr(X)[0][:, :3]
        c = np.sum(R * R, axis=1)
        triples = list(itertools.combinations(range(n), 3))
        v = {}
        for K in triples:
            d = np.linalg.det(R[list(K), :])
            v[K] = d * d
        D = sum(v[K] * v[L] for K in triples for L in triples if set(K).isdisjoint(L))

        for i, q in enumerate(c):
            if q < 1e-12 or q > 1 - 1e-12:
                continue
            gs = []
            for j in range(n):
                if j == i:
                    continue
                a, b = sorted((i, j))
                ri, rj = R[a], R[b]
                gij = np.linalg.det(np.array([[ri @ ri, ri @ rj], [rj @ ri, rj @ rj]]))
                gs.append(max(gij, 0.0))
            gstar = max(gs)
            rhs = 2 * q * (1 - q) * max(0.0, 1 - math.sqrt(6 * gstar / q))
            min_gap = min(min_gap, D - rhs)
            assert D + 1e-10 >= rhs
            nchecks += 1

D0 = 63 * (2 - math.sqrt(3)) / 4096
Ccross = 6 * math.e * D0 ** (-1 / 6)
Cpair = 128 * math.sqrt(2) * math.sqrt(32)
Cdiff = 6 * math.e * 4 ** (1 / 6)

print('QFORM_B11_R36_LATE_HEAVYROW_CHECK_PASS')
print('frame_coordinate_checks=', nchecks)
print('minimum_numeric_gap_D_minus_rhs=', min_gap)
print('D0=', D0)
print('direct_cross_constant=', Ccross)
print('partner_pair_constant=', Cpair)
print('diffuse_constant=', Cdiff)
