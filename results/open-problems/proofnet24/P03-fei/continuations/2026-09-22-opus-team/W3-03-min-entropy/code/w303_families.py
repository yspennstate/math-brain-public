"""Hinf / I on the hard families named in the brief.

Closed forms (checked by brute force on small members):
  tribes(w,s): OR of s disjoint ANDs of width w.  q = (1-2^-w)^s = Pr[false].
      fhat(empty) = 2q-1;  |fhat(S)| = 2^(1-w) q/(1-2^-w) * (2^-w/(1-2^-w))^(t-1)... for S meeting t tribes
      (max over nonempty S: t = 1, value 2^(1-w) q/(1-2^-w));  I = w s 2^(1-w) q/(1-2^-w).
  addressing / Maiorana-McFarland with s address bits, 2^s - 1 data bits and one constant leaf:
      every nonzero |fhat| = 2^-s,  I = s/2 + 1 - 2^-s.
  recursive majority of 3, depth d: Hinf = 2d, I = 1.5^d.
"""
import sys, json
from fractions import Fraction
import numpy as np
import mpmath as mp
import psutil
_p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 10, 11, 12, 13, 14, 15])
sys.path.insert(0, __file__.rsplit("/", 1)[0].rsplit("\\", 1)[0])
from fmei_lib import stats

mp.mp.dps = 40
out = {}


def tt_from_func(n, fn):
    xs = np.arange(1 << n)
    bits = ((xs[:, None] >> np.arange(n)) & 1).astype(bool)   # bit=1 means coordinate "true"
    val = fn(bits)                                            # boolean array, True means f true
    return np.where(val, -1.0, 1.0)


def brute(n, fn):
    s = stats(tt_from_func(n, fn)[None, :])
    return float(s["Hinf"][0]), float(s["I"][0]), float(s["H2"][0])


# ---------- tribes ----------
def tribes_exact(w, s):
    """Exact rationals for w <= 10; 60-digit mpmath beyond (values returned as mpf)."""
    if w <= 10:
        a = Fraction(1, 2 ** w)
        q = (1 - a) ** s
        e0 = (2 * q - 1) ** 2
        m1 = (2 * a * q / (1 - a)) ** 2
        I = w * s * 2 * a * q / (1 - a)
        mx = max(e0, m1)
        Hinf = -mp.log(mp.mpf(mx.numerator) / mx.denominator, 2)
        return Hinf, mp.mpf(I.numerator) / I.denominator, e0, m1
    with mp.workdps(60):
        a = mp.mpf(2) ** (-w)
        q = mp.exp(s * mp.log1p(-a))
        e0 = (2 * q - 1) ** 2
        m1 = (2 * a * q / (1 - a)) ** 2
        I = w * s * 2 * a * q / (1 - a)
        Hinf = -mp.log(max(e0, m1), 2)
        return Hinf, I, e0, m1


def tribes_fn(w, s):
    def fn(bits):
        v = np.zeros(bits.shape[0], dtype=bool)
        for j in range(s):
            v |= bits[:, j * w:(j + 1) * w].all(axis=1)
        return v
    return fn


chk = []
for (w, s) in [(2, 2), (2, 3), (3, 2), (3, 3), (2, 4), (4, 3)]:
    Hb, Ib, _ = brute(w * s, tribes_fn(w, s))
    He, Ie, _, _ = tribes_exact(w, s)
    chk.append([w, s, Hb, float(He), Ib, float(Ie)])
    assert abs(Hb - float(He)) < 1e-9 and abs(Ib - float(Ie)) < 1e-9
out["tribes_bruteforce_check"] = chk

tr = []
for w in range(2, 41):
    best = None
    s0 = int(mp.floor(mp.log(2) / -mp.log(1 - mp.mpf(2) ** -w)))
    for s in range(max(1, s0 - 3), s0 + 5):
        H, I, e0, m1 = tribes_exact(w, s)
        r = H / I
        if best is None or r > best[0]:
            best = (r, s, H, I, e0 >= m1)
    tr.append([w, best[1], float(best[0]), float(best[2]), float(best[3]), bool(best[4])])
out["tribes_best_s_per_w"] = tr
out["two_over_ln2"] = float(2 / mp.log(2))

# ---------- addressing / Maiorana-McFarland ----------
def addr_fn(sa, const_leaf=True):
    # address bits 0..sa-1, data bits sa.. ; leaf y reads data bit (y-1) if const_leaf and y>0, leaf 0 is constant false
    nd = (1 << sa) - (1 if const_leaf else 0)
    def fn(bits):
        y = np.zeros(bits.shape[0], dtype=np.int64)
        for j in range(sa):
            y |= bits[:, j].astype(np.int64) << j
        v = np.zeros(bits.shape[0], dtype=bool)
        for leaf in range(1 << sa):
            sel = (y == leaf)
            if const_leaf:
                if leaf == 0:
                    continue
                v[sel] = bits[sel, sa + leaf - 1]
            else:
                v[sel] = bits[sel, sa + leaf]
        return v
    return sa + nd, fn


