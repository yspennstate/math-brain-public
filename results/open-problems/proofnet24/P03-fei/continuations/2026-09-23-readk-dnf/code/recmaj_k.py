"""FEI / FEI+ ratios for read-once formulas of balanced threshold gates of larger fan-in:
MAJ_a o MAJ_b (n = a*b), and a weighted balanced LTF gate over MAJ_3 children."""
import math, numpy as np
from feicore import spectrum, popcounts, polite
polite()

def compose_tt(outer, children_n, child_fns):
    n = sum(children_n); N = 1 << n; xs = np.arange(N)
    vals = []; off = 0
    for cn, fn in zip(children_n, child_fns):
        blk = (xs >> off) & ((1 << cn) - 1)
        vals.append(fn(blk, cn)); off += cn
    V = np.stack(vals)          # 0/1 child outputs
    return np.where(outer(V), -1, 1), n

def maj(blk, cn):
    pc = np.zeros_like(blk)
    for j in range(cn): pc += (blk >> j) & 1
    return (2 * pc > cn).astype(int)

def stats(tt, n):
    P = spectrum(tt); pc = popcounts(n)
    nz = P > 1e-300; H = float(-(P[nz] * np.log2(P[nz])).sum())
    Hp = H - (P[0] * math.log2(1 / P[0]) if P[0] > 0 else 0.0)
    I = float((P * pc).sum()); Var = 1 - float(P[0])
    return H / I, Hp / (I - Var)

for (a, b) in [(3, 3), (5, 3), (3, 5), (7, 3), (3, 7), (5, 5)]:
    tt, n = compose_tt(lambda V, a=a: 2 * V.sum(axis=0) > a, [b] * a, [maj] * a)
    hi, fp = stats(tt, n)
    print(f"MAJ_{a} o MAJ_{b} (n={n}): H/I = {hi:.4f}, FEI+ ratio = {fp:.4f}", flush=True)
rng = np.random.default_rng(3)
for t in range(3):
    a = 5; w = rng.uniform(0.5, 2.0, size=a)            # balanced (self-dual) weighted majority: sgn(sum w_j y_j), no ties
    tt, n = compose_tt(lambda V, w=w: (V * 2 - 1).T @ w > 0, [3] * a, [maj] * a)
    hi, fp = stats(tt, n)
    print(f"weighted MAJ_5 {np.round(w, 2)} o MAJ_3 (n={n}): H/I = {hi:.4f}, FEI+ ratio = {fp:.4f}", flush=True)
