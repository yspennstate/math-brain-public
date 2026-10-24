import math
import numpy as np

rng = np.random.default_rng(20260923)
max_null = 0.0
max_det = 0.0
max_phase = 0.0
max_invariant = 0.0
trials = 500

for _ in range(trials):
    C = rng.normal(size=(3, 2))
    if np.linalg.matrix_rank(C) < 2:
        continue
    U, s, Vt = np.linalg.svd(C, full_matrices=True)
    E = U[:, :2]
    n = U[:, 2]
    C0 = E.T @ C
    Delta = float(np.prod(s))
    w = np.cross(C[:, 0], C[:, 1])

    P = rng.normal(size=(3, 3))
    P = (P + P.T) / 2
    d = float(n @ P @ n)
    P = P - d * np.outer(n, n)  # impose exact shear stratum n^T P n = 0
    pE = E.T @ P @ n

    y = rng.normal(size=3)
    x = float(n @ y)
    u = E.T @ y
    r = C.T @ y
    u2 = np.linalg.solve(C0.T, r)
    B = E.T @ P @ E

    lhs = float(y @ P @ y)
    rhs = float(u @ B @ u + 2 * x * (pE @ u))

    max_null = max(max_null, abs(float(n @ C[:, 0])), abs(float(n @ C[:, 1])))
    max_det = max(max_det, abs(abs(float(np.linalg.det(C0))) - Delta))
    max_phase = max(max_phase, abs(lhs - rhs), float(np.linalg.norm(u-u2)))
    max_invariant = max(
        max_invariant,
        abs(float(w @ P @ w)),
        abs(float(np.linalg.norm(w) - Delta)),
        abs(float(np.linalg.norm(P @ w) - Delta * np.linalg.norm(pE))),
    )

Csh = 5 * 6 ** (3 / 5) / 2 ** (13 / 10)
H0 = 2 ** (11 / 8) * math.pi ** 0.25
D0 = math.pi * 6 ** 0.75 * H0
Ccalc = (5 / math.pi) * (D0 / 8) ** (4 / 5)

A5 = np.array([
    [0,0,1,1,0],
    [0,0,0,0,1],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [0,1,0,0,0],
], dtype=float)
eigs5 = np.linalg.eigvalsh(A5)

tau = 1/64
A7 = np.zeros((7,7))
A7[:5,:5] = A5
A7[5,6] = A7[6,5] = tau
eigs7 = np.linalg.eigvalsh(A7)
Kpartner = A7[np.ix_([0,1,5],[3,4,6])]
partner_det = float(np.linalg.det(Kpartner))
partner_bound = 3 * abs(partner_det) ** (-1/3)

print(f"TRIALS={trials}")
print(f"MAX_NULL_ERROR={max_null:.17e}")
print(f"MAX_DET_ERROR={max_det:.17e}")
print(f"MAX_PHASE_OR_RECON_ERROR={max_phase:.17e}")
print(f"MAX_INVARIANT_ERROR={max_invariant:.17e}")
print(f"C_SHEAR={Csh:.15f}")
print(f"C_FROM_L1_OPTIMIZATION={Ccalc:.15f}")
print("A5_EIGS=" + np.array2string(eigs5, precision=12, separator=','))
print("A7_EIGS_TAU_1_64=" + np.array2string(eigs7, precision=12, separator=','))
print(f"PARTNER_DET={partner_det:.15f}")
print(f"PARTNER_BOUND={partner_bound:.15f}")
assert max_null < 2e-14
assert max_det < 2e-14
assert max_phase < 5e-14
# Exact-zero shear is imposed through an SVD null vector; the residual below is floating-point cancellation.
assert max_invariant < 2e-13
assert abs(Csh-Ccalc) < 1e-12
assert np.sum(np.abs(eigs5) >= 1-1e-12) >= 4
assert abs(partner_det-tau) < 1e-14
assert abs(partner_bound-12) < 1e-12
print("STATUS=PASS")
