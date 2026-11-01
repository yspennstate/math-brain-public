"""Global sum G(f) = sum_i Delta_i U(f) versus I(f).  If G <= K I for all f, then U <= K I (induction) and FEI follows."""
import numpy as np, json
from feilib import *
from upward import Uprime
from exhaust import scan
from families import *

def G_of(t):
    t = np.asarray(t, dtype=np.int64); n = nbits(len(t)); p = spectrum(t); U = float(Uprime(p, n)); inf = influences(p, n)
    tp = np.stack([restrict(t, n, i, 0) for i in range(n)]); tm = np.stack([restrict(t, n, i, 1) for i in range(n)])
    D = U - 0.5 * (Uprime(spectrum(tp), n - 1) + Uprime(spectrum(tm), n - 1))
    return float(D.sum()), float(inf.sum()), U, D, inf

if __name__ == "__main__":
    for n in [2, 3, 4]:
        r = scan(n); nc = r['I'] > 0; T = r['T'][nc]; p = r['p'][nc]; I = r['I'][nc]
        U = Uprime(p, n); Hd1 = hadamard(n - 1); N = 1 << n; G = np.zeros_like(U)
        for i in range(n):
            pp = ((restrict(T, n, i, 0) @ Hd1.T).astype(np.float64) / (N // 2)) ** 2
            pm = ((restrict(T, n, i, 1) @ Hd1.T).astype(np.float64) / (N // 2)) ** 2
            G += U - 0.5 * (Uprime(pp, n - 1) + Uprime(pm, n - 1))
        k = int(np.argmax(G / I))
        print(n, 'max G/I =', round(float((G / I).max()), 4), 'at', T[k].tolist(), ' min G/I =', round(float((G/I).min()), 4))
    fam = {'pd8': pointdefect(8), 'pd12': pointdefect(12), 'tribes3x3': tribes(3, 3), 'tribes4x3': tribes(4, 3), 'maj9': maj(9), 'maj13': maj(13),
           'addr2': addressing(2), 'addr3': addressing(3), 'x003_k6r6': x003(6, 6), 'actbent': activated_bent(4, 4), 'recmaj9': recmaj3(2), 'bent8': bent(4)}
    for k, t in fam.items():
        G, I, U, D, inf = G_of(t); print(f"{k:10s} G/I={G/I:.3f} U/I={U/I:.3f}")
    for fn in ["../data/anneal_dU.json"]:
        d = json.load(open(fn))
        for key, v in d.items():
            G, I, U, D, inf = G_of(np.array(v['table'])); print(f"anneal {key}: G/I={G/I:.3f} U/I={U/I:.3f}")
    d = json.load(open("../data/anneal_sel.json"))
    for key, v in d.items():
        g = np.array(v['g']); h = np.array(v['h']); f = np.empty(2 * len(g), dtype=np.int64); f[0::2] = g; f[1::2] = h
        G, I, U, D, inf = G_of(f); print(f"sel {key}: G/I={G/I:.3f} U/I={U/I:.3f} min_i ratio={np.min(D[inf>1e-12]/inf[inf>1e-12]):.3f}")
