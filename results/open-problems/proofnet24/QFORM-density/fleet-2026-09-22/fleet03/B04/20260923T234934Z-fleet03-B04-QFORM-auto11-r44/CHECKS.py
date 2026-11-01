import math
import numpy as np

CSTAR = 8.45302122552817687470491804598

# Live rank-five arithmetic.
R = 5.0
tau = 1.0 / 25.0
gamma = 19.0 / 20.0
sigma = 1597.0 / 2000.0
delta = 403.0 / 2000.0
g = (1.0 - math.sqrt(R * tau / gamma)) / 2.0
m_live = g * gamma * sigma - delta
assert m_live > 3.0 / 800.0
assert 13923**2 > 19 * 3194**2
live_bound = CSTAR / m_live
safe_bound = (800.0 / 3.0) * CSTAR

# Designated-partner numerical spend.
delta_partner = 47045881.0 / (12.0 * 10.0**18)
partner_bound = 3.0 * 2.0 ** (4.0 / 3.0) * delta_partner ** (-1.0 / 6.0)
assert partner_bound < 602.012

# Explicit N=128 Walsh example.
N = 128
cols = [0, 1, 2]
U0 = np.empty((N, 3), dtype=float)
for x in range(N):
    for j, c in enumerate(cols):
        parity = (x & c).bit_count() & 1
        U0[x, j] = (-1.0 if parity else 1.0) / math.sqrt(N)

assert np.linalg.norm(U0.T @ U0 - np.eye(3), ord=2) < 1e-12
assert np.linalg.norm(U0[0] - U0[4]) < 1e-12

theta = 0.5 * math.asin(3.0 / 4.0)
c, s = math.cos(theta), math.sin(theta)
U = U0.copy()
w0, w4 = U0[0].copy(), U0[4].copy()
U[0] = c * w0 + s * w4
U[4] = -s * w0 + c * w4
assert np.linalg.norm(U.T @ U - np.eye(3), ord=2) < 1e-12

lev = np.sum(U * U, axis=1)
assert abs(lev[0] - 21.0 / 512.0) < 1e-14
assert abs(lev[4] - 3.0 / 512.0) < 1e-14
for x in range(1, N):
    if x != 4:
        assert abs(lev[x] - 3.0 / 128.0) < 1e-14
assert np.count_nonzero(lev > 1.0 / 25.0) == 1

Lmask = np.ones(N, dtype=bool)
Lmask[0] = False
G = U[Lmask].T @ U[Lmask]
gev = np.linalg.eigvalsh(G)
assert abs(gev[0] - 491.0 / 512.0) < 1e-13
assert abs(gev[1] - 1.0) < 1e-13
assert abs(gev[2] - 1.0) < 1e-13

Lambda = np.diag([2.0, 1.5, -1.5])
S = U @ Lambda @ U.T
E = np.ones((N, N), dtype=float) / 2560.0
A = S + E
assert abs(np.linalg.norm(E, ord=2) - 1.0 / 20.0) < 1e-12
evals = np.linalg.eigvalsh(A)
assert np.count_nonzero(np.abs(evals) >= 1.0) >= 3
assert evals[-2] >= 1.45 - 1e-12
assert evals[0] <= -1.45 + 1e-12

gamma_ex = 491.0 / 512.0
beta_ex = 3.0 / 128.0
g_ex = (1.0 - math.sqrt(3.0 * beta_ex / gamma_ex)) / 2.0
assert abs(g_ex - (0.5 - 3.0 / math.sqrt(491.0))) < 1e-14
m_ex = gamma_ex * g_ex * 1.5 - 1.0 / 20.0
example_bound = CSTAR / m_ex
assert example_bound < 17.82

print({
    "g_live": g,
    "m_live": m_live,
    "live_bound_actual_margin": live_bound,
    "live_bound_safe": safe_bound,
    "partner_bound": partner_bound,
    "example_max_leverage": float(lev.max()),
    "example_heavy_count": int(np.count_nonzero(lev > 1.0 / 25.0)),
    "example_G_eigenvalues": [float(v) for v in gev],
    "example_target_eigs_extreme": [float(evals[0]), float(evals[-2]), float(evals[-1])],
    "example_m": m_ex,
    "example_bound": example_bound,
})
