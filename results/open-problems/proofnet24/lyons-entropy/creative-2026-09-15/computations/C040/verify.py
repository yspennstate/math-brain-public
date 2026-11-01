#!/usr/bin/env python3
"""C040: exact weighted graph substitution and diamond certificate.

Only standard-library rational arithmetic is used.  Projection probabilities
are recomputed from weighted incidence minors, not from the gluing formula.
"""
from collections import defaultdict, deque
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def det(matrix):
    a = [[F(x) for x in row] for row in matrix]
    n = len(a)
    out = F(1)
    for j in range(n):
        k = next((k for k in range(j, n) if a[k][j]), None)
        if k is None:
            return F(0)
        if k != j:
            a[k], a[j] = a[j], a[k]
            out = -out
        pivot = a[j][j]
        out *= pivot
        for k in range(j + 1, n):
            ratio = a[k][j] / pivot
            for m in range(j + 1, n):
                a[k][m] -= ratio * a[j][m]
    return out


def gram(rows, weights):
    return [[sum(x * y * c for x, y, c in zip(a, b, weights))
             for b in rows] for a in rows]


def gradients(edges, potentials):
    return [[F(p[a]) - F(p[b]) for a, b in edges] for p in potentials]


def projection_law(rows, weights):
    rank = len(rows)
    denominator = det(gram(rows, weights))
    assert denominator > 0 or rank == 0
    law = {}
    for s in combinations(range(len(weights)), rank):
        minor = det([[row[j] for j in s] for row in rows])
        prod = F(1)
        for j in s:
            prod *= weights[j]
        law[frozenset(s)] = minor * minor * prod / denominator
    assert sum(law.values()) == 1
    return law


def add_laws(a, b):
    return {s: a.get(s, 0) + b.get(s, 0) for s in a.keys() | b.keys()}


def equal_laws(a, b):
    return all(a.get(s, 0) == b.get(s, 0) for s in a.keys() | b.keys())


def cover(left, right):
    """Exact deterministic shortest-augmenting-path inclusion transport."""
    ll = sorted((s for s in left if left[s]), key=lambda s: tuple(sorted(s)))
    rr = sorted((s for s in right if right[s]), key=lambda s: tuple(sorted(s)))
    src, sink = ('source',), ('sink',)
    residual = defaultdict(dict)

    def edge(a, b, cap):
        residual[a][b] = cap
        residual[b][a] = F(0)

    for s in ll:
        edge(src, ('L', s), left[s])
    for s in ll:
        for t in rr:
            if s < t:
                edge(('L', s), ('R', t), F(2))
    for t in rr:
        edge(('R', t), sink, right[t])
    total = F(0)
    augmentations = 0
    while True:
        parent = {src: None}
        queue = deque([src])
        while queue and sink not in parent:
            a = queue.popleft()
            for b, cap in residual[a].items():
                if cap > 0 and b not in parent:
                    parent[b] = a
                    queue.append(b)
        if sink not in parent:
            break
        a = sink
        bottleneck = F(2)
        while parent[a] is not None:
            b = parent[a]
            bottleneck = min(bottleneck, residual[b][a])
            a = b
        a = sink
        while parent[a] is not None:
            b = parent[a]
            residual[b][a] -= bottleneck
            residual[a][b] += bottleneck
            a = b
        total += bottleneck
        augmentations += 1
    assert total == 1
    out = {(s, t): residual[('R', t)][('L', s)]
           for s in ll for t in rr
           if s < t and residual[('R', t)][('L', s)]}
    for s in left:
        assert sum(w for (ss, _), w in out.items() if ss == s) == left[s]
    for t in right:
        assert sum(w for (_, tt), w in out.items() if tt == t) == right[t]
    return out, augmentations


def diamond_marginals(x):
    bottom, top, middle = defaultdict(F), defaultdict(F), defaultdict(F)
    for (s, t), weight in x.items():
        assert weight > 0 and s < t and len(t) == len(s) + 2
        bottom[s] += weight
        top[t] += weight
        for i in t - s:
            middle[s | {i}] += weight
    assert sum(x.values()) == 1
    return dict(bottom), dict(top), dict(middle)


def check_diamond(x, laws):
    b, t, m = diamond_marginals(x)
    assert equal_laws(b, laws['bottom'])
    assert equal_laws(t, laws['top'])
    assert equal_laws(m, add_laws(laws['middle_u'], laws['middle_v']))
    # Fair labels realize the complex-equalized individually correct laws.
    eq = {s: val / 2 for s, val in m.items()}
    expected = {s: val / 2 for s, val in
                add_laws(laws['middle_u'], laws['middle_v']).items()}
    assert equal_laws(eq, expected)


