#!/usr/bin/env python3
"""Exact/rational-interval checks for UNEQUAL_NAND_CONTRACTION_2026-09-18.md."""
from fractions import Fraction as F
from pathlib import Path
import json

from certify_nand80 import wht, IV, h, LN2_LO, LN2_HI, rational_interval
from check_logarithmic_structures import indicator_metrics, kedge, overlap, log2


def potential(metrics):
    alpha, K, Q, influence, U = metrics
    V = U + IV(2*Q/LN2_HI, 2*Q/LN2_LO)
    return alpha, K, Q, influence, U, V


def boolean_k(a):
    values = [1-2*x for x in a]
    N = len(a)
    n = N.bit_length()-1
    coeff = [F(x, N) for x in wht(values)]
    p = [x*x for x in coeff]
    return sum((kedge(p[S], p[S | (1 << i)])
                for i in range(n) for S in range(N)
                if not S & (1 << i)), IV(0))


def unequal_checks():
    seeds = [
        [1, 0], [0, 1], [1, 0, 0, 0], [1, 1, 1, 0],
        [1, 0, 1, 1], [1]*7+[0], [1, 1, 0, 0, 1, 0, 1, 0]
    ]
    records = []
    for i, a in enumerate(seeds):
        ma = potential(indicator_metrics(a))
        for j, b in enumerate(seeds):
            mb = potential(indicator_metrics(b))
            product = [x*y for x in a for y in b]
            out = [1-x for x in product]
            mo = potential(indicator_metrics(out))
            aa, _, Qa, Ia, Ua, Va = ma
            ab, _, Qb, Ib, Ub, Vb = mb
            ao, _, Qo, Io, Uo, Vo = mo
            assert ao == 1-aa*ab
            assert Io == ab*Ia+aa*Ib
            assert Qo == ab*ab*Qa+aa*aa*Qb
            correction = ((log2(aa)*(1-ab)-log2(ab)*ab)*(2*ab*Qa)
                          +(log2(ab)*(1-aa)-log2(aa)*aa)*(2*aa*Qb))
            overlap(Uo, Ua*ab+Ub*aa+correction)
            rhs = Va*ab+Vb*aa
            assert Vo.hi <= rhs.lo
            records.append({'left_seed': i, 'right_seed': j,
                            'V_out': rational_interval(Vo),
                            'weighted_child_V': rational_interval(rhs)})
    return records


def transfer_checks():
    records = []
    for n in range(1, 4):
        N = 1 << n
        for label in range(1, (1 << N)-1):
            a = [(label >> x) & 1 for x in range(N)]
            alpha, K, Q, influence, U, V = potential(indicator_metrics(a))
            KF = boolean_k(a)
            assert KF.hi <= (4*U).lo
            records.append([n, label])
    return records


def recursive_literal_checks():
    # Deterministic unequal read-once shapes.  Each state is a truth table and
    # a list of its variables; products below are on disjoint blocks.
    states = [([1, 0], 1), ([0, 1], 1)]
    records = []
    for depth in range(1, 7):
        a, na = states[-1]
        b = [1, 0] if depth % 2 else [0, 1]
        product = [x*y for x in a for y in b]
        out = [1-x for x in product]
        mo = potential(indicator_metrics(out))
        _, _, _, influence, _, V = mo
        bound = IV(F(1,2)+F(1,2)/LN2_HI,
                   F(1,2)+F(1,2)/LN2_LO)
        assert (V*(1/influence)).hi <= bound.lo
        KF = boolean_k(out)
        final_bound = IV(F(2)+F(2)/LN2_HI,
                         F(2)+F(2)/LN2_LO)
        assert (KF*(1/influence)).hi <= final_bound.lo
        records.append({'depth': depth, 'variables': na+1,
                        'V_over_I': rational_interval(V*(1/influence)),
                        'K_over_I': rational_interval(KF*(1/influence))})
        states.append((out, na+1))
    return records


def main():
    unequal = unequal_checks()
    transfer = transfer_checks()
    recursive = recursive_literal_checks()
    result = {
        'status': 'PASS',
        'arithmetic': 'exact rational arithmetic and 160-bit outward rational logarithm intervals',
        'unequal_seed_pair_checks': len(unequal),
        'unequal_records': unequal,
        'boolean_transfer_checks': len(transfer),
        'boolean_transfer_range': 'every nonconstant indicator truth table through n=3',
        'recursive_literal_checks': recursive,
        'scope': 'Finite self-checks only. Universal claims are proved algebraically in the note; no independent audit.'
    }
    Path('unequal_nand_potential_certificate.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps({
        'status': result['status'],
        'unequal_seed_pair_checks': len(unequal),
        'boolean_transfer_checks': len(transfer),
        'recursive_literal_checks': len(recursive),
        'last_recursive': recursive[-1]
    }, indent=2))


if __name__ == '__main__':
    main()
