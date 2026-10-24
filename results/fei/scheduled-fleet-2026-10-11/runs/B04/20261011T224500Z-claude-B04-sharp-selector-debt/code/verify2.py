# B04-lead-verify2: (1) one-bit node boundary lemma  Delta_i <= (3/ln2) Inf_i + 2 I(D_i),  D_i = (f|x_i=0 - f|x_i=1)/2;
# (2) its tree consequence H(f) <= sum_S (|S|^2 + (3/ln2-1)|S|) fhat(S)^2 on ALL Boolean f, n<=4;
# (3) independent exact check of A019's rare-translation identity.  float64 entropies = evidence; Walsh/influences exact.
import numpy as np, json, math, random, os, hashlib, time
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', 'out')
LN2 = math.log(2.0); K3 = 3.0 / LN2; T0 = time.time(); res = {"helper_version": "B04-lead-verify2-v1"}
POP = np.array([bin(i).count('1') for i in range(1 << 12)], dtype=np.int64)

def fwht(a):
    a = np.array(a, dtype=np.int64, copy=True); n = a.shape[-1]; lead = a.shape[:-1]; h = 1
    while h < n:
        a = a.reshape(lead + (n // (2 * h), 2, h)); x = a[..., 0, :].copy(); y = a[..., 1, :].copy()
        a[..., 0, :] = x + y; a[..., 1, :] = x - y; a = a.reshape(lead + (n,)); h *= 2
    return a

def ent(p, axis=-1):
    with np.errstate(divide='ignore', invalid='ignore'):
        t = np.where(p > 0, -p * np.log2(np.where(p > 0, p, 1.0)), 0.0)
    return t.sum(axis=axis)

def all_funcs(n):
    M = 1 << n; k = np.arange(1 << M, dtype=np.int64)
    return (1 - 2 * ((k[:, None] >> np.arange(M)[None, :]) & 1)).astype(np.int64)

# (1)+(2): every Boolean f on n<=4 bits, every coordinate i
out1 = {}
for n in (1, 2, 3, 4):
    fs = all_funcs(n); P, M = fs.shape
    W = fwht(fs); W2 = W * W; p = W2 / float(4 ** n); H = ent(p)
    lev = POP[:M]
    I = (p * lev).sum(1); S2 = (p * lev * lev).sum(1)
    second = S2 + (K3 - 1) * I
    ok2 = bool(np.all(H <= second + 1e-9)); ratio2 = float(np.max(np.where(second > 0, H / np.where(second > 0, second, 1), 0)))
    worst_node = -1.0; ok1 = True; tight = 0
    for i in range(n):
        idx0 = [y for y in range(M) if not (y >> i) & 1]; idx1 = [y | (1 << i) for y in idx0]
        g0 = fs[:, idx0]; g1 = fs[:, idx1]
        m = n - 1
        q0 = (fwht(g0) ** 2) / float(4 ** m); q1 = (fwht(g1) ** 2) / float(4 ** m)
        Hb = 0.5 * (ent(q0) + ent(q1)) if m > 0 else np.zeros(P)
        Delta = H - Hb
        has_i = ((np.arange(M) >> i) & 1) == 1
        Inf = p[:, has_i].sum(1)
        ID = (p[:, has_i] * (lev[has_i] - 1)).sum(1)          # I(D_i) = sum_{S contains i} (|S|-1) fhat(S)^2
        bound = K3 * Inf + 2 * ID
        ok1 = ok1 and bool(np.all(Delta <= bound + 1e-9))
        r = np.where(bound > 1e-12, Delta / np.where(bound > 1e-12, bound, 1), 0)
        worst_node = max(worst_node, float(r.max())); tight += int(np.sum(r > 0.999))
    out1[f"n{n}"] = dict(functions=P, node_lemma_holds_all_i=ok1, max_node_ratio=worst_node, near_tight_nodes=tight,
                         second_moment_bound_holds=ok2, max_H_over_second_moment_bound=ratio2)
    print('n', n, json.dumps(out1[f"n{n}"]))
res['node_boundary_lemma_and_second_moment'] = out1

# bent splice: node lemma asymptotics (exact closed form)
bs = {}
for m in (4, 8, 12, 16, 20):
    d = 2.0 ** -m; ID = d * m / 2.0     # D = +-point: I(D) = m*delta/2
    u = 2.0 ** (-m / 2)
    A = sum(-2 * ((1 + e * u) / 2) * (1 - e * u) ** 2 * math.log2(1 - e * u) for e in (1, -1))
    B = sum(((1 + e * u) / 2) * (1 - 2 * e * u) ** 2 * math.log2(abs(1 - 2 * e * u)) for e in (1, -1))
    Delta = m * u * u + A + B
    bs[m] = dict(Delta_over_bound=Delta / (K3 * d + 2 * ID))
res['bent_splice_node_lemma_ratio'] = bs; print('bent', bs)

# (3) A019 identity, independent implementation
def Ek(k):
    dl = 2.0 ** -k; t = (1 - 2 * dl) ** 2
    return (-t * math.log2(t) if t > 0 else 0.0) + 4 * dl * (1 - dl) * (2 * k - 2)
rnd = random.Random(1011); fails = 0; cases = 0; maxerr = 0.0; exact_inf = True
for trial in range(400):
    n = rnd.randint(1, 3); r = rnd.randint(1, 2); ks = [rnd.randint(1, 3) for _ in range(r)]
    if n + sum(ks) > 10: continue
    g = np.array([rnd.choice((-1, 1)) for _ in range(1 << n)], dtype=np.int64)
    vs = [rnd.randrange(1 << n) for _ in range(r)]; zs = [rnd.randrange(1 << k) for k in ks]
    a = sum(ks); ntot = n + a; size = 1 << ntot; idx = np.arange(size)
    y = idx & ((1 << n) - 1); w = idx >> n
    shift = np.zeros(size, dtype=np.int64); off = 0
    for j in range(r):
        wj = (w >> off) & ((1 << ks[j]) - 1); shift ^= np.where(wj == zs[j], vs[j], 0); off += ks[j]
    F = g[y ^ shift]
    WF = fwht(F[None, :])[0]; pF = WF * WF; HF = float(ent(pF / float(4 ** ntot)))
    Wg = fwht(g[None, :])[0]; pg = Wg * Wg; Hg = float(ent(pg / float(4 ** n)))
    rho = [Fraction(int(np.sum(g != g[np.arange(1 << n) ^ v])), 1 << n) for v in vs]
    pred = Hg + sum(float(rho[j]) * Ek(ks[j]) for j in range(r))
    # exact influences
    selmask = (idx >> n) > -1
    IW = Fraction(int(sum(int((pF * ((idx >> (n + b)) & 1)).sum()) for b in range(a))), 4 ** ntot)
    Idat = Fraction(int(sum(int((pF * ((idx >> b) & 1)).sum()) for b in range(n))), 4 ** ntot)
    Ig = Fraction(int((pg * POP[:1 << n]).sum()), 4 ** n)
    IWpred = sum(rho[j] * Fraction(2 * ks[j], 2 ** ks[j]) for j in range(r))
    cases += 1; err = abs(HF - pred); maxerr = max(maxerr, err)
    ok = err < 1e-9 and IW == IWpred and Idat == Ig and (HF - Hg) <= 4 * float(IW) + 1e-9
    if not ok: fails += 1
res['A019_independent'] = dict(cases=cases, failures=fails, max_abs_entropy_error=maxerr,
                               note="H(F)=H(g)+sum rho_j E_kj; I_W=sum rho_j 2k_j 2^-k_j exact; I_data=I(g) exact; B_W<=4 I_W")
print('A019', res['A019_independent'])
res['runtime_seconds'] = round(time.time() - T0, 2)
txt = json.dumps(res, indent=1, default=str); open(os.path.join(OUT, 'verify2_results.json'), 'w', encoding='utf8').write(txt)
print('sha256', hashlib.sha256(txt.encode()).hexdigest(), 'runtime', res['runtime_seconds'])
