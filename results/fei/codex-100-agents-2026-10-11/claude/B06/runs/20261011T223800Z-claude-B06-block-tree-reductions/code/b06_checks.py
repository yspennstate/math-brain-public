# B06 lead checks. Exact integer Walsh spectra throughout. Floating logs are used only to locate
# candidates; certified statements use mpmath interval arithmetic (iv, 40 digits) with an explicit
# outward safety margin of 1e-12 when an interval endpoint is compared with an exact rational.
import functools, json, math, random, sys, time
from fractions import Fraction
import numpy as np
from mpmath import iv
iv.dps = 40
OUT = sys.argv[1]
MARGIN = 1e-12
res = {'spec': 'see REPORT.md section 4'}
t0 = time.time()


@functools.lru_cache(maxsize=None)
def hadamard(n):
    N = 1 << n
    return np.array([[1 - 2 * (bin(S & x).count('1') & 1) for x in range(N)] for S in range(N)], dtype=np.int64)


def all_tables(n):
    N = 1 << n
    t = np.arange(1 << N, dtype=np.int64)[:, None]
    bits = (t >> np.arange(N, dtype=np.int64)[None, :]) & 1
    return 1 - 2 * bits  # row f: f(x) in {+1,-1}, x = bit vector (bit 1 means coordinate value -1)


def h2f(p):
    return 0.0 if p <= 0 or p >= 1 else -(p * math.log2(p) + (1 - p) * math.log2(1 - p))


def packet_float(P, Q):
    s = P + Q
    return 0.0 if s <= 0 else s * h2f(P / s)


def B_float(W2, n, i):  # W2: integer squared Walsh sums; probabilities are W2/N^2
    N = 1 << n
    return sum(packet_float(W2[T] / N / N, W2[T | 1 << i] / N / N) for T in range(N) if not T >> i & 1)


def ivlog2(x):
    return iv.log(x) / iv.log(2)


def packet_iv(P, Q):  # P, Q nonnegative integers on a common scale
    if P == 0 or Q == 0:
        return iv.mpf(0)
    Pi, Qi, Si = iv.mpf(P), iv.mpf(Q), iv.mpf(P + Q)
    return -(Pi * ivlog2(Pi / Si) + Qi * ivlog2(Qi / Si))


def B_iv_scaled(W2, n, i):  # interval for N^2 * B_i
    N = 1 << n
    tot = iv.mpf(0)
    for T in range(N):
        if not T >> i & 1:
            tot += packet_iv(int(W2[T]), int(W2[T | 1 << i]))
    return tot


def I_scaled(W2, n, i):  # exact integer N^2 * Inf_i
    N = 1 << n
    return int(sum(int(W2[S]) for S in range(N) if S >> i & 1))


def proxy_frac(W, n, i):  # exact A_i / I_i, A_i = 2 sum_T |W_T W_{T+i}| (same N^2 scale)
    N = 1 << n
    num = 2 * sum(abs(int(W[T]) * int(W[T | 1 << i])) for T in range(N) if not T >> i & 1)
    den = sum(int(W[T | 1 << i]) ** 2 for T in range(N) if not T >> i & 1)
    return None if den == 0 else Fraction(num, den)


