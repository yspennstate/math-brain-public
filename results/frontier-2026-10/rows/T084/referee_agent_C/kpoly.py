"""D3 on K_n at a fixed lam power, for every n.

At lam^i, N(q) = sum_s n_s q^s has its q-powers in a window starting near 2n, and the q^j coefficient of
N/(1-q)^2 is c(j) = sum_{s<=j} n_s (j-s+1). With t = j - (2n - i) the offset into the window, c(n, i, t) is
(on the evidence here) a polynomial in n for n large enough. This script computes c(n, i, t) from rec.py,
fits each (i, t) as a polynomial in n on all but the last HOLD values of n, checks the fit on the held-out
values, and prints its coefficients in the basis C(n - n0, r). All coefficients >= 0 in that basis means
c(n, i, t) >= 0 for every n >= n0 - if the polynomial form holds, which is not proved here.

python kpoly.py adj|dis IMAX NMAX"""
import sys, json
from fractions import Fraction
from math import comb
import rec

kind, IMAX, NMAX = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
HOLD = 0


def q_coeffs(n):
    """{i: {s: n_s}} for N at lam^i, i <= IMAX, as a polynomial in q (u = 1 - q)."""
    N = rec.Npoly(n, kind)
    out = {}
    for k, x in enumerate(N):
        cs = [int(c) for c in x.coeffs()]
        for i, c in enumerate(cs[:IMAX + 1]):
            if not c:
                continue
            d = out.setdefault(i, {})
            for s in range(k + 1):  # (1-q)^k
                d[s] = d.get(s, 0) + c * comb(k, s) * (-1) ** s
    return {i: {s: v for s, v in d.items() if v} for i, d in out.items()}


def series(d, n, i):
    """c(n,i,t) for t in the window, plus the tail value (a_1)."""
    if not d:
        return {}, 0
    smin, smax = min(d), max(d)
    base = 2 * n - i
    res = {}
    for j in range(smin, smax + 1):
        res[j - base] = sum(v * (j - s + 1) for s, v in d.items() if s <= j)
    tail = sum(v * (smax + 1 - s + 1) for s, v in d.items())
    return res, tail


import os
data = {}
RAW = 'kpoly_%s_raw.json' % kind
if os.path.exists(RAW):  # refit from a saved run
    for k, v in json.load(open(RAW)).items():
        i, t = k.split('|')
        data[(int(i), t if t == 'tail' else int(t))] = {int(n): c for n, c in v.items()}
for n in ([] if data else range(3, NMAX + 1)):
    for i, d in q_coeffs(n).items():
        w, tail = series(d, n, i)
        for t, c in w.items():
            data.setdefault((i, t), {})[n] = c
        data.setdefault((i, 'tail'), {})[n] = tail
    print('n', n, 'done', flush=True)


def fit(pts):
    """Newton forward differences on consecutive n: coefficients in C(n - n0, r)."""
    ns = sorted(pts)
    vals = [Fraction(pts[n]) for n in ns]
    coef = []
    while vals and any(vals):
        coef.append(vals[0])
        vals = [b - a for a, b in zip(vals, vals[1:])]
    return ns[0], coef


json.dump({'%s|%s' % k: v for k, v in data.items()}, open(RAW, 'w'))
V0 = 3 if kind == 'adj' else 4
report = []
for (i, t), pts in sorted(data.items(), key=lambda kv: (kv[0][0], str(kv[0][1]))):
    # a shape with i edges spans at most 2i vertices, so the polynomial has degree <= 2i - V0 in the
    # basis C(n - V0, r), exact for every n >= V0; points beyond the first 2i - V0 + 1 are checks
    def val(n):
        # missing below the window -> 0; past the window's top at this n -> the tail value a_1
        if n in pts:
            return pts[n]
        if t == 'tail':
            return 0
        tops = [tt for (ii, tt) in data if ii == i and tt != 'tail' and n in data[(ii, tt)]]
        if tops and t > max(tops):
            return data[(i, 'tail')].get(n, 0)
        return 0
    full = {n: val(n) for n in range(V0, NMAX + 1)}
    D = 2 * i - V0
    use = {n: full[n] for n in range(V0, min(NMAX, V0 + D) + 1)}
    hold = {n: full[n] for n in range(V0 + D + 1, NMAX + 1)}
    n0, coef = fit(use)
    deg = len(coef) - 1
    pred = lambda n: sum(c * comb(n - n0, r) for r, c in enumerate(coef))
    ok_hold = all(pred(n) == v for n, v in hold.items())
    neg = [r for r, c in enumerate(coef) if c < 0]
    small_neg = [n for n in sorted(full) if full[n] < 0]
    report.append(dict(i=i, t=t, n0=n0, deg=deg, checks=len(hold), hold_ok=ok_hold,
                       neg_basis=neg, any_value_negative=small_neg,
                       coef=[str(c) for c in coef]))
    print(i, t, 'n0', n0, 'deg', deg, 'checks', len(hold), 'hold', ok_hold,
          'neg basis coef', neg, 'neg values', small_neg[:5], flush=True)

json.dump(report, open('kpoly_%s_out.json' % kind, 'w'), indent=1)
