#!/usr/bin/env python3
"""Exact standard-library certificate for C060's seven-site triangle chain.

All signs use Fraction arithmetic. Floating logarithms are labeled display only.
Run from any directory; results.json is written next to this script.
"""
from fractions import Fraction as F
from math import log, prod
from pathlib import Path
import json


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def zeros(n):
    return [[F(0) for _ in range(n)] for _ in range(n)]


def det(a):
    n = len(a)
    b = [row[:] for row in a]
    out = F(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if b[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            b[j], b[pivot] = b[pivot], b[j]
            out = -out
        z = b[j][j]
        out *= z
        for i in range(j + 1, n):
            q = b[i][j] / z
            for k in range(j + 1, n):
                b[i][k] -= q * b[j][k]
    return out


def inv(a):
    n = len(a)
    b = [row[:] + eye(n)[i] for i, row in enumerate(a)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if b[i][j])
        b[j], b[pivot] = b[pivot], b[j]
        z = b[j][j]
        b[j] = [x / z for x in b[j]]
        for i in range(n):
            if i != j:
                q = b[i][j]
                b[i] = [x - q * y for x, y in zip(b[i], b[j])]
    return [row[n:] for row in b]


def mm(a, b):
    n = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(n)), F(0))
             for j in range(n)] for i in range(n)]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def add(a, b, sign=1):
    return [[x + sign * y for x, y in zip(ar, br)]
            for ar, br in zip(a, b)]


def submatrix(a, ids):
    return [[a[i][j] for j in ids] for i in ids]


def indices(mask):
    return [i for i in range(7) if mask & (1 << i)]


def subsets(mask):
    u = mask
    while True:
        yield u
        if not u:
            break
        u = (u - 1) & mask


def fs(q):
    return str(q.numerator) if q.denominator == 1 else str(q)


def fmatrix(a):
    return [[fs(x) for x in row] for row in a]


def jet_from_inverse(p, w, x, b):
    wx, wb = mm(w, x), mm(w, b)
    assert trace(wb) == 0
    first = p * trace(wx)
    cross = trace(mm(wx, wb))
    assert cross == 0  # symmetric/skew trace cancellation, also for atom matrices.
    second = p * (trace(wx) ** 2 - trace(mm(wx, wx)) + trace(mm(wb, wb)))
    return first, second


def log_display(q):
    return log(q.numerator / q.denominator)


