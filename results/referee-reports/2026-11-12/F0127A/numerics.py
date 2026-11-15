#!/usr/bin/env python3
"""Exact finite linear systems for the fast-core / slow-vertex counterexample.

Run: python3 numerics.py --ks 2 3 4 5 6 8 10 16 --output results.json
No Monte Carlo is needed: coalescence is solved by tridiagonal backward equations.
"""
import os

for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS"):
    os.environ[name] = "1"
try:
    current_nice = os.getpriority(os.PRIO_PROCESS, 0)
    if current_nice < 10:
        os.nice(10-current_nice)
except OSError:
    pass

import argparse
import json
import math
import resource
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    resource.setrlimit(resource.RLIMIT_AS, (8 * 1024**3, 8 * 1024**3))
except (ValueError, OSError):
    pass

import numpy as np
import scipy
from scipy.linalg import expm, solve_banded
from scipy.optimize import brentq
from scipy.sparse import coo_matrix, eye, kron
from scipy.sparse.linalg import spsolve


def harmonic(k):
    return math.fsum(1.0 / j for j in range(1, k + 1))


def parameters(k):
    N = k**4
    return N, math.sqrt(math.log(k)) / N


def pair_means(N, k, r):
    """Closed forms, separately checked against the 3-state killed generator."""
    n = N + k
    A = (n*n + N - k) / (2 * (N + 1 + 2*k*r))
    B = ((N - 1)*A + (2*N + k - 1)/(2*r)) / (N + 1)
    D = B + 1/(2*r)
    m = (N*(N - 1)*A + 2*N*k*B + k*(k - 1)*D) / n**2
    # A=core/core distinct; B=core/slow; D=slow/slow distinct.
    killed = np.array([
        [2/N + 2*k*r/N, -2*k*r/N, 0],
        [-r*(N-1)/N, r*(N+k)/N, -(k-1)*r/N],
        [0, -2*r, 2*r],
    ])
    solved = np.linalg.solve(killed, np.ones(3))
    error = float(np.max(np.abs(solved - [A, B, D])) / max(A, B, D))
    assert error < 2e-12, error
    return A, B, D, m, error


def tv_distances(t, N, k, r):
    n = N + k
    between = math.exp(-r*n/N*t)
    slow = math.exp(-r*t)
    fast = math.exp(-(1+k*r/N)*t)
    d_slow = (1-1/k)*slow + N/(k*n)*between
    own = k/(N*n)*between + (1-1/N)*fast
    other = k/(N*n)*between - fast/N
    d_core = 0.5*(own + (N-1)*abs(other) + k/n*between)
    return d_core, d_slow


def mixing_time(N, k, r):
    def objective(t):
        return max(tv_distances(t, N, k, r)) - 0.25
    return brentq(objective, 0, math.log(4)/r, xtol=1e-10, rtol=1e-13)


def coalescence_exact(N, k, r, incoming=True):
    """Solve by total particle number. Only two adjacent levels are retained.

    At total s and slow occupancy l, b=s-l. Migration stays at total s;
    collisions go to total s-1. The matrix at each level is tridiagonal.
    Core moves to empty core sites do not change (b,l) and are omitted.
    """
    previous = {0: 0.0, 1: 0.0}  # the two one-particle configurations
    max_residual = 0.0
    for s in range(2, N+k+1):
        lo, hi = max(0, s-N), min(k, s)
        ls = np.arange(lo, hi+1, dtype=float)
        bs = s-ls
        core_coal = bs*(bs-1)/N
        slow_to_occupied_core = ls*r*bs/N
        core_to_occupied_slow = bs*ls*r/N if incoming else np.zeros_like(ls)
        down = ls*r*(1-bs/N)  # migration l -> l-1
        up = bs*(k-ls)*r/N if incoming else np.zeros_like(ls)
        coal_same_l = core_coal + core_to_occupied_slow
        diagonal = coal_same_l + slow_to_occupied_core + down + up
        rhs = np.ones(len(ls))
        for j, l in enumerate(range(lo, hi+1)):
            if coal_same_l[j] > 0:
                rhs[j] += coal_same_l[j]*previous[l]
            if slow_to_occupied_core[j] > 0:
                rhs[j] += slow_to_occupied_core[j]*previous[l-1]
        band = np.zeros((3, len(ls)))
        band[1] = diagonal
        band[0, 1:] = -up[:-1]
        band[2, :-1] = -down[1:]
        solution = solve_banded((1, 1), band, rhs, check_finite=False)
        residual = diagonal*solution-rhs
        residual[:-1] -= up[:-1]*solution[1:]
        residual[1:] -= down[1:]*solution[:-1]
        scale = np.maximum(1, np.abs(diagonal*solution)+np.abs(rhs))
        max_residual = max(max_residual, float(np.max(np.abs(residual)/scale)))
        previous = dict(zip(range(lo, hi+1), solution))
    assert max_residual < 2e-12, max_residual
    return float(previous[k]), max_residual


def generator(N, k, r):
    n = N+k
    Q = np.zeros((n, n))
    Q[:N, :N] = 1/N
    np.fill_diagonal(Q, 0)
    Q[:N, N:] = r/N
    Q[N:, :N] = r/N
    Q -= np.diag(Q.sum(axis=1))
    return Q


