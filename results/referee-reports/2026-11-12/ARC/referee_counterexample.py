"""Independent rational certificate and symbolic analysis of the cube/pyramids.

Uses positive uniformization exp(tP), not the authors' alternating exp(-tL)
series. The factor exp(-t) cancels from r and r'. All certified operations
are Fraction arithmetic, including the final derivative comparison.
"""
import os
for variable in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
                 'VECLIB_MAXIMUM_THREADS'):
    os.environ[variable] = '1'
import itertools
import json
import math
import resource
import signal
import time
from fractions import Fraction as F
import mpmath as mp
import networkx as nx
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.optimize import brentq, minimize_scalar


def graph():
    vertices = list(itertools.product((0, 1), repeat=3))
    g = nx.Graph()
    g.add_nodes_from(range(10))
    for i, u in enumerate(vertices):
        for j, v in enumerate(vertices[:i]):
            if sum(a != b for a, b in zip(u, v)) == 1:
                g.add_edge(i, j)
        g.add_edge(i, 8 + u[0])
    assert nx.is_connected(g) and all(g.degree(i) == 4 for i in g)
    return g


def positive_series_certificate(g, t=F(7), terms=100):
    nbr = [list(g[i]) for i in g]
    n, d, x, y = len(g), 4, 0, 8
    row = [F(i == x) for i in range(n)]
    total = row.copy()
    for k in range(1, terms + 1):
        row = [t * sum(row[z] for z in nbr[j]) / (d * k) for j in range(n)]
        total = [a + b for a, b in zip(total, row)]
    # Since P is stochastic, every (P^k)_xy <=1. Consecutive scalar-tail
    # terms have ratio at most t/(terms+2).
    tail = t ** (terms + 1) / math.factorial(terms + 1) / (1 - t / (terms + 2))
    deriv = [sum(total[z] for z in nbr[j]) / d for j in range(n)]
    a, b, c, e = total[x], total[y], deriv[x], deriv[y]
    # True a,b,c,e all lie in [partial,partial+tail], all nonnegative.
    gap_lower = b - a - tail
    numerator_upper = (e + tail) * (a + tail) - b * c
    assert gap_lower > 0 and numerator_upper < 0
    derivative_upper = numerator_upper / (a + tail) ** 2
    assert derivative_upper < -F(9, 10000)
    ratio_lower = b / (a + tail)
    ratio_upper = (b + tail) / a
    return dict(terms=terms, uniformization_tail=float(tail),
                ratio_lower=str(ratio_lower), ratio_upper=str(ratio_upper),
                ratio_interval_float=[float(ratio_lower), float(ratio_upper)],
                derivative_upper_float=float(derivative_upper),
                derivative_upper_exact=str(derivative_upper))


def main():
    signal.alarm(240)
    start = time.monotonic()
    g = graph()
    a = nx.to_numpy_array(g)
    lap = np.eye(10) - a / 4
    sym_a = sp.Matrix(a.astype(int))
    print('edges', sorted(g.edges()))
    print('characteristic_polynomial_A', sp.factor(sym_a.charpoly().as_expr()))
    print('exact_eigenvalues_A', sym_a.eigenvals())
    lam2 = (7 - sp.sqrt(17)) / 8
    # Eigenvector constant on each base: u=1 on top face, -1 on bottom;
    # apex value rho-1, where rho=(1+sqrt(17))/2 >2.
    rho = (1 + sp.sqrt(17)) / 2
    eigenvector = sp.Matrix([1 if i < 4 else -1 for i in range(8)] + [rho - 1, 1 - rho])
    assert all(sp.simplify(z) == 0 for z in sym_a * eigenvector - rho * eigenvector)
    print('lambda2', lam2, float(lam2), 'simple; eigenvector', list(eigenvector))
    cert = positive_series_certificate(g)
    print('CERTIFICATE t=7 positive uniformization: terms', cert['terms'],
          'tail', cert['uniformization_tail'])
    print('r(7) interval', cert['ratio_interval_float'])
    print("r'(7) certified upper bound", cert['derivative_upper_float'], '< -0.0009')

    def values(t):
        h = expm(-t * lap)
        hp = -lap @ h
        r = h[0, 8] / h[0, 0]
        rp = (hp[0, 8] - r * hp[0, 0]) / h[0, 0]
        return r, rp
    crossing = brentq(lambda t: values(t)[0] - 1, 1., 6.)
    maximum = minimize_scalar(lambda t: -values(t)[0], bounds=(5., 9.), method='bounded')
    print('first crossing near', crossing, 'maximum', -maximum.fun, 'at', maximum.x)
    print('t, ratio, derivative')
    for t in (0., 1., crossing, 5., maximum.x, 7., 10., 20., 40.):
        print(t, *values(t))
    # Independent high-precision matrix exponential: no shared eigensolver.
    mp.mp.dps = 70
    mh = mp.expm(-7 * mp.matrix(lap.tolist()))
    mhp = -mp.matrix(lap.tolist()) * mh
    mr = mh[0, 8] / mh[0, 0]
    mrp = (mhp[0, 8] - mr * mhp[0, 0]) / mh[0, 0]
    print('mpmath r(7)', mp.nstr(mr, 60))
    print("mpmath r'(7)", mp.nstr(mrp, 60))
    assert cert['ratio_interval_float'][0] - 1e-15 < float(mr) < cert['ratio_interval_float'][1] + 1e-15
    # Exact even-time counterexample if 'symmetric chain' means Q=Q^T.
    # Use Q=(4I+A)/8 so its spectrum is nonnegative.
    count = [int(i == 0) for i in range(10)]
    for k in range(1, 201):
        count = [4 * count[j] + sum(count[z] for z in g[j]) for j in range(10)]
        if k % 2 == 0 and count[8] > count[0]:
            print('symmetric_matrix_even_time_counterexample', k,
                  '(4I+A)^k(0,8)=', count[8], '> (4I+A)^k(0,0)=', count[0],
                  'ratio=', float(F(count[8], count[0])))
            break
    ts = np.linspace(0, 40, 4001)
    eigenvalues, v = np.linalg.eigh(lap)
    eigenvalues[abs(eigenvalues) < 1e-13] = 0
    e = np.exp(-ts[:, None] * eigenvalues)
    heat = np.einsum('il,tl,jl->tij', v, e, v, optimize=True)
    diagonal = np.diagonal(heat, axis1=1, axis2=2)
    average = (heat * a).sum(axis=2) / (4 * diagonal)
    mean = np.einsum('tl,il->ti', e * eigenvalues, v * v) / diagonal
    variance = np.einsum('tl,il->ti', e * eigenvalues ** 2, v * v) / diagonal - mean ** 2
    assert all(np.all(np.isfinite(z)) for z in (heat, average, mean, variance))
    print('neighbour_average minimum_grid_increment', float(np.diff(average, axis=0).min()))
    print('neighbour_average minimum_variance', float(variance.min()))
    print('neighbour_average maximum_identity_error', float(np.max(abs(average - (1 - mean)))))
    with open('referee_counterexample_results.json', 'w') as stream:
        json.dump(dict(certificate=cert, crossing=crossing, maximum_time=maximum.x,
                       maximum_ratio=-maximum.fun, mpmath_ratio=str(mr), mpmath_derivative=str(mrp),
                       edges=sorted(g.edges()), elapsed_seconds=time.monotonic() - start), stream, indent=2)
    print('PASS elapsed_seconds', round(time.monotonic() - start, 3))
    print('peak_RSS_bytes', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


if __name__ == '__main__':
    main()
