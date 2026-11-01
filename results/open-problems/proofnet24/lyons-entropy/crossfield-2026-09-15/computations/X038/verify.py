"""Exact finite checks for the unicyclic phase-damping theorem; no search."""
from itertools import combinations
from pathlib import Path
import json
import sympy as s

Q, I = s.Rational, s.I


def clean(v):
    return s.cancel(s.expand(v))


def det(M):
    return clean(M.det(method="domain-ge")) if M.rows else s.Integer(1)


def sub(M, vertices):
    return M.extract(vertices, vertices)


def marginal(atoms, vertices):
    ans = [s.Integer(0)] * (1 << len(vertices))
    for mask, p in enumerate(atoms):
        t = sum(((mask >> v) & 1) << j for j, v in enumerate(vertices))
        ans[t] += p
    return [clean(v) for v in ans]


def restriction(mask, vertices):
    return sum(((mask >> v) & 1) << j for j, v in enumerate(vertices))


def run_case(name, m, a, phase, reservoir=False):
    n = m + (2 if reservoir else 0)
    K = s.eye(n) / 2
    edges = [(j, (j + 1) % m) for j in range(m)]
    for j, (u, v) in enumerate(edges):
        z = a * (phase if j == m - 1 else 1)
        K[u, v], K[v, u] = z, s.conjugate(z)
    if reservoir:
        edges += [(0, m), (m, m + 1)]
        for (u, v), z in zip(edges[m:], [Q(1, 50), Q(1, 5)]):
            K[u, v] = K[v, u] = z
    d = [Q(v) for v in [0, 1, -1, 2, -2, 3, 2, -1][:n]]
    D = s.diag(*d)
    A = I * (D * K - K * D)
    x2 = {(u, v): (d[u] - d[v]) ** 2 for u, v in edges}
    loop = clean(s.prod(K[j, (j + 1) % m] for j in range(m)))
    q = clean(s.re(loop))
    qhat = (-1) ** (m - 1) * abs(q)
    Kh = K.copy()
    if qhat != q:
        Kh[m - 1, 0] = -Kh[m - 1, 0]
        Kh[0, m - 1] = -Kh[0, m - 1]
    assert clean(s.re(s.prod(Kh[j, (j + 1) % m] for j in range(m)))) == qhat
    for M in [K, s.eye(n) - K, Kh, s.eye(n) - Kh]:
        assert all(det(M[:j, :j]) > 0 for j in range(1, n + 1))
    probs, accelerations = [], []
    for mask in range(1 << n):
        holes = [1 - ((mask >> j) & 1) for j in range(n)]
        M = K - s.diag(*holes)
        p = (-1) ** sum(holes) * det(M)
        R = M.inv(method="DM") * A
        assert clean(s.trace(R)) == 0
        ddp = clean(-p * s.trace(R * R))
        assert p > 0
        probs.append(p)
        accelerations.append(ddp)
    assert sum(probs) == 1 and clean(sum(accelerations)) == 0
    outside = list(range(m, n))
    pu = marginal(probs, outside)
    du = det(sub(K, outside))
    edge_marginals, edge_dets = {}, {}
    ratio_count = 0
    for e in edges:
        rr = [j for j in range(n) if j not in e]
        pr = marginal(probs, rr)
        edge_marginals[e] = (rr, pr)
        edge_dets[e] = det(sub(K, rr))
        if e in edges[:m]:
            for mask, p in enumerate(pr):
                fullmask = sum(((mask >> j) & 1) << v for j, v in enumerate(rr))
                assert clean(p * du - pu[restriction(fullmask, outside)] * edge_dets[e]) >= 0
                ratio_count += 1
    # Equality of coefficient vectors proves the frozen identity for EVERY f.
    cyc_x2 = sum(x2[e] for e in edges[:m])
    for mask, ddp in enumerate(accelerations):
        spin = [2 * ((mask >> j) & 1) - 1 for j in range(n)]
        rhs = s.Integer(0)
        for e in edges:
            u, v = e
            rr, pr = edge_marginals[e]
            rhs -= 2 * clean(K[u, v] * K[v, u]) * x2[e] * spin[u] * spin[v] * pr[restriction(mask, rr)]
        rhs += 2 * (-1) ** (m - 1) * q * cyc_x2 * s.prod(spin[:m]) * pu[restriction(mask, outside)]
        assert clean(ddp - rhs) == 0
    # Extend cycle potential constantly through the attached reservoir.
    dh = d[:m] + ([d[0], d[0]] if reservoir else [])
    Dh = s.diag(*dh)
    Ah = I * (Dh * Kh - Kh * Dh)
    Rh = Kh.inv(method="DM") * Ah
    determinant_square = clean(det(Kh) * s.trace(Rh * Rh))
    signed_laplacian = clean(2 * sum(
        (K[u, v] * K[v, u] * edge_dets[(u, v)] - abs(q) * du) * x2[(u, v)]
        for u, v in edges[:m]))
    assert clean(determinant_square - signed_laplacian) == 0
    assert determinant_square > 0
    # Decimal entropy values illustrate the established identities only.
    import math
    f = [-math.log(float(p)) for p in probs]
    psi = sum(float(pu[restriction(mask, outside)]) * s.prod(
        2 * ((mask >> j) & 1) - 1 for j in range(m)) * f[mask]
        for mask in range(1 << n))
    W = {}
    for e in edges:
        rr, pr = edge_marginals[e]
        W[e] = sum(float(pr[restriction(mask, rr)]) *
                   (2 * ((mask >> e[0]) & 1) - 1) *
                   (2 * ((mask >> e[1]) & 1) - 1) * f[mask]
                   for mask in range(1 << n))
    production = -sum(float(ddp) * val for ddp, val in zip(accelerations, f))
    formula = 2 * sum(float(K[u, v] * K[v, u]) * W[(u, v)] * float(x2[(u, v)]) for u, v in edges)
    formula += 2 * (-1) ** m * float(q) * float(psi) * float(cyc_x2)
    assert abs(production - formula) < 1e-9
    L = K * (s.eye(n) - K).inv(method="DM")
    bad = next(((i, j, k, clean(s.re(-L[i, j] * L[j, k] * L[k, i])))
                for i, j, k in combinations(range(n), 3)
                if clean(s.re(-L[i, j] * L[j, k] * L[k, i])) < 0), None)
    result = dict(name=name, vertices=n, cycle_length=m, loop_product=str(loop),
                  atom_jet_checks=1 << n, forest_ratio_checks=ratio_count,
                  determinant_square=str(determinant_square),
                  frozen_cycle_coefficient=float(psi), gauge_entropy_production=production,
                  comparison_bound=float(abs(psi) / float(du) * float(determinant_square)),
                  negative_normalized_odds_cycle_numerator=[str(v) for v in bad] if bad else None)
    print(name, "PASS", flush=True)
    return result


if __name__ == "__main__":
    cases = [run_case("complex_six_cycle_phase_flip", 6, Q(1, 5), (15 + 8 * I) / 17),
             run_case("strong_six_cycle_tree_reservoir", 6, Q(27, 100), (-15 + 8 * I) / 17, True),
             run_case("odd_five_cycle_phase_flip", 5, Q(1, 5), (-3 + 4 * I) / 5)]
    out = dict(status="PASS", proof_uses_numerics=False, cases=cases)
    Path(__file__).with_name("results.json").write_text(json.dumps(out, indent=2) + "\n")
