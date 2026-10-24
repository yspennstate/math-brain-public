import math
import numpy as np

C_density = 5 * 2 ** (11 / 10)
C_l2 = (5 / 3) * 2 ** (11 / 10)
C_collision = (10 / 3) * 2 ** (11 / 10)

assert abs(C_density - 10.717734625362931) < 1e-12
assert abs(C_l2 - 3.5725782084543107) < 1e-12
assert abs(C_collision - 7.1451564169086215) < 1e-12

# Check the envelope integrations algebraically.
# For |phi| <= min(1,B |t|^{-5/4}), int_R envelope = 10 B^(4/5).
b = 5 / 4
assert abs(2 * b / (b - 1) - 10) < 1e-14
# For |phi|^2 <= min(1,C |t|^{-5/2}), int_R envelope = (10/3) C^(2/5).
b2 = 5 / 2
assert abs(2 * b2 / (b2 - 1) - 10 / 3) < 1e-14

# Strict-N3 witness check for balanced physical partitions.
for m in (8, 12, 16, 100):
    assert m % 4 == 0
    q = m // 4
    gI = np.ones(2 * q) / math.sqrt(m)
    uI = np.r_[np.ones(q), -np.ones(q)] / math.sqrt(m)
    G = np.array([[gI @ gI, gI @ uI], [uI @ gI, uI @ uI]])
    assert np.max(np.abs(G - 0.5 * np.eye(2))) < 1e-12
    Ginv = np.linalg.inv(G)
    leverages = []
    for x, y in zip(gI, uI):
        row = np.array([x, y])
        leverages.append(row @ Ginv @ row)
    assert abs(max(leverages) - 4 / m) < 1e-12
    assert max(leverages) <= 0.5 + 1e-12

    # J has the same balanced vectors.
    v = uI.copy()
    wJ = gI.copy()
    Delta = np.linalg.det(np.array([[v @ v, v @ wJ], [wJ @ v, wJ @ wJ]]))
    Xi = np.linalg.det(G) ** 2 * (v @ v) * Delta
    assert abs(Xi - 1 / 128) < 1e-12
    density = C_density * Xi ** (-0.1)
    collision = C_collision * Xi ** (-0.1)
    assert abs(density - 5 * 2 ** (9 / 5)) < 1e-12
    assert abs(collision - (10 / 3) * 2 ** (9 / 5)) < 1e-12

# Check invariance of Xi under the arbitrary rank-one factorization scaling.
rng = np.random.default_rng(230923)
w = rng.normal(size=7)
u = rng.normal(size=7)
v = rng.normal(size=8)
z = rng.normal(size=8)
G0 = np.array([[w @ w, w @ u], [u @ w, u @ u]])
D0 = np.linalg.det(np.array([[v @ v, v @ z], [z @ v, z @ z]]))
Xi0 = np.linalg.det(G0) ** 2 * (v @ v) * D0
for c in (0.1, 0.7, 3.0, 11.0):
    uc = c * u
    vc = v / c
    Gc = np.array([[w @ w, w @ uc], [uc @ w, uc @ uc]])
    Dc = np.linalg.det(np.array([[vc @ vc, vc @ z], [z @ vc, z @ z]]))
    Xic = np.linalg.det(Gc) ** 2 * (vc @ vc) * Dc
    assert abs(Xic / Xi0 - 1.0) < 1e-10

print('QFORM_B03_R23_CHECK_PASS')
print(f'C_density={C_density:.15f}')
print(f'C_L2sq={C_l2:.15f}')
print(f'C_collision={C_collision:.15f}')
print(f'witness_Xi={1/128:.15f}')
print(f'witness_density={5*2**(9/5):.15f}')
print(f'witness_collision={(10/3)*2**(9/5):.15f}')
