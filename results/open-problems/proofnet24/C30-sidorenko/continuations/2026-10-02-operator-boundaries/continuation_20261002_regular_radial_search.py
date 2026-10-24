"""Numerical search for an obstruction to radial ML10 host smoothing.

This tests an auxiliary sufficient condition, not Sidorenko itself. If
F(W)>=F(J+tau(W-J)) held for every regular host and every tau in[0,1],
it would imply the target. A negative objective obstructs that route.
Only exact follow-up certificates can turn numerical output into a claim.
"""
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.optimize import minimize


def sinkhorn(z, n):
    ix = np.triu_indices(n)
    A = np.empty((n, n))
    A[ix] = np.exp(z)
    A[ix[::-1]] = A[ix]
    d = np.ones(n)
    for _ in range(2000):
        rows = d * (A @ d)
        if np.max(abs(rows / n - 1)) < 2e-13:
            break
        d *= np.sqrt(n / rows)
    W = d[:, None] * A * d[None, :]
    return W, ix, np.max(abs(W.sum(axis=1) / n - 1))


def density_gradient(W):
    n = len(W)
    M = (np.sqrt(W[:, :, None, None] * W[None, None, :, :]) *
         W[:, None, None, :] * W[None, :, :, None]).reshape(n*n, n*n)
    M2 = M @ M
    M4 = M2 @ M2
    value = np.sum(M4 * M) / n**10
    contractions = (5 * M4 * M).reshape(n, n, n, n)
    grad = (contractions.sum(axis=(2, 3)) +
            2 * contractions.sum(axis=(1, 2))) / W / n**10
    grad = (grad + grad.T) / 2
    return value, grad


def objective(z, n, tau):
    W, ix, error = sinkhorn(z, n)
    if error > 1e-8:
        return 1e4, np.zeros_like(z)
    F, g = density_gradient(W)
    Ft, gt = density_gradient(1 + tau * (W-1))
    value = 1 - Ft / F
    gw = Ft / F**2 * g - tau / F * gt
    b = np.sum(gw * W, axis=1)
    v = np.linalg.solve(n * np.eye(n) + W, b)
    gz = W * (gw - v[:, None] - v[None, :])
    answer = gz[ix].copy()
    off = ix[0] != ix[1]
    answer[off] *= 2
    return value, answer


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=6)
    ap.add_argument('--runs', type=int, default=100)
    ap.add_argument('--tau', type=float, default=.8)
    ap.add_argument('--seed', type=int, default=214729)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    rng = np.random.default_rng(args.seed)
    check_z = rng.normal(0, .7, args.n*(args.n+1)//2)
    value, grad = objective(check_z, args.n, args.tau)
    errors = []
    h = 1e-5
    for j in range(len(check_z)):
        delta = np.zeros_like(check_z)
        delta[j] = h
        numerical = (objective(check_z+delta, args.n, args.tau)[0] -
                     objective(check_z-delta, args.n, args.tau)[0]) / (2*h)
        errors.append(abs(numerical-grad[j]))
    assert max(errors) < 1e-6, max(errors)
    records = []
    best = None
    for run in range(args.runs):
        z = rng.normal(0, [.3, 1, 2, 4, 8][run % 5], len(check_z))
        result = minimize(objective, z, args=(args.n, args.tau), jac=True,
                          method='L-BFGS-B', bounds=[(-8, 8)]*len(z),
                          options={'maxiter': 500, 'ftol': 2e-13,
                                   'gtol': 1e-9})
        record = {'run': run, 'value': float(result.fun),
                  'iterations': int(result.nit),
                  'success': bool(result.success)}
        records.append(record)
        if best is None or result.fun < best['value']:
            W, _, error = sinkhorn(result.x, args.n)
            F, _ = density_gradient(W)
            Ft, _ = density_gradient(1+args.tau*(W-1))
            best = record | {'regular_host': W.tolist(),
                             'density': F, 'smoothed_density': Ft,
                             'row_sum_relative_error': float(error)}
            print(best['run'], best['value'], flush=True)
        Path(args.output).write_text(json.dumps({
            'status': 'numerical auxiliary-route exploration only',
            'args': vars(args),
            'finite_difference_gradient_max_error': max(errors),
            'best': best, 'records': records}, indent=2))


if __name__ == '__main__':
    main()
