# Numerical audit of the general-product-measure proof for thresholds (nats):
#  RANK   sum_j Inf_j E_{nu_j} ln+(Lambda/(|T|+1)) / I        <= 5.54
#  GIBBS  the per-level Gibbs bound with theta_k(j) = max(sig_j^2 min(1,k/Lambda), 4 pi_j), evaluated exactly,
#         must be >= LHS and <= 26.3 I
#  CRED   (V ln(1/V) - sum_j Inf_j ln+(4 rho_j/V)) / I          <= 14.7
#  TC     alpha TC(mu_A) / I                                   <= 3.25
import mpmath as mp, random, sys, itertools, math
from isoper3 import biased_P
mp.mp.dps = 40
def elem_sym(vals, k):
    e = [mp.mpf(1)] + [mp.mpf(0)] * k
    for v in vals:
        for j in range(k, 0, -1):
            e[j] += e[j - 1] * v
    return e[k]
def audit(r, t, q):
    f = [1 if bin(x).count('1') >= t else 0 for x in range(1 << r)]
    P = biased_P(f, q); q = [mp.mpf(v) for v in q]
    sig2 = [4 * v * (1 - v) for v in q]; Lam = mp.fsum(sig2)
    V = mp.fsum(P[1:]); I = mp.fsum(bin(A).count('1') * P[A] for A in range(1, 1 << r))
    if V <= 0 or I <= 0: return None
    Inf = [mp.fsum(P[A] for A in range(1 << r) if A >> j & 1) for j in range(r)]
    rho = [Inf[j] / sig2[j] for j in range(r)]
    m = I / V
    lhs = mp.fsum(P[A] * mp.log(mp.fprod(sig2[j] for j in range(r) if A >> j & 1) / P[A]) for A in range(1, 1 << r) if P[A] > 0)
    rank = mp.fsum(P[A] * mp.fsum(max(0, mp.log(Lam / bin(A).count('1'))) for j in range(r) if A >> j & 1) for A in range(1, 1 << r)) / I
    # Gibbs bound per level
    gb = mp.mpf(0)
    for k in range(1, r + 1):
        Wk = mp.fsum(P[A] for A in range(1, 1 << r) if bin(A).count('1') == k)
        if Wk <= 0: continue
        th = [max(sig2[j] * min(1, k / Lam), 4 * Inf[j] / V) for j in range(r)]
        Zk = elem_sym(th, k)
        Ek = mp.fsum(P[A] * mp.fsum(mp.log(sig2[j] / th[j]) for j in range(r) if A >> j & 1) for A in range(1, 1 << r) if bin(A).count('1') == k)
        gb += Wk * mp.log(1 / Wk) + Wk * mp.log(Zk) + Ek
    cred = (V * mp.log(1 / V) - mp.fsum(Inf[j] * max(0, mp.log(4 * rho[j] / V)) for j in range(r))) / I
    # TC on the smaller side
    X = list(range(1 << r))
    w = [mp.fprod(q[j] if x >> j & 1 else 1 - q[j] for j in range(r)) for x in X]
    up = mp.fsum(w[x] for x in X if f[x]); lo = mp.fsum(w[x] for x in X if not f[x])
    side = [x for x in X if (f[x] if up <= lo else not f[x])]; alpha = min(up, lo)
    pa = [w[x] / alpha for x in side]
    H = -mp.fsum(p * mp.log(p) for p in pa if p > 0)
    marg = [mp.fsum(p for x, p in zip(side, pa) if x >> j & 1) for j in range(r)]
    Hm = mp.fsum(-(v * mp.log(v) + (1 - v) * mp.log(1 - v)) for v in marg if 0 < v < 1)
    tc = alpha * (Hm - H) / I
    return {'rank': float(rank), 'gibbs_ok': bool(gb >= lhs - mp.mpf(10) ** -25), 'gibbs': float(gb / I), 'lhs': float(lhs / I), 'cred': float(cred), 'tc': float(tc)}
rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2]); rmax = int(sys.argv[3])
worst = {}; bad = 0
for trial in range(T):
    r = rng.randint(1, rmax); t = rng.randint(1, r)
    q = []
    for _ in range(r):
        u = rng.random()
        q.append(10 ** -rng.uniform(0, 14) if u < 0.35 else (1 - 10 ** -rng.uniform(0, 14) if u < 0.7 else rng.uniform(0.02, 0.98)))
    q = [min(max(v, 1e-15), 1 - 1e-15) for v in q]
    o = audit(r, t, q)
    if o is None: continue
    if not o['gibbs_ok']: bad += 1
    for k in ('rank', 'gibbs', 'lhs', 'cred', 'tc'):
        if k not in worst or o[k] > worst[k][0]: worst[k] = (o[k], r, t, ['%.3g' % x for x in q])
print('gibbs below lhs (must be 0):', bad)
for k, v in worst.items(): print(k, v)
