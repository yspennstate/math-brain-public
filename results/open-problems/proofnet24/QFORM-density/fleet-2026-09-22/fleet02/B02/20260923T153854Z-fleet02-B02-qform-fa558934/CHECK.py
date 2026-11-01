import itertools
import math
import numpy as np

SEED = 2309153854
rng = np.random.default_rng(SEED)


def esym_svals(M, k):
    x = np.linalg.svd(M, compute_uv=False) ** 2
    e = np.zeros(k + 1)
    e[0] = 1.0
    for z in x:
        for j in range(k, 0, -1):
            e[j] += z * e[j - 1]
    return float(e[k])


def minor_mass(M, k):
    m, n = M.shape
    total = 0.0
    row = np.zeros(m)
    col = np.zeros(n)
    for R in itertools.combinations(range(m), k):
        for C in itertools.combinations(range(n), k):
            d = np.linalg.det(M[np.ix_(R, C)])
            w = float(d * d)
            total += w
            for i in R:
                row[i] += w
            for j in C:
                col[j] += w
    return total, row / total, col / total


max_anchor_violation = 0.0
max_c2_violation = 0.0
max_delete_rel_error = 0.0
for _ in range(200):
    P = rng.normal(size=(2, 2))
    while abs(np.linalg.det(P)) < 0.2:
        P = rng.normal(size=(2, 2))
    R = rng.normal(size=(2, 3))
    C = rng.normal(size=(3, 2))
    S = rng.normal(size=(3, 3))
    M = S + C @ np.linalg.solve(P, R)
    B = np.block([[P, R], [C, M]])
    D = abs(np.linalg.det(P))
    E4 = esym_svals(B, 4)
    E2S = esym_svals(S, 2)
    max_anchor_violation = max(max_anchor_violation, D * D * E2S - E4)
    ss = np.linalg.svd(S, compute_uv=False)
    F2 = float(np.sum(ss * ss))
    rho = F2 / float(ss[0] ** 2)
    c2 = (rho - 1.0) / (2.0 * rho)
    max_c2_violation = max(max_c2_violation, c2 * F2 * F2 - E2S)
    mass, alpha, _ = minor_mass(B, 4)
    for i in range(B.shape[0]):
        mdel = esym_svals(np.delete(B, i, axis=0), 4)
        max_delete_rel_error = max(
            max_delete_rel_error,
            abs(mdel - (1.0 - alpha[i]) * mass) / max(1.0, mass),
        )

max_scalar_violation = 0.0
for _ in range(200):
    p = float(rng.normal())
    while abs(p) < 0.2:
        p = float(rng.normal())
    r = rng.normal(size=(1, 4))
    c = rng.normal(size=(4, 1))
    S = rng.normal(size=(4, 4))
    M = S + c @ r / p
    B = np.block([[np.array([[p]]), r], [c, M]])
    E4 = esym_svals(B, 4)
    E2 = esym_svals(S, 2)
    H = p * p * E2
    ss = np.linalg.svd(S, compute_uv=False)
    F2 = float(np.sum(ss * ss))
    rho = F2 / float(ss[0] ** 2)
    if rho > 2.0:
        c3 = (rho - 2.0) / rho**3 if rho <= 3.0 else 1.0 / 27.0
        rhs = c3 * 2.0 ** 1.5 * H ** 1.5 / abs(p)
        max_scalar_violation = max(max_scalar_violation, rhs - E4)

max_partner_identity_error = 0.0
for _ in range(500):
    a, u, v, b = rng.normal(size=4)
    r0 = rng.normal(size=4)
    rho = rng.normal(size=4)
    c0 = rng.normal(size=4)
    gamma = rng.normal(size=4)
    M = rng.normal(size=(4, 4))
    K = b * M - np.outer(gamma, rho)
    P = np.array([[a, u], [v, b]])
    R = np.vstack([r0, rho])
    C = np.column_stack([c0, gamma])
    adjP = np.array([[b, -u], [-v, a]])
    L = np.linalg.det(P) * M - C @ adjP @ R
    rhs = L + u * (v * M - np.outer(c0, rho)) + np.outer(b * c0 - v * gamma, r0)
    max_partner_identity_error = max(max_partner_identity_error, np.linalg.norm(a * K - rhs))

