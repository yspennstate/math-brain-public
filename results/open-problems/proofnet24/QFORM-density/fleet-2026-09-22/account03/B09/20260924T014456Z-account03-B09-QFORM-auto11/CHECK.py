import itertools
import math
import numpy as np

SEED = 24092026
rng = np.random.default_rng(SEED)


def row_defect(D, r, k):
    idx = [i for i in range(len(r)) if i != k]
    rv = r[idx]
    dv = D[k, idx]
    den = float(rv @ rv)
    if den < 1e-14:
        return float(np.linalg.norm(dv))
    alpha = float(dv @ rv) / den
    return float(np.linalg.norm(dv - alpha * rv))


def aligned_distance(D, r):
    # Diagonal is free, so optimize lambda only on ordered off-diagonal entries.
    num = 0.0
    den = 0.0
    n = len(r)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            z = r[i] * r[j]
            num += D[i, j] * z
            den += z * z
    lam = num / den if den > 1e-15 else 0.0
    ss = 0.0
    for i in range(n):
        for j in range(n):
            if i != j:
                ss += (D[i, j] - lam * r[i] * r[j]) ** 2
    return math.sqrt(ss), lam


def e2_cross(C):
    G = C @ C.T
    return 0.5 * (np.trace(G) ** 2 - np.trace(G @ G))


max_kappa_rel = 0.0
max_defect_rel = 0.0
max_stability_ratio = 0.0
min_partition_ratio = float("inf")

for test in range(100):
    m = int(rng.integers(5, 9))
    tau = float(rng.choice([-1.0, 1.0]) * (0.5 + 3.0 * rng.random()))
    u = rng.normal(size=2)
    u /= np.linalg.norm(u)
    B = tau * np.outer(u, u)

    h = int(np.argmax(np.abs(np.diag(B))))
    j = 1 - h
    a = float(B[h, h])
    b = float(B[h, j])

    g = rng.normal(size=2)
    r = rng.normal(size=m)
    if np.max(r * r) / float(r @ r) > 0.94:
        r += 0.2 * rng.normal(size=m)

    X = rng.normal(size=(m, m))
    D = (X + X.T) / 2.0

    gamma = float(g[j] - (b / a) * g[h])
    adjB = np.array([[B[1, 1], -B[0, 1]], [-B[1, 0], B[0, 0]]])
    kappa = float(g @ adjB @ g)
    kerr = abs(a * gamma**2 - kappa) / (1.0 + abs(kappa))
    max_kappa_rel = max(max_kappa_rel, kerr)

    Dh = D - (g[h] ** 2 / a) * np.outer(r, r)
    defects = np.array([row_defect(D, r, k) for k in range(m)])
    defects_h = np.array([row_defect(Dh, r, k) for k in range(m)])
    derr = np.max(np.abs(defects - defects_h)) / (1.0 + np.max(defects))

    ds, _ = aligned_distance(D, r)
    dsh, _ = aligned_distance(Dh, r)
    derr = max(derr, abs(ds - dsh) / (1.0 + ds))
    max_defect_rel = max(max_defect_rel, derr)

    sumd2 = float(defects @ defects)
    if sumd2 > 1e-15:
        max_stability_ratio = max(
            max_stability_ratio, ds / math.sqrt(2.0 * sumd2)
        )

    if test < 25 and abs(gamma) > 1e-9:
        R2 = float(r @ r)
        Xi = gamma**2 * sum(
            (R2 - r[k] ** 2) * defects[k] ** 2 for k in range(m)
        )
        best = 0.0
        for mask in range(1, 2**m - 1):
            S = [k for k in range(m) if (mask >> k) & 1]
            T = [k for k in range(m) if not ((mask >> k) & 1)]
            C = np.zeros((1 + len(S), len(T)))
            C[0, :] = gamma * r[T]
            for ii, k in enumerate(S, start=1):
                C[ii, :] = Dh[k, T]
            best = max(best, float(e2_cross(C)))
        if Xi > 1e-12:
            min_partition_ratio = min(min_partition_ratio, best / Xi)

assert max_kappa_rel < 1e-12
assert max_defect_rel < 1e-12
assert max_stability_ratio <= 1.0 + 1e-12
assert min_partition_ratio >= 4.0 / 27.0 - 1e-12

# Constants from the theorem.
base = 8.0 * (2.0 * math.e) ** 0.25
compiler = base * (27.0 / 4.0) ** 0.125
qdiff = base * (27.0 / (2.0 * (15.0 / 16.0))) ** 0.125
tau_form = qdiff * 2.0 ** (3.0 / 8.0)
omega_form = tau_form * 2.0 ** (1.0 / 8.0)
stress_m64 = compiler * (62.0 / 64.0) ** (-1.0 / 8.0)
partner_constant = 3.0 ** (2.0 / 3.0)

# Six-coordinate partner regression.
B = np.array([[1.0, 1.0], [1.0, 1.0]])
g = np.array([1.0, -1.0])
r = np.ones(4)
D = np.array(
    [[0.0, 0.0, 1.0, 0.0],
     [0.0, 0.0, 0.0, 1.0],
     [1.0, 0.0, 0.0, 0.0],
     [0.0, 1.0, 0.0, 0.0]]
)
A = np.block([[B, np.outer(g, r)], [np.outer(r, g), D]])
eigs = np.linalg.eigvalsh(A)
K = np.array([[1.0, 1.0, 1.0], [-1.0, 1.0, 0.0], [-1.0, 0.0, 1.0]])
assert abs(np.linalg.det(K) - 3.0) < 1e-12
assert sum(abs(x) >= 1.0 - 1e-12 for x in eigs) >= 3

print(f"SEED={SEED}")
print(f"max_kappa_identity_relative_error={max_kappa_rel:.3e}")
print(f"max_defect_invariance_relative_error={max_defect_rel:.3e}")
print(f"max_dstar_over_sqrt2_delta_norm={max_stability_ratio:.12f}")
print(f"min_exhaustive_partition_Z2_over_Xi={min_partition_ratio:.12f}")
print(f"required_4_over_27={4.0/27.0:.12f}")
print(f"base_square_receiver={base:.15f}")
print(f"compiler_constant={compiler:.15f}")
print(f"q_lt_1_over_16_constant={qdiff:.15f}")
print(f"tau_invariant_constant={tau_form:.15f}")
print(f"omega_ge_1_over_4_constant={omega_form:.15f}")
print(f"stress_m64_t1_bound={stress_m64:.15f}")
print("partner_spectrum=" + np.array2string(eigs, precision=12, separator=","))
print(f"partner_detK={np.linalg.det(K):.12f}")
print(f"partner_constant={partner_constant:.15f}")
print("STATUS=PASS")
