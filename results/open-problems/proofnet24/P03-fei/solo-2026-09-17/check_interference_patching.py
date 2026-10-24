#!/usr/bin/env python3
"""Exact checks for INTERFERENCE_PATCHING_THEOREM_2026-09-18.md."""
from fractions import Fraction as F
from pathlib import Path
import json

from certify_nand80 import IV, h, rational_interval, wht


def entropy(p):
    return sum((h(x) for x in p), IV(0))


def check_example(name, m, k, cells, signs, data_masks, local_C):
    nx = 1 << m
    assert len(cells) == len(signs) == nx
    js = sorted(set(cells))
    assert js == list(range(len(data_masks)))

    delta, vhats, local_rows = [], [], []
    local_sum = IV(0)
    dirichlet_sum = F(0)
    for j in js:
        d = F(cells.count(j), nx)
        v = [signs[x] if cells[x] == j else 0 for x in range(nx)]
        ahat = [F(z, nx) for z in wht(v)]
        rho = [a*a/d for a in ahat]
        assert sum(rho, F(0)) == 1
        ej = entropy(rho)
        dj = sum((s.bit_count()*ahat[s]*ahat[s] for s in range(nx)), F(0))
        assert ej.hi <= local_C*dj/d
        delta.append(d)
        vhats.append(ahat)
        local_sum += d*ej
        dirichlet_sum += dj
        local_rows.append({
            'cell': j,
            'mass_exact': str(d),
            'local_entropy': rational_interval(ej),
            'normalized_dirichlet_exact': str(dj/d),
        })

    groups = {}
    for j, a in enumerate(data_masks):
        groups.setdefault(a, []).append(j)
    coarse = []
    lambda_global = F(1)
    conditional = IV(0)
    for a, group in sorted(groups.items()):
        d = sum((delta[j] for j in group), F(0))
        coarse.append(d)
        q, mix = [], []
        for s in range(nx):
            q.append(sum((vhats[j][s] for j in group), F(0))**2/d)
            mix.append(sum((vhats[j][s]**2 for j in group), F(0))/d)
        assert sum(q, F(0)) == sum(mix, F(0)) == 1
        la = max(q[s]/mix[s] for s in range(nx) if mix[s])
        assert F(1) <= la <= len(group)
        lambda_global = max(lambda_global, la)
        conditional += d*entropy(q)
        weights = [delta[j]/d for j in group]

    # Boundary separation, partition boundary, and selector influence.
    eta = F(0)
    ix = F(0)
    for i in range(m):
        for x in range(nx):
            xp = x ^ (1 << i)
            j, ell = cells[x], cells[xp]
            if j != ell:
                eta += F(1, nx)
                disagreement = (F(1, 2) if data_masks[j] != data_masks[ell]
                                else F(signs[x] != signs[xp]))
                assert disagreement >= F(1, 2)
            else:
                disagreement = F(signs[x] != signs[xp])
            ix += disagreement/nx
    assert dirichlet_sum <= ix

    h_cell = entropy(delta)
    h_label = entropy(coarse)
    assert h_cell.hi <= eta
    assert ix >= eta/2
    assert h_cell.hi <= 2*ix

    # Full Fourier spectrum.
    n = 1 << (m+k)
    values = []
    for z in range(n):
        x, y = z & (nx-1), z >> m
        j = cells[x]
        parity = (y & data_masks[j]).bit_count() & 1
        values.append(signs[x] * (-1 if parity else 1))
    ahat = [F(z, n) for z in wht(values)]
    p = [a*a for a in ahat]
    h_full = entropy(p)
    decomposition = h_label + conditional
    assert max(h_full.lo, decomposition.lo) <= min(h_full.hi, decomposition.hi)

    patch_rhs = (lambda_global*h_cell
                 -(lambda_global-1)*h_label
                 +lambda_global*local_sum)
    # In the collision-free example the patching inequality is an equality,
    # so outward intervals necessarily overlap rather than separate.
    if lambda_global == 1:
        assert max(h_full.lo, patch_rhs.lo) <= min(h_full.hi, patch_rhs.hi)
    else:
        assert h_full.hi <= patch_rhs.lo
    assert h_full.hi <= lambda_global*(local_C+2)*ix

    return {
        'name': name,
        'selector_bits': m,
        'data_bits': k,
        'cells': len(js),
        'interference_exact': str(lambda_global),
        'local_constant_certified': str(local_C),
        'H_partition': rational_interval(h_cell),
        'H_data_label': rational_interval(h_label),
        'local_entropy_weighted_sum': rational_interval(local_sum),
        'cell_dirichlet_sum_exact': str(dirichlet_sum),
        'selector_influence_exact': str(ix),
        'H_fourier': rational_interval(h_full),
        'local_cells': local_rows,
    }


def main():
    examples = [
        # Neither cell is a subcube. Distinct labels give Lambda=1.
        check_example(
            'irregular_two_cell_patch', 3, 1,
            [0, 0, 0, 1, 1, 1, 1, 1],
            [1, -1, 1, 1, -1, 1, -1, 1],
            [0, 1], F(2)),

        # Point cells; antipodes 000 and 111 collide coherently at one label.
        check_example(
            'coherent_antipodal_point_patch', 3, 3,
            list(range(8)), [1]*8,
            [0, 1, 2, 3, 4, 5, 6, 0], F(2)),
    ]
    result = {
        'status': 'PASS',
        'arithmetic': ('exact rational Walsh coefficients, energies and '
                       'influences; 160-bit outward rational logarithm intervals'),
        'examples': examples,
        'scope': ('Finite self-checks only. The universal patching and nonreuse '
                  'theorems are proved algebraically in the note; no independent audit.'),
    }
    Path('interference_patching_certificate.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps({
        'status': result['status'],
        'examples': [{
            'name': x['name'],
            'Lambda': x['interference_exact'],
            'H': x['H_fourier'],
            'I_x': x['selector_influence_exact'],
        } for x in examples],
    }, indent=2))


if __name__ == '__main__':
    main()
