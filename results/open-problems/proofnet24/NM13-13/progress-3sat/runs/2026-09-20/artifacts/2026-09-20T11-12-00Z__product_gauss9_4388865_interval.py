#!/usr/bin/env python3
import math
import mpmath as mp

DPS = 850
KMAX = 2300
NGAUSS = 9
SCALE = 1000
mp.iv.dps = DPS
Z = mp.iv.mpf([0, 0])
O = mp.iv.mpf([1, 1])
S = mp.iv.mpf([SCALE, SCALE])

def q(n, d):
    return mp.iv.mpf([n, n]) / d

def dec(s):
    return mp.iv.mpf([s, s])

def contains_zero(x):
    return bool(x.a <= 0 <= x.b)

def solve_interval(A, b):
    n = len(A)
    M = [[A[i][j] for j in range(n)] for i in range(n)]
    y = [b[i] for i in range(n)]
    pivots = []
    for k in range(n):
        p = M[k][k]
        if contains_zero(p):
            raise RuntimeError(f"interval pivot contains zero at {k}: {p}")
        pivots.append(p)
        for i in range(k + 1, n):
            f = M[i][k] / p
            M[i][k] = Z
            for j in range(k + 1, n):
                M[i][j] = M[i][j] - f * M[k][j]
            y[i] = y[i] - f * y[k]
    x = [Z for _ in range(n)]
    for i in range(n - 1, -1, -1):
        s = y[i]
        for j in range(i + 1, n):
            s = s - M[i][j] * x[j]
        if contains_zero(M[i][i]):
            raise RuntimeError(f"back pivot contains zero at {i}")
        x[i] = s / M[i][i]
    return x, pivots

def poly_mul(A, B):
    out = [Z for _ in range(len(A) + len(B) - 1)]
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            out[i + j] = out[i + j] + a * b
    return out

# Exact density and exact symmetric five-support survey.
alpha = q(877773, 200000)  # 4.388865 exactly
vals = [q(33, 5000), q(49, 625), O / 2, q(576, 625), q(4967, 5000)]
probs = [q(139, 2500), q(1831, 10000), q(2613, 5000),
         q(1831, 10000), q(139, 2500)]
lam = 3 * alpha / 2

# Compound-Poisson moments of Q through K+18 by forward differences.
pair = [(probs[i] * probs[j], O - vals[i] * vals[j])
        for i in range(5) for j in range(5)]
NEED = KMAX + 2 * NGAUSS
EZ = [O]
pows = [O for _ in pair]
for jj in range(1, NEED + 1):
    m = Z
    for idx, (wt, base) in enumerate(pair):
        pows[idx] = pows[idx] * base
        m = m + wt * pows[idx]
    EZ.append(mp.iv.exp(lam * (m - O)))

arr = EZ
mus = [O]
series = Z
allpos = True
for k in range(1, NEED + 1):
    arr = [arr[j + 1] - arr[j] for j in range(len(arr) - 1)]
    mu = arr[0] if k % 2 == 0 else -arr[0]
    mus.append(mu)
    allpos = allpos and bool(mu.a > 0)
    if k <= KMAX:
        series += mu * mu / k

L = Z
for i in range(5):
    for j in range(5):
        for h in range(5):
            L += probs[i] * probs[j] * probs[h] * mp.iv.log(O - vals[i] * vals[j] * vals[h])
AK = -series - 2 * alpha * L
muK = mus[KMAX]

# Direct product-measure tilt. If X=Q Q' for iid Q,Q', then under X^K tilt
# s_j = E_K X^j = (mu_{K+j}/mu_K)^2.
sx = [(mus[KMAX + j] / muK) ** 2 for j in range(2 * NGAUSS)]

# Condition the moment problem with Y=1000(1-X).
my = []
for j in range(2 * NGAUSS):
    v = Z
    for ell in range(j + 1):
        term = mp.iv.mpf([math.comb(j, ell), math.comb(j, ell)]) * sx[ell]
        v = v - term if ell % 2 else v + term
    my.append((S ** j) * v)

# Monic degree-9 polynomial orthogonal to 1,Y,...,Y^8.
H = [[my[r + c] for c in range(NGAUSS)] for r in range(NGAUSS)]
rhs = [-my[r + NGAUSS] for r in range(NGAUSS)]
coef, pivots = solve_interval(H, rhs)  # c0,...,c8 in Y^9+c8Y^8+...+c0

def poly(y):
    out = y + coef[8]
    for j in range(7, -1, -1):
        out = out * y + coef[j]
    return out

