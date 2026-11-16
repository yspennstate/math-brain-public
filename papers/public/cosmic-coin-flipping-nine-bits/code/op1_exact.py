"""Mossel-O'Donnell (2005) Open Problem 1 for small n, exactly.

Antisymmetric left-monotone f on {0,1}^n (x <=_L y iff every prefix sum of x is at most that of y).
P_k(f; e) = 2^{1-n} sum_x p(x)^k, p(x) = sum_y f(y) e^{d(x,y)} (1-e)^{n-d(x,y)}.
For each f and 4 <= k <= K we certify D = P_k(x_1) - P_k(f) >= 0 on (0, 1/2), with equality only at the ends.
Certificate: write D(e) = e^a (1-2e)^b g(e); substitute e = t/(2(1+t)), t in (0, inf); multiply by (1+t)^deg.
If all coefficients of the result are >= 0 (and not all 0) then g > 0 on (0,1/2). Otherwise count roots exactly
(Sturm, sympy) and check the sign at e = 1/4.
Usage: python op1_exact.py n K [outfile]
"""
import sys, time, json
from fractions import Fraction
import sympy as sp

n = int(sys.argv[1]); K = int(sys.argv[2]); out = sys.argv[3] if len(sys.argv) > 3 else None
N = 1 << n
bits = [[(x >> (n - 1 - i)) & 1 for i in range(n)] for x in range(N)]   # bit 0 is the leftmost coordinate
pref = [[sum(b[:m + 1]) for m in range(n)] for b in bits]
leq = lambda x, y: all(a <= c for a, c in zip(pref[x], pref[y]))
up = [0] * N; down = [0] * N
for x in range(N):
    for y in range(N):
        if leq(x, y):
            up[x] |= 1 << y; down[y] |= 1 << x
comp = lambda x: (N - 1) ^ x
FULL = (1 << N) - 1

funcs = []
def rec(IN, OUT):
    if IN & OUT:
        return
    und = FULL & ~(IN | OUT)
    if not und:
        funcs.append(IN); return
    x = (und & -und).bit_length() - 1
    rec(IN | up[x], OUT | down[comp(x)])
    rec(IN | up[comp(x)], OUT | down[x])
t0 = time.time()
rec(0, 0)
print(f"n={n}: {len(funcs)} antisymmetric left-monotone functions ({time.time()-t0:.1f}s)", flush=True)

e = sp.symbols('e'); t = sp.symbols('t')
dist = [[bin(x ^ y).count('1') for y in range(N)] for x in range(N)]
ZZe = sp.Poly(e, e, domain='ZZ')
powe = [sp.Poly(e ** d * (1 - e) ** (n - d), e, domain='ZZ') for d in range(n + 1)]

def pvec(F):
    ones = [y for y in range(N) if F >> y & 1]
    res = []
    for x in range(N):
        cnt = [0] * (n + 1)
        for y in ones:
            cnt[dist[x][y]] += 1
        res.append(sum((powe[d] * c for d, c in enumerate(cnt) if c), sp.Poly(0, e, domain='ZZ')))
    return res

dict1 = 0
for y in range(N):
    if bits[y][0] == 1:
        dict1 |= 1 << y
assert dict1 in funcs

def certify(D):
    """D: Poly in e with integer coeffs, times 2^{n-1}. True if D > 0 on (0,1/2)."""
    if D.is_zero:
        return 'zero'
    g = D
    while g.eval(0) == 0:
        g = sp.Poly(sp.quo(g.as_expr(), e), e, domain='ZZ')
    h = sp.Poly(1 - 2 * e, e, domain='ZZ')
    while g.eval(Fraction(1, 2)) == 0:
        g = sp.Poly(sp.quo(g.as_expr(), h.as_expr()), e, domain='ZZ')
    deg = g.degree()
    tr = sp.Poly(sp.expand(sp.together(g.as_expr().subs(e, t / (2 * (1 + t))) * (2 * (1 + t)) ** deg)), t)
    cs = tr.all_coeffs()
    if all(c >= 0 for c in cs):
        return 'descartes'
    if all(c <= 0 for c in cs):
        return 'NEGATIVE'
    nr = g.count_roots(0, Fraction(1, 2))
    if nr == 0:
        return 'sturm' if g.eval(Fraction(1, 4)) > 0 else 'NEGATIVE'
    return f'ROOTS:{nr}'

res = {'n': n, 'K': K, 'count': len(funcs), 'by_k': {}}
pv = {F: pvec(F) for F in funcs}
for k in range(4, K + 1):
    t1 = time.time()
    P1 = sum((p ** k for p in pv[dict1]), sp.Poly(0, e, domain='ZZ'))
    tally = {}; bad = []
    for F in funcs:
        if F == dict1:
            continue
        Pf = sum((p ** k for p in pv[F]), sp.Poly(0, e, domain='ZZ'))
        r = certify(P1 - Pf)
        key = r.split(':')[0]
        tally[key] = tally.get(key, 0) + 1
        if key not in ('descartes', 'sturm'):
            bad.append((hex(F), r))
    res['by_k'][k] = {'tally': tally, 'bad': bad[:20], 'n_bad': len(bad)}
    print(f"k={k}: {tally} bad={len(bad)} ({time.time()-t1:.1f}s)", flush=True)
if out:
    json.dump(res, open(out, 'w'), indent=1)
