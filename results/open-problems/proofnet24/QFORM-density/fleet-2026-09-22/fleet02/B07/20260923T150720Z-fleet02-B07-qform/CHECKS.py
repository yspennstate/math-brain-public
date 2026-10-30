import itertools, math
import numpy as np


def e2(M):
    s = np.linalg.svd(M, compute_uv=False)
    x = s * s
    return sum(x[i] * x[j] for i in range(len(x)) for j in range(i + 1, len(x)))


def gstar_direct(s, r, C, K):
    p, m0 = C.shape
    q = K.shape[1]
    M = np.block([[s.reshape(1, m0), r.reshape(1, q)], [C, K]])
    out = 0.0
    for j in range(m0):
        if s[j] == 0:
            continue
        for R in itertools.combinations(range(p), 2):
            rows = [0, R[0] + 1, R[1] + 1]
            for T in itertools.combinations(range(q), 2):
                cols = [j, m0 + T[0], m0 + T[1]]
                out += np.linalg.det(M[np.ix_(rows, cols)]) ** 2
    return out


def gstar_pivot(s, r, C, K):
    out = 0.0
    for j in range(len(s)):
        if s[j] == 0:
            continue
        Kj = K - np.outer(C[:, j], r) / s[j]
        out += s[j] ** 2 * e2(Kj)
    return out


rng = np.random.default_rng(20260923)
max_rel = 0.0
max_rank2_violation = -math.inf
for _ in range(100):
    p, m0, q = 4, 3, 5
    s = rng.normal(size=m0)
    s += np.sign(s) * 0.25
    r = rng.normal(size=q)
    C = rng.normal(size=(p, m0))
    K = rng.normal(size=(p, q))
    gd = gstar_direct(s, r, C, K)
    gp = gstar_pivot(s, r, C, K)
    rel = abs(gd - gp) / max(1.0, abs(gd), abs(gp))
    max_rel = max(max_rel, rel)
    S2 = float(s @ s)
    singular = np.linalg.svd(K, compute_uv=False)
    dist2 = math.sqrt(float(np.sum(singular[2:] ** 2)))
    rhs = (2.0 * gp / S2) ** 0.25
    max_rank2_violation = max(max_rank2_violation, dist2 - rhs)
    assert rel < 1e-10
    assert dist2 <= rhs + 1e-10

print(f"random_identity_max_relative_error={max_rel:.3e}")
print(f"random_rank2_bound_max_violation={max_rank2_violation:.3e}")

for N in (8, 16, 32, 64):
    one = np.ones(N) / math.sqrt(N)
    alt = ((-1.0) ** np.arange(N)) / math.sqrt(N)
    s = one.copy(); a = one.copy(); b = one.copy(); x = alt.copy(); y = alt.copy()
    C = np.outer(a, s)
    K = np.outer(a, b) + np.outer(x, y)
    M = np.block([[s.reshape(1, N), b.reshape(1, N)], [C, K]])
    sv = np.linalg.svd(M, compute_uv=False)
    gp = gstar_pivot(s, b, C, K)
    U, _, _ = np.linalg.svd(M, full_matrices=False)
    rank = int(np.sum(sv > 1e-10))
    lev = np.sum(U[:, :rank] ** 2, axis=1)
    print(
        f"N={N}: singulars={sv[:2]}, E2K={e2(K):.12f}, "
        f"Gstar={gp:.3e}, max_leverage={lev.max():.12f}"
    )
    assert np.allclose(sv[:2], [2.0, 1.0], atol=1e-10)
    assert np.max(sv[2:]) < 1e-10
    assert abs(e2(K) - 1.0) < 1e-10
    assert gp < 1e-20
    assert lev.max() <= 0.5 + 1e-10

eps = 1 / 8
C_Dprime = 9 * math.sqrt(3 * math.e) * (2 / eps ** 4) ** (1 / 6)
C_F = (4 * 4 / (4 - 2)) * (4.0 ** (-1 / 4))
print(f"epsilon_1_8_Dprime_constant={C_Dprime:.12f}")
print(f"rank4_F_bound={C_F:.12f}")
assert abs(C_Dprime - 115.393683039516) < 1e-9
assert abs(C_F - 4 * math.sqrt(2)) < 1e-12
print("STATUS=PASS")
