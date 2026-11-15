"""Independent exact replay of a sample of STRAT12 certificates (an agent).

Own code for: residual assembly, box -> [0,1]^6 substitution, tensor Bernstein
coefficients. Polynomials come from STRAT12 exact_bernstein.data() (which builds
them from STRAT10 zero_face.construct); the target is cross-checked against
STRAT10 cover_face.polynomials()[0] at random rational points.
Usage: python3 my_replay.py STRAT12_DIR N_SAMPLE SEED
"""
import sys, json, random, time
from fractions import Fraction as F
from math import comb
from pathlib import Path

D = Path(sys.argv[1]).resolve()
N = int(sys.argv[2]); SEED = int(sys.argv[3])
sys.path.insert(0, str(D)); sys.path.insert(0, str(D / 'STRAT10'))
import exact_bernstein as eb

target, gs = eb.data()
gs_all = dict(gs)

def evalp(p, x):
    s = F(0)
    for m, c in p.items():
        t = F(c)
        for xi, e in zip(x, m):
            if e: t *= xi ** e
        s += t
    return s

def shift_axis(p, i, a, w):
    """substitute x_i = a + w*u_i (exact), return dict over u."""
    out = {}
    for m, c in p.items():
        e = m[i]
        for j in range(e + 1):
            coef = F(c) * comb(e, j) * (a ** (e - j)) * (w ** j)
            if coef:
                k = m[:i] + (j,) + m[i + 1:]
                out[k] = out.get(k, 0) + coef
    return {k: v for k, v in out.items() if v}

def bern_min(p, box):
    for i, (a, b) in enumerate(box):
        p = shift_axis(p, i, a, b - a)
    n = [max(m[i] for m in p) for i in range(6)]
    # separable transform: b_k = sum_{j<=k} c_j prod C(k_i,j_i)/C(n_i,j_i)
    cur = dict(p)
    for i in range(6):
        nxt = {}
        for m, c in cur.items():
            j = m[i]
            for k in range(j, n[i] + 1):
                key = m[:i] + (k,) + m[i + 1:]
                nxt[key] = nxt.get(key, 0) + c * F(comb(k, j), comb(n[i], j))
        cur = nxt
    # absent multi-indices have coefficient 0 -> min must include 0 if tensor not full
    full = 1
    for x in n: full *= (x + 1)
    vals = list(cur.values())
    mn = min(vals)
    if len(cur) < full: mn = min(mn, F(0))
    return mn, n

def residual(box, kind, lam):
    gsb = eb.active_constraints(box)
    out = {m: F(c) for m, c in target.items()} if kind == 'positivity' else {}
    for key, v in lam.items():
        v = F(v); assert v >= 0
        names = key.split('*')
        assert all(nm in gsb for nm in names), key
        p = gsb[names[0]]
        if len(names) == 2: p = eb.multiply(p, gsb[names[1]])
        for m, c in p.items():
            out[m] = out.get(m, 0) - v * c
    return {m: c for m, c in out.items() if c}

def leaves(t):
    if t.get('kind') == 'split':
        for ch in t['children']: yield from leaves(ch)
    else:
        yield t

# 1. target cross-check vs STRAT10 cover_face.polynomials()[0]
import cover_face
rng = random.Random(SEED)
try:
    P0 = cover_face.polynomials()[0]
    gens = P0.ring.gens if hasattr(P0, 'ring') else None
    print('cover_face.polynomials()[0] type', type(P0).__name__)
    if isinstance(P0, dict):
        k0 = next(iter(P0)); print('key sample', k0, 'nvars', len(k0) if isinstance(k0, tuple) else '?')
        Q = {}
        for m, c in P0.items():
            if isinstance(m, tuple) and len(m) >= 6 and not any(m[6:]):
                Q[m[:6]] = Q.get(m[:6], 0) + F(c)
        ratios = set()
        for _ in range(6):
            x = [F(rng.randint(-40, 40), rng.randint(1, 9)) for _ in range(6)]
            a, b = evalp(target, x), evalp(Q, x)
            ratios.add(a / b if b else ('zero', a))
        print('TARGET/cover_face ratio at 6 random points:', ratios)
except Exception as e:
    P0 = None; print('cover_face check skipped:', repr(e)[:200])

# 2. sample certificates
X = json.load(open(D / 'certificates.json'))
allleaves = []
for r in X['records']:
    for lf in leaves(r['tree']):
        if lf.get('kind') in ('exclusion', 'positivity'):
            allleaves.append((r['node'], lf))
print('certified leaves', len(allleaves))
rng.shuffle(allleaves)
pos = [x for x in allleaves if x[1]['kind'] == 'positivity'][:N // 2]
exc = [x for x in allleaves if x[1]['kind'] == 'exclusion'][:N - N // 2]
ok = bad = 0
t0 = time.time()
for node, lf in pos + exc:
    box = [tuple(map(F, iv)) for iv in lf['box']]
    p = residual(box, lf['kind'], lf['lambda'])
    mn, n = bern_min(p, box)
    good = mn > 0
    ok += good; bad += (not good)
    print(('PASS' if good else 'FAIL'), node, lf['kind'], lf.get('path', ''), 'deg', n, 'minB', float(mn), flush=True)
print('RESULT', ok, 'PASS', bad, 'FAIL of', ok + bad, 'in %.1f s' % (time.time() - t0))
