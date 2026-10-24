#!/usr/bin/env python3
"""Exact self-check for B16 monomial refunded q-flip multiplier theorem.

Engineering/mathematical self-check only; does not prove full FEI.
Uses exact rational arithmetic and exhaustive coordinate orders through n=7.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import permutations, combinations
from math import comb
import json

def powerset(xs):
    xs = tuple(xs)
    for r in range(len(xs)+1):
        for c in combinations(xs, r):
            yield frozenset(c)

def fixed_p_formula(n: int, k: int, S: frozenset[int], p: int) -> Fraction:
    A = frozenset(range(k))
    if p not in A:
        return Fraction(0)
    a_without_p = len(S & (A - {p}))
    q = len(S - A)
    sign = -1 if a_without_p % 2 else 1
    return Fraction(sign, k * comb(q + k, q))

def total_formula(n: int, k: int, S: frozenset[int]) -> Fraction:
    A = frozenset(range(k))
    a = len(S & A)
    q = len(S - A)
    sign = -1 if a % 2 else 1
    return Fraction(sign * (k - 2*a), k * comb(q + k, q))

def brute_coefficients(n: int, k: int):
    """Return normalized (divide by H_k) average charge Fourier coefficients.

    Sum over the active dummy orbit analytically: h=2^{-|D|} and the
    Walsh sum over all T subset D is zero unless S misses D, in which
    case it equals 2^{|D|}. This keeps the check exact while avoiding
    exponential work inside each coordinate order.
    """
    A = frozenset(range(k))
    masks = [frozenset(i for i in range(n) if (mask >> i) & 1)
             for mask in range(1 << n)]
    total = {S: Fraction(0) for S in masks}
    fixed = {(p,S): Fraction(0) for p in A for S in masks}
    orders = 0
    for perm in permutations(range(n)):
        orders += 1
        pos = {x:j for j,x in enumerate(perm)}
        p = min(A, key=pos.__getitem__)
        D = frozenset(x for x in range(n) if x not in A and pos[x] > pos[p])
        Ap = A - {p}
        for S in masks:
            if S & D:
                continue
            chi = -1 if len(S & Ap) % 2 else 1
            # orbit sum h * sum_{T subset D} chi_S(T) = chi_S(Ap)
            total[S] += chi
            fixed[p,S] += chi
    den = Fraction(1, orders)
    total = {S:v*den for S,v in total.items()}
    fixed = {(p,S):v*den for (p,S),v in fixed.items()}
    return total, fixed, orders

def main():
    coefficient_cases = 0
    fixed_cases = 0
    source_support_cases = 0
    order_count = 0
    max_dummy_ratio = Fraction(0)
    zero_half_core_cases = 0
    for n in range(2,8):
        for k in range(2,n+1):
            total, fixed, orders = brute_coefficients(n,k)
            order_count += orders
            A = frozenset(range(k))
            for S, got in total.items():
                want = total_formula(n,k,S)
                assert got == want, (n,k,S,got,want)
                coefficient_cases += 1
                a = len(S & A)
                q = len(S - A)
                if q >= 1:
                    ratio = abs(got)
                    if ratio > max_dummy_ratio:
                        max_dummy_ratio = ratio
                if k % 2 == 0 and a == k//2:
                    assert got == 0
                    zero_half_core_cases += 1
            for p in A:
                for S in total:
                    got = fixed[p,S]
                    want = fixed_p_formula(n,k,S,p)
                    assert got == want, ("fixed",n,k,p,S,got,want)
                    fixed_cases += 1
                # Genuine p-cut Fourier source for the codimension-k monomial
                # is supported on U subset A\{p}; on that support |multiplier|=1/k.
                for U in powerset(A-{p}):
                    got = fixed[p,U]
                    assert abs(got) == Fraction(1,k), ("support",n,k,p,U,got)
                    source_support_cases += 1
    out = {
        "status":"PASS",
        "scope":"exact_selfcheck_normalized_by_Hk",
        "n_exhaustive":[2,7],
        "coefficient_cases":coefficient_cases,
        "fixed_p_cases":fixed_cases,
        "source_support_cases":source_support_cases,
        "permutation_batches_total":order_count,
        "max_abs_multiplier_with_dummy_frequency":str(max_dummy_ratio),
        "half_core_zero_cases":zero_half_core_cases,
        "full_fei_proved":False,
    }
    print(json.dumps(out, sort_keys=True, indent=2))

if __name__ == "__main__":
    main()
