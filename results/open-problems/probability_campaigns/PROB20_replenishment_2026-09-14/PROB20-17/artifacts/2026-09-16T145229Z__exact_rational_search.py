#!/usr/bin/env python3
"""Exact/certified counterexample search for PROB20-17, 2026-09-16.

Source target: Israel--Krahmer--Ward Conjecture 1.3 (Ducci), norm inside
both averages. Metric is WOR/WR; a certified value >1 is a refutation.

Certificate families:
1) Exact rational rank-one projectors in R^2.  All word norms are rational.
   We exhaust every n-subset (4<=n<=8) of a fixed 10-line rational pool and
   every product length 4<=m<=n.  We also exhaust rational scale patterns
   {1/2,1,2} on the hardest equal-scale geometry found for n=4,5,6.
2) General 2x2 integer PSD matrices.  For m=4 and every distinct 4- and
   5-subset of a fixed 16-matrix library, every product norm is enclosed by
   rigorous dyadic algebraic intervals obtained from the exact 2x2 singular
   value formula.  The aggregate WOR/WR ratio is then enclosed rigorously.

Only Python stdlib exact integers/Fraction arithmetic is used in the proof
path.  Floats are printed only as human-readable approximations after exact
comparisons have been made.
"""
from fractions import Fraction
from math import gcd, isqrt, perm
from functools import reduce
import itertools
import time

def F(x=0, y=1):
    return Fraction(x, y)

def absdot(u, v):
    z = u[0] * v[0] + u[1] * v[1]
    return abs(z)

def rankone_ratio(pool, indices, m, scales=None):
    n = len(indices)
    if scales is None:
        scales = [F(1)] * n
    G = [[absdot(pool[indices[i]], pool[indices[j]]) for j in range(n)] for i in range(n)]
    v = list(scales)
    for _ in range(1, m):
        nv = [F(0) for _ in range(n)]
        for i in range(n):
            if not v[i]:
                continue
            for j in range(n):
                nv[j] += v[i] * G[i][j] * scales[j]
        v = nv
    sum_wr = sum(v, F(0))
    dp = {(1 << j, j): scales[j] for j in range(n)}
    for _size in range(1, m):
        nd = {}
        for (mask, i), val in dp.items():
            for j in range(n):
                if (mask >> j) & 1:
                    continue
                key = (mask | (1 << j), j)
                nd[key] = nd.get(key, F(0)) + val * G[i][j] * scales[j]
        dp = nd
    sum_wor = sum(dp.values(), F(0))
    avg_wr = sum_wr / (n ** m)
    avg_wor = sum_wor / perm(n, m)
    assert avg_wr > 0
    return avg_wor / avg_wr

RANKONE_POOL = [
    (F(1), F(0)),
    (F(15,17), F(8,17)),
    (F(21,29), F(20,29)),
    (F(8,17), F(15,17)),
    (F(7,25), F(24,25)),
    (F(0), F(1)),
    (F(7,25), F(-24,25)),
    (F(8,17), F(-15,17)),
    (F(21,29), F(-20,29)),
    (F(15,17), F(-8,17)),
]
for u in RANKONE_POOL:
    assert u[0]*u[0] + u[1]*u[1] == 1

def exact_rankone_search():
    best = {}
    subset_count = 0
    instance_count = 0
    for n in range(4, 9):
        for comb in itertools.combinations(range(len(RANKONE_POOL)), n):
            subset_count += 1
            for m in range(4, n + 1):
                instance_count += 1
                r = rankone_ratio(RANKONE_POOL, comb, m)
                key = (n, m)
                if key not in best or r > best[key][0]:
                    best[key] = (r, comb)
                assert r < 1
    print("RANKONE_EXACT subsets", subset_count, "(n=4..8)")
    print("RANKONE_EXACT source_instances", instance_count, "(all m=4..n)")
    for key in sorted(best):
        r, comb = best[key]
        print("RANKONE_BEST", key, "ratio_exact", r,
              "ratio_decimal", format(float(r), ".15f"), "subset", comb)
    eq_pool = [(F(1), F(0)) for _ in range(8)]
    for n in range(4, 9):
        for m in range(4, n + 1):
            r = rankone_ratio(eq_pool, tuple(range(n)), m)
            assert r == 1
    print("BASELINE_EQUAL_PROJECTORS ratio_exact 1 scopes n=4..8,m=4..n")
    scale_set = (F(1,2), F(1), F(2))
    scaled_cases = 0
    for n in range(4, 7):
        for m in range(4, n + 1):
            comb = best[(n, m)][1]
            b = (F(0), None)
            for scales in itertools.product(scale_set, repeat=n):
                scaled_cases += 1
                r = rankone_ratio(RANKONE_POOL, comb, m, scales)
                if r > b[0]:
                    b = (r, scales)
                assert r < 1
            print("RANKONE_SCALE_BEST", (n,m), "ratio_exact", b[0],
                  "ratio_decimal", format(float(b[0]), ".15f"),
                  "geometry", comb, "scales", tuple(str(x) for x in b[1]))
    print("RANKONE_SCALE source_instances", scaled_cases)
    return best

