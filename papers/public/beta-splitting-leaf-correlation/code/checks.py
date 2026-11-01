"""Checks for "Correlation of leaf heights at mesoscopic separation in the critical beta-splitting tree".

A clade of m leaves splits at cut i (left child i leaves, right child m - i) at rate m/(2 i (m - i)), 1 <= i < m.
Sections A-F check the finite identities and inequalities of the paper (exact rational arithmetic where the
statement is an identity, double precision elsewhere). Section G is a Monte Carlo simulation of the two tagged
lineages, which uses none of the potentials or martingales of the paper. Run: python checks.py > checks_output.txt
"""
import math
import sys
from fractions import Fraction as Fr

import numpy as np

Z2 = math.pi ** 2 / 6
Z3 = 1.2020569031595942854
C1, C2 = Z2, 2 * Z3
SIG2 = C2 / C1 ** 3
FAIL = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
    if not ok:
        FAIL.append(name)


def harm(n):
    return sum(1.0 / k for k in range(1, n + 1))


# ---------------------------------------------------------------- A. drift and bracket of the potential (Lemma 2.1)
def drift_bracket(m, j):
    """d and v of F(m,j) = log(j(m+1-j)/m) by summing over all m-1 cuts."""
    a, b = j, m + 1 - j
    F0 = math.log(a * b / m)
    d = v = 0.0
    for i in range(1, m):
        rate = m / (2.0 * i * (m - i))
        if i < a:            # left removal of l = i leaves
            mm, jj = m - i, j - i
        else:                # right removal of m - i leaves; the tag stays at j
            mm, jj = i, j
        loss = F0 - math.log(jj * (mm + 1 - jj) / mm)
        d += rate * loss
        v += rate * loss * loss
    return d, v


