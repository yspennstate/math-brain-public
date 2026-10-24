#!/usr/bin/env python3
"""Exact checks for BOUNDED_COLLISION_PARITY_MULTIPLEXERS_2026-09-18.md."""
from fractions import Fraction as F
from pathlib import Path
import json

from certify_nand80 import IV, h, rational_interval, wht


def entropy(probabilities):
    return sum((h(p) for p in probabilities), IV(0))


def overlap(a, b):
    return max(a.lo, b.lo) <= min(a.hi, b.hi)


def make_example(name, m, k, label_fn, data_masks, sign_masks, codims):
    cells = len(data_masks)
    nx = 1 << m
    n = 1 << (m+k)
    labels = [label_fn(x) for x in range(nx)]
    assert set(labels) == set(range(cells))

    delta = [F(labels.count(j), nx) for j in range(cells)]
    assert all(delta[j] == F(1, 1 << codims[j]) for j in range(cells))
    h_j = sum((delta[j]*codims[j] for j in range(cells)), F(0))

    # Cell coefficient functions v_j on selector space.
    vhat = []
    for j in range(cells):
        v = [
            (1 if (x & sign_masks[j]).bit_count() % 2 == 0 else -1)
            if labels[x] == j else 0
            for x in range(nx)
        ]
        vhat.append([F(z, nx) for z in wht(v)])
        positive = [a*a for a in vhat[-1] if a]
        assert len(positive) == 1 << codims[j]
        assert all(p == delta[j]*delta[j] for p in positive)

    groups = {}
    for j, a in enumerate(data_masks):
        groups.setdefault(a, []).append(j)
    R = max(map(len, groups.values()))

    group_rows = []
    coarse = []
    conditional_actual = IV(0)
    conditional_bound = IV(0)
    interference = F(1)
    for a, group in sorted(groups.items()):
        d = sum((delta[j] for j in group), F(0))
        coarse.append(d)
        q = []
        mix = []
        for s in range(nx):
            q.append(sum((vhat[j][s] for j in group), F(0))**2/d)
            mix.append(sum((vhat[j][s]**2 for j in group), F(0))/d)
        assert sum(q, F(0)) == 1
        assert sum(mix, F(0)) == 1
        assert all(q[s] <= len(group)*mix[s] for s in range(nx))
        lambda_a = max(q[s]/mix[s] for s in range(nx) if mix[s])
        assert F(1) <= lambda_a <= len(group)
        interference = max(interference, lambda_a)

        hq = entropy(q)
        hm = entropy(mix)
        assert hq.hi <= (len(group)*hm).lo

        weights = [delta[j]/d for j in group]
        component_bound = entropy(weights) + sum(
            (weights[t]*codims[j] for t, j in enumerate(group)), IV(0))
        assert hm.hi <= component_bound.lo
        conditional_actual += d*hq
        conditional_bound += d*R*component_bound
        group_rows.append({
            'data_mask': a,
            'cells': group,
            'multiplicity': len(group),
            'mass_exact': str(d),
            'interference_exact': str(lambda_a),
            'H_actual_conditional': rational_interval(hq),
            'H_incoherent_mixture': rational_interval(hm),
            'pointwise_domination_exact': True,
        })

    # Boundary separation and exact selector influence.
    eta = F(0)
    ix = F(0)
    min_cross_disagreement = F(1)
    for i in range(m):
        changes = 0
        disagreements = F(0)
        for x in range(nx):
            xp = x ^ (1 << i)
            j, ell = labels[x], labels[xp]
            if j != ell:
                changes += 1
                # Two distinct parity characters disagree on exactly half of y;
                # equal characters disagree always or never according to signs.
                if data_masks[j] != data_masks[ell]:
                    dxy = F(1, 2)
                else:
                    sj = (x & sign_masks[j]).bit_count() & 1
                    sl = (xp & sign_masks[ell]).bit_count() & 1
                    dxy = F(sj != sl)
                min_cross_disagreement = min(min_cross_disagreement, dxy)
                disagreements += dxy
            else:
                sj = (x & sign_masks[j]).bit_count() & 1
                sl = (xp & sign_masks[j]).bit_count() & 1
                disagreements += F(sj != sl)
        eta += F(changes, nx)
        ix += disagreements/nx
    assert min_cross_disagreement >= F(1, 2)
    assert eta >= h_j
    assert ix >= eta/2

    # Full truth table and Fourier law.
    values = []
    for z in range(n):
        x = z & (nx-1)
        y = z >> m
        j = labels[x]
        parity = ((x & sign_masks[j]).bit_count()
                  +(y & data_masks[j]).bit_count()) & 1
        values.append(1 if parity == 0 else -1)
    coeff = [F(z, n) for z in wht(values)]
    p = [a*a for a in coeff]
    h_full = entropy(p)
    h_coarse = entropy(coarse)
    decomposed = h_coarse + conditional_actual
    assert overlap(h_full, decomposed)

    sharp_bound = IV(2*interference*h_j) - (interference-1)*h_coarse
    theorem_bound = F(2*interference)*h_j
    influence_bound = F(4*interference)*ix
    assert h_full.hi <= sharp_bound.lo
    assert h_full.hi <= theorem_bound
    assert h_full.hi <= influence_bound

    return {
        'name': name,
        'selector_bits': m,
        'data_bits': k,
        'cells': cells,
        'collision_multiplicity': R,
        'interference_exact': str(interference),
        'H_cell_exact': str(h_j),
        'H_coarse_label': rational_interval(h_coarse),
        'H_fourier': rational_interval(h_full),
        'selector_influence_exact': str(ix),
        'cell_boundary_sum_exact': str(eta),
        'minimum_cross_boundary_disagreement_exact': str(min_cross_disagreement),
        'groups': group_rows,
    }


def main():
    examples = [
        # Four codimension-two cells. Cells 0 and 3 reuse label zero but are
        # diagonal, so no selector edge joins the equal-label pair.
        make_example(
            'diagonal_collision_equal_cells', 4, 2,
            lambda x: x & 3,
            [0, 1, 2, 0], [0, 4, 8, 12], [2, 2, 2, 2]),

        # Point cells on a three-cube; antipodes 000 and 111 reuse label zero.
        # Every cube edge still crosses two distinct data labels.
        make_example(
            'antipodal_collision_point_cells', 3, 3,
            lambda x: x,
            [0, 1, 2, 3, 4, 5, 6, 0], [0]*8, [3]*8),
    ]
    result = {
        'status': 'PASS',
        'arithmetic': ('exact rational Walsh coefficients, probabilities and '
                       'influences; 160-bit outward rational logarithm intervals'),
        'examples': examples,
        'scope': ('Finite self-checks only. The universal bounded-collision '
                  'theorem is proved algebraically in the note; no independent audit.'),
    }
    Path('bounded_collision_parity_multiplexer_certificate.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps({
        'status': result['status'],
        'examples': [row['name'] for row in examples],
        'summaries': [{
            'name': row['name'],
            'R': row['collision_multiplicity'],
            'Lambda': row['interference_exact'],
            'H_fourier': row['H_fourier'],
            'I_x': row['selector_influence_exact'],
        } for row in examples],
    }, indent=2))


if __name__ == '__main__':
    main()
