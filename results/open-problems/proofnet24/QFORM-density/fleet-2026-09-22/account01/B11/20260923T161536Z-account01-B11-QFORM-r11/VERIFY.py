import itertools
import math
import numpy as np

rng = np.random.default_rng(20260923)

def random_check(k):
    A = rng.normal(size=(k, 3))
    U, _ = np.linalg.qr(A)
    U = U[:, :3]
    O, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    M = O @ np.diag([1.3, 2.1, -1.7]) @ O.T
    weights = []
    det_errors = []
    for J in itertools.combinations(range(k), 3):
        UJ = U[list(J), :]
        w = np.linalg.det(UJ) ** 2
        BJ = UJ @ M @ UJ.T
        weights.append(w)
        det_errors.append(abs(np.linalg.det(BJ) - np.linalg.det(M) * w))
    assert abs(sum(weights) - 1.0) < 1e-12
    assert max(weights) + 1e-12 >= 1 / math.comb(k, 3)
    assert max(det_errors) < 1e-12
    return sum(weights), max(weights), max(det_errors)

for k in [3, 4, 5, 8]:
    print('random', k, random_check(k))

Cbase = 64 * math.sqrt(10)
print('Cbase', Cbase)
print('k4', Cbase * math.comb(4, 3) ** (1 / 3))
print('k5', Cbase * math.comb(5, 3) ** (1 / 3))

for rho in [0.1, 0.5, 0.9]:
    sp = np.array([1.0, math.sqrt(rho), 0.0])
    sm = np.array([1.0, -math.sqrt(rho), 0.0])
    tp = np.array([0.0, math.sqrt(1-rho), 1.0])
    tm = np.array([0.0, math.sqrt(1-rho), -1.0])
    U = np.vstack([sp, sm, tp, tm]) / math.sqrt(2)
    assert np.max(np.abs(U.T @ U - np.eye(3))) < 1e-12
    weights = [np.linalg.det(U[list(J), :]) ** 2
               for J in itertools.combinations(range(4), 3)]
    expected = max(rho, 1-rho) / 2
    assert abs(sum(weights)-1.0) < 1e-12
    assert abs(max(weights)-expected) < 1e-12
    print('rho', rho, 'weights', weights, 'wmax', max(weights))

print('QFORM_B11_PROJECTIVE_BANK_CHECK_PASS')
