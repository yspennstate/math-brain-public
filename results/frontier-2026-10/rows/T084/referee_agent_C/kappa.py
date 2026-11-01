"""D3 on K_n by vertex support.

At lam^i, N = sum over edge-set pairs (A, B) on K_n, each with q^(2n - rank A - rank B). With t the offset of
the q-power from 2n - i, the q^(2n-i+t) coefficient c(n, i, t) of N/(1-q)^2 is a signed count of pair
shapes, and placing a shape whose edges span exactly r + V0 vertices (V0 = 3 adjacent, 4 disjoint, the
vertices of e and f) gives C(n - V0, r) copies. So

    c(n, i, t) = sum_r kappa(i, t, r) C(n - V0, r)    for every n >= V0,

with kappa(i, t, r) depending only on K_(r + V0), recovered exactly by binomial inversion:
    kappa(i, t, r) = sum_{m=0}^{r} (-1)^(r-m) C(r, m) c(m + V0, i, t).
If every kappa >= 0 then D3 holds on every K_n. The tail coefficient (q-powers past the window, equal to a_1)
is handled the same way under t = 'tail'.

python kappa.py adj|dis NMAX     (every kappa with r <= NMAX - V0)"""
import sys, json
from math import comb
import rec

kind, NMAX = sys.argv[1], int(sys.argv[2])
V0 = 3 if kind == 'adj' else 4


def cvals(n):
    """{(i, t): c(n, i, t)} with t an int offset or 'tail'."""
    N = rec.Npoly(n, kind)
    byi = {}
    for k, x in enumerate(N):
        for i, c in enumerate(int(c) for c in x.coeffs()):
            if not c:
                continue
            d = byi.setdefault(i, {})
            for s in range(k + 1):
                d[s] = d.get(s, 0) + c * comb(k, s) * (-1) ** s
    out = {}
    for i, d in byi.items():
        d = {s: v for s, v in d.items() if v}
        if not d:
            continue
        smin, smax = min(d), max(d)
        base = 2 * n - i
        for j in range(smin, smax + 1):
            out[(i, j - base)] = sum(v * (j - s + 1) for s, v in d.items() if s <= j)
        out[(i, 'tail')] = sum(v * (smax + 2 - s) for s, v in d.items())
    return out


C = {}
for n in range(V0, NMAX + 1):
    C[n] = cvals(n)
    print('n', n, 'keys', len(C[n]), flush=True)

TOP = {}
for n in C:
    TOP[n] = {}
    for (i, t) in C[n]:
        if t != 'tail' and t > TOP[n].get(i, -1):
            TOP[n][i] = t


def look(n, key):
    # below the window there are no terms (0); past its top the q^j coefficient of N/(1-q)^2 stays at the
    # tail value a_1, because N vanishes at q = 1
    if key in C[n]:
        return C[n][key]
    i, t = key
    if t == 'tail':
        return 0
    top = TOP[n].get(i)
    if top is not None and t > top:
        return C[n][(i, 'tail')]
    return 0


keys = set()
for n in C:
    keys |= set(C[n])
neg, nz, minpos = [], 0, None
table = {}
for key in keys:
    for r in range(0, NMAX - V0 + 1):
        kap = sum((-1) ** (r - m) * comb(r, m) * look(m + V0, key) for m in range(r + 1))
        if kap:
            nz += 1
            table['%s|%s|%d' % (key[0], key[1], r)] = kap
            if kap < 0:
                neg.append((key, r, kap))
print(kind, 'kappa entries nonzero', nz, 'negative', len(neg))
for x in sorted(neg, key=lambda z: (z[1], z[0][0]))[:20]:
    print('  NEG', x)
# shape check: the largest support seen at each lam power
span = {}
for k in table:
    i, t, r = k.split('|')
    span[int(i)] = max(span.get(int(i), 0), int(r))
print('max r by lam power (first 16):', sorted(span.items())[:16])
json.dump(table, open('kappa_%s_out.json' % kind, 'w'))
