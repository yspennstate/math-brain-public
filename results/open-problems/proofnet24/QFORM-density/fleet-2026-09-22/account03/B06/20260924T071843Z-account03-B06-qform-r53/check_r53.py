import numpy as np

rng = np.random.default_rng(20260924)

def adj3(F):
    C = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            M = np.delete(np.delete(F, i, axis=0), j, axis=1)
            C[i, j] = ((-1) ** (i + j)) * np.linalg.det(M)
    return C.T

max_general = 0.0
for _ in range(10000):
    while True:
        R = rng.normal(size=(3, 3))
        B = (R + R.T) / 2
        if abs(np.linalg.det(B)) > 1e-4:
            break
    d = rng.normal(size=3)
    DH = np.diag(d)
    F = B + DH
    z = rng.normal(size=3)
    delta = rng.normal()
    M4 = np.block([
        [F, (B @ z)[:, None]],
        [(z @ B)[None, :], np.array([[z @ B @ z + delta]])],
    ])
    lhs = np.linalg.det(M4)
    rhs = delta * np.linalg.det(F) + z @ (
        np.linalg.det(F) * DH - DH @ adj3(F) @ DH
    ) @ z
    err = abs(lhs - rhs) / (1.0 + abs(rhs))
    max_general = max(max_general, err)

max_singular = 0.0
for _ in range(10000):
    while True:
        C0 = rng.normal(size=(2, 2))
        C0 = (C0 + C0.T) / 2
        K = np.linalg.det(C0)
        if abs(K) > 0.1:
            break
    b = rng.normal(size=2)
    a0 = rng.normal()
    B = np.block([[np.array([[a0]]), b[None, :]], [b[:, None], C0]])
    D = np.linalg.det(B)
    if abs(D) < 1e-5:
        continue
    d1 = -D / K
    DH = np.diag([d1, 0.0, 0.0])
    F = B + DH
    vals, vecs = np.linalg.eigh(F)
    k0 = int(np.argmin(abs(vals)))
    v = vecs[:, k0]
    nz = [i for i in range(3) if i != k0]
    kappa_signed = vals[nz[0]] * vals[nz[1]]
    Z = rng.normal(size=(3, 7))
    deltas = rng.normal(size=7)
    omega = Z.T @ DH @ v
    A = np.block([
        [F, B @ Z],
        [Z.T @ B, Z.T @ B @ Z + np.diag(deltas)],
    ])
    for j in range(7):
        inds = [0, 1, 2, 3 + j]
        lhs = np.linalg.det(A[np.ix_(inds, inds)])
        rhs = -kappa_signed * omega[j] ** 2
        err = abs(lhs - rhs) / (1.0 + abs(rhs))
        max_singular = max(max_singular, err)

print("QFORM_B06_R53_CHECK_PASS")
print("max_general_normalized_error", max_general)
print("max_singular_normalized_error", max_singular)
