#!/usr/bin/env python3
"""Exact certificates for C048. Requires SymPy; no numerical sign decisions."""
from __future__ import annotations

import itertools
import json
from functools import lru_cache
from pathlib import Path

import sympy as s

Q = s.Rational
OUT = Path(__file__).resolve().parent


def bits(mask, n):
    return [i for i in range(n) if mask >> i & 1]


def real(x):
    y = s.expand_complex(x).expand()
    assert s.im(y) == 0
    return s.re(y)


def abs2(x):
    return real(x * s.conjugate(x))


def mat_json(M):
    return [[str(M[i, j]) for j in range(M.cols)] for i in range(M.rows)]


def cauchy(roots, scales):
    # x_i=roots_i^2, ell_i=scales_i^2: all entries are rational.
    n = len(roots)
    L = s.Matrix(n, n, lambda i, j:
                 2 * scales[i] * scales[j] * roots[i] * roots[j]
                 / (roots[i] ** 2 + roots[j] ** 2))
    K = L * (s.eye(n) + L).inv()
    return L, K


def ldlt_pivots(M):
    n = M.rows
    work = M.copy()
    pivots = []
    for i in range(n):
        d = real(work[i, i])
        assert d > 0
        pivots.append(d)
        for j in range(i + 1, n):
            for k in range(i + 1, n):
                work[j, k] -= work[j, i] * work[i, k] / d
    return pivots


def cauchy_atoms(L, roots, scales):
    n = L.rows
    normalizer = (s.eye(n) + L).det()
    atoms = []
    for mask in range(1 << n):
        ix = bits(mask, n)
        d = s.prod(scales[i] ** 2 for i in ix)
        for i, j in itertools.combinations(ix, 2):
            d *= ((roots[i] ** 2 - roots[j] ** 2)
                  / (roots[i] ** 2 + roots[j] ** 2)) ** 2
        assert d == L.extract(ix, ix).det()
        atoms.append(d / normalizer)
    assert sum(atoms) == 1
    assert all(p > 0 for p in atoms)
    return atoms


def covariance(K, atoms):
    n = K.rows
    mu = s.Matrix([sum(atoms[m] for m in range(1 << n) if m >> i & 1)
                   for i in range(n)])
    assert mu == K.diagonal().T
    Sig = s.Matrix(n, n, lambda i, j:
                   sum(atoms[m] for m in range(1 << n)
                       if (m >> i & 1) and (m >> j & 1)) - mu[i] * mu[j])
    gram = K.multiply_elementwise(s.conjugate(K))
    comp = s.eye(n) - K
    gramc = comp.multiply_elementwise(s.conjugate(comp))
    assert Sig == s.diag(*mu) - gram
    assert s.eye(n) - 2 * Sig == gram + gramc
    # These exact PSD checks are auxiliary; the analytic proof uses Schur products.
    ldlt_pivots(Sig)
    ldlt_pivots(s.eye(n) / 2 - Sig)
    return mu, Sig, gram + gramc


def rational_round_interval(lo, hi, digits=14):
    scale = 10 ** digits
    return Q(s.floor(lo * scale), scale), Q(s.ceiling(hi * scale), scale)


@lru_cache(None)
def log_interval(x):
    """Outward rational log enclosure, using an exact positive atanh tail."""
    x = Q(x)
    assert x > 0
    if x == 1:
        return Q(0), Q(0)
    if x < 1:
        lo, hi = log_interval(1 / x)
        return -hi, -lo
    k = 0
    y = x
    while y >= 2:
        y /= 2
        k += 1

    def unit_log(z):
        h = (z - 1) / (z + 1)
        N = 18
        lo = 2 * sum(h ** (2 * j + 1) / (2 * j + 1) for j in range(N))
        tail = 2 * h ** (2 * N + 1) / ((2 * N + 1) * (1 - h ** 2))
        return lo, lo + tail

    lo, hi = unit_log(y)
    a, b = unit_log(Q(2))
    return rational_round_interval(lo + k * a, hi + k * b)


def scale_interval(c, pair):
    x, y = pair
    return (c * x, c * y) if c >= 0 else (c * y, c * x)


