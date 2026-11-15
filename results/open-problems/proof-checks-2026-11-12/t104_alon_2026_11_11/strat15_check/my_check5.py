"""PLAN item 5 (an agent): sample the 17 STRAT13 collar boxes for every N >= 7 and the limit.

Corroboration, not proof: exact C_N(q) = c0 + c1 q + c2 q^2 (q = N - 6, targets from exact_bernstein,
cross-checked against STRAT10/STRAT8 by my_cs_cross*.py) at rational points that satisfy my own
constraint formulas (my_check1b_lib.G). A point is in scope when every N-free constraint and ratio >= 0
hold and it is not in the a <= 129/250 region proved elsewhere (i.e. not (guard >= 0 and scale14 < 0)).
Per box: random points, points pulled to vertices, and float-minimised points of C_7 and c2 rounded to
rationals. Prints min over scope of C_N/(q+1)^2 for N in {7,8,10,20,100,1e6} and of c2.
Usage: python3 my_check5.py STRAT15_DIR N_PER_BOX SEED
"""
import sys, json, random
from fractions import Fraction as F
from pathlib import Path
import numpy as np
S15 = Path(sys.argv[1]).resolve(); NP = int(sys.argv[2]); rng = random.Random(int(sys.argv[3]))
import importlib.util
_sp = importlib.util.spec_from_file_location('mc1b', Path(__file__).resolve().parent / 'my_check1b_lib.py')
L = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(L)
sys.path.insert(0, str(S15))
import exact_bernstein as ex
targets, gs, cs = ex.chart_data()
c0, c1, c2 = [{m: F(v) for m, v in c.items()} for c in cs]
NS = [7, 8, 10, 20, 100, 10**6]

def ev(p, x):
    s = F(0)
    for m, c in p.items():
        t = c
        for xi, e in zip(x, m):
            if e: t *= xi ** e
        s += t
    return s
def fl(p):
    E = np.array(list(p.keys()), dtype=float); C = np.array([float(v) for v in p.values()])
    return lambda x: float(C @ np.prod(np.asarray(x, float) ** E, axis=1))
CON = {k: v for k, v in L.G.items() if k not in ('scale14', 'scale_guard')}
fcon = {k: fl(v) for k, v in CON.items()}; fg = fl(L.G['scale_guard']); fs = fl(L.G['scale14'])
fc = [fl(c0), fl(c1), fl(c2)]

def in_scope_exact(x):
    if any(ev(g, x) < 0 for g in CON.values()): return False
    return not (ev(L.G['scale_guard'], x) >= 0 and ev(L.G['scale14'], x) < 0)
def viol(x):
    v = sum(max(0.0, -f(x)) for f in fcon.values())
    if fg(x) >= 0: v += max(0.0, -fs(x))
    return v

inv = json.loads((S15 / 'inventory.json').read_text())['records']
boxes = [(r['node'], [tuple(map(F, b)) for b in r['box']]) for r in inv if r['old']['kind'] == 'collar']
print('collar boxes', len(boxes))
from scipy.optimize import minimize
glob = {N: None for N in NS}; glob['c2'] = None; total = 0; neg = []
for node, box in boxes:
    pts = []
    for i in range(NP):
        if i % 2: x = [a + (b - a) * F(rng.randrange(1001), 1000) for a, b in box]
        else:
            x = [(a if rng.random() < .5 else b) for a, b in box]
            x = [xi + (F(1) if xi == a else F(-1)) * (b - a) * F(rng.randrange(1, 60), 1000) for xi, (a, b) in zip(x, box)]
        pts.append(x)
    lo = np.array([float(a) for a, b in box]); hi = np.array([float(b) for a, b in box])
    for which in ('C7', 'c2'):
        f = (lambda x: fc[0](x) + fc[1](x) + fc[2](x)) if which == 'C7' else fc[2]
        for s in range(6):
            x0 = lo + (hi - lo) * np.array([rng.random() for _ in range(6)])
            obj = lambda x: f(np.clip(x, lo, hi)) + 1e6 * viol(np.clip(x, lo, hi))
            r = minimize(obj, x0, method='Nelder-Mead', options=dict(maxiter=3000, xatol=1e-12, fatol=1e-14))
            xr = np.clip(r.x, lo, hi)
            pts.append([min(max(F(float(v)).limit_denominator(10**9), a), b) for v, (a, b) in zip(xr, box)])
    nb = 0; bmin = {}
    for x in pts:
        if not in_scope_exact(x): continue
        nb += 1; a0, a1, a2 = ev(c0, x), ev(c1, x), ev(c2, x)
        for N in NS:
            q = N - 6; v = (a0 + a1 * q + a2 * q * q) / (q + 1) ** 2
            if v < 0: neg.append((node, N, float(v)))
            bmin[N] = v if N not in bmin else min(bmin[N], v)
        bmin['c2'] = a2 if 'c2' not in bmin else min(bmin['c2'], a2)
        if a2 < 0: neg.append((node, 'c2', float(a2)))
    total += nb
    for k, v in bmin.items(): glob[k] = v if glob[k] is None else min(glob[k], v)
    print('node', node, 'in-scope points', nb, ' '.join('%s:%.3g' % (k, float(v)) for k, v in bmin.items()), flush=True)
print('total in-scope points', total, 'negatives', len(neg))
for n in neg[:20]: print('  NEG', n)
print('global min C_N/(q+1)^2:', {k: (float(v) if v is not None else None) for k, v in glob.items()})
print('PASS' if not neg else 'FAIL')