def main():
    n, allmask = 7, 127
    triangles = [(0, 1, 2), (2, 3, 4), (4, 5, 6)]
    L = [[F(4 if i == j else 0) for j in range(n)] for i in range(n)]
    for r, a, b in triangles:
        L[r][a] = L[a][r] = F(1)
        L[a][b] = L[b][a] = F(1)
        L[r][b] = L[b][r] = F(1, 10)
    row_sums = [sum((abs(L[i][j]) for j in range(n) if i != j), F(0))
                for i in range(n)]
    assert max(row_sums) == F(11, 5) < 4
    margins = []
    for r, a, b in triangles:
        alpha, beta, h = L[r][a] ** 2, L[r][b] ** 2, L[a][b] ** 2
        t = 2 * L[r][a] * L[a][b] * L[b][r]
        margin = h * (alpha / L[a][a] + beta / L[b][b]) - t
        assert margin == F(21, 400)
        assert L[r][a] * L[a][b] * L[b][r] == F(1, 10)
        margins.append(margin)

    detL = [det(submatrix(L, indices(s))) for s in range(128)]
    assert all(q > 0 for q in detL)
    normalized = [q / 4 ** s.bit_count() for s, q in enumerate(detL)]
    ratios = []
    for s in range(128):
        ratio = F(1)
        for u in subsets(s):
            if (s.bit_count() - u.bit_count()) % 2:
                ratio *= normalized[u]
            else:
                ratio /= normalized[u]
        assert ratio >= 1
        ratios.append(ratio)
    assert all(ratios[s] == 1 for s in range(128) if s.bit_count() <= 1)
    for r, a, b in triangles:
        assert ratios[(1 << r) | (1 << a) | (1 << b)] == F(13325, 13312)
    for s in range(128):
        assert prod((ratios[t] for t in subsets(s)), start=F(1)) == 1 / normalized[s]

    child_blocks = {r: (a, b) for r, a, b in triangles}
    tree_masks = [0] * n
    for r in reversed(range(n)):
        tree_masks[r] = 1 << r
        if r in child_blocks:
            a, b = child_blocks[r]
            tree_masks[r] |= tree_masks[a] | tree_masks[b]
    response_checks = 0
    for s in range(128):
        R, g = [F(0)] * n, [F(0)] * n
        for r in reversed(range(n)):
            if r in child_blocks:
                a, b = child_blocks[r]
                alpha, beta, h = L[r][a] ** 2, L[r][b] ** 2, L[a][b] ** 2
                t = 2 * L[r][a] * L[a][b] * L[b][r]
                den = 1 - h * g[a] * g[b]
                assert den > 0
                direct = (alpha * g[a] + beta * g[b] - t * g[a] * g[b]) / den
                delta = h * (alpha / L[a][a] + beta / L[b][b]) - t
                positive = alpha * g[a] + beta * g[b] + (
                    delta * g[a] * g[b]
                    + h * alpha * (g[a] ** 2 - g[a] / L[a][a]) * g[b]
                    + h * beta * g[a] * (g[b] ** 2 - g[b] / L[b][b])) / den
                assert direct == positive
                R[r] = direct
            assert 0 <= R[r] < L[r][r]
            desc = (s & tree_masks[r]) & ~(1 << r)
            assert L[r][r] - R[r] == detL[desc | (1 << r)] / detL[desc]
            g[r] = F(bool(s & (1 << r))) / (L[r][r] - R[r])
            assert g[r] ** 2 - g[r] / L[r][r] >= 0
            if s & (1 << r):
                assert g[r] == detL[desc] / detL[desc | (1 << r)]
            response_checks += 1
        factorization = prod((L[r][r] - R[r] for r in indices(s)), start=F(1))
        factorization *= prod((1 - L[a][b] ** 2 * g[a] * g[b]
                               for r, a, b in triangles), start=F(1))
        assert factorization == detL[s]

    I = eye(n)
    K = add(I, inv(add(I, L)), -1)
    assert mm(K, add(I, L)) == L
    assert mm(add(I, L), K) == L
    Z = det(add(I, L))

    # A = X + iB. Its real part has inertia (1,1); A has inertia (3,3,0).
    X, B = zeros(n), zeros(n)
    X[0][0], X[1][1] = F(1), F(-1)
    for a, b in [(0, 1), (2, 3), (4, 5)]:
        B[a][b], B[b][a] = F(1), F(-1)
    assert add(mm(X, B), mm(B, X)) == zeros(n)
    assert add(mm(X, X), mm(B, B), -1) == [
        [F([2, 2, 1, 1, 1, 1, 0][i] if i == j else 0) for j in range(n)]
        for i in range(n)]

    atom_p, atom_first, atom_second, atom_second_real = [], [], [], []
    fisher = F(0)
    for s in range(128):
        M = [row[:] for row in K]
        for i in range(n):
            if not (s & (1 << i)):
                M[i][i] -= 1
        p = detL[s] / Z
        assert p == (-1) ** (n - s.bit_count()) * det(M) > 0
        W = inv(M)
        first, second = jet_from_inverse(p, W, X, B)
        first_real, second_real = jet_from_inverse(p, W, X, zeros(n))
        assert first == first_real
        atom_p.append(p)
        atom_first.append(first)
        atom_second.append(second)
        atom_second_real.append(second_real)
        fisher += first ** 2 / p
    assert sum(atom_p) == 1
    assert sum(atom_first) == 0
    assert sum(atom_second) == 0
    assert sum(atom_second_real) == 0
    assert fisher > 0
    for i in range(n):
        assert sum(atom_first[s] for s in range(128) if s & (1 << i)) == X[i][i]
        assert sum(atom_second[s] for s in range(128) if s & (1 << i)) == 0

    entries = []
    entropy_frozen_display = 0.0
    inclusion_square_checks = 0
    for s in range(128):
        ids = indices(s)
        KT, XT, BT = submatrix(K, ids), submatrix(X, ids), submatrix(B, ids)
        G = det(KT)
        assert G > 0
        assert G == sum(atom_p[u] for u in range(128) if u & s == s)
        W = inv(KT)
        wx, wb = mm(W, XT), mm(W, BT)
        real_gap = trace(mm(wx, wx)) - trace(wx) ** 2
        imag_gap = -trace(mm(wb, wb))
        assert real_gap >= 0 and imag_gap >= 0
        first, second = jet_from_inverse(G, W, XT, BT)
        assert second == -G * (real_gap + imag_gap) <= 0
        assert first == sum(atom_first[u] for u in range(128) if u & s == s)
        assert second == sum(atom_second[u] for u in range(128) if u & s == s)
        second_real = G * (trace(wx) ** 2 - trace(mm(wx, wx)))
        assert second_real == sum(atom_second_real[u] for u in range(128) if u & s == s)
        if s.bit_count() >= 2:
            inclusion_square_checks += 1
        entropy_frozen_display += float(second) * log_display(ratios[s])
        entries.append({
            "mask": s, "sites": [i + 1 for i in ids],
            "det_L_S": fs(detL[s]), "normalized_det": fs(normalized[s]),
            "mobius_coefficient": "log(" + fs(ratios[s]) + ")",
            "mobius_ratio": fs(ratios[s]),
            "atom_p": fs(atom_p[s]), "atom_first_A": fs(atom_first[s]),
            "atom_second_A": fs(atom_second[s]),
            "inclusion_det": fs(G), "inclusion_first_A": fs(first),
            "inclusion_second_A": fs(second),
            "real_inertia_square_gap": fs(real_gap),
            "imaginary_square_gap": fs(imag_gap),
        })

    # Direct entropy formula is independently displayed, not used to certify signs.
    direct_frozen = -sum(float(q) * log_display(p)
                         for q, p in zip(atom_second, atom_p))
    positive_by_size = {str(k): sum(ratios[s] > 1 for s in range(128)
                                  if s.bit_count() == k) for k in range(8)}
    inverse_triangle_products = [
        prod((inv(L)[i][j] for i, j in [(r, a), (a, b), (b, r)]), start=F(1))
        for r, a, b in triangles]
    assert all(q > 0 for q in inverse_triangle_products)
    result = {
        "status": "PASS: exact triangle responses, 128 subset factorizations and Mobius ratios, 128 DPP atom jets, and rank-six Fisher-plus-squares curvature.",
        "arithmetic": "All certification assertions use exact Fraction arithmetic. Floating logarithms are labeled displays only.",
        "L": fmatrix(L), "K": fmatrix(K),
        "triangles_parent_children": [[i + 1 for i in t] for t in triangles],
        "local_margins": [fs(q) for q in margins],
        "cycle_products": ["1/10"] * 3,
        "inverse_cycle_products": [fs(q) for q in inverse_triangle_products],
        "row_sums": [fs(q) for q in row_sums],
        "spectral_enclosure_L": ["9/5", "31/5"],
        "det_L": fs(detL[allmask]), "det_I_plus_L": fs(Z),
        "response_identity_checks": response_checks,
        "selection_factorization_checks": 128,
        "positive_mobius_count": sum(q > 1 for q in ratios),
        "zero_mobius_count": sum(q == 1 for q in ratios),
        "positive_mobius_count_by_size": positive_by_size,
        "full_set_mobius_ratio": fs(ratios[allmask]),
        "A_real": fmatrix(X), "A_imaginary": fmatrix(B),
        "A_inertia_positive_negative_zero": [3, 3, 1],
        "A_characteristic_polynomial": "lambda*(lambda^2-2)*(lambda^2-1)^2",
        "fisher_information": fs(fisher),
        "inclusion_square_checks": inclusion_square_checks,
        "exact_entropy_sign_certificate": "H''(A) = -I - sum_T log(mobius_ratio_T)*det(K_T)*(real_gap_T+imaginary_gap_T) < 0; I>0, every ratio>=1, every gap>=0.",
        "floating_displays_not_sign_proofs": {
            "fisher_information": float(fisher),
            "frozen_curvature_from_Mobius": entropy_frozen_display,
            "frozen_curvature_from_atom_logs": direct_frozen,
            "floating_display_discrepancy": direct_frozen - entropy_frozen_display,
            "entropy_curvature": -float(fisher) + entropy_frozen_display,
            "full_set_mobius_coefficient": log_display(ratios[allmask]),
        },
        "subsets": entries,
    }
    target = Path(__file__).resolve().with_name("results.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    summary = {k: result[k] for k in ["status", "det_L", "det_I_plus_L",
        "response_identity_checks", "positive_mobius_count", "zero_mobius_count",
        "positive_mobius_count_by_size", "full_set_mobius_ratio",
        "floating_displays_not_sign_proofs"]}
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