def add_intervals(pairs):
    return tuple(sum(x[k] for x in pairs) for k in [0, 1])


def interval_json(pair):
    return {"lower": str(pair[0]), "upper": str(pair[1]),
            "display_lower": float(pair[0]), "display_upper": float(pair[1])}


def atom_jets(K, A, atoms):
    n = K.rows
    q, r = [], []
    for mask in range(1 << n):
        M = s.Matrix(n, n, lambda i, j:
                     K[i, j] if mask >> j & 1 else int(i == j) - K[i, j])
        D = s.Matrix(n, n, lambda i, j:
                     A[i, j] if mask >> j & 1 else -A[i, j])
        p = M.det()
        assert p == atoms[mask]
        R = M.inv() * D
        tr = real(s.trace(R))
        q.append(p * tr)
        r.append(p * real(tr ** 2 - s.trace(R * R)))
    assert sum(q) == sum(r) == 0
    for i in range(n):
        assert sum(q[m] for m in range(1 << n) if m >> i & 1) == A[i, i]
        assert sum(r[m] for m in range(1 << n) if m >> i & 1) == 0
    for i, j in itertools.combinations(range(n), 2):
        total = sum(r[m] for m in range(1 << n) if m >> i & 1 and m >> j & 1)
        assert total == 2 * (A[i, i] * A[j, j] - abs2(A[i, j]))
    return q, r


def verify_jets(name, roots, scales):
    n = len(roots)
    L, K = cauchy(roots, scales)
    A = s.zeros(n)
    for i in range(n):
        A[i, i] = Q((-1) ** i * (i + 1), 7)
        for j in range(i + 1, n):
            A[i, j] = Q(i + j + 1, 13) + s.I * Q(j - i, 17)
            A[j, i] = s.conjugate(A[i, j])
    atoms = cauchy_atoms(L, roots, scales)
    mu, Sig, Bsum = covariance(K, atoms)
    q, r = atom_jets(K, A, atoms)
    a = A.diagonal().T
    aa = real((a.T * a)[0])
    FI = sum(q[m] ** 2 / atoms[m] for m in range(1 << n))
    residual = 0
    for mask in range(1 << n):
        centered = sum(a[i] * (int(mask >> i & 1) - mu[i]) for i in range(n))
        residual += atoms[mask] * (q[mask] / atoms[mask] - 2 * centered) ** 2
    gramterm = 2 * real((a.T * Bsum * a)[0])
    assert residual >= 0 and gramterm > 0
    assert FI - 2 * aa == residual + gramterm
    assert FI >= 2 * aa

    pairs = list(itertools.combinations(range(n), 2))
    logs = {}
    for i, j in pairs:
        ratio = (roots[i] ** 2 + roots[j] ** 2) / abs(roots[i] ** 2 - roots[j] ** 2)
        logs[i, j] = scale_interval(Q(2), log_interval(ratio))
    H_atoms = add_intervals([(-FI, -FI)] +
                            [scale_interval(-r[m], log_interval(atoms[m]))
                             for m in range(1 << n)])
    H_pairs = add_intervals([(-FI, -FI)] +
                            [scale_interval(2 * (a[i] * a[j] - abs2(A[i, j])), logs[i, j])
                             for i, j in pairs])
    assert max(H_atoms[0], H_pairs[0]) <= min(H_atoms[1], H_pairs[1])
    assert H_atoms[1] < 0

    Rmin = min(roots[i + 1] ** 2 / roots[i] ** 2 for i in range(n - 1))
    alpha = 1 - 4 * Rmin / (Rmin - 1) ** 2
    assert alpha > 0
    # -H'' - alpha FI - 2 sum c_ij |A_ij|^2
    surplus = add_intervals([((1 - alpha) * FI, (1 - alpha) * FI)] +
                            [scale_interval(-2 * a[i] * a[j], logs[i, j])
                             for i, j in pairs])
    assert surplus[0] > 0
    return {
        "name": name, "n": n, "roots": list(map(str, roots)),
        "external_scales_squared": [str(x ** 2) for x in scales],
        "L": mat_json(L), "K": mat_json(K), "A": mat_json(A),
        "atoms": [{"mask": m, "p": str(atoms[m]), "q": str(q[m]), "r": str(r[m])}
                  for m in range(1 << n)],
        "FI": str(FI), "diagonal_norm_squared": str(aa),
        "FI_identity_residual_square": str(residual),
        "FI_identity_gram_term": str(gramterm),
        "entropy_curvature_atom_interval": interval_json(H_atoms),
        "entropy_curvature_pair_interval": interval_json(H_pairs),
        "Fisher_surplus_coefficient": str(alpha),
        "curvature_certificate_surplus_interval": interval_json(surplus),
        "all_exact_checks": True,
    }


