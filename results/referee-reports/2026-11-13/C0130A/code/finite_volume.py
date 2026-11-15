"""Independent finite-interval walk, with its actual consumed-cookie state.

The graph is finite; solve its Dirichlet equations in rational arithmetic.
For validation only, compare with a finite-generation backward-chain calculation
whose population cutoff has an explicit Chernoff error bound.
"""
import argparse
import json
import os
from collections import deque
from pathlib import Path

os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import mpmath as mp
import sympy as sp
from sympy.polys.matrices import DomainMatrix

from escape import kernel_row


def direct_walk(params, N):
    ps = list(map(sp.Rational, params))
    M = len(ps)
    initial = (1, (0,) * (N - 1))
    states = [initial]
    index = {initial: 0}
    edges = []
    for x, counts in states:
        p = ps[counts[x-1]] if counts[x-1] < M else sp.Rational(1, 2)
        new = list(counts)
        new[x-1] = min(M, new[x-1] + 1)
        out = []
        for y, weight in [(x+1, p), (x-1, 1-p)]:
            if y in (0, N):
                out.append((None, weight, int(y == N)))
            else:
                target = y, tuple(new)
                if target not in index:
                    index[target] = len(states)
                    states.append(target)
                out.append((index[target], weight, None))
        edges.append(out)
    n = len(states)
    A = sp.eye(n)
    b = sp.zeros(n, 1)
    for i, out in enumerate(edges):
        for j, weight, boundary in out:
            if j is None:
                b[i] += weight * boundary
            else:
                A[i, j] -= weight
    da, db = DomainMatrix.from_Matrix(A), DomainMatrix.from_Matrix(b)
    da, db = da.unify(db)
    num, den = da.solve_den(db)
    answer = sp.cancel(num.to_Matrix()[0] / da.domain.to_sympy(den))
    return answer, n


def backward_finite(params, N, K, dps):
    mp.mp.dps = dps
    stack = [mp.mpf(p) for p in params]
    rows = mp.matrix([kernel_row(stack, i, K)[0] for i in range(K)])
    mass = mp.matrix(1, K)
    mass[0, 0] = 1
    for _ in range(N-1):
        mass = mass * rows
    # Bound max population crossing K over these finitely many generations.
    # For n=N-1 iterations, choose theta>0 with f^n(exp(theta))<2,
    # dominate by all-fair backward chain, which has geometric law with mean n.
    # A union bound over generations gives n*(n/(n+1))^K.
    n = N-1
    error = n * (mp.mpf(n)/(n+1))**K
    return mass[0, 0], error


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--p', nargs='+', required=True)
    p.add_argument('--N', type=int, default=4)
    p.add_argument('--K', type=int, default=360)
    p.add_argument('--dps', type=int, default=80)
    p.add_argument('--output', required=True)
    args = p.parse_args()
    if any(sp.Rational(x) < sp.Rational(1, 2) for x in args.p):
        raise ValueError('The all-fair domination bound requires p_j>=1/2.')
    value, n = direct_walk(args.p, args.N)
    approx, error = backward_finite(args.p, args.N, args.K, args.dps)
    exact_float = mp.mpf(str(sp.N(value, args.dps)))
    diff = abs(exact_float - approx)
    assert diff <= error + mp.mpf(10)**(-args.dps+5)
    result = dict(params=args.p, N=args.N, K=args.K, states=n,
                  direct_rational=str(value), direct=mp.nstr(exact_float, args.dps),
                  backward_truncated=mp.nstr(approx, args.dps),
                  absolute_difference=mp.nstr(diff, 15),
                  certified_population_cutoff_error=mp.nstr(error, 15))
    Path(args.output).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
