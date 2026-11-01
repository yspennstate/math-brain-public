import itertools
import math
import numpy as np

RNG = np.random.default_rng(20260923)
TRIALS = 100


def e2_gram(G):
    t = np.trace(G)
    return 0.5 * (t * t - np.trace(G @ G))


def e3_gram(G):
    t1 = np.trace(G)
    t2 = np.trace(G @ G)
    t3 = np.trace(G @ G @ G)
    return (t1**3 - 3 * t1 * t2 + 2 * t3) / 6


def e3_cross(M):
    if min(M.shape) < 3:
        return 0.0
    return max(0.0, e3_gram(M @ M.T))


def moved_packet(A, L, R, i):
    rows = [x for x in L if x != i]
    out = 0.0
    for S in itertools.combinations(rows, 3):
        for J in itertools.combinations(R, 2):
            out += np.linalg.det(A[np.ix_(S, list(J) + [i])]) ** 2
    return out


max_random_cut_relative_error = 0.0
min_full_e3_minus_selected_packet = float("inf")
fixed_pair_violations = 0
frob_sync_violations = 0
max_reconstruction_error = 0.0

for _ in range(TRIALS):
    n = 8
    B = RNG.normal(size=(n, n))
    A = (B + B.T) / 2
    L = list(range(5))
    R = list(range(5, 8))
    K = A[np.ix_(L, R)]
    packets = {i: moved_packet(A, L, R, i) for i in L}

    # Exact average over all red/blue colorings used in Theorem 3.1.
    average_selected = 0.0
    for bits in itertools.product([0, 1], repeat=len(L)):
        Urows = [L[k] for k, bit in enumerate(bits) if bit == 0]
        Vcols = [L[k] for k, bit in enumerate(bits) if bit == 1]
        selected = 0.0
        for i in Vcols:
            for S in itertools.combinations(Urows, 3):
                for J in itertools.combinations(R, 2):
                    selected += np.linalg.det(A[np.ix_(S, list(J) + [i])]) ** 2
        M = A[np.ix_(Urows, R + Vcols)]
        full = e3_cross(M)
        min_full_e3_minus_selected_packet = min(
            min_full_e3_minus_selected_packet, full - selected
        )
        average_selected += selected / (2 ** len(L))

    target = sum(packets.values()) / 16
    max_random_cut_relative_error = max(
        max_random_cut_relative_error,
        abs(average_selected - target) / (1 + abs(target)),
    )

    # Check the fixed singular-pair lower bound and synchronized residual.
    G = K @ K.T
    Z = e2_gram(G)
    U, s, _ = np.linalg.svd(K, full_matrices=True)
    x = s * s
    if len(s) < 2 or Z <= 1e-12 or x[0] * x[1] <= Z / 3:
        continue

    total_energy = np.trace(G)
    mu = np.array(
        [(G[i, i] * total_energy - (G @ G)[i, i]) / Z for i in range(len(L))]
    )
    heavy = {i for i, mass in enumerate(mu) if mass > 2 / 7}
    L0 = np.zeros((len(L), len(L)))
    d2 = 0.0

    for loc, physical_i in enumerate(L):
        if loc in heavy:
            continue
        restricted = np.delete(U[:, :2], loc, axis=0)
        c = A[np.ix_([j for j in L if j != physical_i], [physical_i])].ravel()
        coeff = np.linalg.lstsq(restricted, c, rcond=None)[0]
        error = c - restricted @ coeff
        d = np.linalg.norm(error)
        ell = U[loc, 0] ** 2 + U[loc, 1] ** 2
        lower = x[0] * x[1] * (1 - ell) * d * d
        if packets[physical_i] + 1e-9 < lower:
            fixed_pair_violations += 1
        L0[:, loc] = U[:, :2] @ coeff
        d2 += d * d

    S = (L0 + L0.T) / 2
    C = A[np.ix_(L, L)]
    P = np.diag([1.0 if i in heavy else 0.0 for i in range(len(L))])
    Q = np.eye(len(L)) - P
    M0 = C - S
    RH = P @ M0 + Q @ M0 @ P
    N = M0 - RH
    D = np.diag(np.diag(N))
    E = N - D
    R0 = S + RH
    max_reconstruction_error = max(
        max_reconstruction_error, np.linalg.norm(C - (D + R0 + E))
    )
    if np.linalg.norm(E, "fro") ** 2 > d2 + 1e-9:
        frob_sync_violations += 1

print(f"trials={TRIALS}")
print(f"max_random_cut_relative_error={max_random_cut_relative_error:.17e}")
print(f"min_full_e3_minus_selected_packet={min_full_e3_minus_selected_packet:.17e}")
print(f"fixed_pair_violations={fixed_pair_violations}")
print(f"frob_sync_violations={frob_sync_violations}")
print(f"max_reconstruction_error={max_reconstruction_error:.17e}")
print("STATUS=PASS" if fixed_pair_violations == frob_sync_violations == 0 and min_full_e3_minus_selected_packet >= -1e-8 else "STATUS=FAIL")