ad = []
for sa in (1, 2, 3, 4):
    for cl in (False, True):
        n, fn = addr_fn(sa, cl)
        if n > 20:
            continue
        Hb, Ib, H2b = brute(n, fn)
        Ie = sa / 2 + 1 - (2.0 ** -sa if cl else 0.0)
        ad.append([sa, cl, n, Hb, Ib, Ie, Hb / Ib, H2b])
        assert abs(Ib - Ie) < 1e-9 and abs(Hb - 2 * sa) < 1e-9
out["addressing_bruteforce"] = ad
out["addressing_ratio_formula"] = [[sa, 2 * sa / (sa / 2 + 1 - 2.0 ** -sa)] for sa in (5, 10, 20, 50, 100)]

# ---------- recursive majority ----------
maj3 = lambda b: (b.sum(axis=1) >= 2)
def recmaj_fn(d):
    def fn(bits):
        cur = bits
        for _ in range(d):
            cur = np.stack([maj3(cur[:, 3 * k:3 * k + 3]) for k in range(cur.shape[1] // 3)], axis=1)
        return cur[:, 0]
    return fn
rm = []
for d in (1, 2):
    Hb, Ib, _ = brute(3 ** d, recmaj_fn(d))
    rm.append([d, Hb, Ib, 2 * d, 1.5 ** d])
out["recmaj3"] = rm
out["recmaj3_formula"] = [[d, 2 * d / 1.5 ** d] for d in (3, 5, 10)]

# ---------- majority and majority + flip ----------
mj = []
for n in (5, 9, 13, 17):
    Hb, Ib, _ = brute(n, lambda b: b.sum(axis=1) > b.shape[1] / 2)
    mj.append([n, Hb, Ib, Hb / Ib])
out["majority"] = mj
mf = []
for n in (5, 9, 13, 17):
    ystar = np.array([1] * ((n - 1) // 2) + [0] * ((n + 1) // 2), dtype=bool)
    def fn(b, n=n, ystar=ystar):
        y = b[:, :n]; z = b[:, n]
        return (y.sum(axis=1) > n / 2) | (z & (y == ystar).all(axis=1))
    Hb, Ib, _ = brute(n + 1, fn)
    mf.append([n + 1, Hb, Ib, Hb / Ib])
out["majority_plus_flip"] = mf

# ---------- bent (inner product) and bent + flip ----------
bf = []
for m in (4, 6, 8, 10, 12):
    def ip(b, m=m):
        return (np.sum(b[:, 0:m:2] & b[:, 1:m:2], axis=1) % 2).astype(bool)
    Hb, Ib, _ = brute(m, ip)
    ystar = np.zeros(m, dtype=bool)
    def fn(b, m=m):
        base = ip(b[:, :m])
        flip = b[:, m] & (b[:, :m] == ystar).all(axis=1)
        return base ^ flip
    Hf, If, _ = brute(m + 1, fn)
    bf.append([m, Hb, Ib, Hb / Ib, Hf, If, Hf / If])
out["bent_and_bent_plus_flip"] = bf

# ---------- Numaro's g and its tower ----------
import os
g = np.load(os.path.abspath(__file__).replace("\\", "/").rsplit("W3-03", 1)[0] + "inputs/numaro18_pm1_table.npy").astype(np.float64)
s = stats(g[None, :])
c = s["coeffs"][0]
n = 18
pc = np.array([bin(k).count("1") for k in range(1 << n)])
out["numaro_g"] = dict(Hinf=float(s["Hinf"][0]), I=float(s["I"][0]), H=float(s["H"][0]), H2=float(s["H2"][0]),
                       argmax_set_size=int(pc[int(np.argmax(c * c))]), max_abs=float(np.abs(c).max()))
# tower: m_k = min_T [ log2(1/ghat(T)^2) + |T| m_{k-1} ] over nonempty T (g balanced), I_k = I(g)^k
p = c * c
nz = p > 1e-30
aT = -np.log2(p[nz]); sz = pc[nz]
m = 0.0
tower = []
for k in range(1, 9):
    m = float(np.min(aT + sz * m))
    Ik = float(s["I"][0]) ** k
    tower.append([k, m, Ik, m / Ik])
out["numaro_tower"] = tower

print(json.dumps(out, indent=1))