# ---------------- (a) exhaustive n <= 4 ----------------
sec = {}
for n in range(1, 5):
    N = 1 << n
    Hd = hadamard(n)
    F = all_tables(n)
    W = F @ Hd.T
    W2 = W * W
    absW = np.abs(W)
    ua, inv = np.unique(absW, axis=0, return_inverse=True)
    inv = np.asarray(inv).ravel()
    proxy_min_by_u = []
    best_proxy, best_proxy_row = Fraction(0), None
    for r in range(ua.shape[0]):
        vals = [v for v in (proxy_frac(ua[r], n, i) for i in range(n)) if v is not None]
        m = min(vals) if vals else None
        proxy_min_by_u.append(m)
        if m is not None and m > best_proxy:
            best_proxy, best_proxy_row = m, r
    u2, inv2 = np.unique(W2, axis=0, return_inverse=True)
    inv2 = np.asarray(inv2).ravel()
    first_f = {}
    for fi in range(W2.shape[0]):
        first_f.setdefault(int(inv2[fi]), fi)
    rows = []
    for r in range(u2.shape[0]):
        w2 = u2[r]
        if all(int(w2[S]) == 0 for S in range(1, N)):
            continue
        Bs = [B_float(w2, n, i) for i in range(n)]
        Is = [I_scaled(w2, n, i) / N / N for i in range(n)]
        kappa = min(Bs[i] / Is[i] for i in range(n) if Is[i] > 0)
        beta = sum(Bs) / sum(Is)
        P = w2 / N / N
        H = -sum(float(p) * math.log2(float(p)) for p in P if p > 0)
        rows.append((kappa, beta, H / sum(Is), r))

    def cert_kappa(r):
        w2 = u2[r]
        q = [B_iv_scaled(w2, n, i) / iv.mpf(I_scaled(w2, n, i)) for i in range(n) if I_scaled(w2, n, i) > 0]
        return min(float(x.a) for x in q) - MARGIN, min(float(x.b) for x in q) + MARGIN

    def cert_beta(r):
        w2 = u2[r]
        x = sum((B_iv_scaled(w2, n, i) for i in range(n)), iv.mpf(0)) / iv.mpf(sum(I_scaled(w2, n, i) for i in range(n)))
        return float(x.a) - MARGIN, float(x.b) + MARGIN

    rk = max(rows, key=lambda t: t[0])
    lo_k, hi_k = cert_kappa(rk[3])
    n_int_k = 0
    for (kap, beta, hr, r) in rows:
        if r == rk[3]:
            continue
        pm = proxy_min_by_u[int(inv[first_f[r]])]
        if pm is not None and float(pm) <= lo_k - MARGIN:
            continue  # kappa(f) <= proxy(f) <= certified lower bound of the maximiser
        n_int_k += 1
        hi_k = max(hi_k, cert_kappa(r)[1])
    rb = max(rows, key=lambda t: t[1])
    lo_b, hi_b = cert_beta(rb[3])
    n_int_b = 0
    for (kap, beta, hr, r) in rows:
        if r == rb[3]:
            continue
        Wr = W[first_f[r]]
        num = sum(2 * sum(abs(int(Wr[T]) * int(Wr[T | 1 << i])) for T in range(N) if not T >> i & 1) for i in range(n))
        den = sum(I_scaled(u2[r], n, i) for i in range(n))
        if float(Fraction(num, den)) <= lo_b - MARGIN:
            continue
        n_int_b += 1
        hi_b = max(hi_b, cert_beta(r)[1])
    rh = max(rows, key=lambda t: t[2])
    sec[n] = {
        'truth_tables': int(F.shape[0]), 'distinct_abs_walsh_rows': int(ua.shape[0]), 'distinct_sq_walsh_rows': int(u2.shape[0]),
        'proxy_max_min_Ai_over_Ii_exact': str(best_proxy),
        'proxy_maximiser_abs_walsh': (None if best_proxy_row is None else [int(v) for v in ua[best_proxy_row]]),
        'kappa_true_max_float': rk[0], 'kappa_certified_enclosure': [lo_k, hi_k], 'kappa_rows_interval_checked': n_int_k,
        'kappa_maximiser_truth_table': [int(v) for v in F[first_f[rk[3]]]],
        'kappa_maximiser_walsh': [int(v) for v in W[first_f[rk[3]]]],
        'beta_true_max_float': rb[1], 'beta_certified_enclosure': [lo_b, hi_b], 'beta_rows_interval_checked': n_int_b,
        'beta_maximiser_walsh': [int(v) for v in W[first_f[rb[3]]]],
        'H_over_I_max_float': rh[2], 'H_over_I_maximiser_walsh': [int(v) for v in W[first_f[rh[3]]]],
        'kappa_at_H_over_I_maximiser': rh[0], 'beta_at_H_over_I_maximiser': rh[1],
    }
    print('n', n, json.dumps(sec[n]), flush=True)
res['exhaustive_n_le_4'] = sec


# ---------------- (b) A026 symmetric threshold, n = 32 ----------------
def sym_coeffs(n, fvals):
    a = []
    for k in range(n + 1):
        s = 0
        for w in range(n + 1):
            s += fvals[w] * sum((-1) ** j * math.comb(k, j) * math.comb(n - k, w - j)
                                for j in range(0, min(k, w) + 1) if 0 <= w - j <= n - k)
        a.append(Fraction(s, 2 ** n))
    return a


thr = {}
n = 32
for t in (24, 25):
    fv = [1 if (n - w) >= t else -1 for w in range(n + 1)]
    a = sym_coeffs(n, fv)
    assert sum(math.comb(n, k) * a[k] ** 2 for k in range(n + 1)) == 1
    A1 = 2 * sum(math.comb(n - 1, k) * abs(a[k] * a[k + 1]) for k in range(n))
    I1 = sum(math.comb(n - 1, k) * a[k + 1] ** 2 for k in range(n))
    ratio = A1 / I1
    B1 = sum(math.comb(n - 1, k) * packet_float(float(a[k] ** 2), float(a[k + 1] ** 2)) for k in range(n))
    H = -sum(math.comb(n, k) * float(a[k] ** 2) * math.log2(float(a[k] ** 2)) for k in range(n + 1) if a[k] != 0)
    thr['t%d' % t] = {'proxy_ratio_exact': str(ratio), 'proxy_ratio_float': float(ratio),
                      'equals_A026_value_2220940451/536870912': ratio == Fraction(2220940451, 536870912),
                      'true_B_i_over_I_i_float': B1 / float(I1), 'H_over_I_float': H / (n * float(I1))}
