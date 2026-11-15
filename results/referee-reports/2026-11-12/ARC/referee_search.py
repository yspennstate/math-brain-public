"""Independent small-regular-graph scan; no author code is executed.

Exhaustive connected regular graph atlas through n=7, and explicitly finite
random samples for n=8,9,10. A detected edge decrease gets an exact positive
uniformization certificate. Floating-point noise is never counted as a
counterexample. Every graph and search seed is reconstructible.
"""
import os
for variable in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
                 'VECLIB_MAXIMUM_THREADS'):
    os.environ[variable] = '1'
import json
import math
import resource
import signal
import time
from fractions import Fraction as F
import networkx as nx
import numpy as np


def certify(g, x, y, t, terms=180):
    n, d = len(g), g.degree(0)
    partial = [F(j == x) for j in range(n)]
    term = partial.copy()
    for k in range(1, terms + 1):
        term = [t * sum(term[z] for z in g[j]) / (d * k) for j in range(n)]
        partial = [a + b for a, b in zip(partial, term)]
    tail = t ** (terms + 1) / math.factorial(terms + 1) / (1 - t / (terms + 2))
    assert tail > 0
    deriv = [sum(partial[z] for z in g[j]) / d for j in range(n)]
    a, b, c, e = partial[x], partial[y], deriv[x], deriv[y]
    upper = (e + tail) * (a + tail) - b * c
    assert upper < 0
    result = dict(x=x, y=y, time=str(t), terms=terms, tail=float(tail),
                  ratio_lower=float(b / (a + tail)), ratio_upper=float((b + tail) / a),
                  derivative_upper=float(upper / (a + tail) ** 2),
                  derivative_upper_exact=str(upper / (a + tail) ** 2))
    return result


def candidates():
    for index, g in enumerate(nx.graph_atlas_g()):
        if len(g) >= 2 and nx.is_connected(g) and len(set(dict(g.degree()).values())) == 1:
            yield f'atlas:{index}', nx.convert_node_labels_to_integers(g)
    for n in (8, 9, 10):
        for d in range(2, n - 1):
            if n * d % 2:
                continue
            for seed in range(60):
                g = nx.random_regular_graph(d, n, seed=seed)
                if nx.is_connected(g):
                    yield f'random:n={n},d={d},seed={seed}', nx.convert_node_labels_to_integers(g, ordering='sorted')


def main():
    signal.alarm(240)
    start = time.monotonic()
    ts = np.r_[np.linspace(0, 30, 301), 40., 60., 100.]
    totals = dict(atlas=0, random=0, graphs_with_edge_decrease=0,
                  average_failures=0, average_identity_failures=0)
    by_n = {}
    witnesses = []
    all_records = []
    minimum_average_derivative = 1.
    minimum_average_step = 1.
    max_average_identity_error = 0.
    for origin, g in candidates():
        n, d = len(g), g.degree(0)
        totals['atlas' if origin.startswith('atlas') else 'random'] += 1
        by_n[n] = by_n.get(n, 0) + 1
        a = nx.to_numpy_array(g, nodelist=range(n))
        lam, v = np.linalg.eigh(np.eye(n) - a / d)
        lam[abs(lam) < 1e-13] = 0.
        e = np.exp(-ts[:, None] * lam)
        h = np.einsum('il,tl,jl->tij', v, e, v, optimize=True)
        hp = np.einsum('il,tl,jl->tij', v, -e * lam, v, optimize=True)
        diagonal = np.diagonal(h, axis1=1, axis2=2)
        dp = np.diagonal(hp, axis1=1, axis2=2)
        ratio = h / diagonal[:, :, None]
        derivative = (hp - ratio * dp[:, :, None]) / diagonal[:, :, None]
        edge_derivative = np.where(a[None] != 0, derivative, np.inf)
        worst = float(edge_derivative.min())
        avg = (h * a).sum(axis=2) / (d * diagonal)
        avgp = ((hp * a).sum(axis=2) / d - avg * dp) / diagonal
        mean = np.einsum('tl,il->ti', e * lam, v * v) / diagonal
        variance = np.einsum('tl,il->ti', e * lam ** 2, v * v) / diagonal - mean ** 2
        assert all(np.all(np.isfinite(z)) for z in (h, hp, ratio, derivative, avg, avgp, mean, variance))
        err = float(max(np.max(abs(avg - (1 - mean))), np.max(abs(avgp - variance))))
        max_average_identity_error = max(max_average_identity_error, err)
        minimum_average_derivative = min(minimum_average_derivative, float(avgp.min()))
        minimum_average_step = min(minimum_average_step, float(np.diff(avg, axis=0).min()))
        if err > 2e-12:
            totals['average_identity_failures'] += 1
        if avgp.min() < -2e-12 or np.diff(avg, axis=0).min() < -2e-12:
            totals['average_failures'] += 1
        if worst < -1e-8:
            totals['graphs_with_edge_decrease'] += 1
            # Keep one independently certified example for each order.
            if n not in {w['n'] for w in witnesses}:
                j, x, y = np.unravel_index(np.argmin(edge_derivative), edge_derivative.shape)
                t = F(round(float(ts[j]) * 10), 10)
                cert = certify(g, int(x), int(y), t)
                witness = dict(origin=origin, n=n, d=d, edges=sorted(g.edges()), certificate=cert)
                witnesses.append(witness)
                print('CERTIFIED_WITNESS', json.dumps({**witness, 'certificate': {k: v for k, v in cert.items() if not k.endswith('_exact')}}), flush=True)
        all_records.append(dict(origin=origin, n=n, d=d, minimum_edge_derivative=worst,
                                average_identity_error=err))
    result = dict(totals=totals, samples_by_order=by_n, times=len(ts),
                  time_range=[float(ts[0]), float(ts[-1])], witnesses=witnesses,
                  minimum_average_derivative=minimum_average_derivative,
                  minimum_average_step=minimum_average_step,
                  max_average_identity_error=max_average_identity_error,
                  elapsed_seconds=time.monotonic() - start, records=all_records)
    with open('referee_search_results.json', 'w') as stream:
        json.dump(result, stream, indent=2)
    print('TOTALS', totals, 'by_order', by_n)
    print('average_min_derivative', minimum_average_derivative,
          'average_min_grid_step', minimum_average_step,
          'max_average_identity_error', max_average_identity_error)
    assert totals['average_failures'] == totals['average_identity_failures'] == 0
    print('PASS elapsed_seconds', round(time.monotonic() - start, 3))
    print('peak_RSS_bytes', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


if __name__ == '__main__':
    main()