def independent_checks():
    """Use un-lumped site generators, with small state spaces only."""
    N, k, r = 5, 3, 0.037
    n = N+k
    Q = generator(N, k, r)
    A, B, D, m, _ = pair_means(N, k, r)
    # Full ordered-pair generator, killed on the diagonal.
    G = kron(coo_matrix(Q), eye(n)) + kron(eye(n), coo_matrix(Q))
    keep = np.array([i*n+j for i in range(n) for j in range(n) if i != j])
    times = spsolve(-G.tocsr()[keep][:, keep], np.ones(len(keep)))
    expected = np.array([A if i < N and j < N else D if i >= N and j >= N else B
                         for i in range(n) for j in range(n) if i != j])
    pair_error = float(np.max(np.abs(times-expected))/max(A, B, D))
    stationary_error = abs(float(times.sum()/n**2)-m)/m

    # Full occupied-subset chain: 247 transient states for n=8.
    subsets = [mask for mask in range(1, 1 << n) if mask.bit_count() >= 2]
    index = {mask: i for i, mask in enumerate(subsets)}
    row, col, data = [], [], []
    for mask in subsets:
        i = index[mask]
        diagonal = 0.0
        for x in range(n):
            if not (mask >> x) & 1:
                continue
            for y in range(n):
                if y == x or Q[x, y] == 0:
                    continue
                target = (mask & ~(1 << x)) | (1 << y)
                diagonal += Q[x, y]
                if target in index:
                    row.append(i); col.append(index[target]); data.append(-Q[x, y])
        row.append(i); col.append(i); data.append(diagonal)
    mat = coo_matrix((data, (row, col)), shape=(len(index), len(index))).tocsr()
    full = spsolve(mat, np.ones(len(index)))[index[(1 << n)-1]]
    lumped, _ = coalescence_exact(N, k, r)
    coal_error = abs(float(full)-lumped)/lumped

    tv_error = 0.0
    for t in (0.0, 0.1, 1.0, 10.0, 100.0):
        probabilities = expm(t*Q)
        actual = np.abs(probabilities-1/n).sum(axis=1)/2
        core, slow = tv_distances(t, N, k, r)
        tv_error = max(tv_error, float(np.max(np.abs(actual-np.r_[np.full(N,core), np.full(k,slow)]))))
    errors = dict(pair_relative_error=pair_error, stationary_relative_error=stationary_error,
                  subset_coalescence_relative_error=coal_error, tv_absolute_error=tv_error,
                  subset_transient_states=len(index))
    assert max(pair_error, stationary_error, coal_error, tv_error) < 2e-12, errors
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ks', type=int, nargs='+', default=[2, 3, 4, 5, 6, 8, 10, 16])
    parser.add_argument('--output', type=Path, default=Path('results.json'))
    args = parser.parse_args()
    start = time.monotonic()
    checks = independent_checks()
    rows = []
    print('k n tau_meet t_mix E_C E_C/(2*tau) E_C/(N*sqrt(log(k)))', flush=True)
    for k in args.ks:
        if k < 2:
            raise ValueError('k must be at least 2')
        N, r = parameters(k)
        A, B, D, m, pair_error = pair_means(N, k, r)
        tmix = mixing_time(N, k, r)
        coal, residual = coalescence_exact(N, k, r)
        no_incoming, residual0 = coalescence_exact(N, k, r, incoming=False)
        n = N+k
        M = max(A, B, D)
        J = math.ceil(math.log(n-1)/math.log(4/3))
        bound_B = 2*M*(J+4)
        p = min(1, k*harmonic(k)/N+k*r*(1+harmonic(N)+k))
        lower = (harmonic(k)-1)/r
        upper = harmonic(k)/r+N+p*bound_B
        assert lower <= coal <= upper
        assert no_incoming <= harmonic(k)/r+N+1e-8*N
        row = dict(k=k, N=N, n=n, r=r, A=A, B=B, D=D, tau_meet=m,
                   t_mix=tmix, E_C=coal, E_C_no_incoming=no_incoming,
                   C_over_2tau=coal/(2*m), mix_over_tau=tmix/m,
                   C_over_leading=coal/(N*math.sqrt(math.log(k))),
                   pair_formula_relative_error=pair_error, backward_scaled_residual=residual,
                   no_incoming_scaled_residual=residual0, proof_lower=lower, proof_upper=upper,
                   perturbation_probability_bound=p)
        rows.append(row)
        print(f'{k} {n} {m:.10g} {tmix:.10g} {coal:.10g} {coal/(2*m):.7f} '
              f'{row["C_over_leading"]:.7f}', flush=True)
    # macOS reports ru_maxrss in bytes; Linux reports KiB.
    import sys
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes = peak if sys.platform == 'darwin' else peak*1024
    result = dict(method='exact backward equations in IEEE double precision; no simulation',
                  numpy=np.__version__, scipy=scipy.__version__, cpu_threads=1,
                  timestamp_utc=datetime.now(timezone.utc).isoformat(),
                  process_niceness=os.getpriority(os.PRIO_PROCESS, 0),
                  peak_rss_bytes=peak_bytes, elapsed_seconds=time.monotonic()-start,
                  independent_checks=checks, rows=rows)
    try:
        from threadpoolctl import threadpool_info
        result['threadpools'] = threadpool_info()
        assert all(pool['num_threads'] == 1 for pool in result['threadpools'])
    except ImportError:
        result['threadpools'] = 'threadpoolctl unavailable; environment limits set before NumPy import'
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('Checks:', json.dumps(checks), flush=True)
    print(f'Peak RSS {peak_bytes/1024**2:.1f} MiB; elapsed {result["elapsed_seconds"]:.2f}s', flush=True)


if __name__ == '__main__':
    main()
