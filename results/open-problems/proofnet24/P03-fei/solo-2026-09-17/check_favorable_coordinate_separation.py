#!/usr/bin/env python3
"""Exact checks for FAVORABLE_COORDINATE_SEPARATION_2026-09-18.md."""
from fractions import Fraction as F
from pathlib import Path
import json

from certify_nand80 import IV, h, LN2_LO, LN2_HI, rational_interval
from check_logarithmic_structures import indicator_metrics, kedge, log2, overlap
from check_unequal_nand_potential import potential
from check_shannon_potential_barrier import bent_values, formulas as full_formulas


def cterm(q):
    return IV(2*q/LN2_HI, 2*q/LN2_LO)


def restrict(values, n, i, bit):
    out = []
    for y in range(1 << (n-1)):
        low = y & ((1 << i)-1)
        high = y >> i
        x = low | (bit << i) | (high << (i+1))
        out.append(values[x])
    return out


def data_branch_formulas(m):
    e = F(1, 1 << (m//2))
    d = m-2
    M = 1 << d
    rootM = 1 << (d//2)
    zp = e*e*(1-e)**2
    zm = e*e*(1+e)**2
    y = e**4
    nplus = (M+rootM)//2
    nminus = (M-rootM)//2
    kdata = F(d*M, 4)*kedge(zp, zm)
    kcross = y*((nplus-1)*log2(zp/y)+nminus*log2(zm/y))
    marked = (kdata+2*kcross+2*h(y)+d*h(zp)
              +cterm(2*y+d*zp))
    unmarked = h(e*e)+cterm(e*e)
    return marked, unmarked


def main():
    rows = []
    for m in range(2, 13, 2):
        N = 1 << m
        g = bent_values(m)
        gp = g[:]
        gp[0] *= -1
        a = [(1-v)//2 for v in g]+[(1-v)//2 for v in gp]
        n = m+1
        va = potential(indicator_metrics(a))[-1]
        b0 = potential(indicator_metrics(restrict(a, n, 0, 0)))[-1]
        b1 = potential(indicator_metrics(restrict(a, n, 0, 1)))[-1]
        f0, f1 = data_branch_formulas(m)
        overlap(b0, f0)
        overlap(b1, f1)
        full0, full1, fullA = full_formulas(m)
        overlap(va, fullA)
        selector_defect = fullA-(full0+full1)*F(1, 2)
        data_defect = va-(b0+b1)*F(1, 2)
        if m >= 6:
            assert data_defect.lo > 0
            assert selector_defect.lo > 0
        boolean_data_influence = F(1, 2)+F(1, N)
        boolean_selector_influence = F(1, N)
        rows.append({
            'm': m,
            'marked_data_branch_V': rational_interval(b0),
            'unmarked_data_branch_V': rational_interval(b1),
            'data_defect': rational_interval(data_defect),
            'selector_defect': rational_interval(selector_defect),
            'data_defect_over_boolean_influence':
                rational_interval(data_defect*(1/boolean_data_influence)),
            'selector_defect_over_boolean_influence':
                rational_interval(selector_defect*(1/boolean_selector_influence)),
        })
    result = {
        'status': 'PASS',
        'arithmetic': 'exact rational arithmetic and 160-bit outward rational logarithm intervals',
        'dimensions_checked': [row['m'] for row in rows],
        'all_coordinate_defects_positive_for_checked_m': [6, 8, 10, 12],
        'rows': rows,
        'scope': ('Finite Walsh checks only. The eventual all-coordinate positivity '
                  'and asymptotic separation are proved algebraically in the note; '
                  'no independent audit.')
    }
    Path('favorable_coordinate_separation_certificate.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps({
        'status': result['status'],
        'dimensions_checked': result['dimensions_checked'],
        'positive_dimensions': result['all_coordinate_defects_positive_for_checked_m'],
        'last_row': rows[-1],
    }, indent=2))


if __name__ == '__main__':
    main()
