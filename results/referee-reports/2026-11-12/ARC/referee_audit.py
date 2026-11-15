"""Summarize independent artifacts and audit their reported magnitudes.

This also gives a small exact symmetric stochastic-matrix example for the
terminology issue, independent of the ten-vertex graph and of numerical heat
calculations. All newly generated artifacts stay in the current directory.
"""
import os
for variable in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
                 'VECLIB_MAXIMUM_THREADS'):
    os.environ[variable] = '1'
import json
import math
import resource
import signal
from fractions import Fraction as F
import networkx as nx
import numpy as np
from scipy.linalg import expm


def main():
    signal.alarm(240)
    with open('referee_checks_results.json') as stream:
        suite = json.load(stream)
    with open('referee_search_results.json') as stream:
        search = json.load(stream)
    with open('referee_counterexample_results.json') as stream:
        counter = json.load(stream)
    claimed = [r for r in suite['graphs'] if r['one_walk_regular']]
    print('suite_graphs', len(suite['graphs']), 'claimed_1WR', len(claimed),
          'distance_regular', sum(r['distance_regular'] for r in suite['graphs']))
    for key in ('mean_identity_error', 'variance_identity_error', 'average_identity_error',
                'average_variance_error', 'expm_comparison_error', 'lower_bound_violation',
                'upper_bound_violation', 'maximum_edge_spread'):
        print('maximum_on_1WR', key, max(r[key] for r in claimed))
    print('minimum_step_on_1WR', min(r['minimum_heat_step'] for r in claimed))
    print('minimum_derivative_on_1WR', min(r['minimum_heat_derivative'] for r in claimed))
    print('exact_strict_lazy_graphs_n_ge_3', sum(r['n'] >= 3 and not r['lazy']['equalities']
                                               and not r['lazy']['failures'] for r in suite['graphs']))
    cert = counter['certificate']
    assert F(cert['ratio_lower']) > 1
    assert F(cert['ratio_upper']) > F(cert['ratio_lower'])
    assert F(cert['derivative_upper_exact']) < -F(9, 10000)
    author_tail = F(2 * 14 ** 121, math.factorial(121))
    assert author_tail < F(1, 10 ** 61)
    print('author_degree120_Taylor_tail_recomputed', float(author_tail),
          'derivative_tail_bound', float(2 * author_tail))
    for witness in search['witnesses']:
        assert F(witness['certificate']['derivative_upper_exact']) < 0
    # A 3-state symmetric stochastic chain; every entry is nonnegative,
    # every row sums to one, but P^2(0,1)>P^2(0,0).
    # A generic 3-state example has off-diagonal a,b,c, with diagonal
    # 1-a-b, 1-a-c, 1-b-c. Scan this finite rational grid exactly.
    found = None
    for ia in range(11):
        for ib in range(11):
            for ic in range(11):
                a, b, c = F(ia,10), F(ib,10), F(ic,10)
                p = [[1-a-b, a, b], [a, 1-a-c, c], [b, c, 1-b-c]]
                if min(min(row) for row in p) < 0:
                    continue
                pp00 = sum(p[0][i] * p[i][0] for i in range(3))
                pp01 = sum(p[0][i] * p[i][1] for i in range(3))
                if pp01 > pp00:
                    found = p, pp00, pp01
                    break
            if found:
                break
        if found:
            break
    assert found is not None
    print('symmetric_stochastic_matrix', [[str(x) for x in row] for row in found[0]],
          'P^2(0,0)', found[1], 'P^2(0,1)', found[2])
    for n in (8, 10, 12):
        g = nx.circulant_graph(n, [1, 2])
        a = nx.to_numpy_array(g, nodelist=range(n))
        h = expm(-(np.eye(n) - a / 4))
        print('Cayley_Z'+str(n), 't=1 r01', h[0,1]/h[0,0], 'r02', h[0,2]/h[0,0],
              'edge_triangles', len(set(g[0]) & set(g[1])), len(set(g[0]) & set(g[2])))
    print('ALL_ARTIFACT_ASSERTIONS_PASS peak_RSS_bytes', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


if __name__ == '__main__':
    main()
