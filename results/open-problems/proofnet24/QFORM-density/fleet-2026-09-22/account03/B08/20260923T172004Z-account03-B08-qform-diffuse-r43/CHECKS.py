import itertools
import math
import random

rng = random.Random(4308)

C_E3 = 3 * 2 ** (4 / 3) * math.exp(1 / 3)
C_R2 = C_E3 * (8192 * 448 * 256) ** (1 / 6)
C_PARTNER = (2 ** (4 / 3) + 1) * math.sqrt(3) * 2 ** 0.25

accepted = 0
min_ratio = 1.0
max_identity_error = 0.0

for m in range(4, 9):
    for _ in range(300):
        r1 = [rng.gauss(0, 1) for _ in range(m)]
        r2 = [rng.gauss(0, 1) for _ in range(m)]
        weights = {}
        Z = 0.0
        for i, j in itertools.combinations(range(m), 2):
            d = r1[i] * r2[j] - r1[j] * r2[i]
            q = d * d
            weights[(i, j)] = q
            Z += q
        if Z <= 1e-14:
            continue

        alpha = [0.0] * m
        x = {}
        for e, q in weights.items():
            x[e] = q / Z
            i, j = e
            alpha[i] += x[e]
            alpha[j] += x[e]

        D_direct = 0.0
        for e, xe in x.items():
            for f, xf in x.items():
                if set(e).isdisjoint(f):
                    D_direct += xe * xf
        D_formula = 1 - sum(a * a for a in alpha) + sum(v * v for v in x.values())
        max_identity_error = max(max_identity_error, abs(D_direct - D_formula))
        assert abs(D_direct - D_formula) < 1e-10

        if max(alpha) <= 0.5 + 1e-12:
            accepted += 1
            best = 0.0
            # Fix column 0 red to remove the global color symmetry.
            for mask in range(1 << (m - 1)):
                red = {0}
                for j in range(1, m):
                    if (mask >> (j - 1)) & 1:
                        red.add(j)
                A = sum(q for (i, j), q in weights.items() if i in red and j in red)
                B = sum(q for (i, j), q in weights.items() if i not in red and j not in red)
                best = max(best, A * B)
            ratio = best / (Z * Z)
            min_ratio = min(min_ratio, ratio)
            assert ratio + 1e-12 >= 1 / 448

print(f"C_E3={C_E3:.15f}")
print(f"R2_TRANSVERSE_PAID_CONSTANT={C_R2:.15f}")
print(f"PARTNER_CONSTANT={C_PARTNER:.15f}")
print(f"accepted_diffuse_plucker_instances={accepted}")
print(f"minimum_observed_partition_product_ratio={min_ratio:.15f}")
print(f"maximum_graph_identity_error={max_identity_error:.3e}")
print(f"analytic_partition_target={1/448:.15f}")
print("QFORM_B08_R43_CHECK_PASS")