def separated_example():
    n = 8
    root = Q(5, 2)
    R = root ** 2
    roots = [root ** i for i in range(n)]
    scales = [Q(1)] * n
    L, K = cauchy(roots, scales)
    atoms = cauchy_atoms(L, roots, scales)
    mu, Sig, Bsum = covariance(K, atoms)
    pivots = {"L": list(map(str, ldlt_pivots(L))),
              "K": list(map(str, ldlt_pivots(K))),
              "I-K": list(map(str, ldlt_pivots(s.eye(n) - K)))}
    pair_data = []
    for i, j in itertools.combinations(range(n), 2):
        w = K[i, i] * K[j, j] - K[i, j] ** 2
        x = 1 - K[i, i] - K[j, j] + w
        y, z = K[i, i] - w, K[j, j] - w
        assert min(x, y, z, w) > 0
        T2 = (y + z) ** 2 / (4 * x * w)
        assert 1 <= T2 < Q(49, 25)
        pair_data.append({"i": i, "j": j, "x": str(x), "y": str(y),
                          "z": str(z), "w": str(w), "T_squared": str(T2),
                          "strict_upper_bound": "49/25"})
    old_lower = Q(5, 24) * (4 * sum((n - d) / R ** d for d in range(1, n))
                           - Q(112) / (R ** 7 - 1))
    assert old_lower == Q(3451145142079341346, 3193097398681640625)
    assert old_lower > 1
    new_r = 8 * R / (R - 1) ** 2
    assert new_r == Q(800, 441)
    assert 1 - new_r / 2 == Q(41, 441)
    return {"n": n, "R": str(R), "L": mat_json(L), "K": mat_json(K),
            "external_fields": ["1"] * n, "positive_LDL_pivots": pivots,
            "atoms": [str(p) for p in atoms], "pair_marginals": pair_data,
            "old_full_budget_strict_lower_bound": str(old_lower),
            "old_full_budget_lower_bound_display": float(old_lower),
            "new_spectral_upper_bound": str(new_r),
            "new_Fisher_surplus": "41/441", "all_exact_checks": True}


def main():
    results = {
        "method": "exact rational determinant jets, Schur-product coefficient identity, and rational log bounds",
        "stable_polynomial_source": "https://arxiv.org/pdf/1702.02937 (Corollary 2.10)",
        "separated_eight_site_example": separated_example(),
        "affine_kernel_jet_examples": [
            verify_jets("four_site_unequal_fields", [Q(5, 2) ** i for i in range(4)],
                        [Q(1, 2), Q(1), Q(3, 2), Q(2)]),
            verify_jets("five_site_irregular_spacing", list(map(Q, [1, 3, 10, 30, 100])),
                        [Q(1, 2), Q(1), Q(2), Q(3), Q(4)]),
        ],
        "status": "PASS",
    }
    (OUT / "certificate.json").write_text(json.dumps(results, indent=2) + "\n")
    print("PASS: 304 exact Cauchy minors; 48 full affine-kernel atom jets; covariance and Fisher identities; 28 exact marginal-pair bounds; old-budget separation; two certified Hermitian curvatures.")
    for item in results["affine_kernel_jet_examples"]:
        print(item["name"], item["entropy_curvature_atom_interval"]["display_upper"])
    print("old budget >", results["separated_eight_site_example"]["old_full_budget_lower_bound_display"])


if __name__ == "__main__":
    main()
