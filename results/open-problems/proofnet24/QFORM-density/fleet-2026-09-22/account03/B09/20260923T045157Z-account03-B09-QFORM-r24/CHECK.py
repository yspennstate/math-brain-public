import itertools, math
import numpy as np


def data(U):
    n, k = U.shape
    assert k == 3
    ws = {}
    for S in itertools.combinations(range(n), 3):
        w = float(np.linalg.det(U[list(S), :]) ** 2)
        if w > 1e-13:
            ws[S] = w
    assert abs(sum(ws.values()) - 1) < 1e-10

    rho_avg = 0.0
    eigs = {}
    for S, w in ws.items():
        R = np.eye(3) - U[list(S), :].T @ U[list(S), :]
        eigs[S] = np.linalg.eigvalsh((R + R.T) / 2)
        rho_avg += w * float(np.linalg.det(R))

    rho_direct = 0.0
    for S, w in ws.items():
        for T, v in ws.items():
            if set(S).isdisjoint(T):
                rho_direct += w * v
    assert abs(rho_avg - rho_direct) < 1e-10
    return ws, rho_avg, eigs


# The three exact rho=0 endpoint archetypes.
U3 = np.eye(3)
U2 = np.array([
    [1, 0, 0], [0, 1, 0],
    [0, 0, 2 ** -0.5], [0, 0, 2 ** -0.5],
], float)
U1 = np.array([
    [2 ** -0.5, 0, 0], [2 ** -0.5, 0, 0],
    [0, 2 ** -0.5, 0], [0, 2 ** -0.5, 0],
    [0, 0, 1],
], float)

for name, U, target in [
    ("core3", U3, [0, 0, 0]),
    ("core2_line", U2, [0, 0, 0.5]),
    ("core1_plane", U1, [0, 0.5, 0.5]),
]:
    ws, rho, eigs = data(U)
    assert abs(rho) < 1e-12
    first = next(iter(eigs.values()))
    assert np.allclose(first, target, atol=1e-12)
    print(name, "rho=", rho, "sample_eigs=", first.tolist())

# Complementary-minor identity on a generic frame.
rng = np.random.default_rng(20260923)
M = rng.normal(size=(12, 3))
U = np.linalg.qr(M)[0][:, :3]
ws, rho, eigs = data(U)
print("random_rho=", rho, "positive_bases=", len(ws))

# eta=1/16 routing constants.
eta = 1 / 16
rho0 = eta ** 3 / 2
own = (5 * math.e / 3) * rho0 ** (-1 / 5)
peer = 2 * math.exp(3 / 4) * rho0 ** (-1 / 4)
assert abs((2 * rho0) ** (1 / 3) - eta) < 1e-14
print("eta=", eta, "rho0=", rho0)
print("grouped_two_slope_bound_resource_ge_1=", own)
print("mixed_hub_peer_bound_resource_ge_1=", peer)
print("CHECK_PASS")
