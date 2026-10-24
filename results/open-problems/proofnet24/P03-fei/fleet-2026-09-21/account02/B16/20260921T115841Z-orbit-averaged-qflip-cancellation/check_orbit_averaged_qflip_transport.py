#!/usr/bin/env python3
"""Self-checks for B16 orbit-averaged q-flip transport.

Engineering/scientific self-check only.  The theorem in REPORT.md is analytic.
No sealed benchmark data or external state is used.
"""
from __future__ import annotations
import itertools, math, json
from collections import defaultdict

def pc(x: int) -> int:
    return x.bit_count()

def entropy_bits(signs):
    n = len(signs)
    a = [float(x) for x in signs]
    step = 1
    while step < n:
        for base in range(0, n, 2 * step):
            for j in range(base, base + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    out = 0.0
    for u in a:
        p = (u / n) ** 2
        if p:
            out -= p * math.log2(p)
    return out

def defect(n: int, c: int):
    mask = (1 << c) - 1
    return [-1 if (x & mask) == mask else 1 for x in range(1 << n)]

def disagree(signs, n):
    ans = set()
    for x in range(1 << n):
        for i in range(n):
            y = x ^ (1 << i)
            if x < y and signs[x] != signs[y]:
                ans.add((x, y))
    return ans

def pivot(x: int, order):
    for i in order:
        if (x >> i) & 1:
            return i
    raise ValueError("zero word has no pivot")

def dual_q0(n: int, u: int, order):
    """Affine-gauge exponent dual to q-flip u for ordered-first pivot rule."""
    q = [0] * (1 << n)
    for wt in range(2, n + 1):
        for x in range(1 << n):
            if pc(x) != wt:
                continue
            i = pivot(x, order)
            parent = x ^ (1 << i)
            q[x] = (1 if x == u else 0) ^ q[parent]
    return q

def edge(x, y):
    return (x, y) if x < y else (y, x)

def basis(n: int, a: int, order):
    rows = []
    for v in range(1 << n):
        if pc(v) < 2:
            continue
        i = pivot(v, order)
        pts = (a, a ^ (1 << i), a ^ v, a ^ v ^ (1 << i))
        q0 = dual_q0(n, v, order)
        q = [q0[x ^ a] for x in range(1 << n)]
        rows.append((v, i, pts, q))
    return rows

def routed_shapley(signs, n: int, a: int, order):
    B = basis(n, a, order)
    active = []
    route = {}
    for idx, (_, _, pts, _) in enumerate(B):
        z = 1
        for x in pts:
            z *= signs[x]
        if z == -1:
            active.append(idx)
            e0, e1 = edge(pts[0], pts[1]), edge(pts[2], pts[3])
            d0 = signs[e0[0]] != signs[e0[1]]
            d1 = signs[e1[0]] != signs[e1[1]]
            assert d0 ^ d1
            route[idx] = e0 if d0 else e1

    m = len(active)
    if m == 0:
        assert abs(entropy_bits(signs)) < 1e-12
        return {}
    N = 1 << n
    G = {}
    active_q = [B[idx][3] for idx in active]
    for S in range(1 << m):
        exponent = [0] * N
        for j in range(m):
            if (S >> j) & 1:
                q = active_q[j]
                for x in range(N):
                    exponent[x] ^= q[x]
        phase = [-1 if b else 1 for b in exponent]
        G[S] = entropy_bits(phase)

    facm = math.factorial(m)
    phi = {}
    for j, idx in enumerate(active):
        val = 0.0
        for S in range(1 << m):
            if (S >> j) & 1:
                continue
            k = pc(S)
            w = math.factorial(k) * math.factorial(m - k - 1) / facm
            val += w * (G[S | (1 << j)] - G[S])
        phi[idx] = val
    H = entropy_bits(signs)
    assert abs(sum(phi.values()) - H) < 2e-10

    out = defaultdict(float)
    for idx, value in phi.items():
        out[route[idx]] += value
    return dict(out)

def exhaustive_orbit_case(n: int, c: int):
    signs = defect(n, c)
    total = defaultdict(float)
    count = 0
    for a in range(1 << n):
        for order in itertools.permutations(range(n)):
            for e, value in routed_shapley(signs, n, a, order).items():
                total[e] += value
            count += 1
    D = sorted(disagree(signs, n))
    vals = [total[e] / count for e in D]
    H = entropy_bits(signs)
    target = H / len(D)
    spread = max(vals) - min(vals)
    assert spread < 3e-12
    assert max(abs(v - target) for v in vals) < 3e-12
    assert abs(sum(vals) - H) < 3e-11
    return {
        "n": n, "c": c, "bases": count, "H_bits": H,
        "disagreement_edges": len(D), "edge_load_target": target,
        "max_edge_spread": spread,
    }

def defining_basis_singleton(n: int, c: int):
    assert 2 <= c <= n
    order = tuple(range(n))
    pivot_index = n - c
    u = (1 << pivot_index) | (1 << (pivot_index + 1))
    q = dual_q0(n, u, order)
    signs = [-1 if b else 1 for b in q]
    negative = sum(b for b in q)
    assert negative == 1 << (n - c)
    B = basis(n, 0, order)
    active = []
    for idx, (v, _, pts, _) in enumerate(B):
        z = 1
        for x in pts:
            z *= signs[x]
        if z == -1:
            active.append(v)
    assert active == [u]
    H = entropy_bits(signs)
    qmass = 2.0 ** (-c)
    p0 = (1 - 2 * qmass) ** 2
    p1 = 4 * qmass * qmass
    H_formula = -(p0 * math.log2(p0) if p0 else 0.0)
    H_formula -= (2**c - 1) * p1 * math.log2(p1)
    assert abs(H - H_formula) < 2e-12
    D = disagree(signs, n)
    J = 2 * c * qmass
    assert len(D) == c * (1 << (n - c))
    # Total influence = 2|D|/N
    assert abs(2 * len(D) / (1 << n) - J) < 1e-15
    return {
        "n": n, "c": c, "active_syndrome_count": len(active),
        "negative_vertices": negative, "H_bits": H,
        "J": J, "H_over_J": H / J,
    }

def analytic_table():
    rows = []
    for c in range(2, 33):
        q = 2.0 ** (-c)
        p0 = (1 - 2 * q) ** 2
        p1 = 4 * q * q
        H = -p0 * math.log2(p0)
        H -= (2**c - 1) * p1 * math.log2(p1)
        J = 2 * c * q
        ratio = H / J
        assert ratio < 4.0
        rows.append({"c": c, "H_bits": H, "J": J, "H_over_J": ratio})
    return rows

def main():
    orbit_cases = [
        exhaustive_orbit_case(3, 2),
        exhaustive_orbit_case(3, 3),
        exhaustive_orbit_case(4, 2),
        exhaustive_orbit_case(4, 3),
        exhaustive_orbit_case(4, 4),
        exhaustive_orbit_case(5, 2),
    ]
    singleton = []
    for n in range(2, 9):
        for c in range(2, n + 1):
            singleton.append(defining_basis_singleton(n, c))
    table = analytic_table()
    out = {
        "status": "PASS",
        "scope": "self_check_not_fei_closure",
        "orbit_cases": orbit_cases,
        "singleton_defining_basis_cases": len(singleton),
        "max_checked_H_over_J": max(r["H_over_J"] for r in table),
        "c32_H_over_J": table[-1]["H_over_J"],
        "selected_ratios": [table[c-2] for c in (2,3,4,5,8,16,32)],
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
