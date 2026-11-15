#!/usr/bin/env python3
"""Standalone audit of the explicit gadgets and their bridge chains."""
from fractions import Fraction
import itertools
import json
import os
from pathlib import Path
import resource
import signal


GADGETS = {
    2: (
        [(0, -1), (0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)],
        [(0, 0), (0, 1), (1, -1), (1, 0), (1, 1), (2, -1), (2, 0)],
    ),
    3: (
        [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0), (0, 0, 1), (0, 0, 2)],
        [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (0, 1, 1), (0, 0, 1)],
    ),
}


def graph(vertices):
    # Squared Euclidean distance one is an independent nearest-neighbor test.
    return [(i, j) for i, u in enumerate(vertices)
            for j, v in enumerate(vertices[:i])
            if sum((a - b) ** 2 for a, b in zip(u, v)) == 1]


def cofactor_count(vertices):
    n = len(vertices)
    lap = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i, j in graph(vertices):
        lap[i][i] += 1
        lap[j][j] += 1
        lap[i][j] -= 1
        lap[j][i] -= 1
    a = [row[:-1] for row in lap[:-1]]
    determinant = Fraction(1)
    for k in range(n - 1):
        pivot = a[k][k]
        assert pivot > 0
        determinant *= pivot
        for i in range(k + 1, n - 1):
            ratio = a[i][k] / pivot
            for j in range(k + 1, n - 1):
                a[i][j] -= ratio * a[k][j]
            a[i][k] = 0
    assert determinant.denominator == 1
    return int(determinant)


def connected(n, edges):
    seen = {0}
    while True:
        enlarged = seen | {i for i, j in edges if j in seen} | {j for i, j in edges if i in seen}
        if enlarged == seen:
            return len(seen) == n
        seen = enlarged


def explicit_spanning_trees(vertices):
    n = len(vertices)
    return sum(connected(n, chosen) for chosen in itertools.combinations(graph(vertices), n - 1))


def chain(d, gadget, r):
    spacing = 4 if d == 2 else 3
    vertices = []
    labels = []
    for j in range(r):
        for v in gadget:
            vertices.append((v[0] + spacing * j,) + v[1:])
            labels.append(('gadget', j))
        if j < r - 1:
            vertices.append((spacing * j + spacing - 1,) + (0,) * (d - 1))
            labels.append(('connector', j))
    assert len(set(vertices)) == len(vertices)
    edges = graph(vertices)
    internal_edges = [edge for edge in edges if labels[edge[0]] == labels[edge[1]]]
    external_edges = [edge for edge in edges if labels[edge[0]] != labels[edge[1]]]
    assert len(internal_edges) == len(graph(gadget)) * r
    assert len(external_edges) == 2 * (r - 1)
    assert connected(len(vertices), edges)
    for edge in external_edges:
        assert not connected(len(vertices), [e for e in edges if e != edge])
    return vertices


def canonical_independent(vertices):
    shift = sorted(vertices)[0]
    return tuple(sorted(tuple(v[i] - shift[i] for i in range(len(v))) for v in vertices))


def audit_graph_classification():
    """Try every small labeled bipartite graph, without any lattice generator."""
    accepted = []
    for n in range(2, 7):
        hist = {}
        for a in range(1, n // 2 + 1):
            potential = [(i, j) for i in range(a) for j in range(a, n)]
            for mask in range(1 << len(potential)):
                edges = [edge for k, edge in enumerate(potential) if mask & (1 << k)]
                if len(edges) < n - 1 or not connected(n, edges):
                    continue
                adjacency = [set() for _ in range(n)]
                for i, j in edges:
                    adjacency[i].add(j)
                    adjacency[j].add(i)
                if any(len(adjacency[i] & adjacency[j]) >= 3
                       for i in range(n) for j in range(i)):
                    continue
                tau = sum(connected(n, chosen) for chosen in itertools.combinations(edges, n - 1))
                k = len(edges) - n + 1
                if n <= 5:
                    assert (k, tau) in ((0, 1), (1, 4))
                else:
                    assert (k, tau) in ((0, 1), (1, 4), (1, 6), (2, 15))
                hist[k, tau] = hist.get((k, tau), 0) + 1
        row = {'n': n, 'labeled_bipartite_graphs': sum(hist.values()),
               'histogram': [{'excess': k, 'tau': tau, 'graphs': count}
                             for (k, tau), count in sorted(hist.items())]}
        accepted.append(row)
        print('GRAPH_CLASSIFICATION', json.dumps(row, sort_keys=True), flush=True)
    Path('data/graph_classification.json').write_text(json.dumps(accepted, indent=2) + '\n')


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (1100, 1100))
    signal.alarm(1190)
    print('RUNTIME', json.dumps({'nice': os.getpriority(os.PRIO_PROCESS, 0),
                                 'OMP_NUM_THREADS': os.environ.get('OMP_NUM_THREADS')}))
    audit_graph_classification()
    rows = []
    for d, gadgets in GADGETS.items():
        records = [json.loads(line) for line in Path(f'data/shapes_d{d}.jsonl').read_text().splitlines()]
        lookup = {tuple(tuple(v) for v in row['vertices']): row for row in records}
        for label, gadget in zip(('A', 'B'), gadgets):
            tau = 15 if (d, label) == (2, 'A') else 16 if d == 2 else 4 if label == 'A' else 6
            assert explicit_spanning_trees(gadget) == cofactor_count(gadget) == tau
            assert lookup[canonical_independent(gadget)]['tau'] == tau
            for r in (1, 2, 3, 5):
                vertices = chain(d, gadget, r)
                n = len(vertices)
                e = len(graph(vertices))
                expected_n = (8 if d == 2 else 7) * r - 1
                expected_k = (2 if d == 2 else 1) * r
                assert n == expected_n and e - n + 1 == expected_k
                actual_tau = cofactor_count(vertices)
                assert actual_tau == tau ** r
                row = {'d': d, 'gadget': label, 'r': r, 'n': n,
                       'edges': e, 'excess': e - n + 1, 'tau': actual_tau}
                rows.append(row)
                print('CHAIN', json.dumps(row, sort_keys=True), flush=True)
    Path('data/chain_audit.json').write_text(json.dumps(rows, indent=2) + '\n')
    print('PEAK_RSS_RAW', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    print('ALL_ASSERTIONS_PASSED')


if __name__ == '__main__':
    main()
