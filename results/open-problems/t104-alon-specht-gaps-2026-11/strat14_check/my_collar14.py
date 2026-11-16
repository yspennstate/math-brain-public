"""Independent sampled check of the 14 STRAT14 collar leaves (an agent).

Polynomials (constraints written from STRAT8 necessary(), target from STRAT8 construct()/80)
come from my_replay14.py (its code up to shift_axis, which also re-runs the exact
cross-check against STRAT14). For each collar leaf: random exact rational points in the
leaf box; at every point where all necessary constraints hold (strict ones > 0) the
target must be > 0. Points are drawn uniform and, half of them, pushed toward the box
corner nearest the box's own centre-of-limit (the leaf box is tiny, so uniform suffices).
Also records min target / (L1 distance from the box centre) as a crude local ratio.
Usage: python3 my_collar14.py STRAT14_DIR N_PER_LEAF SEED
"""
import sys, json, random
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
src = (HERE / 'my_replay14.py').read_text()
head = src.split('def shift_axis')[0]
D = Path(sys.argv[1]).resolve(); NP = int(sys.argv[2]); SEED = int(sys.argv[3])
sys.argv = [sys.argv[0], str(D), '0', '0']
exec(compile(head, 'my_replay14_head', 'exec'))

STRICT = {'connected', 'rank', 'ratio'}
def ev(p, x):
    s = F(0)
    for m, c in p.items():
        term = c
        for xi, e in zip(x, m):
            if e: term *= xi ** e
        s += term
    return s

def feasible(x):
    for k, p in G.items():
        v = ev(p, x)
        if v < 0 or (k in STRICT and v == 0): return False
    # outside STRAT8's old_small_scale exclusion (proved by STRAT6): X>=0 and X^2>=H with D>0
    Xv = ev(X, x); Hv = ev(H, x); Dv = ev(Dd, x)
    if Dv > 0 and Xv >= 0 and 40000 * Hv <= Xv * Xv: return False
    return True

def walk(tree, out):
    if tree['kind'] == 'split':
        for ch in tree['children']: walk(ch, out)
    elif tree['kind'] == 'collar':
        out.append(tree)

cert = json.load(open(D / 'certificates.json'))
coll = []
for rec in cert['records']:
    acc = []; walk(rec['tree'], acc)
    for tr in acc: coll.append((rec['node'], tr))
print('collar leaves', len(coll))
rng = random.Random(SEED)
DEN = 10 ** 9
tot_pts = tot_feas = tot_bad = 0
for node, tr in coll:
    box = [tuple(map(F, b)) for b in tr['box']]
    cen = [(a + b) / 2 for a, b in box]
    feas = bad = 0; minv = None; minratio = None
    for k in range(NP):
        x = [a + (b - a) * F(rng.randrange(DEN + 1), DEN) for a, b in box]
        if k % 2:  # pull toward a random vertex of the box (boundary-heavy)
            vtx = [box[i][rng.randrange(2)] for i in range(6)]
            s = F(rng.randrange(1, 1000), 1000)
            x = [xi + (vi - xi) * s for xi, vi in zip(x, vtx)]
        if not feasible(x): continue
        feas += 1
        v = ev(target, x)
        if v <= 0:
            bad += 1; print('BAD', node, tr.get('type'), [str(c) for c in x], v); continue
        d = sum(abs(xi - ci) for xi, ci in zip(x, cen))
        if minv is None or v < minv: minv = v
        if d and (minratio is None or v / d < minratio): minratio = v / d
    tot_pts += NP; tot_feas += feas; tot_bad += bad
    print('node', node, tr.get('type'), 'feasible', feas, 'of', NP, 'bad', bad,
          'min target %.3e' % float(minv) if minv is not None else 'min target -',
          'min target/L1(centre) %.3e' % float(minratio) if minratio is not None else '')
print('TOTAL points', tot_pts, 'feasible', tot_feas, 'nonpositive target at feasible', tot_bad)
