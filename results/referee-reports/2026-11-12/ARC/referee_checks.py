"""Independent checks of PAPER.tex. No author modules are imported.

Run: python3 referee_checks.py > referee_checks_output.txt
Integer walk counts certify the lazy inequalities through k=200. Heat checks
use spectral decomposition, checked against scipy's separate expm routine.
"""
import os
for variable in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
                 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[variable] = '1'
import csv
import itertools as it
import json
import platform
import resource
import signal
import time
from fractions import Fraction
import networkx as nx
import numpy as np
import scipy
from scipy.linalg import expm


def johnson(v, k):
    vertices = list(it.combinations(range(v), k))
    g = nx.Graph()
    g.add_nodes_from(vertices)
    g.add_edges_from((a, b) for a, b in it.combinations(vertices, 2)
                     if len(set(a) & set(b)) == k - 1)
    return g


def hamming(d, q):
    vertices = list(it.product(range(q), repeat=d))
    g = nx.Graph()
    g.add_nodes_from(vertices)
    g.add_edges_from((a, b) for a, b in it.combinations(vertices, 2)
                     if sum(x != y for x, y in zip(a, b)) == 1)
    return g


def exact_one_walk_regular(g):
    """Powers 0,...,n-1 suffice by Cayley--Hamilton; unbounded Python ints."""
    n = len(g)
    power = np.eye(n, dtype=object)
    adjacency = nx.to_numpy_array(g, dtype=int).astype(object)
    for k in range(n):
        if len({power[i, i] for i in range(n)}) != 1:
            return False, k
        if len({power[x, y] for x, y in g.edges()}) != 1:
            return False, k
        power = power @ adjacency
    return True, None


def lazy_integer_check(g, steps=200):
    """M=dI+A, so r_k=M^k_xy/M^k_xx. Check every directed edge exactly."""
    n = len(g)
    d = g.degree(0)
    nbr = [list(g[i]) for i in range(n)]
    failures, equalities = [], []
    smallest = None
    for x in range(n):
        row = [int(x == j) for j in range(n)]
        for k in range(steps):
            nxt = [d * row[j] + sum(row[z] for z in nbr[j]) for j in range(n)]
            for y in nbr[x]:
                numerator = nxt[y] * row[x] - row[y] * nxt[x]
                if numerator < 0 and len(failures) < 8:
                    failures.append([x, y, k])
                if numerator == 0 and len(equalities) < 8:
                    equalities.append([x, y, k])
                delta = Fraction(numerator, nxt[x] * row[x])
                if smallest is None or delta < smallest:
                    smallest = delta
            row = nxt
    return dict(failures=failures, equalities=equalities,
                minimum_exact_increment_float=float(smallest))


