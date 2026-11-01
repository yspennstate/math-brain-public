"""Alternating best responses over sets (n = 3, b = 0 WLOG for invertible A since translating the sets
reproduces every linear term).  s is re-optimised after each sweep.  usage: python altbr3.py NAME START SEED"""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np, time, sys
from scipy.optimize import minimize_scalar
from q3tools import Law, density, g_partial
from mats3 import mats

H = 1/100
def cells_to_law(sel, grid):
    ivs = []; inrun = False
    for idx in range(len(sel)):
        if sel[idx] and not inrun: start = grid[idx]-H/2; inrun = True
        if inrun and (idx == len(sel)-1 or not sel[idx+1]): ivs.append((start, grid[idx]+H/2)); inrun = False
    a, b = zip(*ivs)
    return Law(list(a), list(b)), ivs

def opt_s(A, laws, s0, m=260):
    f = lambda s: -density(A, np.zeros(3), s, laws, m_per_unit=m, eta=0.004)
    ss = s0 + np.linspace(-0.6, 0.6, 25)
    vals = [f(s) for s in ss]; k = int(np.argmin(vals))
    lo, hi = ss[max(k-1,0)], ss[min(k+1,len(ss)-1)]
    r = minimize_scalar(f, bounds=(lo, hi), method='bounded', options=dict(xatol=1e-4))
    return r.x, -r.fun

name, start, seed = sys.argv[1], sys.argv[2], int(sys.argv[3])
A = mats()[name]; rng = np.random.default_rng(seed)
R = 6.0; grid = np.arange(-R, R, H) + H/2
if start == "int":
    laws = [Law([-0.5],[0.5]) for _ in range(3)]
else:   # random union of 2-4 intervals spread over [-3,3]
    laws = []
    for _ in range(3):
        k = rng.integers(2,5); cuts = np.sort(rng.random(k-1)); lens = np.diff(np.concatenate([[0],cuts,[1]]))
        pos = np.sort(rng.uniform(-3,3,k)); a = []; b = []; cur = None
        for p, l in zip(pos, lens):
            p = max(p, (b[-1]+0.05) if b else -1e9); a.append(p); b.append(p+l)
        laws.append(Law(a, b))
T0 = time.time()
s, val = opt_s(A, laws, 0.0)
print(f"{name} start={start} seed={seed}: initial p={val:.4f} s={s:.4f}", flush=True)
for sweep in range(4):
    for i in range(3):
        g = g_partial(A, np.zeros(3), s, i, laws, grid, m_per_unit=200, eta=0.004)
        order = np.argsort(-g); sel = np.zeros(len(g), bool); sel[order[:int(round(1/H))]] = True
        laws[i], ivs = cells_to_law(sel, grid)
    s, val = opt_s(A, laws, s)
    desc = " | ".join(",".join("[%.2f,%.2f]" % iv for iv in zip(l.a, l.b)) for l in laws)
    print(f"  sweep {sweep}: p={val:.4f} s={s:.4f}  sets: {desc}   t={time.time()-T0:.0f}s", flush=True)
    if time.time()-T0 > 150: break
