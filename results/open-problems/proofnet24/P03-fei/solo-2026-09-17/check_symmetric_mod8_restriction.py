#!/usr/bin/env python3
"""Exact checks for SYMMETRIC_MOD8_RESTRICTION_BARRIER_2026-09-18.md."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

from certify_nand80 import IV, h, LN2_LO, LN2_HI, rational_interval
from check_logarithmic_structures import indicator_metrics, kedge, overlap
from check_unequal_nand_potential import potential


def sym_values(n, shift=0):
    return [int((w+shift) % 8 in (0, 1, 2)) for w in range(n+1)]


def sym_coefficients(n, shift=0):
    values = sym_values(n, shift)
    out = []
    for k in range(n+1):
        total = 0
        for w in range(n+1):
            kw = sum((-1)**j*comb(k, j)*comb(n-k, w-j)
                     for j in range(max(0, w-(n-k)), min(k, w)+1))
            total += values[w]*kw
        out.append(F(total, 1 << n))
    return out


def sym_potential(n, shift=0):
    coeff = sym_coefficients(n, shift)
    p = [x*x for x in coeff]
    internal = sum((comb(n, k)*(n-k)*kedge(p[k], p[k+1])
                    for k in range(1, n)), IV(0))
    q = n*p[1]
    return internal+n*h(p[1])+IV(2*q/LN2_HI, 2*q/LN2_LO)


def coordinate_influence(n):
    changes = sum(comb(n-1, w)
                  for w in range(n)
                  if ((w % 8 in (0, 1, 2)) !=
                      ((w+1) % 8 in (0, 1, 2))))
    return F(changes, 1 << (n-1))


def full_values(n):
    return [int(x.bit_count() % 8 in (0, 1, 2)) for x in range(1 << n)]


def main():
    # Full-transform consistency checks are deliberately small; the exact
    # Krawtchouk calculation handles the larger certified dimensions.
    full_checks = []
    for n in (4, 8, 12):
        vals = full_values(n)
        direct = potential(indicator_metrics(vals))[-1]
        symmetric = sym_potential(n)
        overlap(direct, symmetric)
        full_checks.append(n)

    rows = []
    for n in (8, 16, 24, 32, 40, 48, 56, 64):
        parent = sym_potential(n)
        child0 = sym_potential(n-1, 0)
        child1 = sym_potential(n-1, 1)
        defect = parent-(child0+child1)*F(1, 2)
        influence = coordinate_influence(n)
        ratio = defect*(1/influence)
        if n >= 32:
            assert ratio.lo > F(n, 6)
        rows.append({
            'n': n,
            'coordinate_influence_exact': str(influence),
            'parent_V': rational_interval(parent),
            'child0_V': rational_interval(child0),
            'child1_V': rational_interval(child1),
            'restriction_defect': rational_interval(defect),
            'defect_over_coordinate_influence': rational_interval(ratio),
        })

    result = {
        'status': 'PASS',
        'family': 'A_n(x)=1 iff Hamming weight mod 8 is in {0,1,2}',
        'arithmetic': 'exact rational coefficients and 160-bit outward rational logarithm intervals',
        'full_transform_dimensions': full_checks,
        'symmetric_dimensions': [row['n'] for row in rows],
        'certified_growth': 'defect/influence > n/6 for n=32,40,48,56,64',
        'rows': rows,
        'scope': ('Finite exact checks only. The linear asymptotic with explicit '
                  'constant is proved by the root-of-unity argument in the note; '
                  'no independent audit.'),
    }
    Path('symmetric_mod8_restriction_certificate.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps({
        'status': result['status'],
        'full_transform_dimensions': full_checks,
        'symmetric_dimensions': result['symmetric_dimensions'],
        'certified_growth': result['certified_growth'],
        'last_row': rows[-1],
    }, indent=2))


if __name__ == '__main__':
    main()
