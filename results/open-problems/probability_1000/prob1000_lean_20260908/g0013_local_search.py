"""G0013 local search (2026-09-10): hill-climb W_2^2(pi_sigma, U_n (x) U_n) over transpositions from random
permutations, n = 10 and 12, to look for a permutation beating the identity/reversal value. Same LP as
g0013_permutation_search.py. A climb that ends at the identity or reversal from a random start is weak evidence
that they are the global maximisers; a climb that ends ABOVE their value would refute the discrete conjecture."""
import sys, time
import numpy as np
from g0013_permutation_search import w2sq_perm

def climb(n, sigma, rng, val_cache):
    def val(s):
        if s not in val_cache: val_cache[s] = w2sq_perm(n, s)
        return val_cache[s]
    cur = tuple(sigma); v = val(cur); steps = 0
    while True:
        best, bv = None, v
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        rng.shuffle(pairs)
        for i, j in pairs:
            s = list(cur); s[i], s[j] = s[j], s[i]; s = tuple(s)
            sv = val(s)
            if sv > bv + 1e-12: best, bv = s, sv
        if best is None: return cur, v, steps
        cur, v = best, bv; steps += 1

def main(n, starts, seed):
    rng = np.random.default_rng(seed); cache = {}
    ident = tuple(range(n)); rev = tuple(range(n - 1, -1, -1))
    vi = w2sq_perm(n, ident); t0 = time.time()
    print(f"n={n}: identity value {vi:.6f} (reversal {w2sq_perm(n, rev):.6f})", flush=True)
    for k in range(starts):
        s0 = tuple(rng.permutation(n))
        s, v, steps = climb(n, s0, rng, cache)
        tag = "IDENTITY" if s == ident else ("REVERSAL" if s == rev else "OTHER")
        print(f"  start {k}: local max {v:.6f} after {steps} steps -> {tag} {s if tag=='OTHER' else ''}  "
              f"{'ABOVE identity!' if v > vi + 1e-9 else ''} ({time.time()-t0:.0f}s, {len(cache)} LPs)", flush=True)

if __name__ == "__main__":
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    starts = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    main(n, starts, 7)
