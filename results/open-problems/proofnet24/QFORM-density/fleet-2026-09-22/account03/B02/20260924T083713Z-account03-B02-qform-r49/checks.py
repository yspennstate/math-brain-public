#!/usr/bin/env python3
import itertools, json, math
import numpy as np


def e2(G):
    t = float(np.trace(G))
    return 0.5 * (t*t - float(np.trace(G @ G)))


def k2_formula(B):
    G = B @ B.T
    return G @ G - np.trace(G) * G + e2(G) * np.eye(G.shape[0])


def k2_enumerate(B):
    m, q = B.shape
    S = np.zeros((m, m))
    for a, b in itertools.combinations(range(q), 2):
        U = B[:, [a, b]]
        for I in itertools.combinations(range(m), 3):
            C = U[list(I), :]
            wloc = np.cross(C[:, 0], C[:, 1])
            w = np.zeros(m)
            w[list(I)] = wloc
            S += np.outer(w, w)
    return S


def main():
    rng = np.random.default_rng(20260924)
    max_k2_rel = 0.0
    min_dom_eig = float('inf')
    dom_violations = 0
    for _ in range(500):
        m = int(rng.integers(3, 8))
        q = int(rng.integers(2, 7))
        B = rng.normal(size=(m, q))
        S = k2_enumerate(B)
        K = k2_formula(B)
        rel = np.linalg.norm(S-K) / (1.0 + np.linalg.norm(K))
        max_k2_rel = max(max_k2_rel, float(rel))

        G = B @ B.T
        vals, U = np.linalg.eigh(G)
        idx = np.argsort(vals)[::-1]
        vals, U = vals[idx], U[:, idx]
        x1, x2 = max(float(vals[0]), 0.0), max(float(vals[1]), 0.0)
        Ptail = np.eye(m) - U[:, :2] @ U[:, :2].T
        E = 0.5*((K-x1*x2*Ptail)+(K-x1*x2*Ptail).T)
        mineig = float(np.min(np.linalg.eigvalsh(E)))
        min_dom_eig = min(min_dom_eig, mineig)
        if mineig < -1e-8:
            dom_violations += 1

    rng = np.random.default_rng(2026092402)
    max_carrier_rel = 0.0
    min_exterior_ratio = float('inf')
    carrier_violations = 0
    for _ in range(2000):
        p = int(rng.integers(2, 8))
        q = int(rng.integers(2, 8))
        M = rng.normal(size=(p, q))
        U, s, Vt = np.linalg.svd(M, full_matrices=False)
        if len(s) < 2 or s[1] < 1e-10:
            continue
        U2 = U[:, :2]
        V2 = Vt[:2, :].T
        Sigma = np.diag(s[:2])
        c = rng.normal(size=p)
        r = rng.normal(size=q)
        a = float(rng.normal())
        if abs(a) < 0.1:
            a += 1.0 if a >= 0 else -1.0
        B = M - np.outer(c, r)/a
        pp = U2.T @ c
        qq = V2.T @ r
        tau = float(qq @ np.linalg.solve(Sigma, pp))
        lhs = float(np.linalg.det(U2.T @ B @ V2))
        rhs = float(np.prod(s[:2]) * (1.0-tau/a))
        rel = abs(lhs-rhs)/(1.0+abs(rhs))
        max_carrier_rel = max(max_carrier_rel, rel)
        sb = np.linalg.svd(B, compute_uv=False)
        ext = float(sb[0]*sb[1])
        ratio = ext/(abs(lhs)+1e-300)
        min_exterior_ratio = min(min_exterior_ratio, ratio)
        if ext + 1e-9 < abs(lhs):
            carrier_violations += 1

    output = {
        "seed_k2": 20260924,
        "k2_trials": 500,
        "max_relative_k2_identity_error": max_k2_rel,
        "minimum_eigenvalue_of_K2_minus_x1x2_Ptail": min_dom_eig,
        "dominance_violations_below_minus_1e-8": dom_violations,
        "seed_carrier": 2026092402,
        "carrier_trials": 2000,
        "max_relative_carrier_determinant_error": max_carrier_rel,
        "minimum_observed_top2_product_over_abs_compression_det": min_exterior_ratio,
        "carrier_exterior_violations": carrier_violations,
        "constants": {
            "rank2_half_riesz_constant_4sqrt2e": 4*math.sqrt(2*math.e),
            "live_punctured_top2_product_floor_s1s2": math.sqrt(247/2304),
            "live_exact_rank2_pivot_bound_a_ge_1over223_gamma_ge_half": 4*math.sqrt(2*math.e)*math.sqrt(223)*(math.sqrt(247/2304)/2)**(-0.25),
            "partner_rank3_hybrid_constant": 2*(2**(2/3))*(3**0.25)*math.exp(0.75)
        }
    }
    print(json.dumps(output, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