# Stress the capped-simplex c4/c5 bounds used in the star recursion.
rng2 = np.random.default_rng(SEED + 1)
max_c4_violation = 0.0
max_c5_violation = 0.0
for _ in range(20000):
    m = int(rng2.integers(4, 20))
    x = rng2.random(m) ** 3
    T = float(np.sum(x))
    rho = T / float(np.max(x))
    e = np.zeros(6)
    e[0] = 1.0
    for z in x:
        for j in range(5, 0, -1):
            e[j] += z * e[j - 1]
    if rho > 3.0:
        c4 = (rho - 3.0) / rho**4 if rho <= 4.0 else 1.0 / 256.0
        max_c4_violation = max(max_c4_violation, c4 * T**4 - e[4])
    if rho > 4.0 and m >= 5:
        c5 = (rho - 4.0) / rho**5 if rho <= 5.0 else 1.0 / 3125.0
        max_c5_violation = max(max_c5_violation, c5 * T**5 - e[5])

q = 1.5
C_D4_PAIR_G = 3 * math.e ** (2 / 3) / ((2 - q) * q ** (1 / 3)) * (1 / 6) ** (-1 / 12)
C_D4_PAIR_Z864 = C_D4_PAIR_G * 864 ** (1 / 6)
C_D4_SCALAR_H = 9 * math.e ** (8 / 9) * q ** (-4 / 9) / (7 - 4 * q) * 2 ** (-1 / 6) * (4 / 125) ** (-1 / 9)
C_D4_SCALAR_Z864 = C_D4_SCALAR_H * 864 ** (1 / 6)
C_D4_STAR_PAIR_G = 12 * math.e ** (5 / 8) * 2 ** (13 / 48)
C_D4_STAR_PAIR_Z864 = C_D4_STAR_PAIR_G * 864 ** (1 / 6)
C_D4_STAR_SCALAR_H = (
    15 * math.e ** (4 / 5) * 2 ** (-41 / 90) * 6 ** (-1 / 9)
    * (4 / 125) ** (-1 / 9) * (1 / 3125) ** (-1 / 15)
)
C_D4_STAR_SCALAR_Z864 = C_D4_STAR_SCALAR_H * 864 ** (1 / 6)

print(f"seed={SEED}")
print(f"max_anchor_lower_bound_violation={max_anchor_violation:.3e}")
print(f"max_c2_violation={max_c2_violation:.3e}")
print(f"max_delete_rel_error={max_delete_rel_error:.3e}")
print(f"max_scalar_lower_bound_violation={max_scalar_violation:.3e}")
print(f"max_partner_identity_frob_error={max_partner_identity_error:.3e}")
print(f"max_c4_stress_violation={max_c4_violation:.3e}")
print(f"max_c5_stress_violation={max_c5_violation:.3e}")
print(f"C_D4_PAIR_G={C_D4_PAIR_G:.12f}")
print(f"C_D4_PAIR_Z864={C_D4_PAIR_Z864:.12f}")
print(f"C_D4_SCALAR_H={C_D4_SCALAR_H:.12f}")
print(f"C_D4_SCALAR_Z864={C_D4_SCALAR_Z864:.12f}")
print(f"C_D4_STAR_PAIR_G={C_D4_STAR_PAIR_G:.12f}")
print(f"C_D4_STAR_PAIR_Z864={C_D4_STAR_PAIR_Z864:.12f}")
print(f"C_D4_STAR_SCALAR_H={C_D4_STAR_SCALAR_H:.12f}")
print(f"C_D4_STAR_SCALAR_Z864={C_D4_STAR_SCALAR_Z864:.12f}")
print("STATUS=PASS" if max(max_anchor_violation, max_c2_violation, max_scalar_violation, max_c4_violation, max_c5_violation) <= 1e-10 else "STATUS=FAIL")
