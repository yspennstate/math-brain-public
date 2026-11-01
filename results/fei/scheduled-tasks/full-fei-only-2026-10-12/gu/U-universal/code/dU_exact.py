"""Exact local formula for the upward functional (verified numerically against direct restriction):
Delta_i U = sum_T m_T [ s_T log2(r_T/s_T) + (1-s_T) log2(1/(1-s_T)) + KL2(eta_T || x_T) ],
m_T=u^2+v^2, s=v^2/m, r=V(T)/pi(T), eta=2uv/m, x=2C(T)/pi(T), C(T)=sum_{T'>=T} u v, V(T)=sum_{T'>=T} v^2."""
import numpy as np
from feilib import *
from upward import Uprime

def superset_sum(a, k):
    """b[T] = sum_{T' >= T} a[T'] over subsets of k bits."""
    b = a.astype(np.float64).copy(); N = 1 << k; idx = np.arange(N)
    for j in range(k):
        lo = idx[(idx >> j) & 1 == 0]; b[lo] += b[lo | (1 << j)]
    return b

def kl2(e, x):
    a1, a2 = (1 + e) / 2, (1 - e) / 2; b1, b2 = (1 + x) / 2, (1 - x) / 2
    out = np.zeros_like(e)
    with np.errstate(divide='ignore', invalid='ignore'):
        t1 = np.where(a1 > 0, a1 * np.log2(a1 / b1), 0.0); t2 = np.where(a2 > 0, a2 * np.log2(a2 / b2), 0.0)
    return t1 + t2

def local_decomp(t, i):
    t = np.asarray(t, dtype=np.int64); n = nbits(len(t)); W = fwht_int(t).astype(np.float64) / len(t)
    idx = np.arange(1 << n); lo = idx[(idx >> i) & 1 == 0]; hi = lo | (1 << i)
    # re-index T subsets of [n]\i into k=n-1 bits
    u = W[lo]; v = W[hi]
    # map lo indices to compact (n-1)-bit indices by removing bit i
    comp = ((lo >> (i + 1)) << i) | (lo & ((1 << i) - 1))
    U_ = np.zeros(1 << (n - 1)); V_ = np.zeros(1 << (n - 1)); U_[comp] = u; V_[comp] = v
    u, v = U_, V_
    m = u * u + v * v
    pi = superset_sum(m, n - 1); Vs = superset_sum(v * v, n - 1); C = superset_sum(u * v, n - 1)
    mask = m > 0
    s = np.where(mask, v * v / np.where(mask, m, 1), 0); r = np.where(pi > 0, Vs / np.where(pi > 0, pi, 1), 0)
    eta = np.where(mask, 2 * u * v / np.where(mask, m, 1), 0); x = np.where(pi > 0, 2 * C / np.where(pi > 0, pi, 1), 0)
    with np.errstate(divide='ignore', invalid='ignore'):
        t1 = np.where(mask & (s > 0), m * s * np.log2(np.where(s > 0, r / np.where(s>0,s,1), 1)), 0.0)
        t2 = np.where(mask & (s < 1), m * (1 - s) * np.log2(1 / np.where(s < 1, 1 - s, 1)), 0.0)
    t3 = np.where(mask, m * kl2(eta, np.clip(x, -1 + 1e-15, 1 - 1e-15)), 0.0)
    Lam = float((np.where(pi > 0, m / np.where(pi > 0, pi, 1), 0) * Vs).sum())
    return dict(slogrs=float(t1.sum()), tail=float(t2.sum()), KL=float(t3.sum()), total=float(t1.sum() + t2.sum() + t3.sum()), Inf=float((v*v).sum()), Lam=Lam)

if __name__ == "__main__":
    from families import x003, pointdefect, tribes, maj, addressing
    import json
    rng = np.random.default_rng(0)
    # verify against direct restriction on random tables
    for trial in range(6):
        n = int(rng.integers(3, 8)); t = rng.choice([-1, 1], size=1 << n); i = int(rng.integers(n))
        p = spectrum(t); U = float(Uprime(p, n))
        dU = U - 0.5 * (float(Uprime(spectrum(restrict(t, n, i, 0)), n - 1)) + float(Uprime(spectrum(restrict(t, n, i, 1)), n - 1)))
        d = local_decomp(t, i)
        print('check', n, i, round(dU, 10), round(d['total'], 10))
    d = json.load(open("../data/anneal_dU.json"))
    for key in ["5_max", "6_max", "7_max"]:
        t = np.array(d[key]["table"]); n = nbits(len(t)); best = None
        for i in range(n):
            dd = local_decomp(t, i)
            if dd['Inf'] > 1e-12 and (best is None or dd['total'] / dd['Inf'] > best[0]): best = (dd['total'] / dd['Inf'], i, dd)
        b = best[2]
        print(key, 'i', best[1], 'ratio', round(best[0], 3), {k: round(v / b['Inf'], 3) for k, v in b.items() if k != 'Inf'})
    for name, t, i in [('x003_k6r6', x003(6, 6), 0), ('pd8', pointdefect(8), 0), ('tribes3x3', tribes(3, 3), 0)]:
        b = local_decomp(t, i); print(name, {k: round(v / b['Inf'], 3) for k, v in b.items() if k != 'Inf'})
