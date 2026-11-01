#!/usr/bin/env python3
"""Exact finite checks for B15 spectral-independence rigidity and bent point-defect family.

All PASS/FAIL assertions use integer/rational arithmetic except the explicitly
descriptive logarithmic ratios printed for the family. The all-dimensional
claims are proved in REPORT.md and do not depend on finite enumeration.
"""
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction


def fwht(values):
    a = list(values)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def independence_coordinates(values):
    """Return coordinates whose spectral membership bit is independent of the rest.

    Independence is checked exactly from unnormalised squared Walsh coefficients.
    """
    N = len(values)
    n = N.bit_length() - 1
    W = fwht(values)
    assert sum(w*w for w in W) == N*N
    out = []
    for i in range(n):
        bit = 1 << i
        A = sum(W[s]*W[s] for s in range(N) if s & bit)
        ok = True
        for t in range(N):
            if t & bit:
                continue
            x = W[t]*W[t]
            y = W[t | bit]*W[t | bit]
            if y * N*N != A * (x+y):
                ok = False
                break
        if ok:
            out.append((i, Fraction(A, N*N)))
    return out


def exhaustive_rigidity():
    rows = []
    total_functions = 0
    total_independent_coordinates = 0
    nontrivial_half = 0
    for n in range(1, 5):
        N = 1 << n
        funcs = 1 << N
        c_ind = 0
        c_half = 0
        for mask in range(funcs):
            vals = [1 if (mask >> x) & 1 else -1 for x in range(N)]
            coords = independence_coordinates(vals)
            for _, alpha in coords:
                assert alpha in (Fraction(0), Fraction(1,2), Fraction(1))
                c_ind += 1
                c_half += (alpha == Fraction(1,2))
        rows.append({
            "dimension": n,
            "boolean_functions": funcs,
            "independent_spectral_coordinates": c_ind,
            "nontrivial_half_coordinates": c_half,
        })
        total_functions += funcs
        total_independent_coordinates += c_ind
        nontrivial_half += c_half
    return {
        "rows": rows,
        "total_functions": total_functions,
        "total_independent_coordinates": total_independent_coordinates,
        "nontrivial_half_coordinates": nontrivial_half,
    }


def bent_values(r):
    N = 1 << (2*r)
    vals = []
    for x in range(N):
        phase = 0
        for j in range(r):
            phase ^= ((x >> (2*j)) & 1) & ((x >> (2*j+1)) & 1)
        vals.append(-1 if phase else 1)
    return vals


def point_defect_rows():
    rows = []
    for r in range(2, 8):
        N = 1 << (2*r)
        sN = 1 << r
        b = bent_values(r)
        W = fwht(b)
        assert set(abs(w) for w in W) == {sN}
        # g=b-delta_0, h=delta_0.  Since b(0)=1, g(0)=0 and g=b elsewhere.
        g = list(b)
        g[0] = 0
        h = [0] * N
        h[0] = 1
        U = fwht(g)
        V = fwht(h)
        assert all(v == 1 for v in V)
        assert all(U[t] == W[t] - 1 for t in range(N))
        assert sum(u*u for u in U) == N*(N-1)
        pos = sum(w > 0 for w in W)
        neg = N-pos
        assert pos == (N+sN)//2 and neg == (N-sN)//2

        # Spectral conditional laws for selector coordinate:
        # P_t = 1/N and Q_t = U_t^2/[N(N-1)].
        tv = sum(abs(Fraction(1,N) - Fraction(u*u, N*(N-1))) for u in U) / 2
        assert tv == Fraction(1, sN)

        # Every upper/lower magnitude ratio is at least 2^(r-1), proving L/Inf >= r-1.
        min_ratio = min(abs(u) for u in U)  # V_t = 1 in unnormalised coordinates
        assert min_ratio == sN-1
        assert min_ratio >= (1 << (r-1))

        q = 1/sN
        descriptive_L_over_Inf = (
            (1+q)/2 * math.log2(1/q - 1)
            + (1-q)/2 * math.log2(1/q + 1)
        )
        descriptive_KL_PQ = q * math.log2((1+q)/(1-q))

        # Exploratory (not certification): compute L/Inf for the ordinary y coordinates.
        # Parent Fourier coefficients are u=U/N on t-absent labels and v=V/N on t-present labels.
        coeff = [0.0] * (2*N)
        tbit = N
        for s in range(N):
            coeff[s] = U[s] / N
            coeff[s | tbit] = V[s] / N
        y_ratios = []
        for j in range(2*r):
            bit = 1 << j
            inf = 0.0
            L = 0.0
            for s in range(2*N):
                if s & bit:
                    inf += coeff[s] * coeff[s]
            for s in range(2*N):
                if s & bit:
                    continue
                upper = abs(coeff[s | bit])
                lower = abs(coeff[s])
                if upper and lower > upper:
                    L += upper * upper * math.log2(lower / upper)
            y_ratios.append(L/inf if inf else 0.0)

        rows.append({
            "r": r,
            "remaining_dimension": 2*r,
            "N": N,
            "selector_influence": f"1/{N}",
            "conditional_TV_exact": f"1/{sN}",
            "minimum_ratio_exact": min_ratio,
            "certified_L_over_Inf_lower_bound": r-1,
            "descriptive_L_over_Inf": format(descriptive_L_over_Inf, ".15f"),
            "descriptive_KL_P_to_Q_bits": format(descriptive_KL_PQ, ".15f"),
            "descriptive_min_y_L_over_Inf": format(min(y_ratios), ".15f"),
            "descriptive_max_y_L_over_Inf": format(max(y_ratios), ".15f"),
        })
    return rows


def main():
    result = {
        "schema_version": 1,
        "status": "PASS",
        "scope": "finite sanity checks; analytic proofs are in REPORT.md",
        "rigidity_exhaustive": exhaustive_rigidity(),
        "bent_point_defect": point_defect_rows(),
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
