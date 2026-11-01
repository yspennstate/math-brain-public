"""Worker 036: fixed outside diagonal, two-row conditional Hessian checks.

Floating-point exploration only unless explicitly marked as exact arithmetic.
Run from research-session: python computations/036_two_row_slice.py
"""
import json
import numpy as np
from dpp_core import direction_derivatives, entropy_hessian, random_contraction


def h2_gradient(C):
    a, d = C[0, 0].real, C[1, 1].real
    z = C[0, 1]
    r = abs(z) ** 2
    x, y, zp, w = (1-a)*(1-d)-r, a*(1-d)+r, (1-a)*d+r, a*d-r
    L = np.log(y*zp/(x*w))
    ga = (1-d)*np.log(x/y)+d*np.log(zp/w)
    gd = (1-a)*np.log(x/zp)+a*np.log(y/w)
    return np.array([[ga, -L*z], [-L*np.conj(z), gd]])


def conditional(K, D):
    A, B, c = K[:2, :2], K[:2, 2:], K[2, 2].real
    E, V = D[:2, :2], D[:2, 2:]
    C0, C1 = A+B@B.conj().T/(1-c), A-B@B.conj().T/c
    W = V@B.conj().T+B@V.conj().T
    U0, U1 = E+W/(1-c), E-W/c
    q0 = direction_derivatives(C0, U0)
    q1 = direction_derivatives(C1, U1)
    G = h2_gradient(C0)-h2_gradient(C1)
    correction = float(2*np.trace(G@V@V.conj().T).real)
    return {
        "conditional_Hessian": (1-c)*q0["H2"]+c*q1["H2"],
        "correction": correction,
        "total": (1-c)*q0["H2"]+c*q1["H2"]+correction,
        "gradient_difference_eigenvalues": np.linalg.eigvalsh(G).tolist(),
    }


def main():
    rng = np.random.default_rng(20260914036)
    best = None
    max_error = 0.
    largest_slice_eigenvalue = -np.inf
    for iteration in range(1200):
        K = random_contraction(rng, 3, complex_case=False)
        A, B, c = K[:2, :2], K[:2, 2:], K[2, 2]
        G = h2_gradient(A+B@B.T/(1-c))-h2_gradient(A-B@B.T/c)
        vals, vecs = np.linalg.eigh(G)
        if best is None or vals[-1] > best["lambda_max"]:
            best = {"lambda_max": float(vals[-1]), "K": K.tolist(),
                    "gradient_difference": G.tolist(), "witness": vecs[:, -1].tolist()}
        if iteration < 60:
            D = rng.normal(size=(3, 3))
            D = (D+D.T)/2
            D[2, 2] = 0
            predicted = conditional(K, D)
            direct = direction_derivatives(K, D)
            max_error = max(max_error, abs(predicted["total"]-direct["H2"]))
            Hess, basis = entropy_hessian(K, complex_case=True)
            keep = np.array([i for i, E in enumerate(basis) if abs(E[2, 2]) < 1e-12])
            slice_hessian = Hess[np.ix_(keep, keep)]
            largest_slice_eigenvalue = max(largest_slice_eigenvalue, np.linalg.eigvalsh(slice_hessian)[-1])
    result = {
        "seed": 20260914036,
        "gradient_search_count": 1200,
        "conditional_identity_count": 60,
        "maximum_conditional_identity_error": max_error,
        "largest_sampled_slice_hessian_eigenvalue": float(largest_slice_eigenvalue),
        "best_gradient_obstruction": best,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
