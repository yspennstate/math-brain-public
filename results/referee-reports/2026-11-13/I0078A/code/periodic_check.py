#!/usr/bin/env python3
"""Small Metropolis check, not a thermodynamic or mixing certificate.

Energy: sum_{i<j} g_N(x_i-x_j), with local potential -|r|^a.
The convergent even-binomial/zeta expansion evaluates the image kernel.
All number variances are integrated exactly over the observation origin.
"""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
import json, time, csv
from pathlib import Path
import numpy as np
from scipy.special import binom, zeta

ROOT = Path(__file__).resolve().parents[1]
A = 0.5
COEF = np.array([0.] + [-2*binom(A, 2*j)*zeta(2*j-A, 1.) for j in range(1, 19)])

def kernel(r, n, terms=18):
    t = np.abs(np.remainder(r + n/2, n) - n/2)/n
    return n**A * (-t**A + np.polynomial.polynomial.polyval(t*t, COEF[:terms+1]))

def spatial_variance(x, lengths):
    n = len(x)
    ii, jj = np.triu_indices(n, 1)
    d = np.abs(x[ii]-x[jj])
    d = np.minimum(d, n-d)
    return np.array([l-l*l+2/n*np.maximum(l-d, 0).sum() for l in lengths])

def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
    start = time.monotonic()
    rng = np.random.default_rng(780013)
    # Independent checks of the interaction and spatial-variance formula.
    grid = np.linspace(0, 64, 1001)
    truncation_error = float(np.max(np.abs(kernel(grid, 64, 18)-kernel(grid, 64, 14))))
    assert truncation_error < 1e-9
    assert np.max(np.abs(kernel(grid, 64)-kernel(64-grid, 64))) < 1e-10
    lengths = np.array([1., 2., 4., 8., 16.])
    assert np.max(np.abs(spatial_variance(np.arange(64.), lengths))) < 1e-10
    half = spatial_variance(np.arange(64.), np.array([1.5, 4.5]))
    assert np.max(np.abs(half-.25)) < 1e-10
    # Independently integrate using the 2N jump points of the moving window.
    check_x = rng.uniform(0, 64, 64)
    for length, value in zip(lengths, spatial_variance(check_x, lengths)):
        edges = np.unique(np.r_[0., 64., check_x, (check_x-length) % 64])
        origins = (edges[:-1]+edges[1:])/2
        counts = (np.remainder(check_x[:, None]-origins, 64) < length).sum(axis=0)
        integrated = np.sum(np.diff(edges)*(counts-length)**2)/64
        assert abs(integrated-value) < 1e-10
    rows = []
    for n in [32, 64, 128]:
        lens = np.array([1., 2., 4., 8., 16.])
        for beta in [.25, 4.]:
            for initial in ['lattice', 'uniform']:
                x = np.arange(n, dtype=float) if initial == 'lattice' else rng.uniform(0, n, n)
                step = min(2., 1/np.sqrt(beta))
                samples = []
                accepted = proposed = 0
                for sweep in range(1200):
                    for i in rng.permutation(n):
                        trial = (x[i] + rng.uniform(-step, step)) % n
                        # Exclude self explicitly; self-energy is constant, not moved.
                        other = np.r_[x[:i], x[i+1:]]
                        delta = np.sum(kernel(trial-other, n)-kernel(x[i]-other, n))
                        proposed += 1
                        if np.log(rng.random()) < -beta*delta:
                            x[i] = trial
                            accepted += 1
                    if sweep >= 400 and sweep % 8 == 0:
                        samples.append(spatial_variance(x, lens))
                samples = np.array(samples)
                # Ten contiguous block means; useful diagnostics, not proven errors.
                block = samples.reshape(10, 10, len(lens)).mean(axis=1)
                np.savez(ROOT/'data'/f'mc_N{n}_beta{beta}_{initial}.npz',
                         variances=samples, lengths=lens, final_configuration=x)
                for j, length in enumerate(lens):
                    rows.append(dict(N=n, beta=beta, initial=initial, L=length,
                                     variance=float(samples[:, j].mean()),
                                     block_se=float(block[:, j].std(ddof=1)/np.sqrt(10)),
                                     acceptance=accepted/proposed))
                print(json.dumps({'N':n, 'beta':beta, 'initial':initial,
                                  'variance':samples.mean(axis=0).tolist(),
                                  'acceptance':accepted/proposed}), flush=True)
    with (ROOT/'data'/'periodic_variance.csv').open('w') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys()); writer.writeheader(); writer.writerows(rows)
    (ROOT/'data'/'simulation_metadata.json').write_text(json.dumps({
        'a':A, 's':-A, 'seed':780013, 'sweeps':1200, 'burn_sweeps':400,
        'sample_every':8, 'samples_per_chain':100, 'kernel_terms':18,
        'kernel_18_vs_14_error':truncation_error, 'nice':os.getpriority(os.PRIO_PROCESS,0),
        'threads':1, 'elapsed_seconds':time.monotonic()-start,
        'limitations':'Small finite systems; no mixing certificate; block errors are diagnostics only.'
    }, indent=2)+'\n')

if __name__ == '__main__': main()
