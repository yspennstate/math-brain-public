import itertools
import math
import numpy as np

rng = np.random.default_rng(12345)

def make_V(G, n):
    Z = rng.normal(size=(n, 2))
    Q, _ = np.linalg.qr(Z)
    L = np.linalg.cholesky(G)
    return Q @ L.T

def orth_eta(V, tau):
    if tau == 0:
        return np.zeros(V.shape[0])
    while True:
        z = rng.normal(size=V.shape[0])
        e = z - V @ np.linalg.solve(V.T @ V, V.T @ z)
        ne = np.linalg.norm(e)
        if ne > 1e-10:
            return math.sqrt(tau) * e / ne

def trial():
    theta = rng.uniform(0, 2 * np.pi)
    Q = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    lam = rng.uniform(0.15, 0.85, size=2)
    SJ = Q @ np.diag(lam) @ Q.T
    SK = np.eye(2) - SJ

    delta = 0.4 * rng.normal(size=2)
    tauJ = rng.uniform(0, 0.02)
    tauK = rng.uniform(0, 0.02)
    energy = delta @ SJ @ SK @ delta + tauJ + tauK
    if energy >= 0.8:
        return trial()
    c = 1 - energy

    VJ = make_V(SJ, 5)
    VK = make_V(SK, 6)
    etaJ = orth_eta(VJ, tauJ)
    etaK = orth_eta(VK, tauK)

    pJ = SK @ delta
    pK = -SJ @ delta
    alphaJ = VJ @ pJ + etaJ
    alphaK = VK @ pK + etaK
    UJ = np.column_stack([alphaJ, VJ])
    UK = np.column_stack([alphaK, VK])
    R = np.vstack([[math.sqrt(c), 0, 0], UJ, UK])

    errors = [np.max(np.abs(R.T @ R - np.eye(3)))]
    errors.append(np.max(np.abs(pJ - SK @ delta)))
    errors.append(np.max(np.abs(pK + SJ @ delta)))
    errors.append(abs((1-c) - (tauJ + tauK + delta @ SJ @ SK @ delta)))

    E30 = sum(np.linalg.det(UJ[list(I), :])**2
              for I in itertools.combinations(range(len(UJ)), 3))
    E03 = sum(np.linalg.det(UK[list(I), :])**2
              for I in itertools.combinations(range(len(UK)), 3))
    E21 = sum(np.linalg.det(np.vstack([UJ[i], UJ[j], UK[k]]))**2
              for i, j in itertools.combinations(range(len(UJ)), 2)
              for k in range(len(UK)))
    E12 = sum(np.linalg.det(np.vstack([UJ[i], UK[j], UK[k]]))**2
              for i in range(len(UJ))
              for j, k in itertools.combinations(range(len(UK)), 2))

    F30 = tauJ * np.linalg.det(SJ)
    F03 = tauK * np.linalg.det(SK)
    F21 = (np.linalg.det(SJ) * (tauK + delta @ SK @ delta)
           + tauJ * np.linalg.det(SJ) * np.trace(np.linalg.solve(SJ, SK)))
    F12 = (np.linalg.det(SK) * (tauJ + delta @ SJ @ delta)
           + tauK * np.linalg.det(SK) * np.trace(np.linalg.solve(SK, SJ)))

    errors.extend([abs(E30-F30), abs(E21-F21), abs(E12-F12), abs(E03-F03)])
    errors.append(abs(E30 + E21 + E12 + E03 - (1-c)))
    return max(errors)

max_error = 0.0
for _ in range(500):
    max_error = max(max_error, trial())

print(f"max_error={max_error:.17g}")
assert max_error < 1e-11
print("QFORM_B10_R19_NEARSPAN_EXTERIOR_STRATA_CHECK_PASS")
