"""Which leaf type (number of core / auxiliary positions on its path) attains the minimum of
B_w/Inf_w and of Delta_w/Inf_w in Numaro's tower G_k; also the depth-1 ratios by coordinate."""
import sys, os, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from feilib import *
from tower_stable import E_stable, delta_gate_increment, h2_small
set_polite()
g = np.load(os.path.join(HERE, "..", "..", "inputs", "numaro18_pm1_table.npy")).astype(float)
n = 18
gh = wht(g[None, :])[0]; p = gh ** 2
cq = coord_quantities(gh[None, :], n)
Inf = cq["Inf"][0]; Bg = cq["B"][0]; Dg = cq["Delta"][0]
core = [j for j in range(n) if abs(Inf[j] - 57 / 256) < 1e-12]
print("depth-1 B/Inf core:", np.round(Bg[core] / Inf[core], 4).tolist())
print("depth-1 B/Inf aux :", np.round(Bg[9:] / Inf[9:], 4).tolist())
print("depth-1 Delta/Inf core:", np.round(Dg[core] / Inf[core], 4).tolist())
print("depth-1 Delta/Inf aux :", np.round(Dg[9:] / Inf[9:], 4).tolist())
S = np.arange(1 << n); lows = [S[((S >> j) & 1) == 0] for j in range(n)]
ic, ia = 57 / 256, 1 / 256
bestB = {}; bestD = {}
for j in range(n):
    key = (1, 0) if j in core else (0, 1)
    for d, v in ((bestB, Bg[j] / Inf[j]), (bestD, Dg[j] / Inf[j])):
        if v < d.get(key, (np.inf, None))[0]:
            d[key] = (v, (j,))
cX, cD = {}, {}
for depth in range(2, 9):
    nB, nD = {}, {}
    for key in bestB:
        P = ic ** key[0] * ia ** key[1]
        for j in range(n):
            if (j, key) not in cX:
                lo = lows[j]
                cX[(j, key)] = float(E_stable(p[lo], P * P * p[lo | (1 << j)]).sum()) / (Inf[j] * P)
                cD[(j, key)] = (Inf[j] * h2_small(P * P) + delta_gate_increment(gh, n, j, P)) / (Inf[j] * P)
            nk = (key[0] + (j in core), key[1] + (j not in core))
            vB = bestB[key][0] + cX[(j, key)]; vD = bestD[key][0] + cD[(j, key)]
            if vB < nB.get(nk, (np.inf,))[0]: nB[nk] = (vB, (j,) + bestB[key][1])
            if vD < nD.get(nk, (np.inf,))[0]: nD[nk] = (vD, (j,) + bestD[key][1])
    bestB, bestD = nB, nD
    kb = min(bestB, key=lambda k: bestB[k][0]); kd = min(bestD, key=lambda k: bestD[k][0])
    print(f"depth {depth}: min B/Inf {bestB[kb][0]:.6f} at (core,aux)={kb} path(outer->leaf)={bestB[kb][1]};"
          f" min Delta/Inf {bestD[kd][0]:.6f} at {kd} path={bestD[kd][1]}", flush=True)
