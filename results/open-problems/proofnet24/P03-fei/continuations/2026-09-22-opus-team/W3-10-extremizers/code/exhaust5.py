"""Exhaustive atlas of all Boolean functions on at most 5 variables (up to NPN equivalence).

Every f on 5 variables is NPN-equivalent to one whose x4=+1 half g is one of the 222 NPN representatives of
4-variable functions (apply to both halves the transformation that canonicalises g).  So f = (g_rep, h) over
the 222 x 65536 pairs covers every NPN class (with multiplicity).  All quantities are NPN invariant.

For every function: H, I, mean, rho_0 = min_i Delta_i/Inf_i, min_i B_i/Inf_i, number k of relevant variables,
composition-primality (no block A, 2<=|A|<=k-1, with at most two distinct cofactors).
Output: per (k, prime?) bucket the maxima of H/I, J = H/(I-1) (balanced), rho_0, min B/Inf, with argmax tables;
the top functions per objective (deduplicated up to NPN) with their decomposition trees.
"""
import sys, time, json, itertools
import numpy as np
import numba as nb
sys.path.insert(0, '.')
from core import polite, phi, popc, stats, decompose, is_prime

polite()

LOG = open('../logs/exhaust5.log', 'w')


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    LOG.write(s + '\n')
    LOG.flush()


# 4-variable Walsh spectra of all 65536 functions (bit=1 of the code -> true -> value -1)
codes = np.arange(1 << 16, dtype=np.int64)
T4 = 1 - 2 * ((codes[:, None] >> np.arange(16)[None, :]) & 1)  # (65536,16) +-1
Hd = np.array([[(-1) ** bin(x & S).count('1') for x in range(16)] for S in range(16)], dtype=np.int64)
W4 = (T4 @ Hd.T).astype(np.int64)  # W4[f, S]
reps = np.load('../logs/npn_reps_n4.npy')
log('4-var NPN reps:', len(reps))


@nb.njit(cache=True)
def eval_chunk(Wg, W4, gcode, out_H, out_I, out_mu, out_rho, out_minB, out_k, out_prime):
    N = 32
    W = np.empty(N, np.int64)
    tt = np.empty(N, np.int64)
    for hc in range(65536):
        Wh = W4[hc]
        for S in range(16):
            W[S] = Wg[S] + Wh[S]
            W[S + 16] = Wg[S] - Wh[S]
        inv = 1.0 / N
        H = 0.0
        I = 0.0
        for S in range(N):
            p = (W[S] * inv) ** 2
            H += phi(p)
            I += popc(S) * p
        rho = 1e300
        mB = 1e300
        k = 0
        relmask = 0
        for i in range(5):
            bit = 1 << i
            Hp = 0.0
            Hm = 0.0
            Bs = 0.0
            inf = 0.0
            for T in range(N):
                if T & bit:
                    continue
                u = W[T] * inv
                v = W[T | bit] * inv
                a = u * u
                b = v * v
                inf += b
                Bs += phi(a) + phi(b) - phi(a + b)
                Hp += phi((u + v) ** 2)
                Hm += phi((u - v) ** 2)
            if inf > 1e-12:
                k += 1
                relmask |= bit
                d = H - 0.5 * (Hp + Hm)
                r = d / inf
                if r < rho:
                    rho = r
                rb = Bs / inf
                if rb < mB:
                    mB = rb
        out_H[hc] = H
        out_I[hc] = I
        out_mu[hc] = W[0] * inv
        out_rho[hc] = rho if k > 0 else np.nan
        out_minB[hc] = mB if k > 0 else np.nan
        out_k[hc] = k
        # truth table: x<16 -> g, x>=16 -> h ; value 1 if true
        for x in range(16):
            tt[x] = (gcode >> x) & 1
            tt[x + 16] = (hc >> x) & 1
        # primality over relevant variables
        prime = 1
        if k < 3:
            prime = 0
        else:
            rel = np.empty(k, np.int64)
            c = 0
            for i in range(5):
                if (relmask >> i) & 1:
                    rel[c] = i
                    c += 1
            for m in range(1, 1 << k):
                sz = popc(m)
                if sz < 2 or sz > k - 1:
                    continue
                # A = rel[j] for bits j of m ; B = other relevant
                nA = sz
                nB = k - sz
                Aidx = np.empty(nA, np.int64)
                Bidx = np.empty(nB, np.int64)
                ca = 0
                cb = 0
                for j in range(k):
                    if (m >> j) & 1:
                        Aidx[ca] = rel[j]
                        ca += 1
                    else:
                        Bidx[cb] = rel[j]
                        cb += 1
                c1 = -1
                c2 = -1
                ok = True
                for a in range(1 << nA):
                    xa = 0
                    for j in range(nA):
                        if (a >> j) & 1:
                            xa |= 1 << Aidx[j]
                    code = 0
                    for b in range(1 << nB):
                        xb = 0
                        for j in range(nB):
                            if (b >> j) & 1:
                                xb |= 1 << Bidx[j]
                        code |= tt[xa | xb] << b
                    if c1 == -1 or code == c1:
                        c1 = code
                    elif c2 == -1 or code == c2:
                        c2 = code
                    else:
                        ok = False
                        break
                if ok:
                    prime = 0
                    break
        out_prime[hc] = prime


