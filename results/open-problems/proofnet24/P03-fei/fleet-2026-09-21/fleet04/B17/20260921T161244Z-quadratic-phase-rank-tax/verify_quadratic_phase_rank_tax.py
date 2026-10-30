#!/usr/bin/env python3
"""Exact self-checks for B17 quadratic-phase rank-tax FEI mechanism.

Standard library only. Exact rational arithmetic is used for Walsh masses,
autocorrelations, F_2 ranks, and J_aff. Floating point is used only to print
entropy values whose analytic forms are recorded separately in REPORT.md.
"""
from fractions import Fraction
from collections import Counter
from math import log2
import json
import hashlib

def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def rank_f2(vectors, n):
    basis = [0] * n
    r = 0
    for x in vectors:
        y = x
        while y:
            b = y.bit_length() - 1
            if basis[b]:
                y ^= basis[b]
            else:
                basis[b] = y
                r += 1
                break
    return r

def autocorr(vals, v):
    N = len(vals)
    return Fraction(sum(vals[x] * vals[x ^ v] for x in range(N)), N)

def folded_cost(vals, v):
    return (1 - abs(autocorr(vals, v))) / 2

def j_aff(vals):
    n = len(vals).bit_length() - 1
    weighted = sorted((folded_cost(vals, v), v) for v in range(1, 1 << n))
    chosen = []
    total = Fraction(0)
    for cost, v in weighted:
        if rank_f2(chosen + [v], n) > len(chosen):
            chosen.append(v)
            total += cost
            if len(chosen) == n:
                return total, chosen
    raise RuntimeError("no basis")

def polar_data(edge_mask, n):
    rows = [0] * n
    bit = 0
    for i in range(n):
        for j in range(i+1, n):
            if (edge_mask >> bit) & 1:
                rows[i] |= 1 << j
                rows[j] |= 1 << i
            bit += 1
    return rank_f2(rows, n), rows

def quadratic_phase(edge_mask, n):
    vals = []
    for x in range(1 << n):
        q = 0
        bit = 0
        for i in range(n):
            for j in range(i+1, n):
                if ((edge_mask >> bit) & 1) and ((x >> i) & 1) and ((x >> j) & 1):
                    q ^= 1
                bit += 1
        vals.append(-1 if q else 1)
    return vals

def defect(n):
    vals = [1] * (1 << n)
    vals[0] = -1
    return vals

def mul(a, b):
    return [x*y for x, y in zip(a, b)]

def spectral_square_numerators(vals):
    return dict(sorted(Counter(w*w for w in fwht(vals)).items()))

def entropy_bits(vals):
    N = len(vals)
    out = 0.0
    for w in fwht(vals):
        if w:
            p = (w/N)**2
            out -= p * log2(p)
    return out

quadratic_checks = []
for n in (4, 5):
    count = 1 << (n * (n - 1) // 2)
    for edge_mask in range(count):
        r, rows = polar_data(edge_mask, n)
        q = quadratic_phase(edge_mask, n)
        d = defect(n)
        f = mul(q, d)
        J, _ = j_aff(f)
        N = 1 << n
        claimed_J = Fraction(r, 2) + Fraction(2 * (n - 2*r), N)
        assert J == claimed_J
        for v in range(1, N):
            Bv = 0
            for i in range(n):
                if (v >> i) & 1:
                    Bv ^= rows[i]
            claimed_cost = Fraction(2, N) if Bv == 0 else Fraction(1, 2) - Fraction(2, N)
            assert folded_cost(f, v) == claimed_cost
        Jd, _ = j_aff(d)
        assert Jd == Fraction(2*n, N)
        assert 4 * (J - Jd) >= r
        assert mul(q, f) == d
    quadratic_checks.append({
        "n": n,
        "homogeneous_quadratic_forms_checked": count,
        "directional_cost_formula": "PASS",
        "J_aff_formula": "PASS",
        "rank_tax_payment_at_C4": "PASS",
        "phase_peeling_identity": "PASS",
    })

f = [1,-1,-1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1]
extended = [f[x & 15] for x in range(32)]
h = []
for x in range(32):
    q = ((x >> 0) & 1) * ((x >> 4) & 1)
    h.append(extended[x] * (-1 if q else 1))

Jf, basis_f = j_aff(f)
Jh, basis_h = j_aff(h)
assert Jf == Fraction(3, 2)
assert Jh == Fraction(7, 4)
assert spectral_square_numerators(f) == {4: 10, 36: 6}
assert spectral_square_numerators(h) == {0: 8, 16: 14, 64: 8, 144: 2}

Hf = entropy_bits(f)
Hh = entropy_bits(h)
delta_H = Hh - Hf
delta_J = float(Jh - Jf)
ratio = delta_H / delta_J
assert ratio > 2.0

result = {
    "schema_version": 1,
    "status": "PASS",
    "quadratic_defect_family": quadratic_checks,
    "bridge_coefficient_2_counterexample": {
        "f_truth_table_integer_order": f,
        "bridge_phase": "(-1)^(x_0*y) on one fresh bit y",
        "polar_rank": 2,
        "f_walsh_square_numerator_counts_denominator_256": spectral_square_numerators(f),
        "h_walsh_square_numerator_counts_denominator_1024": spectral_square_numerators(h),
        "J_aff_f": f"{Jf.numerator}/{Jf.denominator}",
        "J_aff_h": f"{Jh.numerator}/{Jh.denominator}",
        "delta_J": f"{(Jh-Jf).numerator}/{(Jh-Jf).denominator}",
        "H_f_formula": "6-(27/16)*log2(3)",
        "H_h_formula": "5-(9/16)*log2(3)",
        "delta_H_formula": "-1+(9/8)*log2(3)",
        "delta_H_numeric": delta_H,
        "delta_H_over_delta_J_formula": "-4+(9/2)*log2(3)",
        "delta_H_over_delta_J_numeric": ratio,
        "coefficient_2_refuted_exactly_by": "log2(3)>4/3, equivalently 27>16",
        "basis_f": basis_f,
        "basis_h": basis_h,
    },
    "scope_note": "Finite checks support the analytic report; they are not a proof of full FEI."
}
print(json.dumps(result, sort_keys=True, indent=2))
