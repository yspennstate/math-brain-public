"""Lemma G-key (exact integers) and Theorem G (float) on the campaign falsifier families, plus the
selector-coordinate ratios Delta_y U / Inf_y and Delta_y H / Inf_y claimed in U-X003, and the
tightness claims (addressing, 2-bit bent, point defects).

Index convention: bit i of x is 1 iff x_i = -1 (equivalently the 0/1 variable equals 1).
"""
import math, json, sys
import numpy as np
from rlib import Spec, walsh, superset_sum, popcounts, plogq, restrict_tables

rng = np.random.default_rng(31337)
out = {}


def gkey_exact(f):
    """returns (#violations, #pairs, #equalities) of W_S^2 4^n <= 4^{|S|-1} Pi_S^2, using Python ints."""
    W = walsh(np.asarray(f, dtype=np.int64))
    N = W.shape[-1]; n = N.bit_length() - 1
    P = [int(w) * int(w) for w in W]
    Pi = superset_sum(np.array(P, dtype=object))
    pc = popcounts(n)
    v = 0; e = 0
    for S in range(1, N):
        lhs = P[S] * N * N
        rhs = (4 ** (int(pc[S]) - 1)) * int(Pi[S]) ** 2
        if lhs > rhs:
            v += 1
        elif lhs == rhs and P[S] > 0:
            e += 1
    return v, N - 1, e


def thmG(f):
    sp = Spec.from_tables(np.asarray(f, dtype=np.int64))
    H = float(sp.H()[0]); I = float(sp.I()[0]); U = float(sp.U()[0]); Var = float(sp.Var()[0]); p0 = 1 - Var
    rhs = 2 * (I - Var) + 2 * U - (p0 * math.log2(1 / p0) if p0 > 0 else 0.0)
    return dict(H=H, I=I, U=U, Var=Var, rhs=rhs, slack=rhs - H, ratio=(H / rhs if rhs > 0 else float('nan')))


def coord_ratios(f, i):
    """Delta_i H/Inf_i and Delta_i U/Inf_i by direct physical restriction."""
    f = np.asarray(f, dtype=np.int64)
    sp = Spec.from_tables(f)
    inf = float(sp.infl()[0, i])
    a = Spec.from_tables(restrict_tables(f, i, 1)); b = Spec.from_tables(restrict_tables(f, i, -1))
    dH = float(sp.H()[0] - 0.5 * (a.H()[0] + b.H()[0]))
    dU = float(sp.U()[0] - 0.5 * (a.U()[0] + b.U()[0]))
    return dict(Inf=inf, dH_over_Inf=dH / inf, dU_over_Inf=dU / inf)


def bits(x, i):
    return (x >> i) & 1


fam = {}

# ---- X001 parity lifts of random g (n = 3..7) -> n+1 bits (bit n = z)
rows = []
for n in range(3, 8):
    for trial in range(4):
        g = rng.choice([-1, 1], size=1 << n)
        N = 1 << (n + 1)
        f = np.empty(N, dtype=np.int64)
        for x in range(N):
            z = bits(x, n)
            y = 0
            for i in range(n):
                y |= ((bits(x, i) ^ z) << i)
            f[x] = g[y]
        v, tot, e = gkey_exact(f); r = thmG(f)
        rows.append(dict(n=n + 1, gkey_viol=v, slack=r['slack']))
fam['X001_parity_lift'] = dict(cases=len(rows), gkey_viol=sum(r['gkey_viol'] for r in rows), min_slack=min(r['slack'] for r in rows))

