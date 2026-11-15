"""Check the clique-lift identity used in the referee's scope argument.

The small weighted base used here is a mechanism test, not the RS
counterexample. The counterexample-transfer proof is in REPORT.md.
"""
import os
for variable in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
                 'VECLIB_MAXIMUM_THREADS'):
    os.environ[variable] = '1'
import resource
import signal
import time
import numpy as np
from scipy.linalg import expm


def main():
    signal.alarm(240)
    start = time.monotonic()
    order = 5
    weights = {1: 2, 4: 2, 2: 4, 3: 4}
    degree = sum(weights.values())
    weighted_adj = np.zeros((order, order), dtype=int)
    for x in range(order):
        for s, m in weights.items():
            weighted_adj[x, (x+s) % order] = m
    base_lap = degree * np.eye(order) - weighted_adj
    for fibers in (11, 21, 31):
        n = order * fibers
        adj = np.zeros((n, n), dtype=int)
        for x in range(order):
            for i in range(fibers):
                for j in range(fibers):
                    if j != i:
                        adj[x*fibers+i, x*fibers+j] = 1
                for s, m in weights.items():
                    for j in list(range(1, m//2+1)) + list(range(-m//2, 0)):
                        adj[x*fibers+i, ((x+s) % order)*fibers + (i+j) % fibers] = 1
        total_degree = fibers - 1 + degree
        assert np.all(adj == adj.T) and np.all(np.diag(adj) == 0)
        assert np.all(adj.sum(axis=1) == total_degree)
        assert adj[0, fibers + 1] == 1
        lap = total_degree * np.eye(n) - adj
        embedding = np.kron(np.eye(order), np.ones((fibers, 1)) / np.sqrt(fibers))
        intertwined = np.einsum('ij,jk->ik', lap, embedding)
        restriction = np.einsum('ij,jk->ik', embedding, base_lap)
        assert np.all(np.isfinite(intertwined)) and np.all(np.isfinite(restriction))
        assert np.max(abs(intertwined - restriction)) < 1e-12
        clique_lap = np.kron(np.eye(order), fibers*np.eye(fibers) - np.ones((fibers, fibers)))
        external_minimum = float(np.linalg.eigvalsh(lap - clique_lap).min())
        assert external_minimum > -1e-11
        for tau in (.1, .3, .7):
            with np.errstate(all='ignore'):
                base_heat = expm(-tau * base_lap)
                lifted_heat = expm(-tau * lap)
            assert np.all(np.isfinite(base_heat)) and np.all(np.isfinite(lifted_heat))
            lifted_constant_part = np.kron(base_heat, np.ones((fibers, fibers)) / fibers)
            error = float(np.max(abs(lifted_heat - lifted_constant_part)))
            bound = float(np.exp(-fibers * tau))
            assert error <= bound + 1e-12
            base_ratio = base_heat[0,1] / base_heat[0,0]
            lifted_edge_ratio = lifted_heat[0, fibers+1] / lifted_heat[0,0]
            print(f'N={fibers} vertices={n} degree={total_degree} tau={tau} '
                  f'max_entry_error={error:.6e} bound={bound:.6e} '
                  f'base_ratio={base_ratio:.12f} actual_edge_ratio={lifted_edge_ratio:.12f}')
    print('PASS elapsed_seconds', round(time.monotonic() - start, 3),
          'peak_RSS_bytes', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


if __name__ == '__main__':
    main()