res['A026_threshold_n32'] = thr
print('threshold', json.dumps(thr), flush=True)


# ---------------- helpers for small random checks ----------------
def walsh(fv, n):
    return hadamard(n) @ np.array(fv, dtype=np.int64)


def ent(P):
    return -sum(q * math.log2(q) for q in P if q > 1e-300)


def spec(W, N):
    return (W.astype(float) / N) ** 2


def cond_block(W, n, mask):  # H(S_A | S_{A^c}) = H(S) - H(S_{A^c})
    N = 1 << n
    P = spec(W, N)
    marg = {}
    for S in range(N):
        marg[S & ~mask] = marg.get(S & ~mask, 0.0) + P[S]
    return ent(P) - ent(marg.values())


def restrict(fv, n, i, b):
    g = [0] * (1 << (n - 1))
    for x in range(1 << n):
        if (x >> i & 1) == b:
            g[(x & ((1 << i) - 1)) | ((x >> (i + 1)) << i)] = fv[x]
    return g


def inf(fv, n, i):
    return sum(1 for x in range(1 << n) if fv[x] != fv[x ^ (1 << i)]) / (1 << n)


# ---------------- (c) A027 activation identity and stated bounds ----------------
a027 = {'cases': 0, 'max_abs_identity_error': 0.0, 'bound_violations': 0, 'max_ratio_BW_over_p(2dm+2)': 0.0,
        'influence_identity_failures': 0}
for m in (1, 2, 3):
    for r in (1, 2, 3):
        n = m + r
        N = 1 << n
        p = 2.0 ** -r
        for t in range(1 << (1 << m)):
            u = [1 - 2 * ((t >> x) & 1) for x in range(1 << m)]
            Fv = [u[x & ((1 << m) - 1)] if (x >> m) == 0 else 1 for x in range(N)]
            W = walsh(Fv, n)
            BW = cond_block(W, n, (1 << m) - 1)
            mu = sum(u) / len(u)
            d = 1 - mu
            v = 1 - mu * mu
            delta = d / 2
            Pu = spec(walsh(u, m), 1 << m)
            L = ent([q / v for q in Pu[1:]]) if v > 1e-15 else 0.0
            R0 = 1 - 4 * p * delta + 4 * p * p * delta
            last = (R0 / p) * h2f(p * p * v / R0) if R0 > 1e-15 else 0.0
            formula = p * (v * L + 4 * delta * (1 - p) * h2f(delta) + last)
            a027['max_abs_identity_error'] = max(a027['max_abs_identity_error'], abs(formula - BW))
            bound = p * (2 * d * m + 2)
            if bound > 0:
                a027['max_ratio_BW_over_p(2dm+2)'] = max(a027['max_ratio_BW_over_p(2dm+2)'], BW / bound)
            if BW > bound + 1e-12:
                a027['bound_violations'] += 1
            IW = sum(inf(Fv, n, i) for i in range(m))
            Ic = sum(inf(Fv, n, i) for i in range(m, n))
            Iu = sum(inf(u, m, i) for i in range(m))
            if abs(IW - p * Iu) > 1e-12 or abs(Ic - r * p * d) > 1e-12:
                a027['influence_identity_failures'] += 1
            a027['cases'] += 1
res['A027_activation'] = a027
print('A027', json.dumps(a027), flush=True)