# ---- X002 selector synergy, odd m
rows = []; x002 = []
for m in [3, 5, 7, 9, 11]:
    n = m + 1; N = 1 << n
    f = np.empty(N, dtype=np.int64)
    for x in range(N):
        y = [bits(x, i) for i in range(m)]     # y_1..y_m at bits 0..m-1
        s = bits(x, m)                          # selector at bit m
        t = [(y[j] + y[m - 1]) % 2 for j in range(m - 1)]
        q = sum(t[2 * a] * t[2 * a + 1] for a in range((m - 1) // 2))
        g0 = (-1) ** q
        f[x] = g0 if s == 0 else ((-1) ** y[m - 1]) * g0
    v, tot, e = gkey_exact(f); r = thmG(f)
    cr = coord_ratios(f, m)
    rows.append(dict(m=m, gkey_viol=v, slack=r['slack'], H=r['H'], I=r['I']))
    x002.append(dict(m=m, H=r['H'], I=r['I'], **cr))
fam['X002_selector_synergy'] = dict(cases=rows)
out['X002_selector_ratios'] = x002

# ---- X003 sparse activation splice, k = 4, 6
x003 = []
for k in [4, 6]:
    r_ = 2 * k; n = 1 + r_ + k; N = 1 << n
    xs = np.arange(N)
    xb = (xs & ((1 << k) - 1))                    # x bits 0..k-1
    zb = (xs >> k) & ((1 << r_) - 1)              # z bits k..k+r-1
    yb = (xs >> (k + r_)) & 1                     # selector y at bit k+r
    q = np.zeros(N, dtype=np.int64)
    for a in range(k // 2):
        q += ((xb >> (2 * a)) & 1) * ((xb >> (2 * a + 1)) & 1)
    b = 1 - 2 * (q & 1)
    bp = b.copy(); bp[xb == 0] = b[xb == 0] - 2      # b' = b - 2*1_{x=0}; b(0) = 1 -> -1
    A = (zb == 0).astype(np.int64)
    Gf = 1 + A * (b - 1); Hf = 1 + A * (bp - 1)
    f = np.where(yb == 0, Gf, Hf)
    assert set(np.unique(f)) <= {-1, 1}
    v, tot, e = gkey_exact(f) if n <= 13 else (None, None, None)
    r = thmG(f)
    cr = coord_ratios(f, k + r_)
    x003.append(dict(k=k, n=n, gkey_viol=v, slack=r['slack'], **cr))
out['X003'] = x003

# ---- X004 overlapping supports  F(z,y) = zy  and X005  F(z,y) = g(z) y
rows = []
f = np.array([1, -1, -1, 1], dtype=np.int64)
v, tot, e = gkey_exact(f); rows.append(dict(name='zy', gkey_viol=v, slack=thmG(f)['slack']))
for n in range(2, 7):
    g = rng.choice([-1, 1], size=1 << n)
    N = 1 << (n + 1); f = np.empty(N, dtype=np.int64)
    for x in range(N):
        f[x] = g[x & ((1 << n) - 1)] * (1 - 2 * bits(x, n))
    v, tot, e = gkey_exact(f); rows.append(dict(name=f'g(z)y n={n+1}', gkey_viol=v, slack=thmG(f)['slack']))
fam['X004_X005'] = rows

# ---- X009 bent splice with one flip, selector t
x009 = []
for m in [4, 6, 8, 10, 12]:
    n = m + 1; N = 1 << n
    xs = np.arange(N); yb = xs & ((1 << m) - 1); t = (xs >> m) & 1
    q = np.zeros(N, dtype=np.int64)
    for a in range(m // 2):
        q += ((yb >> (2 * a)) & 1) * ((yb >> (2 * a + 1)) & 1)
    b = 1 - 2 * (q & 1)
    b2 = b.copy(); b2[yb == 0] = b[yb == 0] - 2
    f = np.where(t == 0, b, b2)
    v, tot, e = gkey_exact(f) if n <= 11 else (None, None, None)
    r = thmG(f); cr = coord_ratios(f, m)
    x009.append(dict(m=m, gkey_viol=v, slack=r['slack'], **cr))
out['X009'] = x009

# ---- X011 activations F = 1 + A_r (g - 1) for random balanced-ish g, r = 1..4
rows = []
for r_ in range(1, 5):
    for trial in range(3):
        m = int(rng.integers(2, 5)); g = rng.choice([-1, 1], size=1 << m)
        n = m + r_; N = 1 << n; xs = np.arange(N)
        A = ((xs >> m) == 0).astype(np.int64)
        f = 1 + A * (g[xs & ((1 << m) - 1)] - 1)
        v, tot, e = gkey_exact(f); rows.append(dict(r=r_, m=m, gkey_viol=v, slack=thmG(f)['slack']))
fam['X011_activation'] = dict(cases=len(rows), gkey_viol=sum(r['gkey_viol'] for r in rows), min_slack=min(r['slack'] for r in rows))

# ---- X012 addressing a = 1,2,3 : f(x,y) = y_x
addr = []
for a in [1, 2, 3]:
    n = a + (1 << a); N = 1 << n; xs = np.arange(N)
    adr = xs & ((1 << a) - 1)
    f = 1 - 2 * ((xs >> (a + adr)) & 1)
    v, tot, e = gkey_exact(f); r = thmG(f)
    addr.append(dict(a=a, n=n, gkey_viol=v, H=r['H'], I=r['I'], U=r['U'], rhs=r['rhs'], slack=r['slack'], H_expected=2 * a, I_expected=1 + a / 2))
out['X012_addressing'] = addr

# ---- 2-bit bent
f = np.array([1, 1, 1, -1], dtype=np.int64)
out['bent2'] = thmG(f)

# ---- point defects r = 1..16 (exact formulas, no transform needed): p0=(1-2p)^2, p_S=4p^2
pd = []
for r_ in range(2, 42, 3):
    p = 2.0 ** -r_
    H = (1 - 2 * p) ** 2 * math.log2(1 / (1 - 2 * p) ** 2) if p < 0.5 else 0.0
    H += (2 ** r_ - 1) * 4 * p * p * math.log2(1 / (4 * p * p))
    I = 2 * r_ * p; Var = 1 - (1 - 2 * p) ** 2
    # pi(S) = 4p 2^{-|S|}: U = p0 log(1/p0) + sum_{k>=1} binom(r,k) 4p^2 log2(2^{r-k}) = p0log(1/p0) + 4p^2 sum_k binom(r,k)(r-k)
    p0 = (1 - 2 * p) ** 2
    U = (p0 * math.log2(1 / p0) if 0 < p0 < 1 else 0.0) + 4 * p * p * sum(math.comb(r_, k) * (r_ - k) for k in range(1, r_ + 1))
    rhs = 2 * (I - Var) + 2 * U - (p0 * math.log2(1 / p0) if 0 < p0 < 1 else 0.0)
    pd.append(dict(r=r_, H_over_I=H / I, U_over_I=U / I, H_over_rhs=H / rhs))
out['point_defects'] = pd
# brute-force check of the point-defect formulas for r <= 10
pdb = []
for r_ in range(1, 11):
    f = np.ones(1 << r_, dtype=np.int64); f[0] = -1
    v, tot, e = gkey_exact(f); rr = thmG(f)
    pdb.append(dict(r=r_, gkey_viol=v, gkey_equalities=e, of=tot, H_over_rhs=rr['ratio']))
out['point_defects_bruteforce'] = pdb

# ---- random functions and random sparse perturbations, n = 5..12
rows = []
for trial in range(60):
    n = int(rng.integers(5, 13)); N = 1 << n
    kind = trial % 3
    if kind == 0:
        f = rng.choice([-1, 1], size=N).astype(np.int64)
    elif kind == 1:   # sparse perturbation of a bent function (even n) or constant
        m = n - (n % 2); xs = np.arange(N); q = np.zeros(N, dtype=np.int64)
        for a in range(m // 2):
            q += ((xs >> (2 * a)) & 1) * ((xs >> (2 * a + 1)) & 1)
        f = (1 - 2 * (q & 1)).astype(np.int64)
        flips = rng.choice(N, size=int(rng.integers(1, 5)), replace=False); f[flips] *= -1
    else:             # biased random function (rare -1)
        f = np.where(rng.random(N) < 0.03, -1, 1).astype(np.int64)
        if f.min() == 1:
            f[int(rng.integers(N))] = -1
    v, tot, e = gkey_exact(f) if n <= 11 else (None, None, None)
    rows.append(dict(n=n, kind=kind, gkey_viol=v, slack=thmG(f)['slack']))
fam['random_and_sparse'] = dict(cases=len(rows), gkey_viol=sum((r['gkey_viol'] or 0) for r in rows), min_slack=min(r['slack'] for r in rows))

# ---- negative control: non-Boolean coherent vector psi_n = n^{-1/2} sum_i x_i (X006): lemma and theorem must FAIL
neg = []
for n in [2, 3, 4, 8]:
    N = 1 << n
    p = np.zeros(N)
    for i in range(n):
        p[1 << i] = 1.0 / n
    sp = Spec(p)
    H = float(sp.H()[0]); I = float(sp.I()[0]); U = float(sp.U()[0]); Var = 1.0
    lem_fails = sum(1 for i in range(n) if p[1 << i] > (4 ** 0) * sp.pi[0, 1 << i] ** 2 + 1e-15)
    neg.append(dict(n=n, H=H, rhsG=2 * (I - Var) + 2 * U, lemma_failures=lem_fails))
out['negative_control_psi_n'] = neg

out['families'] = fam
print(json.dumps(out, indent=1, default=str))
with open('falsifiers_results.json', 'w', encoding='utf-8') as fh:
    json.dump(out, fh, indent=1, default=str)
