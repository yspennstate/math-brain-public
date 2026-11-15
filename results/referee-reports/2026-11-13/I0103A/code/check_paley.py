#!/usr/bin/env python3
"""Small reproducible checks; numerical evidence is not an asymptotic proof."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))
import csv
from fractions import Fraction
import json
from pathlib import Path
import resource
import time
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
assert Path.cwd().resolve() == ROOT
START = time.monotonic()
RNG = np.random.default_rng(10320261113)
PRIMES = [101, 257, 509, 1009, 2017]

def legendre(p):
    chi = -np.ones(p, dtype=np.int64)
    chi[0] = 0
    chi[(np.arange(1, p, dtype=np.int64) ** 2) % p] = 1
    return chi

def gram(chi, indices):
    p = len(chi)
    indices = np.asarray(indices)
    finite = indices[indices != p]
    c = chi[(finite[:, None] - finite[None, :]) % p].astype(float)
    if p in indices:
        # Always return the special column last.
        c = np.block([[c, np.ones((len(finite), 1))],
                      [np.ones((1, len(finite))), np.zeros((1, 1))]])
    return np.eye(len(indices)) + c / np.sqrt(p)

def stats(g):
    ev = np.linalg.eigvalsh(g)
    return dict(lambda_min=float(ev[0]), lambda_max=float(ev[-1]),
                delta=float(max(1-ev[0], ev[-1]-1)),
                condition=float(np.sqrt(ev[-1]/ev[0])))

def clique_seed(chi):
    p = len(chi)
    selected = [0]
    candidates = np.flatnonzero(chi == 1)
    while len(candidates):
        # Deterministic greedy clique, not claimed to be maximum.
        v = int(candidates[0])
        selected.append(v)
        candidates = candidates[chi[(candidates-v) % p] == 1]
    return selected

checks = []
interval_rows = []
search_rows = []
for p in PRIMES:
    chi = legendre(p)
    assert all(p % d for d in range(2, int(p**0.5)+1)) and p % 4 == 1
    # Exact integer identity for the full conference matrix, at small p only.
    if p <= 257:
        c = chi[(np.arange(p)[:,None] - np.arange(p)[None,:]) % p]
        c = np.block([[c, np.ones((p,1), dtype=np.int64)],
                      [np.ones((1,p), dtype=np.int64), np.zeros((1,1), dtype=np.int64)]])
        assert np.array_equal(c @ c, p*np.eye(p+1, dtype=np.int64))
    # Independent Fourier construction of the selected Gram entries.
    selected = list(range(12)) + [p]
    q = np.flatnonzero(chi == 1)
    phi = np.zeros(((p+1)//2, len(selected)), dtype=complex)
    phi[0,:-1] = 1/np.sqrt(p)
    phi[1:,:-1] = np.sqrt(2/p)*np.exp(-2j*np.pi*q[:,None]*np.asarray(selected[:-1])[None,:]/p)
    phi[0,-1] = 1
    direct_gram = np.einsum('ri,rj->ij', phi.conj(), phi, optimize=False)
    gram_error = float(np.max(np.abs(direct_gram - gram(chi, selected))))
    assert gram_error < 1e-11
    # rho=1/32: N=p^(17/32). Whole subdictionary and principal submatrices.
    n = int(p**(17/32))
    g = gram(chi, list(range(n)))
    sg = stats(g)
    ext = stats(gram(chi, list(range(n))+[p]))
    # Toeplitz -> circulant compression. This finite FFT bound is a matrix
    # inequality, not an estimate of the continuous symbol maximum.
    length = 1 << (2*n-2).bit_length()
    kernel = np.zeros(length)
    kernel[1:n] = chi[1:n]
    kernel[-(n-1):] = chi[1:n][::-1]
    fourier_ev = np.fft.fft(kernel)
    assert np.max(np.abs(fourier_ev.imag)) < 1e-9
    fft_bound = float(np.max(np.abs(fourier_ev.real))/np.sqrt(p))
    assert sg['delta'] <= fft_bound + 1e-11
    # Discrete quadrature checks the continuous-symbol Rayleigh identity:
    # this grid integrates all terms exactly (up to floating-point error).
    z = RNG.standard_normal(n) + 1j*RNG.standard_normal(n)
    z /= np.linalg.norm(z)
    freq = np.arange(length)/length
    poly = np.einsum('ij,j->i', np.exp(2j*np.pi*freq[:,None]*np.arange(n)[None,:]), z, optimize=False)
    quad = float(np.mean(fourier_ev.real * np.abs(poly)**2)/np.sqrt(p))
    rayleigh = float(np.real(np.einsum('i,ij,j->', z.conj(), g-np.eye(n), z, optimize=False)))
    symbol_error = abs(quad-rayleigh)
    assert symbol_error < 1e-11
    # Affine progression invariance (also test a nonsquare step).
    for step in (1, 2, int(np.flatnonzero(chi == -1)[0])):
        ids = (7 + step*np.arange(n)) % p
        ga = gram(chi, ids)
        assert np.max(np.abs(ga-np.eye(n)-chi[step]*(g-np.eye(n)))) < 1e-11
    sub = np.sort(RNG.choice(n, max(2,n//2), replace=False))
    assert stats(g[np.ix_(sub,sub)])['delta'] <= sg['delta'] + 1e-11
    absnorm = float(np.linalg.eigvalsh(np.abs(g-np.eye(n)))[-1])
    assert abs(absnorm-(n-1)/np.sqrt(p)) < 1e-11
    interval_rows.append(dict(p=p, n=n, **sg,
                              extended_condition=ext['condition'], fft_upper_bound=fft_bound,
                              absolute_value_norm=absnorm))
    checks.append(dict(p=p, gram_error=gram_error, symbol_identity_error=symbol_error))
    clique = clique_seed(chi)
    for exponent in (0.55, 0.60):
        k = int(p**exponent)
        random_set = list(map(int, RNG.choice(p+1,k,replace=False)))
        padded = clique + list(map(int, RNG.choice(np.setdiff1d(np.arange(p),clique), k-len(clique),replace=False)))
        seeds = [('interval',list(range(k))), ('random',random_set), ('clique_padded',padded)]
        best = None
        for label, seed in seeds:
            current = list(seed)
            current_stats = stats(gram(chi,current))
            for trial in range(40):
                proposal = current.copy()
                slot = int(RNG.integers(k))
                candidate = int(RNG.integers(p+1))
                if candidate in proposal:
                    continue
                proposal[slot] = candidate
                proposed_stats = stats(gram(chi,proposal))
                if proposed_stats['condition'] > current_stats['condition']:
                    current, current_stats = proposal, proposed_stats
            record = dict(p=p, exponent=exponent, k=k, seed=label,
                          initial_clique_size=len(clique), **current_stats,
                          indices=current)
            if best is None or record['condition'] > best['condition']:
                best = record
        search_rows.append(best)

# Exponent audited in exact rational arithmetic in two parameterizations.
rho = Fraction(1,32)
alpha = Fraction(9,16)-rho
eta = rho/Fraction(3)
error_exp = Fraction(2,3)*alpha + Fraction(1,8) + eta - Fraction(1,2)
assert error_exp == -rho/Fraction(3)
eps = Fraction(1,32)
assert Fraction(2,3)*(Fraction(1,2)+eps)+Fraction(1,8)-Fraction(1,2) == -Fraction(1,48)

def write_csv(name, rows):
    with (ROOT/'data'/name).open('w') as output:
        writer = csv.DictWriter(output, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

write_csv('interval_checks.csv', interval_rows)
with (ROOT/'data/search_results.json').open('w') as output:
    json.dump(search_rows,output,indent=2)
summary = dict(seed=10320261113, nice=os.getpriority(os.PRIO_PROCESS,0),
               threads={key:os.environ[key] for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS')},
               checks=checks, elapsed_seconds=time.monotonic()-START,
               peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
               exponent_check=str(error_exp), all_checks_passed=True)
(ROOT/'data/verification.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
print('Worst conditions from bounded local search:')
for row in search_rows:
    print(row['p'], row['k'], row['seed'], row['condition'])
