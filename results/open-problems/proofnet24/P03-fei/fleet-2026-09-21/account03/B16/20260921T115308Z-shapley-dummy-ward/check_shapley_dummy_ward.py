#!/usr/bin/env python3
"""
Finite falsification checker for the B16 Shapley dummy-coordinate Ward identity.

This is a sanity check only. The all-dimensional statements in REPORT.md are
proved algebraically; enumeration is not used as a universal proof.
"""
from fractions import Fraction
from math import comb, log2, isclose, factorial
from itertools import combinations

def entropy_bits(vals):
    N = len(vals)
    H = 0.0
    for s in range(N):
        z = 0
        for x, fx in enumerate(vals):
            z += fx * (-1 if ((s & x).bit_count() & 1) else 1)
        a = z / N
        p = a*a
        if p:
            H -= p*log2(p)
    return H

def one_subcube_entropy_bits(c):
    # A Boolean phase equal to -1 on one codimension-c cell.
    q = 2.0**(-c)
    p0 = (1.0 - 2.0*q)**2
    p1 = 4.0*q*q
    H = 0.0
    if p0:
        H -= p0*log2(p0)
    if p1:
        H -= ((1 << c)-1)*p1*log2(p1)
    return H

def union_cell_values(c, selected_mask):
    # Active coordinates are bits 0,1. Dummy suffix bits are 2..c-1.
    N = 1 << c
    out = []
    for x in range(N):
        if (x & 0b11) == 0b11:
            d = x >> 2
            out.append(-1 if ((selected_mask >> d) & 1) else 1)
        else:
            out.append(1)
    return out

def shapley_entropy(c):
    m = 1 << (c-2)
    Hcache = {}
    for mask in range(1 << m):
        Hcache[mask] = entropy_bits(union_cell_values(c, mask))
    phi = []
    for v in range(m):
        total = 0.0
        others = [u for u in range(m) if u != v]
        for k in range(m):
            weight = factorial(k)*factorial(m-k-1)/factorial(m)
            for S in combinations(others, k):
                mask = sum(1 << u for u in S)
                total += weight*(Hcache[mask | (1 << v)] - Hcache[mask])
        phi.append(total)
    return Hcache[(1 << m)-1], phi

def avoid_ratio(n, r, c):
    if c-1 > n-1-r:
        return Fraction(0, 1)
    return Fraction(comb(n-1-r, c-1), comb(n-1, c-1))

def corrected_multiplier_exact(n, r):
    s = Fraction(0, 1)
    for c in range(2, n+1):
        htilde = Fraction(2, 1 << (c-2))
        s += htilde * (Fraction(1 << (c-1), 1) * avoid_ratio(n, r, c) - 1)
    return s / n

def corrected_closed_form(n, r):
    return Fraction(4, r+1) - Fraction(8, n) + Fraction(8, n*(1 << n))

def raw_multiplier(n, r):
    s = 0.0
    for c in range(2, n+1):
        Hc = one_subcube_entropy_bits(c)
        s += Hc*((1 << (c-1))*float(avoid_ratio(n,r,c)) - 1.0)
    return s/n

def main():
    print("B16_SHAPLEY_DUMMY_WARD_CHECK")
    print("shapley_small_c:")
    for c in range(2, 6):
        Hfull, phi = shapley_entropy(c)
        target = 2.0 / (1 << (c-2))
        assert isclose(Hfull, 2.0, rel_tol=0.0, abs_tol=1e-12)
        assert all(isclose(x, target, rel_tol=0.0, abs_tol=2e-12) for x in phi)
        Hc = one_subcube_entropy_bits(c)
        print(f"c={c} players={len(phi)} H_face={Hfull:.12f} "
              f"phi={phi[0]:.12f} target={target:.12f} "
              f"H_generator={Hc:.12f} curvature_refund={Hc-target:.12f}")
    print("multiplier_table: n r raw_A corrected_A exact_closed")
    for n in (10,20,40,80):
        for r in (1,2,3):
            raw = raw_multiplier(n,r)
            corr = corrected_multiplier_exact(n,r)
            closed = corrected_closed_form(n,r)
            assert corr == closed
            assert abs(float(corr)) <= 2.0
            print(f"{n} {r} {raw:.12f} {float(corr):.12f} "
                  f"{closed.numerator}/{closed.denominator}")
    print("all_modes_uniform_bound:")
    count = 0
    max_abs = Fraction(0,1)
    argmax = None
    for n in range(2,101):
        for r in range(1,n):
            a = corrected_multiplier_exact(n,r)
            assert a == corrected_closed_form(n,r)
            if abs(a) > max_abs:
                max_abs = abs(a); argmax=(n,r,a)
            assert abs(a) <= 2
            count += 1
    print(f"exact_cases={count} max_abs={float(max_abs):.12f} argmax={argmax}")
    print("PASS")

if __name__ == "__main__":
    main()
