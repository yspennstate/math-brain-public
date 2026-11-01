"""Exhaustive monotone weighted thresholds on n <= NMAX coordinates; maximize H+/Delta over biases.

Usage: python search_small.py NMAX WMAX STARTS SEED
Writes data/search_small_n{NMAX}.json  (float evidence only).
"""
import sys, json, math, itertools, time
import numpy as np
from scipy.optimize import minimize
from biased import ltf_table, metrics

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4
WMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 6
STARTS = int(sys.argv[3]) if len(sys.argv) > 3 else 8
SEED = int(sys.argv[4]) if len(sys.argv) > 4 else 1
rng = np.random.default_rng(SEED)


def all_ltfs(n, wmax):
    seen = {}
    for w in itertools.combinations_with_replacement(range(wmax, 0, -1), n):
        w = list(w)  # non-increasing positive integers
        idx = np.arange(2 ** n)
        Ws = np.zeros(2 ** n)
        for i in range(n):
            Ws += w[i] * ((idx >> i) & 1)
        for th in sorted(set(Ws.tolist())):
            if th <= 0:
                continue
            T = (Ws >= th).astype(np.int64)
            # every coordinate must be relevant
            rel = True
            for i in range(n):
                a = T.reshape(-1, 2, 2 ** i)
                if np.array_equal(a[:, 0, :], a[:, 1, :]):
                    rel = False
                    break
            if not rel:
                continue
            key = T.tobytes()
            if key not in seen:
                seen[key] = (w, th, T)
    return list(seen.values())


def neg_ratio(x, T):
    q = 1.0 / (1.0 + np.exp(-np.clip(x, -14, 14)))
    m = metrics(T, q, with_rho=False)
    if m['Delta'] < 1e-12:
        return 0.0
    return -m['Hplus'] / m['Delta']


def optimize(T, n):
    best = (0.0, None)
    starts = [np.zeros(n)] + [rng.normal(0, 3, n) for _ in range(STARTS)]
    for x0 in starts:
        r = minimize(neg_ratio, x0, args=(T,), method='Nelder-Mead',
                     options=dict(maxiter=600 * n, xatol=1e-4, fatol=1e-7))
        if -r.fun > best[0]:
            best = (-r.fun, r.x.copy())
    return best


t0 = time.time()
results = []
for n in range(2, NMAX + 1):
    fns = all_ltfs(n, WMAX)
    for (w, th, T) in fns:
        val, x = optimize(T, n)
        q = (1 / (1 + np.exp(-np.clip(x, -14, 14)))).tolist() if x is not None else None
        results.append(dict(n=n, w=w, theta=th, ratio=val, q=q))
    print(n, len(fns), 'functions; best so far',
          max(r['ratio'] for r in results if r['n'] == n), round(time.time() - t0, 1), 's', flush=True)

results.sort(key=lambda r: -r['ratio'])
with open(f'../data/search_small_n{NMAX}.json', 'w', encoding='utf-8') as fh:
    json.dump(results, fh, indent=1)
for r in results[:15]:
    print(round(r['ratio'], 4), r['n'], r['w'], r['theta'], [round(v, 4) for v in r['q']])
