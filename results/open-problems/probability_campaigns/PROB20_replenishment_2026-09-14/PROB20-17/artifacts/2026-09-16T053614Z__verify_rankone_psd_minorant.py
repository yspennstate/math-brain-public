import itertools
import math
import numpy as np

SEED = 20260916053614
rng = np.random.default_rng(SEED)


def abs_gram(U):
    return np.abs(U @ U.conj().T)


def hamiltonian_mean(G):
    n = G.shape[0]
    total = 0.0
    for p in itertools.permutations(range(n)):
        w = 1.0
        for k in range(n - 1):
            w *= G[p[k], p[k + 1]]
        total += w
    return total / math.factorial(n)


def owner_rankone(U, a):
    n = len(a)
    G = abs_gram(U)
    q = np.sqrt(a)
    M = (q[:, None] * G) * q[None, :]
    H = hamiltonian_mean(G)
    L = np.prod(a) * H
    R = (q @ np.linalg.matrix_power(M, n - 1) @ q) / (n ** n)
    return G, H, L, R


def row_min_c(G):
    n = G.shape[0]
    c = np.zeros(n)
    for i in range(n):
        h = min(G[i, j] for j in range(n) if j != i)
        c[i] = math.sqrt(max(h, 0.0))
    return c


def minorant_bound(G, a, c):
    n = len(a)
    residuals = [
        c[i] * c[j] - G[i, j]
        for i in range(n)
        for j in range(i + 1, n)
    ]
    residuals.extend([-float(c.min()), float(c.max()) - 1.0])
    feas = max(0.0, max(residuals))

    S = float(np.sum(a))
    Q = float(
        np.sum(a * a)
        + 2.0
        * sum(
            a[i] * a[j] * c[i] * c[j]
            for i in range(n)
            for j in range(i + 1, n)
        )
    )
    d = Q / (S * S)
    lower = (S / n) ** n * d ** (n - 1)
    return feas, Q, d, lower


# Strict-extension example: real unit vectors at angles 0,60,75,105 degrees.
angles = np.deg2rad(np.array([0.0, 60.0, 75.0, 105.0]))
U = np.column_stack([np.cos(angles), np.sin(angles)])
a = np.ones(4)
G, H, L, R = owner_rankone(U, a)
c = np.array(
    [
        math.sin(math.radians(15.0)),
        math.cos(math.radians(15.0)),
        1.0,
        math.sqrt(3.0) - 1.0,
    ]
)
feas, Q, d, lower = minorant_bound(G, a, c)
off = G[np.triu_indices(4, 1)]
gmin, gmax = float(off.min()), float(off.max())
old_band_rhs = (1.0 + 3.0 * gmin) / 4.0

print("seed", SEED)
print("strict_example")
print("gmin", gmin)
print("gmax", gmax)
print("old_band_rhs", old_band_rhs)
print("old_band_pass", gmax <= old_band_rhs + 1e-14)
print("c", c.tolist())
print("feas_residual", feas)
print("H4", H)
print("d", d)
print("d^3", d**3)
print("new_certificate_pass", H <= d**3 + 1e-14)
print("L", L)
print("R", R)
print("R/L", R / L)

assert not (gmax <= old_band_rhs + 1e-14)
assert feas <= 1e-13
assert H <= d**3 + 1e-13
assert R >= L - 1e-13

# Random deterministic checks of the theorem using the universally feasible
# row-min choice c_i = sqrt(min_{j != i} g_ij).
min_transfer_ratio = float("inf")
min_minorant_ratio = float("inf")
max_feas = 0.0

for n in (4, 5, 6):
    for dim in (2, 3, 5):
        for _ in range(40):
            X = rng.normal(size=(n, dim)) + 1j * rng.normal(size=(n, dim))
            X /= np.linalg.norm(X, axis=1)[:, None]
            a = np.exp(rng.normal(scale=0.7, size=n))
            G, H, L, R = owner_rankone(X, a)
            c = row_min_c(G)
            feas, Q, d, lower = minorant_bound(G, a, c)
            max_feas = max(max_feas, feas)
            min_minorant_ratio = min(
                min_minorant_ratio,
                R / lower if lower > 0 else float("inf"),
            )

            # Verify the exact transfer identity by direct word enumeration.
            total = 0.0
            for word in itertools.product(range(n), repeat=n):
                scales = 1.0
                edges = 1.0
                for idx in word:
                    scales *= a[idx]
                for k in range(n - 1):
                    edges *= G[word[k], word[k + 1]]
                total += scales * edges

            q = np.sqrt(a)
            M = (q[:, None] * G) * q[None, :]
            transfer = q @ np.linalg.matrix_power(M, n - 1) @ q
            min_transfer_ratio = min(
                min_transfer_ratio,
                transfer / total if total > 0 else 1.0,
            )

            assert feas <= 5e-13
            assert transfer >= total * (1.0 - 5e-12)
            assert R >= lower * (1.0 - 5e-12)

print("random_checks")
print("max_feas_residual", max_feas)
print("min_transfer_ratio", min_transfer_ratio)
print("min_actual_R_over_minorant_lower", min_minorant_ratio)
