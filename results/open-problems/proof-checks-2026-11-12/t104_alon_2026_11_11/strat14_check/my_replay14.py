"""Independent exact check of a sample of STRAT14 certificates (an agent).

Own code for: the necessary constraints (written from STRAT8 cover_face.necessary,
variables [t,v1,z1,v2,z2,z] as STRAT8 ROOT), residual assembly, box -> [0,1]^6
substitution and tensor Bernstein coefficients. Target: STRAT8 zero_face.construct()[-1]/80,
the accepted STRAT8 face numerator; cross-checked against STRAT14 exact_bernstein.data().
Also: every record's leaves partition its STRAT8 box (exact volume sum, disjoint paths).
Usage: python3 my_replay14.py STRAT14_DIR N_SAMPLE SEED
"""
import sys, json, random, time
from fractions import Fraction as F
from math import comb
from pathlib import Path

D = Path(sys.argv[1]).resolve()
N = int(sys.argv[2]); SEED = int(sys.argv[3])

# ---- tiny exact polynomial algebra over 6 variables ----
Z = (0,) * 6
def var(i):
    m = [0] * 6; m[i] = 1; return {tuple(m): F(1)}
def const(c): return {Z: F(c)} if c else {}
def add(*ps):
    out = {}
    for p in ps:
        for m, c in p.items(): out[m] = out.get(m, 0) + c
    return {m: c for m, c in out.items() if c}
def scal(k, p): return {m: F(k) * c for m, c in p.items() if k}
def mul(a, b):
    out = {}
    for m, c in a.items():
        for n, d in b.items():
            k = tuple(x + y for x, y in zip(m, n)); out[k] = out.get(k, 0) + c * d
    return {m: c for m, c in out.items() if c}
def sub(a, b): return add(a, scal(-1, b))

t, v1, z1, v2, z2, z = (var(i) for i in range(6))
xs = [v1, v2, sub(sub(const(1), t), add(v1, v2)), t, const(-1)]
ys = [z1, z2, scal(-1, add(z, z1, z2)), {}, z]
G = {}
G['orientation'] = sub(sub(mul(t, t), const(1)), mul(z, z))
G['order12'] = sub(v2, v1)
G['order23'] = sub(xs[2], v2)
G['x3bound'] = add(xs[2], const(1))
for i in range(5):
    G['row%d' % i] = sub(scal(4, t), add(mul(xs[i], xs[i]), mul(ys[i], ys[i])))
for i in range(5):
    for j in range(i + 1, 5):
        if (i, j) != (3, 4):
            G['g%d%d' % (i, j)] = add(t, mul(xs[i], xs[j]), mul(ys[i], ys[j]))
M00 = add(*[mul(x, x) for x in xs]); M11 = add(*[mul(y, y) for y in ys])
M01 = add(*[mul(x, y) for x, y in zip(xs, ys)])
delta = sub(mul(M00, M11), mul(M01, M01)); tau = add(M00, M11)
G['spectral00'] = sub(scal(5, t), M00)
G['spectral11'] = sub(scal(5, t), M11)
G['connected'] = sub(mul(sub(scal(5, t), M00), sub(scal(5, t), M11)), mul(M01, M01))
G['rank'] = delta
G['ratio'] = sub(scal(784, delta), scal(75, mul(tau, tau)))
Dd = sub(scal(20, t), tau)
X = sub(scal(103, Dd), scal(200, tau))          # = 200 * (103/200 D - N)
H = sub(mul(tau, tau), scal(4, delta))
SCALE14 = sub(scal(40000, H), mul(X, X))        # >0 off STRAT8's old_small_scale region when X>=0

# ---- target from STRAT8 ----
sys.path.insert(0, str(D / 'STRAT8'))
from zero_face import construct
num = construct()[-1]
target = {}
for mon, c in num.terms():
    target[tuple(mon)] = F(int(c.numerator), int(c.denominator)) / 80

# ---- cross-check against STRAT14's own polynomials ----
sys.path.insert(0, str(D))
import exact_bernstein as eb
t14, g14 = eb.data()
assert {m: F(c) for m, c in t14.items()} == target, 'target mismatch'
for k, p in g14.items():
    mine = SCALE14 if k == 'scale14' else (X if k == 'scale_guard' else G[k])
    assert {m: F(c) for m, c in p.items()} == mine, ('constraint mismatch', k)
assert set(g14) == set(G) | {'scale14', 'scale_guard'}, set(g14) ^ set(G)
print('target and all %d constraints match STRAT8 formulas exactly' % len(g14))