def graph_suite():
    graphs = {}
    for n in (3, 4, 5, 6, 7, 8, 9, 10, 12, 20):
        graphs[f'C{n}'] = nx.cycle_graph(n)
    for n in (2, 3, 4, 5, 8, 10):
        graphs[f'K{n}'] = nx.complete_graph(n)
    for m in (2, 3, 4, 5):
        graphs[f'K{m},{m}'] = nx.complete_bipartite_graph(m, m)
    graphs.update({'Petersen': nx.petersen_graph(), 'Q3': hamming(3, 2),
                   'Q4': hamming(4, 2), 'Heawood': nx.heawood_graph(),
                   'J(6,2)': johnson(6, 2), 'J(7,3)': johnson(7, 3),
                   'H(2,3)': hamming(2, 3), 'H(3,3)': hamming(3, 3),
                   'icosahedron': nx.icosahedral_graph(),
                   'dodecahedron': nx.dodecahedral_graph()})
    # Abelian Cayley graphs. Different edge triangle counts prove they are
    # not edge/arc transitive, while translations prove vertex transitivity.
    graphs['Cayley_Z8_pm1_pm2'] = nx.circulant_graph(8, [1, 2])
    graphs['Cayley_Z10_pm1_pm2'] = nx.circulant_graph(10, [1, 2])
    graphs['Cayley_Z12_pm1_pm2'] = nx.circulant_graph(12, [1, 2])
    # Nonabelian Cayley(D_5 x Z_2,{r,r^-1,s,t}) = pentagonal prism x K2.
    # r/s edges have different cycle counts; automatic orbit check below.
    prism = nx.cartesian_product(nx.cycle_graph(5), nx.path_graph(2))
    graphs['Cayley_D5xZ2_prism_xK2'] = nx.cartesian_product(prism, nx.path_graph(2))
    # S4, right multiplication by the three adjacent transpositions.
    permutations = list(it.permutations(range(4)))
    s4 = nx.Graph()
    s4.add_nodes_from(permutations)
    for p in permutations:
        for i in range(3):
            q = list(p)
            q[i], q[i + 1] = q[i + 1], q[i]
            s4.add_edge(p, tuple(q))
    graphs['Cayley_S4_adjacent_transpositions'] = s4
    # Explicit non-distance-regular examples within the theorem's scope.
    graphs['arc_C13_pm1_pm5'] = nx.circulant_graph(13, [1, 5])
    blown = nx.Graph()
    for i in range(7):
        for j, k in it.product(range(2), repeat=2):
            blown.add_edge((i, j), ((i + 1) % 7, k))
    graphs['arc_C7_doubled'] = blown
    for n, k in ((8, 3), (12, 5)):
        gp = nx.Graph()
        for i in range(n):
            gp.add_edge(i, (i + 1) % n)
            gp.add_edge(i, n + i)
            gp.add_edge(n + i, n + (i + k) % n)
        graphs[f'arc_GP({n},{k})'] = gp
    return graphs


