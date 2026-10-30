import itertools
import math
import numpy as np

rho0 = 1.0 / 512.0
tau0 = (rho0 / 2.0) ** (1.0 / 3.0)
alpha0 = 1.0 - rho0 - tau0
beta0 = 1.0 - rho0 - tau0 / (1.0 - tau0)
K0 = 3.0 * math.e ** (1.0 / 3.0) * 2.0 ** (1.0 / 6.0)
Ktri = K0 * (2.0 * beta0 * (1.0 - alpha0) / 3.0) ** (-1.0 / 6.0)
Kpeer = 2.0 * math.sqrt(math.e) * rho0 ** (-1.0 / 4.0)
Kstar = 3.0 * 2.0 ** (7.0 / 6.0)

print(f"rho0={rho0:.15f}")
print(f"tau0={tau0:.15f}")
print(f"alpha0={alpha0:.15f}")
print(f"beta0={beta0:.15f}")
print(f"promoted_pivot_constant={K0:.15f}")
print(f"near_triangle_constant={Ktri:.15f}")
print(f"large_rho_peer_constant={Kpeer:.15f}")
print(f"exact_star_split_constant={Kstar:.15f}")

assert Ktri < 7.514
assert Kpeer < 15.686
assert Kstar < 6.735

# Deterministic/random algebra regression for the near-triangle resource inequality.
rng = np.random.default_rng(12345)
for _ in range(1000):
    C = rng.normal(size=(6, 2))
    G = C.T @ C
    if np.linalg.det(G) < 1e-10:
        continue
    eig, vec = np.linalg.eigh(G)
    U = C @ vec @ np.diag(eig ** (-0.5)) @ vec.T
    ell = np.sum(U * U, axis=1)
    beta, S = max(
        (np.linalg.det(U[list(S)].T @ U[list(S)]), S)
        for S in itertools.combinations(range(6), 3)
    )
    a = max(ell[list(S)])
    if beta <= 1e-12 or a >= 1.0:
        continue
    lhs = max(np.sum(C[list(S)] ** 2, axis=1) * (1.0 - ell[list(S)]))
    rhs = (2.0 * beta * (1.0 - a) / 3.0) * math.sqrt(np.linalg.det(G))
    assert lhs + 1e-9 >= rhs

# Exact-star Gram identity: det G = ||alpha||^2 det(c,d)^2 for unit d.
for _ in range(1000):
    th = rng.uniform(-math.pi, math.pi)
    d = np.array([math.cos(th), math.sin(th)])
    c = rng.normal(size=2)
    if abs(np.linalg.det(np.column_stack([c, d]))) < 1e-5:
        continue
    alpha = rng.normal(size=7)
    A2 = float(alpha @ alpha)
    G = np.outer(c, c) + A2 * np.outer(d, d)
    wedge = float(np.linalg.det(np.column_stack([c, d])))
    assert abs(np.linalg.det(G) - A2 * wedge * wedge) < 1e-8 * max(1.0, abs(np.linalg.det(G)))

print("PASS QFORM fleet03/B09 r28 checks")
