# Frozen spec: B05 selector family F(y,x,z) (y bit 0, bent data x on k bits, control z on r bits, active iff z=0,
# one-point flip of the bent at x=0 when y=1), k=6 r=12 (n=19) and k=4 r=8 (n=13, repeat), four fixed orders,
# badness thresholds K in {3,4,5}. Exact integer face/edge counts; float64 entropies. < 300 MB, < 10 min.
import numpy as np, math, json, sys
LOG2E = 1.0 / math.log(2.0)


def fwht(a):
    a = np.array(a, dtype=np.int64); N = a.shape[-1]; h = 1
    while h < N:
        b = a.reshape(a.shape[:-1] + (N // (2 * h), 2, h))
        x = b[..., 0, :].copy(); y = b[..., 1, :].copy()
        b[..., 0, :] = x + y; b[..., 1, :] = x - y
        a = b.reshape(a.shape[:-1] + (N,)); h *= 2
    return a


def split(f, i):
    N = f.shape[-1]; b = f.reshape(f.shape[:-1] + (N // (2 << i), 2, 1 << i))
    return b[..., 0, :].reshape(f.shape[:-1] + (N // 2,)), b[..., 1, :].reshape(f.shape[:-1] + (N // 2,))


def edges_cut(u):
    m = u.shape[-1].bit_length() - 1; tot = np.zeros(u.shape[:-1], dtype=np.int64)
    for j in range(m):
        g, h = split(u, j); tot += (g != h).sum(axis=-1)
    return tot


def h2(t):
    t = np.asarray(t, dtype=np.float64)
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where((t > 0) & (t < 1), -t * np.log2(np.where(t > 0, t, 1.0)) - (1 - t) * np.log2(np.where(t < 1, 1 - t, 1.0)), 0.0)


def ent(p):
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(p > 0, -p * np.log2(np.where(p > 0, p, 1.0)), 0.0).sum(axis=-1)


def node(f, i):
    g, h = split(f, i); M = g.shape[-1]
    a = fwht(g).astype(np.float64) / M; b = fwht(h).astype(np.float64) / M
    q = (a * a + b * b) / 2; e = (a - b) ** 2 / 4
    with np.errstate(divide='ignore', invalid='ignore'):
        th = np.where(q > 0, e / np.where(q > 0, q, 1.0), 0.0)
    return g, h, (q * h2(th)).sum(axis=-1), ent(q) - (ent(a * a) + ent(b * b)) / 2, (g != h).sum(axis=-1) / M, edges_cut(g * h) / M


def family(k, r):
    # lean version (no n-column bit matrix): peak well under 100 MB at n=19
    n = 1 + k + r; X = np.arange(1 << n, dtype=np.int64)
    bit = lambda j: (X >> j) & 1
    s = np.zeros(1 << n, dtype=np.int64)
    for j in range(0, k, 2):
        s += bit(1 + j) * bit(2 + j)
    v = 1 - 2 * (s % 2)
    datamask = ((1 << k) - 1) << 1
    flip = (bit(0) == 1) & ((X & datamask) == 0)
    v = np.where(flip, -v, v)
    ctrlmask = ((1 << r) - 1) << (1 + k)
    active = (X & ctrlmask) == 0
    return np.where(active, v, 1).astype(np.int64), n


res = {}
for (k, r) in [(4, 8), (6, 12)]:
    f, n = family(k, r)
    W = fwht(f).astype(np.float64) / f.size; p = W * W
    sizes = np.array([bin(t).count('1') for t in range(f.size)], dtype=np.float64)
    H = float(ent(p)); I = float((p * sizes).sum())
    I_formula = 2.0 ** (-k - r) + 2.0 ** (-r) * (k / 2 + k * 2.0 ** (-k)) + r * 2.0 ** (-r) * (1 - 2.0 ** (-k / 2) + 2.0 ** (-k))
    ctrl = list(range(1 + k, n)); data = list(range(1, 1 + k))
    orders = {'selector_first': [0] + ctrl + data, 'control_first': ctrl + [0] + data,
              'data_first': data + ctrl + [0], 'control_data_selector': ctrl + data + [0]}
    out = dict(k=k, r=r, n=n, H=H, I=I, I_formula=I_formula, root_credit_selector_first=(k + r) * 2.0 ** (-k - r),
               root_ratio_bound=2.0 ** (1 - k), orders={})
    for name, od in orders.items():
        cur = f[None, :]; pos = list(range(n)); Dsum = 0.0; Isum = 0.0; credit = 0.0
        acc = {K: [0.0, 0, 0.0] for K in (3.0, 4.0, 5.0)}
        for t, c in enumerate(od):
            i = pos.index(c); g, h, B, JS, d, half = node(cur, i); w = 2.0 ** (-t)
            Dsum += w * float((B + JS).sum()); Isum += w * float(d.sum()); credit += w * float(half.sum())
            for K in acc:
                bad = B > K * d + 1e-12
                acc[K][0] += w * float(half[bad].sum()); acc[K][1] += int(bad.sum()); acc[K][2] += w * float((B - K * d)[bad].sum())
            cur = np.concatenate([g, h], axis=0); pos.pop(i)
        assert abs(Dsum - H) < 1e-9 and abs(Isum - I) < 1e-9
        out['orders'][name] = dict(credit_total=credit, **{('K=%g' % K): dict(bad_credit=v[0], bad_credit_over_I=v[0] / I,
                                                                              n_bad=v[1], excess_B_over_I=v[2] / I)
                                                            for K, v in acc.items()})
    res['k%d_r%d' % (k, r)] = out
    print(json.dumps(out, indent=1)); sys.stdout.flush()
with open(sys.argv[1], 'w', encoding='utf-8') as fh:
    json.dump(res, fh, indent=1)
