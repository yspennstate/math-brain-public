"""Structured families: compute H, I, B, L, U' (upward), TC, DTC ratios.  EVIDENCE (float logs)."""
import numpy as np, itertools, json
from feilib import *
from upward import Uprime, upper_sets

def table_from(fn, n):
    xs = np.array([[1 - 2 * ((x >> i) & 1) for i in range(n)] for x in range(1 << n)])
    return np.array([fn(v) for v in xs], dtype=np.int64)

def Lfun(p, n):
    idx = np.arange(1 << n); tot = 0.0
    for i in range(n):
        hi = idx[(idx >> i) & 1 == 1]; lo = hi ^ (1 << i)
        a = p[hi]; b = p[lo]; m = a > 0
        tot += (a[m] * np.log2(1 + b[m] / a[m])).sum()
    return tot

def stats(t):
    t = np.asarray(t); n = nbits(len(t)); p = spectrum(t)
    H = float(entropy(p)); inf = influences(p, n); I = float(inf.sum()); B = float(erasure_terms(p, n).sum())
    U = float(Uprime(p, n)); L = Lfun(p, n); TC = float(binh(inf).sum() - H); Var = float(1 - p[0])
    return dict(n=n, H=H, I=I, HI=H / I, BI=B / I, LI=L / I, UI=U / I, DTCI=(H - B) / I, TCI=TC / I, Var=Var,
                gran=(2 * (I - Var) + 2 * U) / H if H > 0 else None)

def maj(n): return table_from(lambda v: 1 if v.sum() > 0 else -1, n)
def tribes(w, m): return table_from(lambda v: -1 if any(all(v[j*w:(j+1)*w] == -1) for j in range(m)) else 1, w * m)
def addressing(a): return table_from(lambda v: v[a + int(sum(((1 - v[i]) // 2) << i for i in range(a)))], a + (1 << a))
def pointdefect(r): return table_from(lambda v: -1 if all(v == 1) else 1, r)
def recmaj3(depth):
    n = 3 ** depth
    def g(v):
        w = list(v)
        while len(w) > 1: w = [1 if w[3*i] + w[3*i+1] + w[3*i+2] > 0 else -1 for i in range(len(w) // 3)]
        return w[0]
    return table_from(g, n)
def bent(m): return table_from(lambda v: int(np.prod([1 if not (v[2*i] == -1 and v[2*i+1] == -1) else -1 for i in range(m)])), 2 * m)
def activated_bent(k, r):  # X003 child G: 1 + A(z)(b-1)
    def g(v):
        x, z = v[:k], v[k:]
        b = int(np.prod([(-1 if (x[2*i] == -1 and x[2*i+1] == -1) else 1) for i in range(k // 2)]))
        A = all(z == 1)
        return b if A else 1
    return table_from(g, k + r)
def x003(k, r):  # selector y between G and H (H = point-flipped)
    def g(v):
        y, x, z = v[0], v[1:k+1], v[k+1:]
        b = int(np.prod([(-1 if (x[2*i] == -1 and x[2*i+1] == -1) else 1) for i in range(k // 2)]))
        if y == -1 and all(x == 1): b = -b
        return b if all(z == 1) else 1
    return table_from(g, 1 + k + r)
def ltf(n, seed, thr=0.0):
    rng = np.random.default_rng(seed); w = rng.normal(size=n)
    return table_from(lambda v: 1 if v @ w - thr * np.abs(w).sum() > 0 else -1, n)

if __name__ == "__main__":
    fams = {}
    for n in [5, 9, 13]: fams[f"maj{n}"] = maj(n)
    for (w, m) in [(2, 3), (3, 3), (3, 4), (4, 3)]: fams[f"tribes{w}x{m}"] = tribes(w, m)
    for a in [1, 2, 3]: fams[f"addr{a}"] = addressing(a)
    for r in [4, 8, 12]: fams[f"pd{r}"] = pointdefect(r)
    fams["recmaj3_d2"] = recmaj3(2)
    for m in [2, 3, 4]: fams[f"bent{2*m}"] = bent(m)
    fams["actbent_k4r4"] = activated_bent(4, 4); fams["x003_k4r4"] = x003(4, 4); fams["x003_k4r6"] = x003(4, 6)
    for s in range(3): fams[f"ltf12_{s}"] = ltf(12, s); fams[f"ltf12b_{s}"] = ltf(12, s, 0.3)
    res = {}
    for k, t in fams.items():
        s = stats(t); res[k] = s
        print(f"{k:14s} n={s['n']:2d} H/I={s['HI']:.3f} B/I={s['BI']:.3f} L/I={s['LI']:.3f} U'/I={s['UI']:.3f} DTC/I={s['DTCI']:.3f} TC/I={s['TCI']:.3f} (2(I-V)+2U')/H={s['gran'] if s['gran'] is None else round(s['gran'],3)}")
    json.dump(res, open("../data/families.json", "w"), indent=1)
