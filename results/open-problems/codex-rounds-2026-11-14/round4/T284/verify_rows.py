#!/usr/bin/env python3
"""Exact finite checks of the row reduction, not a MUCIO implementation."""
import json
import math
import os
import resource
import time
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path

started = time.monotonic()
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15


def edge_list(n):
    return list(combinations(range(n), 2))


def row_vectors(graph, n, edges):
    return tuple(tuple((graph >> e) & 1 for e, (i, _) in enumerate(edges) if i == v)
                 for v in range(n-1))


def induced_mask(vertices, edges):
    return sum(1 << e for e, (i, j) in enumerate(edges)
               if (vertices >> i) & 1 and (vertices >> j) & 1)


def mass(graph, pairs, bias):
    present = graph.bit_count()
    return bias**present * (1-bias)**(pairs-present)


def ceil_log2(n):
    return (n-1).bit_length()


pair_checks = repair_checks = tape_checks = product_checks = 0
for n in range(1, 5):
    edges = edge_list(n)
    graphs = range(1 << len(edges))
    rows = [row_vectors(g, n, edges) for g in graphs]
    pair_masks = [induced_mask(v, edges) for v in range(1 << n)]
    independent = [[v for v, mask in enumerate(pair_masks) if not (g & mask)]
                   for g in graphs]
    for g, h in product(graphs, repeat=2):
        changed_by_rows = sum(1 << i for i, (a, b) in enumerate(zip(rows[g], rows[h]))
                              if a != b)
        # Second computation uses changed edges, with no row-vector comparison.
        changed_by_edges = 0
        for e, (i, _) in enumerate(edges):
            if ((g ^ h) >> e) & 1:
                changed_by_edges |= 1 << i
        assert changed_by_rows == changed_by_edges
        remaining = ((1 << n)-1) ^ changed_by_rows
        assert g & pair_masks[remaining] == h & pair_masks[remaining]
        pair_checks += 1
        for tape_changed in (0, 1):
            hamming = sum(a != b for a, b in zip(rows[g], rows[h])) + tape_changed
            assert changed_by_rows.bit_count() <= hamming
            assert hamming <= n
            tape_checks += 1
        for vertices in independent[h]:
            repaired = vertices & remaining
            assert not (g & pair_masks[repaired])
            assert repaired.bit_count() >= vertices.bit_count()-changed_by_rows.bit_count()
            repair_checks += 1
    # Check the product law by multiplication over actual row alphabets.
    for bias in (F(1, 17), F(2, 7), F(1, 2)):
        for g in graphs:
            from_rows = F(1)
            for row in rows[g]:
                from_rows *= bias**sum(row)*(1-bias)**(len(row)-sum(row))
            assert from_rows == mass(g, len(edges), bias)
            product_checks += 1

# A row may change many edges; deleting its owner still costs one vertex.
n = 20
edges = edge_list(n)
star = sum(1 << e for e, (i, _) in enumerate(edges) if i == 0)
empty = 0
rows_star = row_vectors(star, n, edges)
rows_empty = row_vectors(empty, n, edges)
assert sum(a != b for a, b in zip(rows_star, rows_empty)) == 1
assert star.bit_count() == 19
assert not (star & induced_mask(((1 << n)-1) ^ 1, edges))

