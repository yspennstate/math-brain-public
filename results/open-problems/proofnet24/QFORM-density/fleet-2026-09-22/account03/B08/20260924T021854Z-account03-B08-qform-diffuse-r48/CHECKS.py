import math
import numpy as np

SEED = 480021854
rng = np.random.default_rng(SEED)


def tangent_data(K, tol=1e-12):
    vals, V = np.linalg.eigh(K)
    pos = np.where(vals > tol)[0]
    neg = np.where(vals < -tol)[0]
    if len(pos) == 0 or len(neg) == 0:
        raise ValueError("K is not indefinite")

    candidates = []
    for p in pos:
        for n in neg:
            for sign in (1.0, -1.0):
                y = np.zeros(3)
                y[p] = math.sqrt(-vals[n])
                y[n] = sign * math.sqrt(vals[p])
                w = V @ y
                h = K @ w
                candidates.append((abs(h[0]), w, h))

    candidates.sort(key=lambda x: x[0], reverse=True)
    h0, w, h = candidates[0]
    if h0 < tol:
        raise ValueError("no tangent graph with h_0 != 0")

    c = h[1:] / h[0]
    a = K[0, 0]
    r = K[1:, 0]
    R = K[1:, 1:]
    Rc = R - np.outer(r, c) - np.outer(c, r) + a * np.outer(c, c)
    g = r - a * c
    return w, h, c, Rc, g


max_null = 0.0
max_det = 0.0
max_parameter_currency_error = 0.0
max_physical_currency_relative_error = 0.0
parameter_tests = 0
physical_tests = 0

for _ in range(1000):
    Q, _ = np.linalg.qr(rng.normal(size=(2, 2)))
    ev = rng.uniform(0.2, 3.0, size=2) * rng.choice([-1, 1], size=2)
    R = Q @ np.diag(ev) @ Q.T

    if np.all(ev > 0):
        d = -rng.uniform(0.2, 3.0)
    elif np.all(ev < 0):
        d = rng.uniform(0.2, 3.0)
    else:
        d = rng.choice([-1, 1]) * rng.uniform(0.2, 3.0)

    m = rng.normal(size=2)
    a = d + m @ R @ m
    r = R @ m
    K = np.block([[np.array([[a]]), r[None, :]], [r[:, None], R]])

    w, h, c, Rc, g = tangent_data(K)
    max_null = max(max_null, abs(w @ K @ w))
    max_det = max(max_det, abs(np.linalg.det(Rc)))

    vals2, V2 = np.linalg.eigh(Rc)
    idx = np.argmax(np.abs(vals2))
    lam = vals2[idx]
    v = V2[:, idx]
    k = np.array([-v[1], v[0]])
    gk = k @ g

    lhs = abs(lam) * gk**2
    rhs = abs(d * np.linalg.det(R))
    max_parameter_currency_error = max(max_parameter_currency_error, abs(lhs - rhs))
    parameter_tests += 1

    for _ in range(2):
        mphys = int(rng.integers(3, 12))
        N = rng.normal(size=(2, mphys))
        if np.linalg.matrix_rank(N) < 2:
            continue

        sraw = N.T @ v
        snorm = np.linalg.norm(sraw)
        if snorm < 1e-10:
            continue
        s = sraw / snorm
        lambda_phys = lam * snorm**2
        gphys = N.T @ g
        hphys = gphys - s * (s @ gphys)

        lhs2 = abs(lambda_phys) * (hphys @ hphys)
        rhs2 = abs(d * np.linalg.det(R)) * np.linalg.det(N @ N.T)
        rel = abs(lhs2 - rhs2) / max(rhs2, 1e-15)
        max_physical_currency_relative_error = max(max_physical_currency_relative_error, rel)
        physical_tests += 1

constant_base = 3 * 4 ** (2 / 3)
constant_mu_third = constant_base * (3 / 2) ** (1 / 3)

print(f"seed={SEED}")
print(f"parameter_tests={parameter_tests}")
print(f"physical_tests={physical_tests}")
print(f"max_abs_wKw={max_null:.17e}")
print(f"max_abs_det_Rc={max_det:.17e}")
print(f"max_abs_parameter_currency_error={max_parameter_currency_error:.17e}")
print(f"max_physical_currency_relative_error={max_physical_currency_relative_error:.17e}")
print(f"base_constant={constant_base:.15f}")
print(f"mu_le_1_over_3_constant={constant_mu_third:.15f}")

assert max_null < 1e-11
assert max_det < 1e-11
assert max_parameter_currency_error < 1e-11
assert max_physical_currency_relative_error < 1e-11
assert constant_mu_third < 8.653498
print("QFORM_B08_R48_TANGENT_SHEAR_CHECK_PASS")
