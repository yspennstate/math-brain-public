"""G0013 exact integer search, 2026-09-12 (claude-q2-attack-0912).

Same discretisation as prob1000_lean_20260908/g0013_permutation_search.py: marginals uniform on
x_i=(i+1/2)/n, coupling pi_sigma = (1/n) sum_i delta_{(x_i, x_sigma(i))}, product nu = uniform on the
n^2 grid.  W_2^2(pi_sigma, nu) is a transportation problem with n^2 unit sources and n sinks of
capacity n.  Scaling coordinates by n, every cost (j-i)^2 + (k-sigma(i))^2 is an integer, so the
optimum is an exact integer T(sigma) and W_2^2 = T(sigma)/n^4.  Solved as an n^2 x n^2 assignment
(each atom expanded into n copies) with scipy's Hungarian algorithm: exact, milliseconds.
Symmetries used to cut the enumeration: sigma -> sigma^-1 (swap coordinates), sigma -> rev o sigma
(y -> 1-y), sigma -> sigma o rev (x -> 1-x); all preserve nu and the value.
"""
import itertools, sys, time
import numpy as np
from scipy.optimize import linear_sum_assignment

def T_of(n, sigma, _cache={}):
    key = (n, tuple(sigma))
    if key in _cache: return _cache[key]
    J, K = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")
    src = np.stack([J.ravel(), K.ravel()], 1)                       # n^2 grid points
    s = np.asarray(sigma)
    C = (src[:, None, 0] - np.arange(n)[None, :]) ** 2 + (src[:, None, 1] - s[None, :]) ** 2   # n^2 x n
    Cexp = np.repeat(C, n, axis=1)                                   # n^2 x n^2
    r, c = linear_sum_assignment(Cexp)
    val = int(Cexp[r, c].sum())
    _cache[key] = val
    return val

def canon(sigma):
    n = len(sigma); s = tuple(sigma)
    inv = tuple(np.argsort(s))
    rev = lambda t: tuple(n - 1 - x for x in t)
    revpos = lambda t: tuple(reversed(t))
    forms = set()
    for t in (s, inv):
        for u in (t, rev(t)):
            for v in (u, revpos(u)):
                forms.add(v)
    return min(forms), forms

def main(n):
    t0 = time.time()
    seen = set(); vals = {}
    for sigma in itertools.permutations(range(n)):
        if sigma in seen: continue
        c, forms = canon(sigma)
        seen |= forms
        vals[c] = T_of(n, sigma)
    best = max(vals.values())
    arg = [s for s, v in vals.items() if v == best]
    ident = tuple(range(n))
    print(f"n={n}: {len(vals)} classes ({len(seen)} perms), max T={best} -> W2^2={best/n**4:.6f}; "
          f"identity T={vals[ident]} ; maximisers (canonical reps) {arg}; conjecture holds={arg==[ident]} ({time.time()-t0:.0f}s)", flush=True)
    second = max(v for s, v in vals.items() if s != ident)
    s2 = [s for s, v in vals.items() if v == second][:4]
    print(f"      runner-up T={second} -> {second/n**4:.6f} at {s2}", flush=True)
    return vals

if __name__ == "__main__":
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception: pass
    import pickle
    for n in [int(a) for a in sys.argv[1:]] or [3, 4, 5, 6, 7]:
        vals = main(n)
        pickle.dump(vals, open(f"g0013_vals_n{n}.pkl", "wb"))
