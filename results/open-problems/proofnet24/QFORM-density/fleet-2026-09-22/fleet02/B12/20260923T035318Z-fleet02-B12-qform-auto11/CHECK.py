import json, math
import numpy as np

rng = np.random.default_rng(12011)
violations = 0
minimum_margin = float('inf')
count = 0
for n in range(6, 21):
    for _ in range(20):
        r = int(rng.integers(0, min(4, n-5) + 1))
        M0 = rng.normal(size=(n, n))
        U = rng.normal(size=(n, r)) if r else np.zeros((n, 0))
        V = rng.normal(size=(n, r)) if r else np.zeros((n, 0))
        L = U @ V.T
        E = rng.normal(size=(n, n))
        E *= 0.1 / np.linalg.norm(E, 2)
        s0 = np.linalg.svd(M0, compute_uv=False)
        sf = np.linalg.svd(M0 + L + E, compute_uv=False)
        for j in range(5):
            lb = max(float(s0[j+r]) - 0.1, 0.0)
            margin = float(sf[j]) - lb
            minimum_margin = min(minimum_margin, margin)
            violations += int(margin < -1e-9)
            count += 1

m = 256
rho = 0.02
a = 1.98
B = a * math.sqrt(m-3)
Ctail = 9 * math.sqrt(3) * math.e / 2
Csharp = Ctail * (a*a*B) ** (-1/3)
Ce5f = 9 * math.sqrt(3*math.e) * (a*a*B) ** (-1/3)
Cd5 = 5 * math.sqrt(2*math.e) / 1.99

print(json.dumps({
    'rank_dense_singular_tests': count,
    'violations': violations,
    'minimum_margin': minimum_margin,
    'D5_uniform_constant_at_a_1_99': Cd5,
    'D5_partner_pivot_threshold': 4/Cd5,
    'leaky_m256_B': B,
    'leaky_m256_gate_rhs': B/15,
    'leaky_sharp_constant': Csharp,
    'leaky_e5f_constant': Ce5f,
    'leaky_sharp_partner_threshold': 4/Csharp,
}, indent=2, sort_keys=True))