def main():
    signal.alarm(240)
    start = time.monotonic()
    print('versions', platform.python_version(), np.__version__, scipy.__version__, nx.__version__)
    ts = np.unique(np.r_[0., np.geomspace(1e-7, .01, 31), np.linspace(.01, 20, 1001),
                         25., 40., 80., 200.])
    records = []
    with open('referee_heat_grid.csv', 'w', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['graph', 'x', 'y', 't', 'ratio', 'derivative', 'lower_bound', 'one_minus_ratio', 'upper_bound'])
        for name, original in graph_suite().items():
            g = nx.convert_node_labels_to_integers(original, ordering='default')
            n = len(g)
            d = g.degree(0)
            assert nx.is_connected(g) and all(g.degree(x) == d for x in g)
            one_wr, first_bad_power = exact_one_walk_regular(g)
            assert one_wr or name.startswith('Cayley'), (name, first_bad_power)
            a = nx.to_numpy_array(g)
            lap = np.eye(n) - a / d
            lam, v = np.linalg.eigh(lap)
            lam[abs(lam) < 1e-13] = 0.
            weights = np.exp(-ts[:, None] * lam)
            heat = np.einsum('il,tl,jl->tij', v, weights, v, optimize=True)
            heatprime = np.einsum('il,tl,jl->tij', v, -weights * lam, v, optimize=True)
            heat[0] = np.eye(n)
            heatprime[0] = -lap
            diagonal = np.diagonal(heat, axis1=1, axis2=2)
            moment1 = np.einsum('tl,il->ti', weights * lam, v * v) / diagonal
            moment2 = np.einsum('tl,il->ti', weights * lam ** 2, v * v) / diagonal
            variance = moment2 - moment1 ** 2
            arcs = [(x, y) for x in g for y in g[x]]
            xs = np.array([x for x, y in arcs])
            ys = np.array([y for x, y in arcs])
            ratio = heat[:, xs, ys] / diagonal[:, xs]
            prime = ((heatprime[:, xs, ys] - ratio * np.diagonal(heatprime, axis1=1, axis2=2)[:, xs])
                     / diagonal[:, xs])
            remaining = 1 - 1 / (n * diagonal[:, xs])
            lower, upper = lam[1] * remaining, lam[-1] * remaining
            lower_violation = float(np.max(lower - (1 - ratio)))
            upper_violation = float(np.max((1 - ratio) - upper))
            avg = (heat * a).sum(axis=2) / (d * diagonal)
            avg_prime = ((heatprime * a).sum(axis=2) / d - avg * np.diagonal(heatprime, axis1=1, axis2=2)) / diagonal
            exact_lazy = lazy_integer_check(g)
            discrepancy = 0.
            for t in (0., 20., 40.):
                # Accelerate can leave spurious floating exception flags in
                # matmul. Validate the returned entries explicitly instead.
                with np.errstate(all='ignore'):
                    alternate = expm(-t * lap)
                assert np.all(np.isfinite(alternate))
                discrepancy = max(discrepancy, float(np.max(abs(alternate - heat[np.flatnonzero(ts == t)[0]]))))
            assert all(np.all(np.isfinite(z)) for z in (heat, heatprime, moment1, moment2, variance, ratio, prime))
            rec = dict(graph=name, n=n, d=d, one_walk_regular=one_wr,
                       first_bad_power=first_bad_power, distance_regular=nx.is_distance_regular(g),
                       minimum_heat_step=float(np.diff(ratio, axis=0).min()),
                       minimum_heat_derivative=float(prime.min()),
                       maximum_edge_spread=float(np.ptp(ratio, axis=1).max()),
                       mean_identity_error=float(np.max(abs(ratio - (1 - moment1[:, xs])))),
                       variance_identity_error=float(np.max(abs(prime - variance[:, xs]))),
                       lower_bound_violation=lower_violation, upper_bound_violation=upper_violation,
                       average_minimum_step=float(np.diff(avg, axis=0).min()),
                       average_identity_error=float(np.max(abs(avg - (1 - moment1)))),
                       average_variance_error=float(np.max(abs(avg_prime - variance))),
                       expm_comparison_error=discrepancy, lazy=exact_lazy)
            assert discrepancy < 2e-12
            assert rec['average_identity_error'] < 2e-12 and rec['average_variance_error'] < 2e-12
            if one_wr:
                assert rec['minimum_heat_step'] > -2e-12
                assert max(lower_violation, upper_violation) < 2e-12
                assert rec['mean_identity_error'] < 2e-12 and rec['variance_identity_error'] < 2e-12
                assert not exact_lazy['failures']
                assert n == 2 or not exact_lazy['equalities']
            if name.startswith('Cayley'):
                triangles = {f'{x}-{y}': len(set(g[x]) & set(g[y])) for x, y in g.edges()}
                rec['edge_triangle_counts'] = sorted(set(triangles.values()))
                # Different A^k entries are themselves an automorphism invariant.
                # Exact one-walk-regular failure + Cayley translations proves
                # non-arc-transitivity, without expensive automorphism enumeration.
                assert not one_wr
            for edge_index, (x, y) in enumerate(arcs):
                if x == 0:
                    for j, t in enumerate(ts):
                        writer.writerow([name, x, y, t, ratio[j, edge_index], prime[j, edge_index],
                                         lower[j, edge_index], 1 - ratio[j, edge_index], upper[j, edge_index]])
            records.append(rec)
            print(f"{name}: n={n} d={d} 1WR={one_wr} DR={rec['distance_regular']} "
                  f"min_heat_step={rec['minimum_heat_step']:.3e} "
                  f"edge_spread={rec['maximum_edge_spread']:.3e} "
                  f"bounds_violation={max(lower_violation, upper_violation):.2e} "
                  f"lazy_bad={exact_lazy['failures']} lazy_equal={exact_lazy['equalities']} "
                  f"lazy_min_delta={exact_lazy['minimum_exact_increment_float']:.3e}", flush=True)
    with open('referee_checks_results.json', 'w') as stream:
        json.dump(dict(grid_points=len(ts), time_range=[float(ts[0]), float(ts[-1])],
                       graphs=records, elapsed_seconds=time.monotonic() - start), stream, indent=2)
    print('PASS', len(records), 'graphs;', len(ts), 'times; exact lazy k=0..200 on every directed edge;'
          ' elapsed_seconds', round(time.monotonic() - start, 3))
    print('peak_RSS_bytes', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


if __name__ == '__main__':
    main()