def table5(gcode, hc):
    t = np.empty(32, dtype=np.int8)
    for x in range(16):
        t[x] = -1 if (gcode >> x) & 1 else 1
        t[x + 16] = -1 if (hc >> x) & 1 else 1
    return t


# NPN canonical form for 5-variable tables (for dedup of the reported maximisers)
def npn5_maps():
    n = 5
    N = 32
    x = np.arange(N)
    maps = []
    for perm in itertools.permutations(range(n)):
        for neg in range(N):
            y = np.zeros(N, dtype=np.int64)
            for i in range(n):
                y |= (((x >> i) & 1) ^ ((neg >> i) & 1)) << perm[i]
            maps.append(y)
    return np.array(maps)


MAPS5 = npn5_maps()
PW = (1 << np.arange(32)).astype(np.int64)


def canon5(t):
    b = (t == -1).astype(np.int64)
    g = np.empty((MAPS5.shape[0], 32), dtype=np.int64)
    g[np.arange(MAPS5.shape[0])[:, None], MAPS5] = b[None, :]
    c1 = (g * PW).sum(axis=1)
    c2 = ((1 - g) * PW).sum(axis=1)
    return int(min(c1.min(), c2.min()))


OBJ = ['ratio', 'J', 'rho0', 'minB']
best = {}  # (obj, k, prime) -> (value, gcode, hc)
top = {o: [] for o in OBJ}  # (value, gcode, hc)
KEEP = 400
counts = {}
t0 = time.time()
oH = np.empty(65536); oI = np.empty(65536); omu = np.empty(65536); orho = np.empty(65536)
omB = np.empty(65536); ok_ = np.empty(65536, np.int64); opr = np.empty(65536, np.int64)
for ri, gcode in enumerate(reps):
    gcode = int(gcode)
    eval_chunk(W4[gcode], W4, gcode, oH, oI, omu, orho, omB, ok_, opr)
    nonconst = ok_ > 0
    ratio = np.where(nonconst & (oI > 0), oH / np.where(oI > 0, oI, 1), np.nan)
    bal = (np.abs(omu) < 1e-12) & (oI > 1 + 1e-9)
    J = np.where(bal, oH / np.where(bal, oI - 1, 1), np.nan)
    vals = {'ratio': ratio, 'J': J, 'rho0': np.where(nonconst, orho, np.nan), 'minB': np.where(nonconst, omB, np.nan)}
    for k in range(1, 6):
        for pr in (0, 1):
            sel = (ok_ == k) & (opr == pr)
            counts[(k, pr)] = counts.get((k, pr), 0) + int(sel.sum())
            if not sel.any():
                continue
            for o in OBJ:
                v = np.where(sel, vals[o], np.nan)
                if np.all(np.isnan(v)):
                    continue
                j = int(np.nanargmax(v))
                key = (o, k, pr)
                if key not in best or v[j] > best[key][0] + 1e-13:
                    best[key] = (float(v[j]), gcode, j)
    for o in OBJ:
        v = vals[o]
        v = np.where(np.isnan(v), -np.inf, v)
        idx = np.argpartition(-v, 60)[:60]
        for j in idx:
            if np.isfinite(v[j]):
                top[o].append((float(v[j]), gcode, int(j)))
        top[o].sort(key=lambda z: -z[0])
        top[o] = top[o][:KEEP]
    if ri % 20 == 0:
        log('rep %d/%d  %.1fs' % (ri, len(reps), time.time() - t0))

log('\ncounts (k relevant vars, prime flag) -> number of (rep,h) pairs:')
for k in range(1, 6):
    log(' k=%d composite=%d prime=%d' % (k, counts.get((k, 0), 0), counts.get((k, 1), 0)))

log('\nMaxima per bucket (value, decomposition of an argmax):')
res = {}
for o in OBJ:
    log('--- objective', o)
    for k in range(1, 6):
        for pr in (0, 1):
            key = (o, k, pr)
            if key in best:
                v, gc, hc = best[key]
                t = table5(gc, hc)
                s = stats(t)
                log('  k=%d %s  max=%.9f  %s   [H=%.6f I=%.6f mean=%.4f rho0=%.5f]' % (
                    k, 'prime' if pr else 'compo', v, decompose(t), s['H'], s['I'], s['mean'], s['rho0']))
                res['%s_k%d_%s' % (o, k, 'prime' if pr else 'comp')] = dict(value=v, table=''.join('1' if z == -1 else '0' for z in t),
                                                                              tree=decompose(t))

log('\nTop functions per objective (deduplicated up to NPN):')
for o in OBJ:
    log('--- objective', o)
    seen = set()
    c = 0
    for v, gc, hc in top[o]:
        t = table5(gc, hc)
        cf = canon5(t)
        if cf in seen:
            continue
        seen.add(cf)
        s = stats(t)
        log('  %.9f  k=%d prime=%s  %s  [H=%.6f I=%.6f mean=%.4f rho0=%.5f minB=%.5f]' % (
            v, s['nrel'], is_prime(t), decompose(t), s['H'], s['I'], s['mean'], s['rho0'], s['minB']))
        c += 1
        if c >= 25:
            break
json.dump(res, open('../logs/exhaust5_best.json', 'w'), indent=1)
log('done %.1fs' % (time.time() - t0))