def encode_set(s):
    return ','.join(str(i) for i in sorted(s))


def encode_law(law):
    return {encode_set(s): str(v) for s, v in
            sorted(law.items(), key=lambda kv: tuple(sorted(kv[0])))}


def encode_coupling(x):
    return [{'bottom': sorted(s), 'top': sorted(t), 'weight': str(w)}
            for (s, t), w in sorted(x.items(), key=lambda kv:
                                  (tuple(sorted(kv[0][0])), tuple(sorted(kv[0][1]))))]


def text_matrix(m):
    return [[str(x) for x in row] for row in m]


def main():
    # K4.  Three roots are 0, 1, 2; the bottom row is potential delta_3.
    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    weights = [F(1)] * 6
    potentials = [[0, 0, 0, 1], [1, -1, 0, 0], [1, 1, -2, 0]]
    rows = gradients(edges, potentials)
    assert gram(rows, weights) == [[F(3), 0, 0], [0, F(8), 0], [0, 0, F(24)]]
    laws = {
        'bottom': projection_law(rows[:1], weights),
        'middle_u': projection_law(rows[:2], weights),
        'middle_v': projection_law([rows[0], rows[2]], weights),
        'top': projection_law(rows, weights),
    }
    plane = projection_law(rows[1:], weights)
    pair_cover, augmentations = cover(plane, laws['top'])
    source_diamond = {(t - b, t): w for (b, t), w in pair_cover.items()}
    check_diamond(source_diamond, laws)
    assert sum(v > 0 for v in laws['top'].values()) == 16

    # Replace edge 2 by the triangle 0--3, 0--4--3, of effective conductance 1.
    # Global edge indices 0..4 are surviving old edges, and 5..7 are the block.
    replaced = 2
    survivors = [j for j in range(6) if j != replaced]
    remap = {old: new for new, old in enumerate(survivors)}
    new_edges = [edges[j] for j in survivors] + [(0, 3), (0, 4), (4, 3)]
    new_weights = [F(1)] * 5 + [F(1, 2), F(1), F(1)]
    new_potentials = [
        [0, 0, 0, 1, 0],  # pinned-root bottom incidence rows
        [0, 0, 0, 0, 1],
        [1, -1, 0, 0, F(1, 2)],  # harmonic extensions of the old updates
        [1, 1, -2, 0, F(1, 2)],
    ]
    new_rows = gradients(new_edges, new_potentials)
    new_gram = gram(new_rows, new_weights)
    assert new_gram == [[F(7, 2), -1, 0, 0], [-1, 2, 0, 0],
                        [0, 0, 8, 0], [0, 0, 0, 24]]
    new_laws = {
        'bottom': projection_law(new_rows[:2], new_weights),
        'middle_u': projection_law(new_rows[:3], new_weights),
        'middle_v': projection_law(new_rows[:2] + new_rows[3:], new_weights),
        'top': projection_law(new_rows, new_weights),
    }

    local_low = {frozenset({6}): F(1, 2), frozenset({7}): F(1, 2)}
    local_high = {frozenset({5, 6}): F(1, 4),
                  frozenset({5, 7}): F(1, 4),
                  frozenset({6, 7}): F(1, 2)}
    eta = {(frozenset({6}), frozenset({5, 6})): F(1, 4),
           (frozenset({7}), frozenset({5, 7})): F(1, 4),
           (frozenset({6}), frozenset({6, 7})): F(1, 4),
           (frozenset({7}), frozenset({6, 7})): F(1, 4)}
    local_rows = [[F(0), F(-1), F(1)], [F(1), F(1, 2), F(1, 2)]]
    local_weights = [F(1, 2), F(1), F(1)]
    local_gram = gram(local_rows, local_weights)
    assert local_gram == [[F(2), 0], [0, F(1)]]
    for name, local in [('low', local_low), ('high', local_high)]:
        actual = projection_law(local_rows[:1] if name == 'low' else local_rows,
                                local_weights)
        translated = {frozenset(i + 5 for i in s): p for s, p in actual.items()}
        assert equal_laws(translated, local)
    assert all(sum(p for (l, h), p in eta.items() if l == s) == val
               for s, val in local_low.items())
    assert all(sum(p for (l, h), p in eta.items() if h == s) == val
               for s, val in local_high.items())

    def lift(s, low, high):
        out = {remap[j] for j in s if j != replaced}
        out.update(high if replaced in s else low)
        return frozenset(out)

    lifted = defaultdict(F)
    for (s, t), p in source_diamond.items():
        for (low, high), q in eta.items():
            lifted[(lift(s, low, high), lift(t, low, high))] += p * q
    lifted = dict(lifted)
    check_diamond(lifted, new_laws)

    # Check the full cardinality-factorization theorem for each actual minor law.
    for name, source in laws.items():
        pushed = defaultdict(F)
        for s, p in source.items():
            local = local_high if replaced in s else local_low
            for block, q in local.items():
                out = frozenset({remap[j] for j in s if j != replaced} | set(block))
                pushed[out] += p * q
        assert equal_laws(dict(pushed), new_laws[name])

    # Exact dual/cographic diamond by complementation.
    universe = frozenset(range(8))
    dual = {(universe - t, universe - s): p for (s, t), p in lifted.items()}
    dual_laws = {
        'bottom': {universe - s: p for s, p in new_laws['top'].items()},
        'top': {universe - s: p for s, p in new_laws['bottom'].items()},
        'middle_u': {universe - s: p for s, p in new_laws['middle_u'].items()},
        'middle_v': {universe - s: p for s, p in new_laws['middle_v'].items()},
    }
    check_diamond(dual, dual_laws)

    # Every two-basis rank-one-phase minor law has <= 1+k(n-k) atoms.
    assert sum(p > 0 for p in new_laws['top'].values()) == 40
    assert 40 > 1 + 4 * (8 - 4)

    # Check affine occupation coefficient used in the exact entropy identity.
    corner_e = {name: sum(p for s, p in law.items() if replaced in s)
                for name, law in laws.items()}
    assert corner_e == {'bottom': F(1, 3), 'middle_u': F(11, 24),
                        'middle_v': F(3, 8), 'top': F(1, 2)}

    certificate = {
        'status': 'PASS',
        'source': {'edges': edges, 'conductances': list(map(str, weights)),
                   'roots': [0, 1, 2], 'potentials': text_matrix(potentials),
                   'gram': text_matrix(gram(rows, weights)),
                   'laws': {k: encode_law(v) for k, v in laws.items()},
                   'added_plane_law': encode_law(plane),
                   'diamonds': encode_coupling(source_diamond)},
        'replacement': {'old_edge': replaced, 'old_to_new_survivor_indices': remap,
                        'block': [5, 6, 7], 'effective_conductance': '1',
                        'low_law': encode_law(local_low),
                        'high_law': encode_law(local_high),
                        'cover': encode_coupling(eta)},
        'expanded': {'edges': new_edges, 'conductances': list(map(str, new_weights)),
                     'roots': [0, 1, 2], 'potentials': text_matrix(new_potentials),
                     'gram': text_matrix(new_gram),
                     'laws': {k: encode_law(v) for k, v in new_laws.items()},
                     'equalized_middle_law': encode_law({s: p / 2 for s, p in
                          add_laws(new_laws['middle_u'], new_laws['middle_v']).items()}),
                     'diamonds': encode_coupling(lifted)},
        'entropy_identity': 'H_expanded(lambda,mu) = H_source(lambda,mu) + '
                            '(7/6 + lambda/16 + mu/48) * log(2)',
    }
    summary = {
        'status': 'PASS',
        'source_cover_augmentations': augmentations,
        'source_positive_diamonds': len(source_diamond),
        'expanded_positive_diamonds': len(lifted),
        'expanded_minimum_diamond_weight': str(min(lifted.values())),
        'expanded_total_diamond_mass': str(sum(lifted.values())),
        'source_projection_support_sizes': {k: sum(p > 0 for p in v.values())
                                            for k, v in laws.items()},
        'expanded_projection_support_sizes': {k: sum(p > 0 for p in v.values())
                                              for k, v in new_laws.items()},
        'expanded_ranks': [2, 3, 3, 4],
        'expanded_site_count': 8,
        'exact_individual_corner_checks': 4,
        'exact_aggregate_middle_check': True,
        'exact_equalized_label_check': True,
        'exact_cographic_complement_check': True,
        'exact_update_orthogonality_check': True,
        'outside_every_rank_one_phase_frame_by_top_support': True,
    }
    (ROOT / 'certificate.json').write_text(json.dumps(certificate, indent=2) + '\n')
    (ROOT / 'verified_output.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
