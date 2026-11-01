import math
import numpy as np

rng = np.random.default_rng(20260924)
TARGET = 20000
count = 0
max_factorization_error = 0.0
max_twojacobian_error = 0.0
max_area_identity_error = 0.0
min_exterior_ratio = float("inf")

while count < TARGET:
    M = rng.normal(size=(3, 3))
    M = (M + M.T) / 2
    ev = np.linalg.eigvalsh(M)
    s = float(np.min(np.abs(ev)))
    if s < 0.05:
        continue

    x = M[0, 1:].copy()
    O = np.eye(3)
    if np.linalg.norm(x) > 1e-10:
        e2 = x / np.linalg.norm(x)
        e3 = np.array([-e2[1], e2[0]])
        O[1:, 1] = e2
        O[1:, 2] = e3
    M = O.T @ M @ O

    a, r = float(M[0, 0]), float(M[0, 1])
    b, c, d = float(M[1, 1]), float(M[1, 2]), float(M[2, 2])
    if abs(a) < 1e-6 or abs(d) < 1e-6:
        continue

    gamma = float(np.linalg.det(M) / (a * d))
    q = float(rng.uniform(0.01, 1.0))
    H, T0, Y, W = rng.normal(size=4)
    Z = math.sqrt(q) * H + math.sqrt(1 - q) * T0
    U = Z + (r / a) * Y
    V = W + (c / d) * Y

    Q1 = a * Z * Z + 2 * r * Z * Y + b * Y * Y + 2 * c * Y * W + d * W * W
    Q2 = a * U * U + gamma * Y * Y + d * V * V
    max_factorization_error = max(max_factorization_error, abs(Q1 - Q2))

    u = np.array([math.sqrt(q), math.sqrt(1 - q), r / a, 0.0])
    y = np.array([0.0, 0.0, 1.0, 0.0])
    v = np.array([0.0, 0.0, c / d, 1.0])
    gradQ = 2 * a * U * u + 2 * gamma * Y * y + 2 * d * V * v
    Jsq = float((y @ y) * (gradQ @ gradQ) - (y @ gradQ) ** 2)
    rhs = float(4 * (a * a * U * U + d * d * V * V))
    max_twojacobian_error = max(max_twojacobian_error, abs(Jsq - rhs))

    G = np.array([[u @ u, u @ v], [u @ v, v @ v]])
    area = math.sqrt(max(0.0, float(np.linalg.det(G))))
    formula_area = math.sqrt(1 + (r / a) ** 2 + (c / d) ** 2)
    max_area_identity_error = max(max_area_identity_error, abs(area - formula_area))

    exterior = abs(a * d) * area
    Me1 = M @ np.array([1.0, 0.0, 0.0])
    Me3 = M @ np.array([0.0, 0.0, 1.0])
    exterior2 = math.sqrt(max(0.0, float((Me1 @ Me1) * (Me3 @ Me3) - (Me1 @ Me3) ** 2)))
    max_area_identity_error = max(max_area_identity_error, abs(exterior - exterior2))
    min_exterior_ratio = min(min_exterior_ratio, exterior / (s * s))
    count += 1

print("QFORM fleet01/B11 nonzero LDL two-Jacobian deterministic verification")
print("checks", count)
print("max_factorization_error", max_factorization_error)
print("max_twojacobian_error", max_twojacobian_error)
print("max_area_identity_error", max_area_identity_error)
print("min_exterior_ratio", min_exterior_ratio)
print("sqrt_2pi", math.sqrt(2 * math.pi))
assert min_exterior_ratio >= 1 - 1e-9
print("QFORM_B11_LDL_TWOJACOBIAN_CHECK_PASS")
