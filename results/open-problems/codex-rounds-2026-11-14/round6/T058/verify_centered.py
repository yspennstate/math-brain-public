"""Exact finite audits of centered packing loss. Standard library, one thread."""

import itertools
import json
import math
import os
import resource
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
started = time.monotonic()


def choose(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0


def e(k):
    return k*(k-1)//2


def family_data(n, k):
    sets = [sum(1 << v for v in A)
            for A in itertools.combinations(range(n), k)]
    disjoint = [sum(1 << j for j, B in enumerate(sets) if not A & B)
                for A in sets]
    return sets, disjoint


def matching_table(disjoint):
    # Split a family into packings omitting its first edge and containing it.
    table = bytearray(1 << len(disjoint))
    for mask in range(1, len(table)):
        bit = mask & -mask
        rest = mask ^ bit
        i = bit.bit_length()-1
        table[mask] = max(table[rest], 1+table[rest & disjoint[i]])
    return table


def vertex_matching(mask, sets, n):
    # Independent recursion over the used VERTICES rather than family indices.
    family = [A for i, A in enumerate(sets) if mask & (1 << i)]
    dp = [0]*(1 << n)
    for S in range(1, len(dp)):
        bit = S & -S
        best = dp[S ^ bit]
        for A in family:
            if A & bit and A & S == A:
                best = max(best, 1+dp[S ^ A])
        dp[S] = best
    return dp[-1]


def independent_audit(n, k):
    sets, disjoint = family_data(n, k)
    N = len(sets)
    table = matching_table(disjoint)
    first = [0]*(N+1)
    second = [0]*(N+1)
    pivotal = [0]*N
    checks = 0
    for mask, matching in enumerate(table):
        m = mask.bit_count()
        loss = m-matching
        first[m] += loss
        second[m] += loss*loss
        if n <= 5:
            assert matching == vertex_matching(mask, sets, n)
        if (n, k) == (6, 3):
            # Here every disjoint partner is the unique complementary triple.
            has_pair = any(mask & (1 << i) and mask & disjoint[i]
                           for i in range(N))
            assert matching == (2 if has_pair else int(bool(mask)))
        # Check every coordinate for small N, one canonical coordinate otherwise.
        candidates = range(N) if N <= 10 else (0,)
        for i in candidates:
            bit = 1 << i
            if mask & bit:
                continue
            gain = table[mask | bit]-matching
            delta = 1-gain
            assert gain in (0, 1) and delta in (0, 1)
            intersects = bool(mask & (((1 << N)-1) ^ disjoint[i]))
            assert delta*delta <= intersects
            if i == 0:
                pivotal[m] += delta*delta
            checks += 1
    rows = []
    # Include the prescribed q, plus asymmetric parameters checking q(1-q).
    probabilities = sorted({Fraction(1, 2**e(k)), Fraction(1, 4), Fraction(3, 4)})
    R = N-1-choose(n-k, k)
    assert R == N-1-disjoint[0].bit_count()
    for q in probabilities:
        mean = sum(Fraction(count)*q**m*(1-q)**(N-m)
                   for m, count in enumerate(first))
        moment2 = sum(Fraction(count)*q**m*(1-q)**(N-m)
                      for m, count in enumerate(second))
        var = moment2-mean**2
        pivot_mean = sum(Fraction(count)*q**m*(1-q)**(N-1-m)
                         for m, count in enumerate(pivotal))
        es_exact = N*q*(1-q)*pivot_mean
        es_intersection = N*q*(1-q)*(1-(1-q)**R)
        es_union = N*q*q*(1-q)*R
        mu = N*q
        loose = mu*mu*Fraction(k*k, n)
        conflicts = Fraction(N*R, 2)*q*q
        if 2*k > n:
            # Then M=1_{X>0}, and X is exactly binomial.
            p0 = (1-q)**N
            assert mean == mu-1+p0
            assert var == N*q*(1-q)+p0*(1-p0)-2*mu*p0
        if (n, k) == (6, 3):
            # Ten independent complementary pairs determine the matching size.
            assert mean == mu-2+(1-q*q)**10+(1-q)**20
        assert 0 <= var <= es_exact <= es_intersection <= es_union <= loose
        assert 0 <= mean <= conflicts <= loose/2
        rows.append({'q': str(q), 'mean_loss': str(mean), 'variance_loss': str(var),
                     'ES_exact': str(es_exact), 'ES_intersection': str(es_intersection),
                     'ES_union': str(es_union), 'mu_squared_k_squared_over_n': str(loose),
                     'expected_conflicts': str(conflicts)})
    return {'n': n, 'k': k, 'candidate_sets': N, 'families': len(table),
            'coordinate_checks': checks, 'rows': rows}


def original_graph_audit(n, k):
    sets, disjoint = family_data(n, k)
    N = len(sets)
    assert N <= 15
    table = matching_table(disjoint)
    edges = list(itertools.combinations(range(n), 2))
    constraints = [sum(1 << i for i, (v, w) in enumerate(edges)
                       if A & (1 << v) and A & (1 << w)) for A in sets]
    histogram = Counter()
    pairs_by_j = [0]*k
    sum_loss = sum_x = 0
    for graph in range(1 << len(edges)):
        family = sum(1 << i for i, C in enumerate(constraints) if not graph & C)
        histogram[family] += 1
        indices = [i for i in range(N) if family & (1 << i)]
        Y = 0
        for i, j in itertools.combinations(indices, 2):
            overlap = (sets[i] & sets[j]).bit_count()
            if overlap:
                pairs_by_j[overlap] += 1
                Y += 1
        X = len(indices)
        loss = X-table[family]
        assert 0 <= loss <= Y
        sum_x += X
        sum_loss += loss
    graphs = 1 << len(edges)
    q = Fraction(1, 2**e(k))
    assert Fraction(sum_x, graphs) == N*q
    actual_pairs = [Fraction(pairs_by_j[j], graphs) for j in range(1, k)]
    formula_pairs = [Fraction(N*choose(k, j)*choose(n-k, k-j),
                              2**(2*e(k)-e(j)+1)) for j in range(1, k)]
    assert actual_pairs == formula_pairs
    # Independent common-vertex count checks the previous leading term's factor.
    expected_y1 = Fraction(n*choose(n-1, k-1)*choose(n-k, k-1), 2)*q*q
    assert formula_pairs[0] == expected_y1
    # TV distance of the ENTIRE labelled family, not just its count or matching.
    tv = Fraction(0)
    for mask in range(1 << N):
        m = mask.bit_count()
        independent_probability = q**m*(1-q)**(N-m)
        tv += abs(Fraction(histogram.get(mask, 0), graphs)-independent_probability)
    tv /= 2
    if k == 2:
        assert tv == 0
    return {'n': n, 'k': k, 'graphs': graphs, 'family_TV': str(tv),
            'family_TV_float': float(tv), 'mean_loss': str(Fraction(sum_loss, graphs)),
            'expected_pairs_by_overlap': [str(x) for x in formula_pairs],
            'edge_sharing_Delta': str(sum(formula_pairs[1:]))}


independent = [independent_audit(n, k) for n, k in
               [(5, 2), (5, 3), (5, 4), (6, 3), (6, 4)]]
original = [original_graph_audit(n, k) for n, k in
            [(5, 2), (5, 3), (5, 4), (6, 4)]]
result = {'status': 'all exact centered-loss, pair-count and family-TV audits passed',
          'nice': os.getpriority(os.PRIO_PROCESS, 0),
          'independent_hypergraphs': independent, 'original_graphs': original,
          'elapsed_seconds': time.monotonic()-started,
          'peak_rss_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
assert result['elapsed_seconds'] < 1200
assert result['peak_rss_bytes'] < 1_000_000_000
Path('centered_verification.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