print('A. drift and bracket of the potential, all 1 <= j <= m <= 400, and m = 2^10..2^14 at j = 1..64 and j = m/2')
worst = [0.0, 0.0]
neg = 0.0
kone = 0.0
pts = [(m, j) for m in range(1, 401) for j in range(1, m + 1)]
pts += [(m, j) for m in (2 ** 10, 2 ** 12, 2 ** 14) for j in list(range(1, 65)) + [m // 2]]
for m, j in pts:
    d, v = drift_bracket(m, j)
    k = min(j, m + 1 - j)
    e1, e2 = C1 - d, C2 - v
    if k == 1:
        kone = max(kone, abs(d), abs(v))
        continue
    neg = min(neg, e1, e2)
    worst[0] = max(worst[0], e1 * k / (1 + math.log(k + 1)))
    worst[1] = max(worst[1], e2 * k / (1 + math.log(k + 1) ** 2))
check('A1 at k = 1 the drift and bracket vanish', kone < 1e-12, 'max |d|,|v| = %.1e' % kone)
check('A2 e_1, e_2 >= 0 for k >= 2', neg > -1e-12, 'min = %.2e' % neg)
check('A3 e_p k / (1 + log^p(k+1)) bounded', max(worst) < 10,
      'max over the grid: p=1 %.4f, p=2 %.4f' % tuple(worst))
d, v = drift_bracket(2 ** 14, 2 ** 13)
k = 2 ** 13
check('A4 at m = 2^14, j = 2^13 the errors are within the bounds of A3',
      0 <= C1 - d <= 2 * (1 + math.log(k + 1)) / k and 0 <= C2 - v <= 3 * (1 + math.log(k + 1) ** 2) / k,
      'd = %.6f (zeta(2) = %.6f), v = %.6f (2 zeta(3) = %.6f)' % (d, C1, v, C2))

# ---------------------------------------------------------------- B. the common-clade chain, exact (Lemma 3.1, (3.1)-(3.2))
print('B. common-clade chain by enumeration of starts and cuts, exact rationals, 1 <= r < m <= 26')
ok_rate = ok_kill = ok_unif = ok_sep = True
for m in range(2, 27):
    hm1 = sum(Fr(1, k) for k in range(1, m))
    for r in range(1, m):
        s = m - r
        cnt = {}                              # (child size k, child start rank) -> rate mass
        kill = Fr(0)
        sep = {}
        for j in range(1, s + 1):             # first tag at j, second at j + r; each start has mass 1/s
            for i in range(1, m):
                rate = Fr(m, 2 * i * (m - i)) / s
                if j + r <= i:                # both in the left child (size i)
                    cnt[(i, j)] = cnt.get((i, j), 0) + rate
                elif j > i:                   # both in the right child (size m - i), start rank j - i
                    cnt[(m - i, j - i)] = cnt.get((m - i, j - i), 0) + rate
                else:                         # separated: i = j + a - 1, 1 <= a <= r
                    kill += rate
                    sep[(j, i - j + 1)] = rate
        for k in range(r + 1, m):
            masses = [cnt.get((k, jj), Fr(0)) for jj in range(1, k - r + 1)]
            tot = sum(masses)
            if tot != Fr(m * (k - r), (m - r) * k * (m - k)):
                ok_rate = False
            if len(set(masses)) != 1:
                ok_unif = False
        h = lambda q: sum(Fr(1, t) for t in range(1, q + 1))
        if kill != h(m - 1) - h(m - r - 1) + Fr(r, m - r) * (h(m - 1) - h(r)):
            ok_kill = False
        if kill + sum(cnt.values()) != hm1:
            ok_kill = False
        if any(sep[(j, a)] != Fr(m, 2 * (j + a - 1) * (m - j - a + 1)) / s for (j, a) in sep):
            ok_sep = False
check('B1 a_r(m,k) = m(k-r)/((m-r)k(m-k))', ok_rate)
check('B2 kappa_r(m) as in (3.2), and total rate h_{m-1}', ok_kill)
check('B3 start rank uniform in the retained child', ok_unif)
check('B4 separating cut (j,a) has rate lambda_m(j+a-1)/s', ok_sep)


# ---------------------------------------------------------------- C. drift of g(m) = log(m/r) for the killed chain ((3.3)-(3.5))
def hvec(n):
    return np.concatenate([[0.0], np.cumsum(1.0 / np.arange(1, n + 1))])


print('C. drift of g = log(m/r) for the killed chain, 1 <= r < m <= 600')
H = hvec(5000)
worst_id = worst_c = worst_low = 0.0
low_ok = True
d0_ok = True
for m in range(2, 601):
    ks = np.arange(1, m)
    d0 = np.sum(np.log(m / ks) / (m - ks))
    if not (0 <= C1 - d0 <= 2 * (1 + math.log(m)) / m):
        d0_ok = False
    for r in range(1, m):
        kk = np.arange(r + 1, m)
        a = m * (kk - r) / ((m - r) * kk * (m - kk))
        kap = H[m - 1] - H[m - r - 1] + r / (m - r) * (H[m - 1] - H[r])
        direct = np.sum(a * np.log(m / kk)) + kap * math.log(m / r)
        kr = np.arange(1, r + 1)
        formula = d0 - np.sum(np.log(r / kr) / (m - kr)) + r / (m - r) * np.sum(np.log(kk / r) / kk)
        worst_id = max(worst_id, abs(direct - formula))
        if m >= 2 * r:
            bound = (1 + math.log(m)) / m + (r / m) * (1 + math.log(m / r) ** 2)
            worst_c = max(worst_c, abs(direct - C1) / bound)
        elif m < 4 * r:
            if not (0 <= direct <= C1 + 1):
                low_ok = False
            worst_low = max(worst_low, direct)
check('C1 identity (3.3) for the drift', worst_id < 1e-9, 'max error %.1e' % worst_id)
check('C2 0 <= zeta(2) - d0(m) <= 2(1 + log m)/m', d0_ok)
check('C3 (3.5) for m >= 2r: |d - zeta(2)| / [(1+log m)/m + (r/m)(1+log^2(m/r))] bounded', worst_c < 10,
      'max ratio %.4f' % worst_c)
check('C4 0 <= d <= zeta(2) + 1 for r < m < 2r', low_ok, 'max d = %.4f' % worst_low)

# ---------------------------------------------------------------- D. exit and killing rates (Lemma 2.2, Proposition 3.2)
print('D. exit and killing rates')
check('D1 floor(k/2)/(2(k-1)) >= 1/4 for 2 <= k <= 10^6',
      all((k // 2) / (2 * (k - 1)) >= 0.25 for k in range(2, 10 ** 6 + 1)))
mn = 1.0
for r in range(1, 301):
    for m in range(r + 1, 4 * r):
        mn = min(mn, H[m - 1] - H[m - r - 1] + r / (m - r) * (H[m - 1] - H[r]))
check('D2 kappa_r(m) > 1/4 for r < m < 4r, r <= 300', mn > 0.25, 'min %.4f' % mn)
mn = 10.0
for r in (1, 2, 3, 7, 20, 50):
    for q in range(0, 4):
        L = 4 * r * 2 ** q
        for m in range(L, 2 * L):
            kk = np.arange(-(-L // 2), L)
            mn = min(mn, np.sum(m * (kk - r) / ((m - r) * kk * (m - kk))))
check('D3 exit rate of the bin [L, 2L), L = 4r 2^q, at least 1/8', mn >= 1 / 8, 'min %.4f' % mn)

# ---------------------------------------------------------------- E. mean separation time and mean height (Proposition 3.2)
print('E. E S_r(n) - log(n/r)/zeta(2) and E D_n - log(n)/zeta(2), exact recursion in double precision')
N = 1 << 13
HN = hvec(N)
ED = np.zeros(N + 1)
for m in range(2, N + 1):
    ks = np.arange(1, m)
    ED[m] = (1 + np.sum(ED[ks] / (m - ks))) / HN[m - 1]


def mean_sep(r, n):
    ES = np.zeros(n + 1)
    for m in range(r + 1, n + 1):
        kk = np.arange(r + 1, m)
        a = m * (kk - r) / ((m - r) * kk * (m - kk))
        ES[m] = (1 + np.sum(a * ES[kk])) / HN[m - 1]
    return ES


offs = []
print('   n       r    E S - log(n/r)/zeta(2)')
for r in (1, 4, 16, 64, 256, 1024, 4096):
    ES = mean_sep(r, N)
    for n in (1 << 9, 1 << 11, 1 << 13):
        if n > r:
            o = ES[n] - math.log(n / r) / C1
            offs.append(o)
            print('%6d %6d   %+.4f' % (n, r, o))
check('E1 E S - log(n/r)/zeta(2) bounded on the grid', max(abs(o) for o in offs) < 2,
      'range [%.4f, %.4f]' % (min(offs), max(offs)))
c0 = Z3 / Z2 ** 2 + 0.5772156649015329 / Z2
print('   E D_n - log(n)/zeta(2) at n = 2^9, 2^11, 2^13: %.4f %.4f %.4f (c0 = %.4f)'
      % tuple([ED[n] - math.log(n) / C1 for n in (1 << 9, 1 << 11, 1 << 13)] + [c0]))
check('E2 E D_n - log(n)/zeta(2) close to c0 = zeta(3)/zeta(2)^2 + gamma/zeta(2)',
      abs(ED[N] - math.log(N) / C1 - c0) < 1e-3, '%.6f vs %.6f' % (ED[N] - math.log(N) / C1, c0))

# ---------------------------------------------------------------- F. the rectangle estimate (Lemma 4.1)
print('F. E_w G^2 on the rectangle 1 <= j <= s, 1 <= a <= r, weight 1/(i(m-i)), i = j+a-1, m = s+r')


def rect_moment(r, s, fun):
    j = np.arange(1, s + 1, dtype=float)[:, None]
    a = np.arange(1, r + 1, dtype=float)[None, :]
    m = s + r
    i = j + a - 1
    w = 1.0 / (i * (m - i))
    return float(np.sum(w * fun(j, a, r, s, m, i)) / np.sum(w))


G2 = lambda j, a, r, s, m, i: np.log(j * a * (m - i) / ((s + 1 - j) * (r + 1 - a) * i)) ** 2
grid = [1, 2, 3, 5, 10, 30, 100, 300, 1000, 3000]
vals = {(r, s): rect_moment(r, s, G2) for r in grid for s in grid}
mx = max(vals.values())
print('   E_w G^2 at r = s:', ' '.join('%g:%.3f' % (r, vals[(r, r)]) for r in grid))
print('   E_w G^2 at r = 1, 30, 3000 with s = 3000:', ' '.join('%.3f' % vals[(r, 3000)] for r in (1, 30, 3000)))
check('F1 E_w G^2 bounded over r, s in {1,...,3000} grid', mx < 10, 'max %.4f' % mx)
sym = max(abs(vals[(r, s)] - vals[(s, r)]) for r in grid for s in grid)
check('F2 symmetric under (j,s) <-> (a,r)', sym < 1e-9, 'max asymmetry %.1e' % sym)
ctl = [rect_moment(r, r, lambda j, a, r, s, m, i: np.log(a) ** 2) for r in (10, 100, 1000, 3000)]
check('F3 negative control: E_w log^2(a) grows with r (no cancellation)', ctl[-1] > 2 * ctl[0],
      ' '.join('%.3f' % c for c in ctl))

# ---------------------------------------------------------------- G. Monte Carlo of the two tagged lineages
print('G. Monte Carlo: J uniform on [n], partner J + r mod n, 40000 trees per row, seed 20261014')
LOG2 = math.log(2.0)


def hfloat(k):
    k = k.astype(np.float64)
    small = k < 40
    out = np.empty_like(k)
    out[small] = HT[k[small].astype(np.int64)]
    kb = k[~small]
    out[~small] = np.log(kb) + 0.5772156649015329 + 1 / (2 * kb) - 1 / (12 * kb ** 2) + 1 / (120 * kb ** 4)
    return out


HT = hvec(40)


def inv_sample(rng, K):
    """i in {1..K} with P(i) proportional to 1/i: log-uniform proposal, accept with prob log2 (1/i)/log(1+1/i)."""
    out = np.zeros(K.size, dtype=np.int64)
    todo = np.arange(K.size)
    while todo.size:
        Kt = K[todo].astype(np.float64)
        i = np.minimum(np.floor(np.exp(rng.random(todo.size) * np.log1p(Kt))).astype(np.int64), K[todo])
        i = np.maximum(i, 1)
        acc = rng.random(todo.size) < LOG2 / (i * np.log1p(1.0 / i))
        out[todo[acc]] = i[acc]
        todo = todo[~acc]
    return out


def cut(rng, m):
    i = inv_sample(rng, m - 1)
    return np.where(rng.random(m.size) < 0.5, i, m - i)


def simulate(n, r, N, rng):
    J = rng.integers(1, n + 1, size=N, dtype=np.int64)
    P = (J - 1 + r) % n + 1
    x, y = np.minimum(J, P), np.maximum(J, P)            # positions inside the common clade
    m = np.full(N, n, dtype=np.int64)
    t = np.zeros(N)
    together = np.ones(N, dtype=bool)
    S = np.zeros(N)
    mr = np.zeros(N, dtype=np.int64)                      # size of the right tag's clade after separation
    while together.any():                                 # common clade until the separating cut
        idx = np.flatnonzero(together)
        mm = m[idx]
        t[idx] += rng.exponential(1.0, idx.size) / hfloat(mm - 1)
        i = cut(rng, mm)
        left = y[idx] <= i
        right = x[idx] > i
        sep = ~(left | right)
        m[idx[left]] = i[left]
        m[idx[right]] = mm[right] - i[right]
        x[idx[right]] -= i[right]
        y[idx[right]] -= i[right]
        S[idx[sep]] = t[idx[sep]]
        # after separation: the left tag is in the left child, the right tag in the right child
        ii = idx[sep]
        y[ii] -= i[sep]
        m[ii] = i[sep]
        mr[ii] = mm[sep] - i[sep]
        together[ii] = False
    hx = run_single(rng, m.copy(), x.copy(), S.copy())
    hy = run_single(rng, mr, y.copy(), S.copy())
    return hx, hy, S


def run_single(rng, m, j, t):
    alive = m > 1
    while alive.any():
        idx = np.flatnonzero(alive)
        mm = m[idx]
        t[idx] += rng.exponential(1.0, idx.size) / hfloat(mm - 1)
        i = cut(rng, mm)
        inleft = j[idx] <= i
        m[idx] = np.where(inleft, i, mm - i)
        j[idx] = np.where(inleft, j[idx], j[idx] - i)
        alive[idx] = m[idx] > 1
    return t


rng = np.random.default_rng(20261014)
NS = 40000
print('   log2 n  r          alpha   E S-log(n/r)/z2  Cov-s2 log(n/r)  Var-s2 log n   rho     1-alpha')
rows = []
for e in (20, 40):
    n = 2 ** e
    for alpha in (0.25, 0.5, 0.75):
        r = int(round(n ** alpha))
        hx, hy, S = simulate(n, r, NS, rng)
        both = np.concatenate([hx, hy])
        mu, var = both.mean(), both.var()
        cov = float(np.mean(hx * hy) - mu ** 2)
        rho = cov / var
        rows.append((e, alpha, rho))
        print('   %2d  %13d  %.2f   %+.3f           %+.3f           %+.3f        %.3f   %.2f'
              % (e, r, alpha, S.mean() - math.log(n / r) / C1, cov - SIG2 * math.log(n / r),
                 var - SIG2 * math.log(n), rho, 1 - alpha))
inc = all(rows[k + 3][2] > rows[k][2] - 0.02 for k in range(3))
check('G1 correlations ordered by alpha and below 1 - alpha by O(1/log n)',
      all(rows[k][2] > rows[k + 1][2] for k in (0, 1, 3, 4)) and all(rows[k][2] < 1 - rows[k][1] for k in range(6)) and inc)
n = 2 ** 20
rr = []
for r in (1, n - 1):
    hx, hy, S = simulate(n, r, NS, rng)
    both = np.concatenate([hx, hy])
    rr.append((np.mean(hx * hy) - both.mean() ** 2) / both.var())
print('   n = 2^20: rho at offset 1 = %.3f, at oriented offset n - 1 = %.3f' % tuple(rr))
check('G2 control: the oriented offset n - 1 gives the law of offset 1, far from 1 - alpha = 0',
      abs(rr[0] - rr[1]) < 0.03 and rr[1] > 0.8)

print()
print('ALL CHECKS PASS' if not FAIL else 'FAILED: ' + ', '.join(FAIL))
sys.exit(1 if FAIL else 0)
