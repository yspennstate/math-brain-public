#!/usr/bin/env python3
"""Finite support check for B18 synchronized corner/Han block descent.

This is only computational support.  The report's theorem is analytic.
Enumerates Boolean functions up to global sign through n=4, retains functions
whose H/I is maximal among every nonconstant physical restriction descendant,
and checks the half-block same-selector inequalities.
"""
from functools import lru_cache
from itertools import combinations
from math import log2
import numpy as np

TOL = 1e-10

def fwht(vals):
    a = np.array(vals, dtype=float)
    N = len(a)
    h = 1
    while h < N:
        for z in range(0, N, 2*h):
            u = a[z:z+h].copy()
            v = a[z+h:z+2*h].copy()
            a[z:z+h] = u + v
            a[z+h:z+2*h] = u - v
        h *= 2
    return a / N

@lru_cache(None)
def stats(vals):
    N = len(vals)
    n = (N.bit_length() - 1)
    arr = np.array(vals)
    coeff = fwht(vals)
    p = coeff * coeff
    nz = p > 1e-15
    H = float(np.sum(-p[nz] * np.log2(p[nz])))
    pop = np.array([s.bit_count() for s in range(N)], dtype=float)
    I = float(np.sum(p * pop))
    idx = np.arange(N)
    infl = []
    for i in range(n):
        infl.append(float(np.mean(arr != arr[idx ^ (1 << i)])))
    Gamma = 0.0
    for i in range(n):
        for j in range(i+1, n):
            mask = (1 << i) | (1 << j)
            reps = [x for x in range(N) if (x & mask) == 0]
            mixed = 0
            for x in reps:
                prod = vals[x] * vals[x ^ (1 << i)] * vals[x ^ (1 << j)] * vals[x ^ mask]
                mixed += (prod == -1)
            Gamma += mixed / len(reps)
    return H, I, tuple(infl), Gamma

def restrict(vals, n, A, ass):
    A = tuple(sorted(A))
    rem = [i for i in range(n) if i not in A]
    out = []
    for y in range(1 << len(rem)):
        x = 0
        for t, i in enumerate(rem):
            x |= ((y >> t) & 1) << i
        for t, i in enumerate(A):
            x |= ((ass >> t) & 1) << i
        out.append(vals[x])
    return tuple(out)

def max_desc_ratio(vals, n):
    ans = -1.0
    for mask in range(1, 1 << n):
        A = [i for i in range(n) if (mask >> i) & 1]
        for ass in range(1 << len(A)):
            child = restrict(vals, n, A, ass)
            H, I, _, _ = stats(child)
            if I > 1e-12:
                ans = max(ans, H / I)
    return ans

def check():
    counts = {}
    violations = 0
    max_product = (-1.0, None)
    for n in range(2, 5):
        k = n // 2
        core_count = 0
        # quotient by global sign: fix first truth-table value to +1.
        for bits in range(1 << ((1 << n) - 1)):
            vals = (1,) + tuple(
                1 if (bits >> (x-1)) & 1 else -1
                for x in range(1, 1 << n)
            )
            H, I, infl, Gamma = stats(vals)
            if I <= 1e-12:
                continue
            r = H / I
            if max_desc_ratio(vals, n) > r + TOL:
                continue
            core_count += 1
            if Gamma <= 1e-12:
                continue
            R = Gamma / I
            rows = []
            for A in combinations(range(n), k):
                I_A = sum(infl[i] for i in A)
                J = I - I_A
                if J <= 1e-12:
                    continue
                Havg = Iavg = Gavg = 0.0
                for ass in range(1 << k):
                    child = restrict(vals, n, A, ass)
                    Hc, Ic, _, Gc = stats(child)
                    w = 1.0 / (1 << k)
                    Havg += w * Hc
                    Iavg += w * Ic
                    Gavg += w * Gc
                assert abs(Iavg - J) < 1e-9
                e = H - Havg - r * I_A
                ell = e / J
                barR = Gavg / Iavg if Iavg > 1e-12 else 0.0
                c = R - barR
                rows.append((A, e, J, ell, c, barR))
            denom = sum(row[2] for row in rows)
            Ghan = sum(row[1] for row in rows) / denom
            Cbar = (k / (n - 1)) * R
            M = 2 * (n - 1) / k - 1
            good = [
                row for row in rows
                if row[4] >= Cbar / 2 - 1e-9
                and row[3] <= M * Ghan + 1e-9
            ]
            if not good:
                violations += 1
                raise AssertionError(("synchronized selector failed", n, vals, R, Ghan))
            product = R * Ghan
            if product > max_product[0]:
                max_product = (product, (n, vals, r, R, Ghan))
        counts[n] = core_count
    print("status PASS")
    print("restriction_maximal_core_counts", counts)
    print("total_cores", sum(counts.values()))
    print("synchronized_selector_violations", violations)
    p, data = max_product
    n, vals, r, R, Ghan = data
    print("max_observed_R_times_GammaHan", repr(p))
    print("max_case_n", n)
    print("max_case_ratio_H_over_I", repr(r))
    print("max_case_R_Gamma2_over_I", repr(R))
    print("max_case_GammaHan", repr(Ghan))
    print("max_case_truth_table", vals)

if __name__ == "__main__":
    check()
