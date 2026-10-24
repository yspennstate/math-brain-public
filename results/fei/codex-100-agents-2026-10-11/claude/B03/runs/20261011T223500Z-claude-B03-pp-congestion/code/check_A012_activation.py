"""Independent re-check of A012's general activation ledger (lead review, B03).
F = 1 + A_r (g - 1) on r control bits + m core bits; A_r = 1[all controls true], p = 2^-r, mu = E g, a = 1-mu, v = 1-mu^2.
Claimed: I(F) = p I(g) + r p a ;  H(F) = L((1-pa)^2) + (p-p^2) a^2 log2(1/(p^2 a^2)) + p[H(g) - L(mu^2)] + 2 r p v,
with L(t) = t log2(1/t), L(0)=0.  Domain: m = 3, all 256 g, r = 1,2,3 (768 activations). Exact integer WHT;
influences as Fractions (exact); entropies as exact finite sums evaluated with mpmath at 50 digits, compared at 1e-40.
"""
import itertools
from fractions import Fraction
import numpy as np
import mpmath as mp

mp.mp.dps = 50


def wht(a):
    a = a.astype(np.int64).copy()
    n = a.shape[0]
    h = 1
    while h < n:
        a = a.reshape(-1, 2, h)
        x = a[:, 0, :].copy(); y = a[:, 1, :].copy()
        a[:, 0, :] = x + y; a[:, 1, :] = x - y
        a = a.reshape(n); h *= 2
    return a


def spec(f, nvar):
    W = wht(f)
    N = 1 << nvar
    pc = np.array([bin(s).count('1') for s in range(N)], dtype=np.int64)
    I = Fraction(int(np.sum(W * W * pc)), N * N)
    H = mp.mpf(0)
    for w in W.tolist():
        if w:
            p = mp.mpf(w) ** 2 / mp.mpf(N) ** 2
            H += p * mp.log(1 / p, 2)
    mu = Fraction(int(W[0]), N)
    return I, H, mu


def M(x):
    return mp.mpf(x.numerator) / x.denominator if isinstance(x, Fraction) else mp.mpf(x)


def L(t):
    t = M(t)
    return mp.mpf(0) if t == 0 else t * mp.log(1 / t, 2)


m = 3
checks = 0
worst = mp.mpf(0)
for bits in range(1 << (1 << m)):
    g = np.array([1 if (bits >> x) & 1 else -1 for x in range(1 << m)], dtype=np.int64)
    Ig, Hg, mu = spec(g, m)
    for r in (1, 2, 3):
        nv = r + m
        N = 1 << nv
        # low r bits = controls, high m bits = core
        F = np.empty(N, dtype=np.int64)
        for x in range(N):
            ctrl = x & ((1 << r) - 1)
            core = x >> r
            F[x] = g[core] if ctrl == (1 << r) - 1 else 1
        IF, HF, _ = spec(F, nv)
        p = Fraction(1, 1 << r)
        a = 1 - mu
        v = 1 - mu * mu
        assert IF == p * Ig + r * p * a, (bits, r)
        pa2 = (p * a) ** 2
        Hc = L((1 - p * a) ** 2) + (M((p - p * p) * a * a) * mp.log(1 / M(pa2), 2) if a != 0 else 0) \
            + M(p) * (Hg - L(mu * mu)) + 2 * r * M(p) * M(v)
        d = abs(HF - Hc)
        worst = max(worst, d)
        assert d < mp.mpf(10) ** -40, (bits, r, HF, Hc)
        checks += 2
print(f"A012 activation ledger: {checks} exact/high-precision assertions passed over 768 activations; worst |H-formula| = {mp.nstr(worst, 5)}")