# Certified disjoint root brackets from an independent 950-digit diagnostic.
centers = [
    '0.131618622381117055709051703602489702223002663031510182490738',
    '0.471935218596784764561173073858563256776056213744010043422210',
    '1.036588569161853847581458850434943222576775584123761843082740',
    '1.846633943110408433115855101255376171356575933395977488853080',
    '2.925864097892503131346117482724479370383596544845603596864040',
    '4.316692403121601554862748593746595843347283436843019236700670',
    '6.103582916458009449127351414791968050213680655332359999396220',
    '8.431006453696684247667501536474301024792244105290814418601950',
    '11.690595737715236492984659200971566839781652270566374639300900',
]
eps = dec('0.00000000000000000001')
root_signs = []
y = []
for cs in centers:
    c = dec(cs)
    lo, hi = c - eps, c + eps
    plo, phi = poly(lo), poly(hi)
    root_signs.append((bool(plo.b < 0), bool(plo.a > 0),
                       bool(phi.b < 0), bool(phi.a > 0)))
    y.append(mp.iv.mpf([lo.a, hi.b]))

root_sign_ok = True
for i, (lo_neg, lo_pos, hi_neg, hi_pos) in enumerate(root_signs):
    root_sign_ok = root_sign_ok and ((lo_neg and hi_pos) if i % 2 == 0 else (lo_pos and hi_neg))
ordered = all(bool(y[i].b < y[i + 1].a) for i in range(NGAUSS - 1))
inside = bool(y[0].a > 0 and y[-1].b < S.a)

# Gaussian weights from the degree-8 Lagrange basis.
w = []
for i in range(NGAUSS):
    numpoly = [O]
    den = O
    for j in range(NGAUSS):
        if j == i:
            continue
        numpoly = poly_mul(numpoly, [-y[j], O])
        den = den * (y[i] - y[j])
    num = Z
    for r, cc in enumerate(numpoly):
        num += cc * my[r]
    w.append(num / den)

# Sanity check: exactness on degrees 0,...,8 is interval-contained.
match = []
for j in range(NGAUSS):
    qmom = Z
    for i in range(NGAUSS):
        qmom += w[i] * (y[i] ** j)
    rr = qmom - my[j]
    match.append(bool(rr.a <= 0 <= rr.b))

checks = {
    'all_mu_positive_1_to_Kplus18': allpos,
    'all_elimination_pivots_positive': all(bool(pp.a > 0) for pp in pivots),
    'root_brackets_sign_certified': root_sign_ok,
    'root_intervals_ordered': ordered,
    'Y_roots_inside_0_1000': inside,
    'weights_positive': all(bool(ww.a > 0) for ww in w),
    'moment_match_0_to_8_interval_contains_zero': all(match),
}

# Complete direct-product Gaussian tail. For h_T(x)=sum_{t=1}^T x^t/(K+t),
# h_T^(18)>=0 on [0,1]. Degree-17 Hermite interpolation at the nine Gaussian
# nodes therefore gives E_K h_T(X) >= sum_i w_i h_T(x_i). Letting T->infinity
# by monotone convergence is valid because all certified nodes x_i are <1.
# Evaluate h_inf(x)=sum_{t>=1}x^t/(K+t) as
# x^{-K}[-log(1-x)-sum_{n=1}^K x^n/n].
x = [O - y[i] / S for i in range(NGAUSS)]
h = []
for i in range(NGAUSS):
    xx = x[i]
    partial = Z
    pp = xx
    for n in range(1, KMAX + 1):
        partial += pp / n
        pp *= xx
    hh = (-mp.iv.log(O - xx) - partial) / (xx ** KMAX)
    h.append(hh)

tail = Z
for i in range(NGAUSS):
    tail += w[i] * h[i]
TLB = muK * muK * tail
Aup = AK - TLB

mp.iv.dps = 90
print('NM13-13 T04 DIRECT PRODUCT-MEASURE NINE-NODE GAUSSIAN CERTIFICATE')
print('alpha = 877773/200000 = 4.388865')
print('survey support = {33/5000,49/625,1/2,576/625,4967/5000}')
print('survey weights = {139/2500,1831/10000,2613/5000,1831/10000,139/2500}')
print('KMAX =', KMAX)
print('NGAUSS =', NGAUSS)
print('complete tail used')
print('interval dps =', DPS)
print('checks =', checks)
print('A_K =', AK)
print('mu_K =', muK)
print('orthogonal solve pivots =', pivots)
print('degree-9 coefficients c0..c8 =', coef)
print('root sign tuples =', root_signs)
for i in range(NGAUSS):
    print('Y%d =' % (i + 1), y[i], '; X%d =' % (i + 1), x[i], '; w%d =' % (i + 1), w[i])
print('complete direct-product Gauss9 tail lower bound =', TLB)
print('A upper bound =', Aup)
print('CERTIFIED_STRUCTURAL_CHECKS =', all(checks.values()))
print('CERTIFIED_A_UPPER_NEGATIVE =', bool(Aup.b < 0))
print('CERTIFIED_A_NEGATIVE =', bool(Aup.b < 0),
      'because A <= A_K - complete_direct_product_Gauss9_tail_LB')
