import itertools, math
import numpy as np


def v(phi):
    return np.array([math.sqrt(2.0) * math.cos(phi),
                     math.sqrt(2.0) * math.sin(phi),
                     1.0], dtype=float)


def build(N=5, eps=0.1):
    base = [0.0, 2 * math.pi / 3, 4 * math.pi / 3]
    rows = [math.sqrt((1 - eps) / 3.0) * v(phi) for phi in base]
    shift = 1.0 / 7.0
    rows += [math.sqrt(eps / N) * v(2 * math.pi * (j + shift) / N)
             for j in range(N)]
    R = np.stack(rows)
    Lam = np.diag([1.0, 1.0, -2.0])
    A = R @ Lam @ R.T
    return R, Lam, A


R, Lam, A = build()
n = R.shape[0]
triples = list(itertools.combinations(range(n), 3))
w = {B: float(np.linalg.det(R[list(B), :]) ** 2) for B in triples}
D0 = sum(w[B] * w[T] for B in triples for T in triples
         if set(B).isdisjoint(T))
lev = np.sum(R * R, axis=1)

# Volume-law one-coordinate inclusion identity.
inc = np.array([sum(w[B] for B in triples if i in B) for i in range(n)])

# Fair half-cut identity and cross singular-value bridge.
det_products = []
s3s = []
bridge_min_margin = 1e100
prod_identity_err = 0.0
for mask in range(1 << n):
    S = [i for i in range(n) if (mask >> i) & 1]
    T = [i for i in range(n) if not ((mask >> i) & 1)]
    RS = R[S, :] if S else np.zeros((0, 3))
    RT = R[T, :] if T else np.zeros((0, 3))
    G = RS.T @ RS
    H = RT.T @ RT
    dh = float(np.linalg.det(G) * np.linalg.det(H))
    if abs(dh) < 1e-14:
        dh = 0.0
    det_products.append(dh)
    C = A[np.ix_(S, T)] if S and T else np.zeros((len(S), len(T)))
    sv = np.linalg.svd(C, compute_uv=False)
    s3 = float(sv[2]) if len(sv) >= 3 else 0.0
    s3s.append(s3)
    delta3 = float(np.prod(sv[:3])) if len(sv) >= 3 else 0.0
    rhs = abs(np.linalg.det(Lam)) * math.sqrt(max(dh, 0.0))
    prod_identity_err = max(prod_identity_err, abs(delta3 - rhs))
    # min |lambda| = 1 in this check.
    bridge_min_margin = min(bridge_min_margin,
                            s3 - math.sqrt(max(dh, 0.0)))

print("QFORM_D0_HALFCUT_CHECK")
print("parseval_error", np.linalg.norm(R.T @ R - np.eye(3)))
print("spectrum", np.round(np.linalg.eigvalsh(A), 12).tolist())
print("zero_diag_max", np.max(np.abs(np.diag(A))))
print("sum_basis_weights", sum(w.values()))
print("inclusion_identity_max_error", np.max(np.abs(inc - lev)))
print("D0", D0)
print("halfcut_average", np.mean(det_products))
print("D0_over_64", D0 / 64.0)
print("halfcut_identity_error", abs(np.mean(det_products) - D0 / 64.0))
print("cross_product_identity_max_error", prod_identity_err)
print("cross_s3_bridge_min_margin", bridge_min_margin)
print("guaranteed_cross_s3", math.sqrt(D0) / 8.0)
print("max_cross_s3", max(s3s))
print("base_pair_abs", abs(A[0, 1]))
print("finite_ray_stability_bound_8eps3", 8 * (0.1 ** 3))
print("D0_le_8eps3", D0 <= 8 * (0.1 ** 3) + 1e-12)

assert np.linalg.norm(R.T @ R - np.eye(3)) < 1e-12
assert np.max(np.abs(np.diag(A))) < 1e-12
assert abs(sum(w.values()) - 1) < 1e-12
assert np.max(np.abs(inc - lev)) < 1e-12
assert abs(np.mean(det_products) - D0 / 64) < 1e-12
assert prod_identity_err < 1e-11
assert bridge_min_margin > -1e-11
assert D0 <= 8 * (0.1 ** 3) + 1e-12
assert abs(abs(A[0, 1]) - 0.9) < 1e-12
print("QFORM_D0_HALFCUT_CHECK_PASS")
