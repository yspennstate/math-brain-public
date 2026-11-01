import math
import numpy as np

rng = np.random.default_rng(20260922)

def rand_orth():
    M = rng.normal(size=(3, 3))
    Q, R = np.linalg.qr(M)
    d = np.sign(np.diag(R))
    d[d == 0] = 1
    return Q @ np.diag(d)

max_rel = 0.0
min_eta = float('inf')
max_null = 0.0
for _ in range(10000):
    vals = 1 + 20 * rng.random(3)
    if rng.random() < 0.5:
        diag = np.array([vals[0], vals[1], -vals[2]])
        u0 = np.array([math.sqrt(vals[2] / (vals[0] + vals[2])), 0.0,
                       math.sqrt(vals[0] / (vals[0] + vals[2]))])
    else:
        diag = np.array([-vals[0], -vals[1], vals[2]])
        u0 = np.array([math.sqrt(vals[2] / (vals[0] + vals[2])), 0.0,
                       math.sqrt(vals[0] / (vals[0] + vals[2]))])
    O = rand_orth()
    Lam = O @ np.diag(diag) @ O.T
    u = O @ u0
    null = float(u @ Lam @ u)
    v = Lam @ u
    eta = float(np.linalg.norm(v))
    e1 = v / eta
    e2 = np.cross(u, e1)
    e2 /= np.linalg.norm(e2)
    B = np.column_stack([u, e1, e2])
    M = B.T @ Lam @ B
    det = float(np.linalg.det(Lam))
    rel = abs(det + eta * eta * M[2, 2]) / max(1.0, abs(det))
    max_rel = max(max_rel, rel)
    min_eta = min(min_eta, eta)
    max_null = max(max_null, abs(null))

C = 2 ** (3 / 4) * math.exp(1 / 2) * (8 * math.exp(1 / 4) + 2)
print(f"trials=10000")
print(f"max_relative_det_error={max_rel:.16e}")
print(f"max_null_pivot_error={max_null:.16e}")
print(f"min_eta={min_eta:.16f}")
print(f"C_null={C:.15f}")
assert max_rel < 1e-12
assert max_null < 1e-12
assert min_eta >= 1 - 1e-12
assert C < 34.029
print("STATUS=PASS")