# ---------------- (d) R1 and the C006 block identity on random Boolean functions ----------------
rng = random.Random(20261011)
r1 = {'cases': 0, 'min_gap_HA_minus_sum_Bi': 1e9, 'max_abs_block_identity_error': 0.0, 'min_channel_term': 1e9}
for trial in range(300):
    n = rng.choice([4, 5, 6])
    N = 1 << n
    dens = rng.choice([0.5, 0.2, 0.05])
    fv = [(-1 if rng.random() < dens else 1) for _ in range(N)]
    if len(set(fv)) == 1:
        continue
    W = walsh(fv, n)
    Bs = [cond_block(W, n, 1 << i) for i in range(n)]
    k = rng.randint(1, n)
    A = rng.sample(range(n), k)
    mask = sum(1 << i for i in A)
    HA = cond_block(W, n, mask)
    r1['min_gap_HA_minus_sum_Bi'] = min(r1['min_gap_HA_minus_sum_Bi'], HA - sum(Bs[i] for i in A))
    keep = [j for j in range(n) if j not in A]
    Ys = []
    for assign in range(1 << k):
        g = []
        for y in range(1 << len(keep)):
            x = 0
            for idx, j in enumerate(keep):
                if y >> idx & 1:
                    x |= 1 << j
            for idx, j in enumerate(A):
                if assign >> idx & 1:
                    x |= 1 << j
            g.append(fv[x])
        Ys.append(spec(walsh(g, len(keep)), 1 << len(keep)) if keep else np.array([1.0]))
    EH = sum(ent(Y) for Y in Ys) / len(Ys)
    chan = ent(sum(Ys) / len(Ys)) - EH
    r1['max_abs_block_identity_error'] = max(r1['max_abs_block_identity_error'], abs((ent(spec(W, N)) - EH) - (HA + chan)))
    r1['min_channel_term'] = min(r1['min_channel_term'], chan)
    r1['cases'] += 1
res['R1_block_to_singleton'] = r1
print('R1', json.dumps(r1), flush=True)

# ---------------- (e) R2 leaf-partition telescopes on random adaptive trees ----------------
r2 = {'trees': 0, 'max_err_H_telescope': 0.0, 'max_err_I_telescope': 0.0, 'max_err_pivotal_count': 0.0}


def walk(fv, coords, depth_left, w, acc, fixed):
    k = len(coords)
    Wv = walsh(fv, k) if k > 0 else np.array([fv[0]])
    if k == 0 or depth_left == 0 or len(set(fv)) == 1 or rng.random() < 0.15:
        acc['leafH'] += w * ent(spec(Wv, 1 << k))
        acc['leafI'] += w * sum(inf(fv, k, i) for i in range(k))
        acc['leaves'].append((dict(fixed), w))
        return
    i = rng.randrange(k)
    Bi = cond_block(Wv, k, 1 << i)
    g0, g1 = restrict(fv, k, i, 0), restrict(fv, k, i, 1)
    P0 = spec(walsh(g0, k - 1), 1 << (k - 1)) if k > 1 else np.array([1.0])
    P1 = spec(walsh(g1, k - 1), 1 << (k - 1)) if k > 1 else np.array([1.0])
    JS = ent((P0 + P1) / 2) - (ent(P0) + ent(P1)) / 2
    acc['path'] += w * (Bi + JS)
    acc['pathI'] += w * inf(fv, k, i)
    lab, rest = coords[i], coords[:i] + coords[i + 1:]
    for b, g in ((0, g0), (1, g1)):
        fixed[lab] = b
        walk(g, rest, depth_left - 1, w / 2, acc, fixed)
        del fixed[lab]


for trial in range(120):
    n = rng.choice([4, 5, 6])
    N = 1 << n
    dens = rng.choice([0.5, 0.25, 0.1])
    fv = [(-1 if rng.random() < dens else 1) for _ in range(N)]
    if len(set(fv)) == 1:
        continue
    Hf = ent(spec(walsh(fv, n), N))
    If = sum(inf(fv, n, i) for i in range(n))
    acc = {'path': 0.0, 'pathI': 0.0, 'leafH': 0.0, 'leafI': 0.0, 'leaves': []}
    walk(fv, list(range(n)), rng.randint(1, n), 1.0, acc, {})
    r2['max_err_H_telescope'] = max(r2['max_err_H_telescope'], abs(acc['path'] - (Hf - acc['leafH'])))
    r2['max_err_I_telescope'] = max(r2['max_err_I_telescope'], abs(acc['pathI'] - (If - acc['leafI'])))
    piv = 0.0
    for fixed, w in acc['leaves']:
        free = [j for j in range(n) if j not in fixed]
        base = sum(1 << j for j, b in fixed.items() if b)
        for y in range(1 << len(free)):
            x = base
            for idx, j in enumerate(free):
                if y >> idx & 1:
                    x |= 1 << j
            piv += sum(1 for j in fixed if fv[x] != fv[x ^ (1 << j)]) / N
    r2['max_err_pivotal_count'] = max(r2['max_err_pivotal_count'], abs(piv - acc['pathI']))
    r2['trees'] += 1
res['R2_leaf_partition'] = r2
print('R2', json.dumps(r2), flush=True)
res['runtime_seconds'] = time.time() - t0
with open(OUT, 'w', encoding='utf-8') as fh:
    json.dump(res, fh, indent=1)
print('saved', OUT, 'runtime', res['runtime_seconds'])
