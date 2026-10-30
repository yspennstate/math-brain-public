import itertools
import math
import numpy as np

rng = np.random.default_rng(12345)


def e2_gram(M):
    s = np.linalg.svd(M, compute_uv=False)
    y = s * s
    return sum(y[i] * y[j] for i in range(len(y)) for j in range(i + 1, len(y)))


max_rel = 0.0
for _ in range(1000):
    m, n = 4, 5
    b = float(rng.normal())
    if abs(b) < 0.1:
        b += 0.3
    r = rng.normal(size=n)
    c = rng.normal(size=m)
    D = rng.normal(size=(m, n))
    N = np.block([[np.array([[b]]), r.reshape(1, -1)], [c.reshape(-1, 1), D]])
    C = b * D - np.outer(c, r)

    lhs = 0.0
    for js in itertools.combinations(range(m), 2):
        rows = (0, js[0] + 1, js[1] + 1)
        for ts in itertools.combinations(range(n), 2):
            cols = (0, ts[0] + 1, ts[1] + 1)
            d = np.linalg.det(N[np.ix_(rows, cols)])
            lhs += d * d

    rhs = e2_gram(C) / (b * b)
    rel = abs(lhs - rhs) / max(1.0, abs(rhs))
    max_rel = max(max_rel, rel)

c3 = 11907 / 16384
L0 = math.sqrt(3937) / 1024 * c3
Z0 = L0 * L0 / 64
paid = 9 * math.sqrt(3 * math.e) * Z0 ** (-1 / 6)
cofactor_rel = (1 / (128 * math.sqrt(2))) / L0
D0 = math.sqrt(3937) / 64 * c3
core_rel = (1 / (4 * math.sqrt(2))) / D0

print(f"max_relative_identity_error={max_rel:.17g}")
print(f"c3={c3:.17g}")
print(f"L0={L0:.17g}")
print(f"L0_sq={L0*L0:.17g}")
print(f"Z0=L0_sq/64={Z0:.17g}")
print(f"Dprime_paid_constant={paid:.17g}")
print(f"cofactor_relative_distance={cofactor_rel:.17g}")
print(f"cofactor_tail_energy_fraction={cofactor_rel**2:.17g}")
print(f"cofactor_top1_energy_fraction={1-cofactor_rel**2:.17g}")
print(f"D0={D0:.17g}")
print(f"core_relative_distance={core_rel:.17g}")
print(f"core_tail_energy_fraction={core_rel**2:.17g}")
print(f"core_top2_energy_fraction={1-core_rel**2:.17g}")
