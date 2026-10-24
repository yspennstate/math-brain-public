"""Restriction decrements of the upward functional U'.  Delta_i U' = U'(f) - (U'(f_+)+U'(f_-))/2.
Question: is Delta_i U' <= K Inf_i for ALL i (universal local) or for SOME i?  EVIDENCE."""
import numpy as np, json
from feilib import *
from upward import Uprime
from families import *

def dU(t):
    t = np.asarray(t); n = nbits(len(t)); p = spectrum(t); U = float(Uprime(p, n))
    inf = influences(p, n); out = []
    for i in range(n):
        pp = spectrum(restrict(t, n, i, 0)); pm = spectrum(restrict(t, n, i, 1))
        out.append(U - 0.5 * (float(Uprime(pp, n - 1)) + float(Uprime(pm, n - 1))))
    return np.array(out), inf

if __name__ == "__main__":
    # exhaustive n<=4: max over f and i of Delta_i U'/Inf_i ; and max_f min_i
    from exhaust import scan
    for n in [2, 3, 4]:
        r = scan(n); T = r['T']; nc = r['I'] > 0
        T = T[nc]; p = r['p'][nc]; inf = r['inf'][nc]
        U = Uprime(p, n)
        D = np.zeros_like(inf)
        Hd1 = hadamard(n - 1); N = 1 << n
        for i in range(n):
            tp = restrict(T, n, i, 0); tm = restrict(T, n, i, 1)
            pp = ((tp @ Hd1.T).astype(np.float64) / (N // 2)) ** 2
            pm = ((tm @ Hd1.T).astype(np.float64) / (N // 2)) ** 2
            D[:, i] = U - 0.5 * (Uprime(pp, n - 1) + Uprime(pm, n - 1))
        with np.errstate(divide='ignore', invalid='ignore'):
            ratio = np.where(inf > 1e-12, D / inf, np.nan)
        print(n, 'min Delta_iU:', np.nanmin(D), ' max_i,f Delta_iU/Inf_i:', np.nanmax(ratio), ' max_f min_i:', np.nanmax(np.nanmin(np.where(inf>1e-12, ratio, np.inf), axis=1)))
    for k, t in [('x003_k4r4', x003(4, 4)), ('x003_k4r6', x003(4, 6)), ('x003_k6r6', x003(6, 6)), ('pd8', pointdefect(8)), ('tribes3x3', tribes(3, 3)), ('maj9', maj(9)), ('addr2', addressing(2)), ('actbent_k4r4', activated_bent(4, 4))]:
        d, inf = dU(t); rel = inf > 1e-12
        print(f"{k:12s} Delta_iU/Inf_i: max={np.max(d[rel]/inf[rel]):.3f} min={np.min(d[rel]/inf[rel]):.3f}  first coords: {np.round(d[rel][:3]/inf[rel][:3],3)}")
