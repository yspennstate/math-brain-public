#!/usr/bin/env python3
"""Exact constants and independent matrix audits for PROOF.md (stdlib only)."""
from fractions import Fraction as Q
from math import factorial, isqrt
from pathlib import Path
import json
import os
import random
import resource
import time

START = time.monotonic()
C = Q(121, 147)


def guard():
    assert os.environ['OMP_NUM_THREADS'] == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 128*1024**2
    assert time.monotonic()-START < 120


def squared_bound(r, k):
    assert k >= 2 and k % 2 == 0
    return r**(2*k)*(k*(k+(k-1)*C))**(k//2)/factorial(k)**2


def product_bound(r, k):
    # The product contains every factorial denominator once in each copy.
    # It does not call factorial or use the exponent k/2 from squared_bound.
    result = Q(1)
    row_product = k*(k+(k-1)*C)
    for j in range(1, k+1):
        result *= r*r/(j*j)
        if j % 2 == 0:
            result *= row_product
    return result


def enclosure(value, digits=12):
    scale = 10**digits
    lo = isqrt(value.numerator*scale**2//value.denominator)
    assert Q(lo,scale)**2 <= value < Q(lo+1,scale)**2
    return Q(lo,scale), Q(lo+1,scale)


def constants():
    rows = []
    comparisons = 0
    for r in (Q(1,2), Q(1), Q(2)):
        first = None
        for k in range(2, 101, 2):
            guard()
            value = squared_bound(r, k)
            assert value == product_bound(r, k)
            comparisons += 1
            if first is None and value <= Q(1,10**12):
                first = k
        assert first is not None
        value = squared_bound(r, first)
        lo, hi = enclosure(value)
        prev_lo, prev_hi = enclosure(squared_bound(r, first-2))
        rows.append(dict(R=str(r), first_even_order=first,
                         lower=str(lo), upper=str(hi),
                         preceding_even_order_lower=str(prev_lo),
                         preceding_even_order_upper=str(prev_hi)))
    assert [row['first_even_order'] for row in rows] == [14,26,58]
    value = squared_bound(Q(2),58)
    assert Q(913316,10**12)**2 < value < Q(913317,10**12)**2 < Q(1,10**12)
    assert all(squared_bound(Q(2), k)>Q(1,10**12) for k in range(2,58,2))
    assert Q(390,58) == Q(195,29)
    # Independent elementary verification of the integrand division used
    # to certify pi<22/7. Coefficients are in ascending order.
    quotient = [4,0,-4,0,5,-4,1]
    product = [0]*9
    for i, a in enumerate(quotient):
        product[i] += a
        product[i+2] += a
    product[0] -= 4
    numerator = [0,0,0,0,1,-4,6,-4,1]
    assert product == numerator
    integral_polynomial = sum((Q(a,i+1) for i,a in enumerate(quotient)),Q(0))
    assert integral_polynomial == Q(22,7)
    return dict(rows=rows, direct_vs_product_checks=comparisons,
                polynomial_division_and_integral_exact=True,
                R2_squared_bound=str(value))


def determinant(a):
    # Rational Gaussian elimination, independent of the Pfaffian expansion.
    b = [row[:] for row in a]
    answer = Q(1)
    for i in range(len(b)):
        pivot = next((j for j in range(i,len(b)) if b[j][i]), None)
        if pivot is None:
            return Q(0)
        if pivot != i:
            b[pivot],b[i] = b[i],b[pivot]
            answer = -answer
        d = b[i][i]
        answer *= d
        for j in range(i+1,len(b)):
            q = b[j][i]/d
            for l in range(i+1,len(b)):
                b[j][l] -= q*b[i][l]
    return answer


def pfaffian(a):
    n = len(a)
    if n == 0:
        return Q(1)
    result = Q(0)
    for j in range(1,n):
        keep = [l for l in range(1,n) if l != j]
        minor = [[a[l][m] for m in keep] for l in keep]
        result += (-1)**(j+1)*a[0][j]*pfaffian(minor)
    return result


def matrices():
    # These are exact abstract matrices satisfying the scaled kernel entry
    # constraints. They are not samples of the GOE process. They test the
    # determinant exponent, diagonal terms and congruence algebra.
    rng = random.Random(89058)
    unit_pairs = [(Q(1),Q(0)), (Q(0),Q(1)),
                  (Q(3,5),Q(4,5)), (Q(5,13),Q(12,13))]
    cases = congruences = 0
    for k in range(1,5):
        for trial in range(30):
            guard()
            b = [[Q(0) for _ in range(2*k)] for _ in range(2*k)]
            for i in range(k):
                b[2*i][2*i+1],b[2*i+1][2*i] = Q(1),Q(-1)
            for i in range(k):
                for j in range(i+1,k):
                    s,d = rng.choice(unit_pairs)
                    s *= rng.choice([-1,1])
                    d *= rng.choice([-1,1])
                    p = rng.choice([Q(-9,10),Q(0),Q(9,10)])
                    # B_ij = [[p,s],[-s,d]], B_ji=-transpose(B_ij).
                    for ii,jj,v in [(2*i,2*j,p),(2*i,2*j+1,s),
                                    (2*i+1,2*j,-s),(2*i+1,2*j+1,d)]:
                        b[ii][jj],b[jj][ii] = v,-v
                    assert s*s+d*d == 1 and p*p <= C
            row_squares = [sum(v*v for v in row) for row in b]
            for i in range(k):
                assert row_squares[2*i] <= k+(k-1)*C
                assert row_squares[2*i+1] <= k
            det_b = determinant(b)
            pf_b = pfaffian(b)
            assert det_b == pf_b*pf_b
            # Hadamard and the two row types, without taking any roots.
            product = Q(1)
            for n in row_squares:
                product *= n
            assert det_b*det_b <= product <= (k*(k+(k-1)*C))**k
            # Verify determinant-one congruence both for determinant and Pf.
            scales = [q for _ in range(k) for q in (Q(2),Q(1,2))]
            a = [[b[i][j]/(scales[i]*scales[j]) for j in range(2*k)]
                 for i in range(2*k)]
            assert determinant(a) == det_b
            assert pfaffian(a) == pf_b
            cases += 1
            congruences += 1
    return dict(exact_antisymmetric_matrix_cases=cases,
                determinant_vs_pfaffian=cases,
                determinant_one_congruences=congruences,
                row_type_and_Hadamard_checks=cases)


def main():
    guard()
    result = dict(constants=constants(), matrices=matrices())
    guard()
    result['resources'] = dict(OMP_NUM_THREADS=os.environ['OMP_NUM_THREADS'],
        nice=os.getpriority(os.PRIO_PROCESS,0),
        peak_rss_bytes_macos=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        measured_rss_guard_bytes=128*1024**2, elapsed_guard_seconds=120,
        elapsed_seconds=round(time.monotonic()-START,3), os_hard_memory_cap=False)
    Path(__file__).with_name('remainder_data.json').write_text(json.dumps(result,indent=2)+'\n')
    print('All exact remainder and matrix checks passed.')
    for key,value in result.items():
        print(key+': '+json.dumps(value,sort_keys=True))


if __name__ == '__main__':
    main()
