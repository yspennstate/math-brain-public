# B05 lead check: isoperimetric payment of the rare logarithm and the exact odd-face telescope.
# FROZEN SPEC (written before the first run, not changed after):
#   families: all Boolean f on n<=4 (exhaustive); AND_r r=2..12; quadratic bent b_k k=2..12 even;
#   fair bent/one-point-flip selector F'_k k=4..10; activated bent G_{k,r} (k=4: r=2..8, k=6: r=2..5);
#   B05 selector family k=4, r=8 (n=13) under four fixed orders; random n=8 functions (seed 20261011)
#   for the tree telescope; exhaustive n=3,4 localized-bridge scan over all coordinate orders, K in {2,3,4}.
#   Arithmetic: Walsh coefficients, edge counts and face counts are integers (exact); the integer
#   isoperimetric test s^s 2^e >= 2^(m s) uses Python integers (exact); entropies are float64 and every
#   entropy margin is reported with its value so the float error (< 1e-12 here) can be read off.
#   Budget: < 300 MB, < 10 minutes. No GPU, no window, nothing left running.
import numpy as np, math, json, sys, itertools
LOG2E = 1.0 / math.log(2.0)
OUT = {}


def fwht(a):
    a = np.array(a, dtype=np.int64)
    N = a.shape[-1]; h = 1
    while h < N:
        b = a.reshape(a.shape[:-1] + (N // (2 * h), 2, h))
        x = b[..., 0, :].copy(); y = b[..., 1, :].copy()
        b[..., 0, :] = x + y; b[..., 1, :] = x - y
        a = b.reshape(a.shape[:-1] + (N,)); h *= 2
    return a


def split(f, i):
    """children of f along coordinate i: g = f|x_i=0, h = f|x_i=1 (same index order)."""
    N = f.shape[-1]
    b = f.reshape(f.shape[:-1] + (N // (2 << i), 2, 1 << i))
    return (b[..., 0, :].reshape(f.shape[:-1] + (N // 2,)),
            b[..., 1, :].reshape(f.shape[:-1] + (N // 2,)))


def dim(N):
    return N.bit_length() - 1


def edges_cut(u):
    """number of cube edges along which the +-1 function u changes sign."""
    m = dim(u.shape[-1]); tot = np.zeros(u.shape[:-1], dtype=np.int64)
    for j in range(m):
        g, h = split(u, j); tot += (g != h).sum(axis=-1)
    return tot


def n_odd(f):
    """number of 2-faces whose four corner values multiply to -1."""
    n = dim(f.shape[-1]); tot = np.zeros(f.shape[:-1], dtype=np.int64)
    for i in range(n):
        g, h = split(f, i); tot += edges_cut(g * h)
    assert np.all(tot % 2 == 0)          # each face {i,j} is seen from i and from j
    return tot // 2


def ent(p):
    p = np.asarray(p, dtype=np.float64)
    with np.errstate(divide='ignore', invalid='ignore'):
        t = np.where(p > 0, -p * np.log2(np.where(p > 0, p, 1.0)), 0.0)
    return t.sum(axis=-1)


def h2(t):
    t = np.asarray(t, dtype=np.float64)
    with np.errstate(divide='ignore', invalid='ignore'):
        v = np.where((t > 0) & (t < 1),
                     -t * np.log2(np.where(t > 0, t, 1.0)) - (1 - t) * np.log2(np.where(t < 1, 1 - t, 1.0)), 0.0)
    return v


def spectral(f):
    return fwht(f).astype(np.float64) / f.shape[-1]


def HI(f):
    N = f.shape[-1]; p = spectral(f) ** 2
    sizes = np.array([bin(s).count('1') for s in range(N)], dtype=np.float64)
    return ent(p), (p * sizes).sum(axis=-1)


def node_stats(f, i):
    g, h = split(f, i); M = g.shape[-1]
    a = spectral(g); b = spectral(h)
    q = (a * a + b * b) / 2; e = (a - b) ** 2 / 4
    with np.errstate(divide='ignore', invalid='ignore'):
        th = np.where(q > 0, e / np.where(q > 0, q, 1.0), 0.0)
    B = (q * h2(th)).sum(axis=-1)
    JS = ent(q) - (ent(a * a) + ent(b * b)) / 2
    dcount = (g != h).sum(axis=-1)
    cut = edges_cut(g * h)
    return dict(g=g, h=h, B=B, JS=JS, d=dcount / M, dcount=dcount, cut=cut, halfI=cut / M, M=M)


def all_functions(n):
    N = 1 << n; idx = np.arange(1 << N, dtype=np.int64)[:, None]
    bits = (idx >> np.arange(N, dtype=np.int64)[None, :]) & 1
    return (1 - 2 * bits).astype(np.int64)


C_JS_C005 = 2 * LOG2E      # C005 constant
C_JS_TOPSOE = 4.0          # self-contained: JS_bits <= Delta/2 (Topsoe) and Delta <= 8 min(d, 1-d)

# ---------------- Part A: exhaustive n<=4 ----------------
partA = {}
for n in range(1, 5):
    F = all_functions(n); m = n - 1
    H, I = HI(F); No = n_odd(F); Q = No * 2.0 ** (1 - n)
    res = dict(functions=int(F.shape[0]), splits=0, iso_integer_failures=0, telescope_failures=0,
               min_margin_lemma=None, max_B_when_d0=0.0, max_identity_error=0.0,
               min_margin_JS_C005=None, min_margin_JS_topsoe=None, max_B_over_d=0.0,
               min_margin_halfI_le_avgI=None)
    mins = dict(lem=np.inf, js1=np.inf, js2=np.inf, avg=np.inf)
    for i in range(n):
        st = node_stats(F, i); res['splits'] += int(F.shape[0])
        s = st['dcount']; ec = st['cut']
        for sv, ev in set(zip(s.tolist(), ec.tolist())):
            if sv >= 1 and (sv ** sv) * (2 ** ev) < 2 ** (m * sv):
                res['iso_integer_failures'] += int(((s == sv) & (ec == ev)).sum())
        tel = No - (ec + n_odd(st['g']) + n_odd(st['h']))
        res['telescope_failures'] += int((tel != 0).sum())
        d = st['d']; B = st['B']; JS = st['JS']; pos = d > 0
        marg = st['halfI'] + LOG2E * d - B
        if pos.any():
            mins['lem'] = min(mins['lem'], float(marg[pos].min()))
            res['max_B_over_d'] = max(res['max_B_over_d'], float((B[pos] / d[pos]).max()))
        if (~pos).any():
            res['max_B_when_d0'] = max(res['max_B_when_d0'], float(np.abs(B[~pos]).max()))
        Hg, Ig = HI(st['g']); Hh, Ih = HI(st['h'])
        res['max_identity_error'] = max(res['max_identity_error'], float(np.abs(H - (Hg + Hh) / 2 - B - JS).max()))
        mn = np.minimum(d, 1 - d)
        mins['js1'] = min(mins['js1'], float((C_JS_C005 * mn - JS).min()))
        mins['js2'] = min(mins['js2'], float((C_JS_TOPSOE * mn - JS).min()))
        mins['avg'] = min(mins['avg'], float(((Ig + Ih) / 2 - st['halfI']).min()))
    res['min_margin_lemma'] = mins['lem']; res['min_margin_JS_C005'] = mins['js1']
    res['min_margin_JS_topsoe'] = mins['js2']; res['min_margin_halfI_le_avgI'] = mins['avg']
    res['min_margin_H_le_(log2e+2/ln2)I+Q'] = float(((LOG2E + C_JS_C005) * I + Q - H).min())
    res['min_margin_H_le_(log2e+4)I+Q'] = float(((LOG2E + C_JS_TOPSOE) * I + Q - H).min())
    res['max_Q_over_I'] = float((Q[I > 0] / I[I > 0]).max())
    partA[n] = res
OUT['partA_exhaustive'] = partA
print('PART A', json.dumps(partA, indent=1)); sys.stdout.flush()


# ---------------- Part B: families with exact closed forms ----------------
def tt_from(fun, n):
    xs = ((np.arange(1 << n)[:, None] >> np.arange(n)[None, :]) & 1)
    return np.array([fun(x) for x in xs], dtype=np.int64)


def bent(x):
    s = 0
    for j in range(0, len(x) - 1, 2):
        s += int(x[j]) * int(x[j + 1])
    return 1 - 2 * (s % 2)


fam = []
for r in range(2, 13):
    f = tt_from(lambda x: -1 if all(v == 0 for v in x) else 1, r)
    H, I = HI(f[None, :]); No = int(n_odd(f[None, :])[0]); Qx = No * 2.0 ** (1 - r)
    Qf = r * (r - 1) * 2.0 ** (-r); If = r * 2.0 ** (1 - r)
    assert abs(Qx - Qf) < 1e-12 and abs(float(I[0]) - If) < 1e-12
    fam.append(dict(family='AND_r', r=r, H=float(H[0]), I=float(I[0]), Q=Qx, Q_over_I=Qx / float(I[0]),
                    H_over_I=float(H[0] / I[0])))
for k in range(2, 13, 2):
    f = tt_from(bent, k); H, I = HI(f[None, :]); No = int(n_odd(f[None, :])[0])
    assert abs(No * 2.0 ** (1 - k) - k / 4) < 1e-12
    fam.append(dict(family='bent_k', k=k, H=float(H[0]), I=float(I[0]), Q=No * 2.0 ** (1 - k)))
for k in range(4, 11, 2):
    n = k + 1; dl = 2.0 ** (-k)

    def Fp(x):
        v = bent(x[1:])
        if x[0] == 1 and all(t == 0 for t in x[1:]):
            v = -v
        return v
    f = tt_from(Fp, n); H, I = HI(f[None, :]); No = int(n_odd(f[None, :])[0]); Qx = No * 2.0 ** (1 - n)
    st = node_stats(f[None, :], 0)
    Qf = k / 4 + (k * k - k) * dl / 2; If = k / 2 + (k + 1) * dl
    assert abs(Qx - Qf) < 1e-12 and abs(float(I[0]) - If) < 1e-9
    fam.append(dict(family="fair_selector_bent_vs_onepoint_flip", k=k, H=float(H[0]), I=float(I[0]),
                    H_le_k_plus_1=bool(H[0] <= k + 1 + 1e-12), H_over_I=float(H[0] / I[0]), Q=Qx,
                    B_y_over_d=float(st['B'][0] / st['d'][0]), h2d_over_d=float(h2(st['d'][0]) / st['d'][0]),
                    halfI_gh_over_d=float(st['halfI'][0] / st['d'][0])))


def actG(k, r):
    def G(x):
        return bent(x[:k]) if all(t == 0 for t in x[k:]) else 1
    return tt_from(G, k + r)


for (k, rr) in [(4, range(2, 9)), (6, range(2, 6))]:
    for r in rr:
        f = actG(k, r); n = k + r; H, I = HI(f[None, :]); No = int(n_odd(f[None, :])[0]); Qx = No * 2.0 ** (1 - n)
        Eb = 2.0 ** (-k / 2)
        Qf = 0.5 * (r * (r - 1) * (1 - Eb) + k / 2 + r * k) * 2.0 ** (-r)
        assert abs(Qx - Qf) < 1e-12, (k, r, Qx, Qf)
        fam.append(dict(family='activated_bent_G', k=k, r=r, H=float(H[0]), I=float(I[0]), Q=Qx,
                        Q_over_I=Qx / float(I[0]), H_over_I=float(H[0] / I[0])))
OUT['partB_families'] = fam
print('PART B ok', len(fam)); sys.stdout.flush()


# ---------------- Part C: tree telescope and bad-node ledger ----------------
def ledger(F, order, Ks=(2.0, 3.0, 4.0)):
    """F: (nf, N). Fixed coordinate order. Returns per-function arrays."""
    nf = F.shape[0]; n = dim(F.shape[-1])
    cur = F[:, None, :]; pos = list(range(n))
    out = dict(cut=np.zeros(nf, dtype=np.int64), I=np.zeros(nf), Delta=np.zeros(nf), credit=np.zeros(nf),
               B=np.zeros(nf))
    for K in Ks:
        out['bad%g' % K] = np.zeros(nf); out['nbad%g' % K] = np.zeros(nf, dtype=np.int64)
        out['Bbad%g' % K] = np.zeros(nf)
    for t, coord in enumerate(order):
        i = pos.index(coord); st = node_stats(cur, i); w = 2.0 ** (-t)
        out['cut'] += st['cut'].sum(axis=1); out['I'] += w * st['d'].sum(axis=1)
        out['Delta'] += w * (st['B'] + st['JS']).sum(axis=1); out['credit'] += w * st['halfI'].sum(axis=1)
        out['B'] += w * st['B'].sum(axis=1)
        for K in Ks:
            bad = st['B'] > K * st['d'] + 1e-12
            out['bad%g' % K] += w * (st['halfI'] * bad).sum(axis=1)
            out['Bbad%g' % K] += w * ((st['B'] - K * st['d']) * bad).sum(axis=1)
            out['nbad%g' % K] += bad.sum(axis=1)
        cur = np.concatenate([st['g'], st['h']], axis=1); pos.pop(i)
    return out


rng = np.random.default_rng(20261011)
tel = []
for trial in range(12):
    n = 8
    if trial % 3 == 0:
        f = rng.choice([-1, 1], size=1 << n).astype(np.int64)
    elif trial % 3 == 1:
        f = np.where(rng.random(1 << n) < 0.05, -1, 1).astype(np.int64)
    else:
        f = tt_from(lambda x: bent(x[:6]) * (1 if (x[6] or x[7]) else -1), 8)
    No = int(n_odd(f[None, :])[0]); H, I = HI(f[None, :])
    for o in range(2):
        order = [int(v) for v in rng.permutation(n)]
        L = ledger(f[None, :], order)
        ok = (No == int(L['cut'][0])) and abs(float(H[0]) - float(L['Delta'][0])) < 1e-9 \
            and abs(float(I[0]) - float(L['I'][0])) < 1e-9 and abs(No * 2.0 ** (1 - n) - float(L['credit'][0])) < 1e-12
        assert ok
        tel.append(dict(trial=trial, order=order, N_odd=No, sum_cut=int(L['cut'][0]), H=float(H[0]),
                        I=float(I[0]), credit=float(L['credit'][0]), Q=No * 2.0 ** (1 - n)))
OUT['partC_telescope_random_n8'] = tel
print('PART C telescope ok', len(tel)); sys.stdout.flush()

# B05 selector family k=4, r=8: y = bit 0, data x = bits 1..4, control z = bits 5..12
k = 4; r = 8; n = 1 + k + r


def B05(x):
    if any(t == 1 for t in x[1 + k:]):
        return 1
    v = bent(x[1:1 + k])
    if x[0] == 1 and all(t == 0 for t in x[1:1 + k]):
        v = -v
    return v


fB = tt_from(B05, n)
HB, IB = HI(fB[None, :]); NoB = int(n_odd(fB[None, :])[0]); QB = NoB * 2.0 ** (1 - n)
ctrl = list(range(1 + k, n)); data = list(range(1, 1 + k))
orders = {'selector_first': [0] + ctrl + data, 'control_first': ctrl + [0] + data,
          'data_first': data + ctrl + [0], 'control_data_selector': ctrl + data + [0]}
b05 = dict(k=k, r=r, n=n, H=float(HB[0]), I=float(IB[0]), N_odd=NoB, Q=QB, Q_over_I=QB / float(IB[0]), orders={})
for name, od in orders.items():
    L = ledger(fB[None, :], od)
    assert int(L['cut'][0]) == NoB and abs(float(L['Delta'][0]) - float(HB[0])) < 1e-9
    b05['orders'][name] = {key: (float(v[0]) if v.dtype.kind == 'f' else int(v[0])) for key, v in L.items()}
    for K in (2.0, 3.0, 4.0):
        b05['orders'][name]['bad%g_over_I' % K] = float(L['bad%g' % K][0] / IB[0])
OUT['partC_B05_family'] = b05
print('PART C B05', json.dumps(b05, indent=1)); sys.stdout.flush()

# exhaustive localized-bridge scan: n = 3, 4, every coordinate order
scan = {}
for n in (3, 4):
    F = all_functions(n); H, I = HI(F); nz = I > 0
    best = {K: np.full(F.shape[0], np.inf) for K in (2.0, 3.0, 4.0)}
    worst = {K: np.zeros(F.shape[0]) for K in (2.0, 3.0, 4.0)}
    for od in itertools.permutations(range(n)):
        L = ledger(F, list(od))
        assert np.all(L['cut'] == n_odd(F)) and np.allclose(L['Delta'], H, atol=1e-9)
        for K in (2.0, 3.0, 4.0):
            ratio = np.where(nz, L['bad%g' % K] / np.where(nz, I, 1.0), 0.0)
            best[K] = np.minimum(best[K], ratio); worst[K] = np.maximum(worst[K], ratio)
    scan[n] = {('K=%g' % K): dict(max_over_f_of_min_over_orders=float(best[K].max()),
                                  max_over_f_and_orders=float(worst[K].max()),
                                  functions_with_some_bad_node_in_every_order=int((best[K] > 0).sum()))
               for K in (2.0, 3.0, 4.0)}
OUT['partC_exhaustive_localized_scan'] = scan
print('PART C scan', json.dumps(scan, indent=1)); sys.stdout.flush()

with open(sys.argv[1], 'w', encoding='utf-8') as fh:
    json.dump(OUT, fh, indent=1)
print('saved', sys.argv[1])
