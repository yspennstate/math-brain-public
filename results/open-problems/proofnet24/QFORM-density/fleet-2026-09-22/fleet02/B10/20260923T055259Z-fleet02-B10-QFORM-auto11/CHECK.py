import math
import numpy as np


def build(m):
    assert m % 2 == 0 and m >= 64
    rho = 1/128
    c = 127/128
    rho_m = 1/256
    ell = 1/256
    eta = 15/16
    nu = 1/16
    eps = 1/m
    s = math.sqrt(1-eps**2)
    Lam = np.array([[-eps, 0.0, s], [0.0, 1.0, 0.0], [s, 0.0, eps]])

    rows = [math.sqrt(c)*np.array([1.0, 0.0, 0.0])]
    a = math.sqrt(rho_m/m)
    b = math.sqrt(eta/m)
    signs = np.r_[np.ones(m//2), -np.ones(m//2)]
    rows.extend(np.array([a, sig*b, 0.0]) for sig in signs)

    d = math.sqrt(ell/m)
    rows.extend(np.array([d, 0.0, 0.0]) for _ in range(m))

    q = math.sqrt(nu/m)
    rows.extend(np.array([0.0, q, 0.0]) for _ in range(m))

    r = 1/math.sqrt(m)
    rows.extend(np.array([0.0, 0.0, r]) for _ in range(m))

    R = np.vstack(rows)
    A = R @ Lam @ R.T
    return R, Lam, A


def check(m):
    R, Lam, A = build(m)
    c = 127/128
    eta = 15/16
    rho_m = 1/256

    diag_max = float(np.max(np.abs(np.diag(A))))
    d = np.diag(A)
    pair_det = np.abs(d[:, None]*d[None, :] - A*A)
    np.fill_diagonal(pair_det, 0.0)
    pair_max = float(np.max(pair_det))

    # Exact analytical bounds from Hadamard and |det Lambda|=1.
    triple_bound = max(c/m**2, 1/m**3)
    hub_mixed_u_triple = c*eta/m**2

    print({
        "m": m,
        "gram_inf_error": float(np.linalg.norm(R.T@R-np.eye(3), ord=np.inf)),
        "eigenvalues_Lambda": np.linalg.eigvalsh(Lam).tolist(),
        "diag_max": diag_max,
        "diag_bound_1_over_m": 1/m,
        "pair_det_max": pair_max,
        "pair_bound_2_over_m": 2/m,
        "hub_mixed_u_triple": hub_mixed_u_triple,
        "triple_bound": triple_bound,
        "hub_packet_exact_formula": c,
        "slope_product_exact_formula": eta/rho_m,
    })


for m in (64, 128, 256):
    check(m)