def shift_axis(p, i, a, w):
    out = {}
    for m, c in p.items():
        e = m[i]
        for j in range(e + 1):
            coef = c * comb(e, j) * (a ** (e - j)) * (w ** j)
            if coef:
                k = m[:i] + (j,) + m[i + 1:]; out[k] = out.get(k, 0) + coef
    return {k: v for k, v in out.items() if v}

def bern_min(p, box):
    for i, (a, b) in enumerate(box): p = shift_axis(p, i, a, b - a)
    n = [max([m[i] for m in p] or [0]) for i in range(6)]
    cur = dict(p)
    for i in range(6):
        nxt = {}
        for m, c in cur.items():
            j = m[i]
            for k in range(j, n[i] + 1):
                key = m[:i] + (k,) + m[i + 1:]
                nxt[key] = nxt.get(key, 0) + c * F(comb(k, j), comb(n[i], j))
        cur = nxt
    full = 1
    for x in n: full *= x + 1
    vals = list(cur.values()); mn = min(vals) if vals else F(0)
    if len(cur) < full: mn = min(mn, F(0))
    return mn

def guard_ok(box):
    # scale14 allowed only if X >= 0 on the whole box (own Bernstein bound)
    return bern_min(X, box) >= 0

def residual(box, kind, lam):
    out = dict(target) if kind == 'positivity' else {}
    for key, v in lam.items():
        v = F(v); assert v >= 0
        names = key.split('*')
        polys = []
        for nm in names:
            if nm == 'scale14':
                assert guard_ok(box), 'scale14 used where X>=0 not certified'
                polys.append(SCALE14)
            else:
                polys.append(G[nm])
        p = polys[0] if len(polys) == 1 else mul(polys[0], polys[1])
        out = add(out, scal(-v, p))
    return out

def vol(box):
    r = F(1)
    for a, b in box: r *= b - a
    return r

def walk(tree, box, path, acc):
    if tree['kind'] == 'split':
        ax = tree['axis']; lo, hi = box[ax]; mid = (lo + hi) / 2
        l = list(box); r = list(box); l[ax] = (lo, mid); r[ax] = (mid, hi)
        walk(tree['children'][0], l, path + '0', acc)
        walk(tree['children'][1], r, path + '1', acc)
    else:
        assert [tuple(map(F, x)) for x in tree['box']] == [tuple(b) for b in box], 'leaf box mismatch'
        acc.append((tree, box))

cert = json.load(open(D / 'certificates.json'))
recs = cert['records']
leaves = []; kinds = {}; vol_ok = 0
for rec in recs:
    box = [tuple(map(F, x)) for x in rec['box']]
    acc = []
    walk(rec['tree'], box, '', acc)
    assert sum(vol(b) for _, b in acc) == vol(box)
    vol_ok += 1
    for tr, b in acc:
        kinds[tr['kind']] = kinds.get(tr['kind'], 0) + 1
        leaves.append((rec['node'], tr, b))
print('records', len(recs), 'partition volume ok', vol_ok, 'leaf kinds', kinds)
assert 'open' not in kinds

rng = random.Random(SEED)
bern = [x for x in leaves if x[1]['kind'] in ('exclusion', 'positivity')]
pos = [x for x in bern if x[1]['kind'] == 'positivity']; exc = [x for x in bern if x[1]['kind'] == 'exclusion']
sample = rng.sample(pos, min(N // 2, len(pos))) + rng.sample(exc, min(N // 2, len(exc)))
# deep leaves are the risky ones: add the 10 deepest of each kind
for group in (pos, exc):
    sample += sorted(group, key=lambda x: -x[1]['depth'])[:10]
npass = nfail = 0; t0 = time.time()
for node, tr, b in sample:
    p = residual(b, tr['kind'], tr['lambda'])
    mn = bern_min(p, b)
    ok = mn > 0
    npass += ok; nfail += (not ok)
    if not ok: print('FAIL', node, tr['path'], tr['kind'], mn)
print('sampled', len(sample), 'PASS', npass, 'FAIL', nfail, 'seconds %.1f' % (time.time() - t0))
collars = [x for x in leaves if x[1]['kind'] not in ('exclusion', 'positivity')]
print('non-Bernstein leaves', len(collars), sorted(set(x[1]['kind'] for x in collars)))
for node, tr, b in collars[:3]:
    print(' collar example node', node, json.dumps({k: v for k, v in tr.items() if k not in ('box',)})[:400])
