#!/usr/bin/env python3
"""Exact checks for SUBCUBE_PARITY_MULTIPLEXERS_2026-09-18.md."""
from fractions import Fraction as F
from math import log2
from pathlib import Path
import json

from certify_nand80 import IV, edge, h, rational_interval, wht


def prefix_label(x, m):
    """First zero in bits 0,...,m-1, or the final all-one cell."""
    for j in range(m):
        if not (x >> j) & 1:
            return j
    return m


def make_example(name, m, k, label_fn, data_masks, sign_masks, codims):
    N = 1 << (m+k)
    values = []
    labels = []
    for z in range(N):
        x = z & ((1 << m)-1)
        y = z >> m
        j = label_fn(x)
        labels.append(j)
        parity = ((y & data_masks[j]).bit_count()
                  +(x & sign_masks[j]).bit_count()) & 1
        values.append(1 if parity == 0 else -1)

    coeff = [F(v, N) for v in wht(values)]
    p = [a*a for a in coeff]
    entropy = sum((h(q) for q in p), IV(0))
    influence = sum((S.bit_count()*p[S] for S in range(N)), F(0))

    # The first m coordinates are selector coordinates in this indexing.
    selector_influence = sum(
        F(sum(values[z] != values[z ^ (1 << i)] for z in range(N)), N)
        for i in range(m)
    )

    probs = []
    for j in range(len(data_masks)):
        probs.append(F(sum(label_fn(x) == j for x in range(1 << m)), 1 << m))
    assert all(probs[j] == F(1, 1 << codims[j]) for j in range(len(probs)))
    label_entropy = sum((-q*F(codims[j]) for j, q in enumerate(probs)), F(0))
    # Correct the sign: log_2(delta_j)=-codim.
    label_entropy = -label_entropy

    # Check each distinct data label has uniform conditional selector spectrum.
    for j, dmask in enumerate(data_masks):
        masses = []
        for smask in range(1 << m):
            masses.append(p[smask | (dmask << m)])
        positive = [q for q in masses if q]
        assert len(positive) == 1 << codims[j]
        assert all(q == probs[j]*probs[j] for q in positive)

    predicted = IV(2*label_entropy)
    assert max(entropy.lo, predicted.lo) <= min(entropy.hi, predicted.hi)
    assert entropy.hi <= (4*selector_influence)

    # Exact aggregate erasure B and its data-coordinate part.
    B = IV(0)
    By = IV(0)
    for i in range(m+k):
        term = sum((edge(p[S], p[S | (1 << i)])
                    for S in range(N) if not S & (1 << i)), IV(0))
        B += term
        if i >= m:
            By += term
    assert By.hi <= (2*selector_influence)
    assert B.hi <= entropy.hi

    return {
        'name': name,
        'selector_bits': m,
        'data_bits': k,
        'cells': len(data_masks),
        'codimensions': codims,
        'label_probabilities': [str(q) for q in probs],
        'H_label_exact': str(label_entropy),
        'H_fourier': rational_interval(entropy),
        'selector_influence_exact': str(selector_influence),
        'total_influence_exact': str(influence),
        'data_erasure': rational_interval(By),
        'total_erasure': rational_interval(B),
    }


def main():
    examples = []

    # Variable-depth prefix partition: codimensions 1,2,3,3.
    examples.append(make_example(
        'prefix_1_2_3_3', 3, 2,
        lambda x: prefix_label(x, 3),
        [0, 1, 2, 3], [0, 2, 4, 3], [1, 2, 3, 3]))

    # Four equal codimension-two cells, labeled by all two-bit parities.
    examples.append(make_example(
        'four_equal_cells', 4, 2,
        lambda x: x & 3,
        [0, 1, 2, 3], [0, 4, 8, 12], [2, 2, 2, 2]))

    # Full addressing: every selector point has its own data parity label.
    examples.append(make_example(
        'point_addressing', 3, 3,
        lambda x: x,
        list(range(8)), [0, 1, 2, 3, 4, 5, 6, 7], [3]*8))

    # Standard addressing: selector point j chooses the j-th data singleton.
    examples.append(make_example(
        'standard_addressing', 3, 8,
        lambda x: x,
        [1 << j for j in range(8)], [0]*8, [3]*8))

    result = {
        'status': 'PASS',
        'arithmetic': ('exact rational Walsh coefficients and influences; '
                       '160-bit outward rational logarithm intervals'),
        'examples': examples,
        'scope': ('Finite self-checks only. The universal subcube-parity theorem '
                  'and arbitrary parity-multiplexer erasure lemma are proved '
                  'algebraically in the note; no independent audit.'),
    }
    Path('subcube_parity_multiplexer_certificate.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps({
        'status': result['status'],
        'examples': [row['name'] for row in examples],
        'last_example': examples[-1],
    }, indent=2))


if __name__ == '__main__':
    main()