def mm2(A, B):
    return (
        (A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]),
        (A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]),
    )
I2 = ((1,0),(0,1))

def sqrt_bounds(q, bits=60):
    q = Fraction(q)
    assert q >= 0
    if q == 0:
        return F(0), F(0)
    num, den = q.numerator, q.denominator
    z = isqrt((num << (2 * bits)) // den)
    lo = Fraction(z, 1 << bits)
    if lo * lo == q:
        return lo, lo
    hi = Fraction(z + 1, 1 << bits)
    assert lo * lo <= q <= hi * hi
    return lo, hi

def norm2_bounds(M, bits=60):
    a,b = M[0]
    c,d = M[1]
    s = a*a + b*b + c*c + d*d
    det = a*d - b*c
    disc = s*s - 4*det*det
    assert disc >= 0
    dl, du = sqrt_bounds(F(disc), bits)
    lam_lo = (F(s) + dl) / 2
    lam_hi = (F(s) + du) / 2
    nl, _ = sqrt_bounds(lam_lo, bits)
    _, nu = sqrt_bounds(lam_hi, bits)
    assert nl <= nu
    return nl, nu

def is_psd2(A):
    return (A[0][1] == A[1][0] and A[0][0] >= 0 and A[1][1] >= 0
            and A[0][0]*A[1][1] - A[0][1]*A[0][1] >= 0)

PSD_LIBRARY = [
    ((1,0),(0,1)),
    ((1,0),(0,2)), ((2,0),(0,1)),
    ((1,1),(1,1)), ((1,-1),(-1,1)),
    ((1,1),(1,2)), ((1,-1),(-1,2)),
    ((2,1),(1,1)), ((2,-1),(-1,1)),
    ((1,2),(2,4)), ((1,-2),(-2,4)),
    ((4,2),(2,1)), ((4,-2),(-2,1)),
    ((2,1),(1,3)), ((2,-1),(-1,3)),
    ((3,1),(1,2)),
]
assert all(is_psd2(A) for A in PSD_LIBRARY)
assert len(set(PSD_LIBRARY)) == len(PSD_LIBRARY)

def certified_fullrank_m4_search():
    L = len(PSD_LIBRARY)
    cache = {}
    for w in itertools.product(range(L), repeat=4):
        P = I2
        for idx in w:
            P = mm2(P, PSD_LIBRARY[idx])
        cache[w] = norm2_bounds(P, bits=60)
    def interval_ratio(sub):
        n = len(sub)
        wr_lo = wr_hi = F(0)
        for lw in itertools.product(range(n), repeat=4):
            w = tuple(sub[i] for i in lw)
            lo, hi = cache[w]
            wr_lo += lo; wr_hi += hi
        wor_lo = wor_hi = F(0)
        for lw in itertools.permutations(range(n), 4):
            w = tuple(sub[i] for i in lw)
            lo, hi = cache[w]
            wor_lo += lo; wor_hi += hi
        wr_lo /= n**4; wr_hi /= n**4
        wor_lo /= perm(n,4); wor_hi /= perm(n,4)
        assert wr_lo > 0
        return wor_lo / wr_hi, wor_hi / wr_lo
    total = 0
    for n in (4,5):
        best_upper = (F(0), None, None)
        ncount = 0
        for sub in itertools.combinations(range(L), n):
            ncount += 1; total += 1
            lo, up = interval_ratio(sub)
            assert up < 1
            if up > best_upper[0]:
                best_upper = (up, sub, lo)
        up, sub, lo = best_upper
        print("PSD2_CERTIFIED", "n", n, "m", 4, "subsets", ncount,
              "max_ratio_lower", lo,
              "max_ratio_upper", up,
              "upper_decimal", format(float(up), ".15f"),
              "subset", sub)
    print("PSD2_CERTIFIED source_instances", total,
          "library_size", L, "dyadic_bits", 60)

def main():
    t0 = time.time()
    print("PROB20-17 exact/certified source-ratio search")
    print("metric = WOR_average / WR_average; refutation requires certified ratio > 1")
    exact_rankone_search()
    certified_fullrank_m4_search()
    print("ALL_CERTIFICATES_PASS")
    print("elapsed_seconds", format(time.time() - t0, ".3f"))
if __name__ == "__main__":
    main()
