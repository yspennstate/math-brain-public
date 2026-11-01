#!/usr/bin/env python3
from itertools import permutations
from fractions import Fraction
import json

def gf2_rank(rows, ncols):
    rows = list(rows)
    r = 0
    for c in range(ncols):
        pivot = next((k for k in range(r, len(rows)) if (rows[k] >> c) & 1), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        for k in range(len(rows)):
            if k != r and ((rows[k] >> c) & 1):
                rows[k] ^= rows[r]
        r += 1
    return r

def matrix_from_quad(n, quadmask):
    rows = [0] * n
    bit = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (quadmask >> bit) & 1:
                rows[i] |= 1 << j
                rows[j] |= 1 << i
            bit += 1
    return rows

def delete_index_matrix(rows, n, i):
    out = []
    for r_old in range(n):
        if r_old == i:
            continue
        val = 0
        cnew = 0
        for c_old in range(n):
            if c_old == i:
                continue
            if (rows[r_old] >> c_old) & 1:
                val |= 1 << cnew
            cnew += 1
        out.append(val)
    return out

def qeval(n, quadmask, linmask, x):
    s = 0
    bit = 0
    for i in range(n):
        if ((linmask >> i) & 1) and ((x >> i) & 1):
            s ^= 1
        for j in range(i + 1, n):
            if ((quadmask >> bit) & 1) and ((x >> i) & 1) and ((x >> j) & 1):
                s ^= 1
            bit += 1
    return s

def walsh_spectrum(n, quadmask, linmask):
    N = 1 << n
    a = [1 if qeval(n, quadmask, linmask, x) == 0 else -1 for x in range(N)]
    h = 1
    while h < N:
        for i in range(0, N, 2 * h):
            for j in range(i, i + h):
                u, v = a[j], a[j + h]
                a[j], a[j + h] = u + v, u - v
        h *= 2
    return a

def influence_truth(n, quadmask, linmask, i):
    N = 1 << n
    cnt = 0
    for x in range(N):
        if qeval(n, quadmask, linmask, x) != qeval(n, quadmask, linmask, x ^ (1 << i)):
            cnt += 1
    return Fraction(cnt, N)

def B_from_uniform_support(support, i):
    supp = set(support)
    pair_count = sum(1 for s in support if ((s >> i) & 1) == 0 and (s | (1 << i)) in supp)
    return Fraction(2 * pair_count, len(support))

def rank_principal(rows, n, keep):
    new = []
    for rold in keep:
        val = 0
        for cnew, cold in enumerate(keep):
            if (rows[rold] >> cold) & 1:
                val |= 1 << cnew
        new.append(val)
    return gf2_rank(new, len(keep))

def order_R(rows, n, order):
    keep = list(range(n))
    rprev = gf2_rank(rows, n)
    R = Fraction(0)
    for i in order:
        keep2 = [j for j in keep if j != i]
        rnew = rank_principal(rows, n, keep2)
        R += Fraction(rprev - rnew, 2)
        keep = keep2
        rprev = rnew
    return R

def synergy_matrix_g0(m):
    rows = [0] * m
    center = m - 1
    for a in range(0, m - 1, 2):
        b = a + 1
        for u, v in ((a, b), (a, center), (b, center)):
            rows[u] |= 1 << v
            rows[v] |= 1 << u
    return rows

def synergy_matrix_F(m):
    rows = [0] * (m + 1)
    g = synergy_matrix_g0(m)
    for i in range(m):
        for j in range(i + 1, m):
            if (g[i] >> j) & 1:
                rows[i + 1] |= 1 << (j + 1)
                rows[j + 1] |= 1 << (i + 1)
    center = m
    rows[0] |= 1 << center
    rows[center] |= 1
    return rows

def main():
    exhaustive = {}
    for n in range(1, 6):
        qbits = n * (n - 1) // 2
        checked = 0
        failures = []
        for quadmask in range(1 << qbits):
            rows = matrix_from_quad(n, quadmask)
            r = gf2_rank(rows, n)
            for linmask in range(1 << n):
                W = walsh_spectrum(n, quadmask, linmask)
                support = [s for s, w in enumerate(W) if w]
                sq = {w * w for w in W if w}
                checked += 1
                if len(support) != (1 << r) or sq != {1 << (2 * n - r)}:
                    failures.append(["flat-spectrum", quadmask, linmask])
                    break
                for i in range(n):
                    B = B_from_uniform_support(support, i)
                    rd = gf2_rank(delete_index_matrix(rows, n, i), n - 1)
                    if B != Fraction(r - rd, 2):
                        failures.append(["B-rank-drop", quadmask, linmask, i, str(B), r, rd])
                        break
                    inf = influence_truth(n, quadmask, linmask, i)
                    expected = Fraction(1, 2) if rows[i] else Fraction((linmask >> i) & 1, 1)
                    if inf != expected:
                        failures.append(["influence", quadmask, linmask, i, str(inf), str(expected)])
                        break
                if failures:
                    break
            if failures:
                break
        exhaustive[str(n)] = {"forms_checked": checked, "failures": failures}

    order_checks = {}
    for n in range(1, 5):
        qbits = n * (n - 1) // 2
        checked = 0
        failures = []
        for quadmask in range(1 << qbits):
            rows = matrix_from_quad(n, quadmask)
            r = gf2_rank(rows, n)
            for order in permutations(range(n)):
                checked += 1
                if order_R(rows, n, order) != Fraction(r, 2):
                    failures.append([quadmask, list(order)])
                    break
            if failures:
                break
        order_checks[str(n)] = {
            "quadratic_matrices": 1 << qbits,
            "orders_checked": checked,
            "failures": failures,
        }

    synergy = []
    for m in (3, 5, 7, 9):
        rg = gf2_rank(synergy_matrix_g0(m), m)
        rf = gf2_rank(synergy_matrix_F(m), m + 1)
        Ig = Fraction(m, 2)
        IF = Fraction(m + 1, 2)
        synergy.append({
            "m": m,
            "rank_g0": rg,
            "A_g0": str(Fraction(rg, 2) / Ig),
            "rank_F": rf,
            "A_F": str(Fraction(rf, 2) / IF),
        })

    result = {
        "status": "PASS" if all(not v["failures"] for v in exhaustive.values())
                         and all(not v["failures"] for v in order_checks.values()) else "FAIL",
        "exhaustive_quadratic_phase_checks": exhaustive,
        "fixed_order_rank_telescope_checks": order_checks,
        "p03_erasure_synergy_family": synergy,
        "note": "Global sign/constant term is omitted because it does not change squared Fourier law or influences."
    }
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
