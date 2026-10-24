"""Biased FEI+ for SYMMETRIC gates under i.i.d. product measures (every input 1 with probability p).
For G: {0..r} -> {+-1} (value by Hamming weight) the mu-biased coefficient on a set S of size s is
sigma^s a_s with a_s = 2^{-s} E_{c ~ Bin(r-s, p)} [ sum_j C(s,j) (-1)^{s-j} G(c+j) ], so P(S) = sigma^{2s} a_s^2,
W_s = C(r,s) P(S), and the biased FEI+ ratio is  sum_{s>=1} W_s log2(1/a_s^2) / sum_{s>=1} (s-1) W_s.
Exact in 80-digit arithmetic (the alternating sums lose everything in floats). Question: is the ratio bounded
uniformly in r, the profile and p (conjecturally by 2 + 4 log2 e = 7.7708)?"""
import itertools, math, numpy as np
import mpmath as mp
mp.mp.dps = 80
BOUND = 2 + 4 / mp.log(2)

def ratio(G, p):
    r = len(G) - 1; p = mp.mpf(p); q = 1 - p; sig2 = 4 * p * q
    tot = mp.mpf(0); lhs = mp.mpf(0); rhs = mp.mpf(0)
    for s in range(0, r + 1):
        m = r - s
        pc = [mp.binomial(m, c) * p ** c * q ** (m - c) for c in range(m + 1)]
        acc = mp.mpf(0)
        for c in range(m + 1):
            d = mp.fsum([mp.binomial(s, j) * (-1) ** (s - j) * G[c + j] for j in range(s + 1)])
            acc += pc[c] * d
        a = acc / mp.mpf(2) ** s
        W = mp.binomial(r, s) * sig2 ** s * a * a
        tot += W
        if s >= 1 and a != 0:
            lhs += W * mp.log(1 / (a * a), 2)
            rhs += (s - 1) * W
    assert abs(tot - 1) < mp.mpf('1e-40'), tot
    return (lhs / rhs if rhs > mp.mpf('1e-60') else mp.mpf(0)), lhs, rhs

ps = [mp.mpf(10) ** (-e) for e in (1, 2, 3, 4, 6, 8)] + [mp.mpf('0.3'), mp.mpf('0.5'), mp.mpf('0.7')] + \
     [1 - mp.mpf(10) ** (-e) for e in (1, 2, 3, 4, 6, 8)]
best = (0, None)
# thresholds of every fan-in up to 30 and every threshold
for r in list(range(2, 13)) + [16, 20, 25, 30]:
    for t in range(1, r + 1):
        G = [1 - 2 * (1 if w >= t else 0) for w in range(r + 1)]
        for p in ps:
            R, _, _ = ratio(G, p)
            if R > best[0]: best = (R, ('thr', r, t, mp.nstr(p, 3)))
print('thresholds r <= 30: max ratio', mp.nstr(best[0], 8), best[1], flush=True)
# every symmetric function (every +-1 weight profile) up to r = 8
best2 = (0, None)
for r in range(2, 9):
    for prof in itertools.product([1, -1], repeat=r + 1):
        if len(set(prof)) == 1: continue
        for p in ps:
            R, _, _ = ratio(list(prof), p)
            if R > best2[0]: best2 = (R, ('sym', r, prof, mp.nstr(p, 3)))
print('all symmetric functions r <= 8: max ratio', mp.nstr(best2[0], 8), best2[1], flush=True)
print('2 + 4 log2 e =', mp.nstr(BOUND, 8))
