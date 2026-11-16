"""Independent exact check of STRAT15 exclusion transfers (an agent).

Own polynomial algebra and tensor Bernstein code (Fractions only). The all-N constraints are
written from the formulas (STRAT10 cover_face.necessary with the all-N ratio r >= 3/25 and the
all-N scale premise a >= 129/250). For a sample of 'weaker-Farkas' transfers in domain_audit.json:
residual = -sum lambda_k g_k (products allowed) must have Bernstein minimum > 0 on the box, and
scale14 may be used only where X = 129 D - 250 tau has Bernstein minimum >= 0 on the box.
Usage: python3 my_check1b.py DOMAIN_AUDIT_JSON N_SAMPLE SEED
"""
import sys, json, random, time
from fractions import Fraction as F
from math import comb

Z = (0,) * 6
def var(i):
    m = [0] * 6; m[i] = 1; return {tuple(m): F(1)}
def const(c): return {Z: F(c)} if c else {}
def add(*ps):
    out = {}
    for p in ps:
        for m, c in p.items(): out[m] = out.get(m, 0) + c
    return {m: c for m, c in out.items() if c}
def scal(k, p): return {m: F(k) * c for m, c in p.items()} if k else {}
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
G['ratio'] = sub(scal(784, delta), scal(75, mul(tau, tau)))      # r >= 3/25
Dd = sub(scal(20, t), tau)
X = sub(scal(129, Dd), scal(250, tau))                            # 250 (129/250 D - tau)
G['scale_guard'] = X
G['scale14'] = sub(scal(62500, sub(mul(tau, tau), scal(4, delta))), mul(X, X))

def shift_axis(p, i, a, w):
    out = {}
    for m, c in p.items():
        e = m[i]
        for j in range(e + 1):
            coef = c * comb(e, j) * (a ** (e - j)) * (w ** j)
            if coef:
                k = m[:i] + (j,) + m[i + 1:]; out[k] = out.get(k, 0) + coef
    return {k: v for k, v in out.items() if v}

def bern_min(p, box, degs=None):
    for i, (a, b) in enumerate(box): p = shift_axis(p, i, a, b - a)
    n = [max([m[i] for m in p] or [0]) for i in range(6)]
    if degs: n = [max(a, int(b)) for a, b in zip(n, degs)]
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

def residual(box, lam):
    out = {}
    used_scale = False
    for key, v in lam.items():
        v = F(v); assert v >= 0, ('negative multiplier', key)
        names = key.split('*')
        polys = [G[nm] for nm in names]
        used_scale |= 'scale14' in names
        p = polys[0]
        for q in polys[1:]: p = mul(p, q)
        out = add(out, scal(-v, p))
    return out, used_scale

d = json.load(open(sys.argv[1]))
NS = int(sys.argv[2]); rng = random.Random(int(sys.argv[3]))
far = [x for x in d['transferred'] if x['transfer']['method'] == 'weaker-Farkas']
print('weaker-Farkas transfers', len(far))
sample = rng.sample(far, min(NS, len(far)))
ok = fail = guardfail = 0; t0 = time.time()
for x in sample:
    cert = x['transfer']['certificate']
    box = [tuple(map(F, b)) for b in cert['box']]
    p, used = residual(box, cert['lambda'])
    if used and bern_min(X, box) < 0:
        guardfail += 1; print('GUARD FAIL', x['source'], x['node'], x['path']); continue
    mn = bern_min(p, box, cert.get('bernstein_degrees'))
    if mn > 0: ok += 1
    else: fail += 1; print('FAIL', x['source'], x['node'], x['path'], float(mn))
print('sampled', len(sample), 'PASS', ok, 'FAIL', fail, 'GUARD FAIL', guardfail, 'seconds %.1f' % (time.time() - t0))
