import math
import numpy as np

rng = np.random.default_rng(230923)
max_e2_relerr = 0.0
min_k1_ratio = float('inf')

for _ in range(300):
    m = int(rng.integers(3, 10))
    n = int(rng.integers(2, 8))
    M = rng.normal(size=(m, n))
    W = np.zeros((m, m))
    for i in range(m):
        for j in range(i + 1, m):
            a, b = M[i], M[j]
            w = max(0.0, float(a @ a * (b @ b) - (a @ b) ** 2))
            W[i, j] = W[j, i] = w

    E2_pairs = sum(W[i, j] for i in range(m) for j in range(i + 1, m))
    G = M.T @ M
    E2_gram = 0.5 * (np.trace(G) ** 2 - np.trace(G @ G))
    max_e2_relerr = max(
        max_e2_relerr,
        abs(E2_pairs - E2_gram) / max(1.0, abs(E2_pairs), abs(E2_gram)),
    )

    if E2_pairs <= 1e-12:
        continue
    for i in range(m):
        Hi = float(W[i].sum())
        rho2 = float(M[i] @ M[i])
        if Hi <= 1e-12 or rho2 <= 1e-12:
            continue
        partners = [j for j in range(m) if j != i and W[i, j] > 1e-15]
        q = np.array([W[i, j] / Hi for j in partners])
        Hq = -sum(float(x) * math.log(float(x)) for x in q)
        avg_log_norm2 = sum(
            float(x) * math.log(float(M[j] @ M[j]))
            for x, j in zip(q, partners)
        )
        K1 = math.exp(Hq + avg_log_norm2)
        min_k1_ratio = min(min_k1_ratio, K1 / (Hi / rho2))

Cstar = 12 * 2 ** (17 / 24) * math.exp(5 / 24)
CE2 = 12 * 2 ** (5 / 6) * math.exp(5 / 24)
CdiffuseE2 = 8 * math.exp(1 / 4)
Cpartner = 2 ** (23 / 8)

print(f'max_E2_identity_relative_error={max_e2_relerr:.17g}')
print(f'min_K1_over_Hi_over_rho2={min_k1_ratio:.17g}')
print(f'Cstar_C1_sqrt2={Cstar:.15f}')
print(f'CE2_C1_sqrt2={CE2:.15f}')
print(f'Cdiffuse_E2={CdiffuseE2:.15f}')
print(f'Cpartner_concentrated_star={Cpartner:.15f}')

assert max_e2_relerr < 1e-12
assert min_k1_ratio >= 1 - 1e-10
assert CE2 > CdiffuseE2
print('STATUS=PASS')