# Exact total variation and solver-success measure transfer on graph+tape pairs.
tv_checks = event_transfer_checks = 0
for n, p, bits in product((2, 3, 4), (F(1, 5), F(2, 7), F(3, 4)), (3, 6)):
    edges = edge_list(n)
    pairs = len(edges)
    q = F((p * (1 << bits)).numerator // (p * (1 << bits)).denominator, 1 << bits)
    p_mass = [mass(g, pairs, p) for g in range(1 << pairs)]
    q_mass = [mass(g, pairs, q) for g in range(1 << pairs)]
    assert sum(p_mass) == sum(q_mass) == 1
    tv = sum((abs(a-b) for a, b in zip(p_mass, q_mass)), F(0))/2
    assert tv <= pairs*(p-q) <= F(pairs, 1 << bits)
    # The maximizing sign event independently characterizes total variation.
    positive_difference = sum((a-b for a, b in zip(p_mass, q_mass) if a > b), F(0))
    assert positive_difference == tv
    tv_checks += 1
    subsets = sorted(range(1 << n), key=lambda v: (-v.bit_count(), v))
    for k in range(1, n+1):
        success_p = success_q = F(0)
        for g in range(1 << pairs):
            best = next(v for v in subsets if not (g & induced_mask(v, edges)))
            # A toy deterministic graph+tape predicate: tape 1 rejects.
            for tape in (0, 1):
                succeeds = tape == 0 and best.bit_count() >= k
                if succeeds:
                    success_p += p_mass[g]/2
                    success_q += q_mass[g]/2
        assert abs(success_p-success_q) <= tv
        event_transfer_checks += 1

# Finite-bit arithmetic and full error budgets: exact, including huge symbolic n.
budget_checks = threshold_checks = 0
for n, degree, S, ell in product((2, 3, 7, 20, 1000, 2**64, 2**512),
                                (F(1, 100), F(3), F(41, 7)), (1, 3, 9), (1, 2, 7)):
    if n <= degree:
        continue
    m = ceil_log2(n)
    w = (S+ell+6)*m
    p = degree/n
    scaled = p*(1 << w)
    numerator = scaled.numerator // scaled.denominator
    q = F(numerator, 1 << w)
    eta = F(math.comb(n, 2), 1 << w)
    epsilon = F(1, 2*n**S)
    delta = F(1, 2*n**ell)
    assert F(0) < q <= p < 1
    assert 0 <= p-q < F(1, 1 << w)
    assert eta <= F(1, 2*n**(S+ell+4))
    assert F(1, n**S)-eta >= epsilon
    assert delta+eta <= F(1, n**ell)
    assert 1/(epsilon*delta) == 4*n**(S+ell)
    budget_checks += 1

# Directly enumerate a small dyadic sampler's fair-bit sample space.
for bits, n, degree in product(range(1, 9), (3, 7, 11), (F(1, 2), F(2))):
    p = degree/n
    scaled = p*(1 << bits)
    threshold = scaled.numerator // scaled.denominator
    successes = sum(u < threshold for u in range(1 << bits))
    assert F(successes, 1 << bits) == F(threshold, 1 << bits)
    assert 0 <= p-F(successes, 1 << bits) < F(1, 1 << bits)
    threshold_checks += 1

report = {
    'status': 'PASS',
    'graph_pair_induced_agreement_checks': pair_checks,
    'independent_set_repair_checks': repair_checks,
    'graph_and_tape_distance_checks': tape_checks,
    'exact_row_product_mass_checks': product_checks,
    'exact_graph_total_variation_checks': tv_checks,
    'seeded_solver_event_transfer_checks': event_transfer_checks,
    'exact_full_error_budget_checks': budget_checks,
    'fair_bit_threshold_checks': threshold_checks,
    'star_example': '19 changed edges in one row; one vertex deletion suffices',
    'largest_graph_n': 20,
    'largest_exhaustive_graph_n': 4,
    'largest_symbolic_n': '2^512; no n-sized allocation',
    'nice': os.getpriority(os.PRIO_PROCESS, 0),
    'omp_num_threads': os.environ['OMP_NUM_THREADS'],
    'elapsed_seconds': round(time.monotonic()-started, 4),
    'max_rss_bytes_macos': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    'limitations': 'Checks the application and sampling transfer, not the imported concentration theorem; no MUCIO implementation or barrier-crossing experiment.'
}
assert report['max_rss_bytes_macos'] < 1024**3
Path('row_verification.json').write_text(json.dumps(report, indent=2)+'\n')
for key, value in report.items():
    print(f'{key}: {value}')
