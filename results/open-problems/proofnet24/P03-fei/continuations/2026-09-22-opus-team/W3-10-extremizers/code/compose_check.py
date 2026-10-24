"""Theorem A (restriction monotonicity under balanced composition) - numerical checks and controls.

Claim (proved in the report): for every Boolean G, input j and c in [-1,1],
    br(G,j,c) := Inf_j(G) h2(c^2) + H(G) - (Ht_G(j,c) + Ht_G(j,-c))/2  >= 0,
where Ht_G(j,mu) is the spectral entropy of G with input j of mean mu (others uniform).  By F4 Thm 4.1 this is
Delta_w(F) - Inf_j(G) Delta_w(g_j) for F = G(g_1..g_k) with balanced blocks and c = ghat_j({w}).

Checks:
 1. F4 Thm 4.1 against brute force on random compositions with balanced blocks (independent implementation).
 2. br >= 0 on every 3- and 4-input function, every j, c on a 401-point grid; and on Numaro's g (18 inputs).
 3. Control A (must fail): drop the Inf_j h2(c^2) term.
 4. Scope test: with BIASED blocks, is Delta_w(F)/Inf_w(F) >= Delta_w(g_j)/Inf_w(g_j)?  (search for violations)
"""
import sys, itertools, time
import numpy as np
sys.path.insert(0, '.')
from core import polite, walsh_int, stats_from_walsh, stats, is_prime

polite()
rng = np.random.default_rng(20260923)
OUT = open('../logs/compose_check.log', 'w')


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    OUT.write(s + '\n')
    OUT.flush()


def phi(p):
    p = np.asarray(p, dtype=np.float64)
    out = np.zeros_like(p)
    m = p > 0
    out[m] = -p[m] * np.log2(p[m])
    return out


def h2(q):
    return float(phi(q) + phi(1 - q))


def fhat(tt):
    return walsh_int(np.ascontiguousarray(tt, dtype=np.int8)) / tt.shape[0]


def Ht(Gh, k, j, mu):
    """spectral entropy of G with input j at mean mu, other inputs uniform."""
    N = 1 << k
    bit = 1 << j
    V = 1 - mu * mu
    U = np.arange(N)
    lo = U[(U & bit) == 0]
    a = Gh[lo] + mu * Gh[lo | bit]
    b = np.sqrt(max(V, 0.0)) * Gh[lo | bit]
    return float(phi(a * a).sum() + phi(b * b).sum())


def br(Gh, k, j, c):
    N = 1 << k
    U = np.arange(N)
    Inf = float((Gh[(U >> j) & 1 == 1] ** 2).sum())
    H = float(phi(Gh ** 2).sum())
    return Inf * h2(c * c) + H - 0.5 * (Ht(Gh, k, j, c) + Ht(Gh, k, j, -c))


def compose(G, k, blocks):
    """F(x) = G(g_1(x^1),...,g_k(x^k)); blocks: list of +-1 tables; variables concatenated block by block."""
    sizes = [int(round(np.log2(b.shape[0]))) for b in blocks]
    n = sum(sizes)
    N = 1 << n
    x = np.arange(N)
    idx = np.zeros(N, dtype=np.int64)
    off = 0
    for jj, (b, s) in enumerate(zip(blocks, sizes)):
        sub = (x >> off) & ((1 << s) - 1)
        val = b[sub]
        idx |= ((val == -1).astype(np.int64)) << jj
        off += s
    return G[idx].astype(np.int8), sizes


def rand_balanced(m):
    t = np.array([1] * (1 << (m - 1)) + [-1] * (1 << (m - 1)), dtype=np.int8)
    rng.shuffle(t)
    return t


def rand_odd(m):
    N = 1 << m
    t = np.zeros(N, dtype=np.int8)
    for x in range(N):
        y = x ^ (N - 1)
        if x < y:
            v = rng.choice([-1, 1])
            t[x] = v
            t[y] = -v
    return t


# ---------------------------------------------------------------- 1. F4 Thm 4.1 against brute force
log('== 1. restriction-drop law (F4 Thm 4.1) vs brute force, balanced blocks')
worst = 0.0
nviol = 0
cnt = 0
for trial in range(300):
    k = int(rng.integers(2, 5))
    G = np.where(rng.random(1 << k) < 0.5, 1, -1).astype(np.int8)
    if len(set(G.tolist())) == 1:
        continue
    blocks = []
    for jj in range(k):
        m = int(rng.integers(1, 4))
        blocks.append(rand_odd(m) if rng.random() < 0.3 else rand_balanced(m))
    if sum(int(np.log2(b.shape[0])) for b in blocks) > 13:
        continue
    F, sizes = compose(G, k, blocks)
    sF = stats(F)
    Gh = fhat(G)
    UG = np.arange(1 << k)
    off = 0
    for jj, (b, s) in enumerate(zip(blocks, sizes)):
        sg = stats(b)
        gh = fhat(b)
        InfjG = float((Gh[(UG >> jj) & 1 == 1] ** 2).sum())
        for wl in range(s):
            w = off + wl
            c = float(gh[1 << wl])
            pred = InfjG * (sg['Delta'][wl] + h2(c * c)) + float(phi(Gh ** 2).sum()) \
                - 0.5 * (Ht(Gh, k, jj, c) + Ht(Gh, k, jj, -c))
            err = abs(pred - sF['Delta'][w])
            worst = max(worst, err)
            cnt += 1
            if sF['Delta'][w] < InfjG * sg['Delta'][wl] - 1e-12:
                nviol += 1
        off += s
log('  %d leaf checks, max |formula - brute| = %.3e ; violations of Delta_w(F) >= Inf_j(G) Delta_w(g_j): %d' % (cnt, worst, nviol))

# ---------------------------------------------------------------- 2. br >= 0 exhaustive small gates
log('== 2. br(G,j,c) >= 0 on every NPN class of 2-, 3- and 4-input functions (br is NPN invariant), c-grid 2001 points')
cgrid = np.linspace(-1, 1, 2001)


def br_grid(Gh, k, j, cg):
    N = 1 << k
    bit = 1 << j
    U = np.arange(N)
    lo = U[(U & bit) == 0]
    Inf = float((Gh[lo | bit] ** 2).sum())
    H = float(phi(Gh ** 2).sum())
    A = Gh[lo][None, :] + cg[:, None] * Gh[lo | bit][None, :]
    Am = Gh[lo][None, :] - cg[:, None] * Gh[lo | bit][None, :]
    Bv = (1 - cg[:, None] ** 2) * (Gh[lo | bit][None, :] ** 2)
    Htp = phi(A * A).sum(axis=1) + phi(Bv).sum(axis=1)
    Htm = phi(Am * Am).sum(axis=1) + phi(Bv).sum(axis=1)
    h = phi(cg ** 2) + phi(1 - cg ** 2)
    return Inf * h + H - 0.5 * (Htp + Htm), H - 0.5 * (Htp + Htm), Inf


for k in (2, 3, 4):
    N = 1 << k
    reps = range(1 << N) if k == 2 else np.load('../logs/npn_reps_n%d.npy' % k)
    mn = np.inf
    arg = None
    ctrl_min = np.inf
    for code in reps:
        code = int(code)
        G = np.array([-1 if (code >> x) & 1 else 1 for x in range(N)], dtype=np.int8)
        Gh = fhat(G)
        for j in range(k):
            v, ctrl, Inf = br_grid(Gh, k, j, cgrid)
            if Inf == 0:
                continue
            i = int(np.argmin(v))
            if v[i] < mn:
                mn, arg = float(v[i]), (code, j, float(cgrid[i]))
            ctrl_min = min(ctrl_min, float(ctrl.min()))
    log('  k=%d: min br = %.3e at (code=%d, j=%d, c=%.4f); control (no h2 term) min = %.4f' % (k, mn, arg[0], arg[1], arg[2], ctrl_min))

# Numaro's g
g = np.load('../../inputs/numaro18_pm1_table.npy').astype(np.int8)
gh = fhat(g)
log('  Numaro g: H=%.12f' % float(phi(gh ** 2).sum()))
for j in (0, 9):
    vals = [br(gh, 18, j, c) for c in np.linspace(0, 1, 201)]
    ctrl = [float(phi(gh ** 2).sum()) - 0.5 * (Ht(gh, 18, j, c) + Ht(gh, 18, j, -c)) for c in np.linspace(0, 1, 201)]
    log('  Numaro g, input %d: min br over c in [0,1] = %.3e ; control min = %.4e' % (j, min(vals), min(ctrl)))

# ---------------------------------------------------------------- 4. biased blocks
log('== 4. scope: blocks with nonzero mean.  Is Delta_w(F)/Inf_w(F) >= Delta_w(g_j)/Inf_w(g_j)?')
worst = np.inf
ex = None
cnt = 0
for trial in range(3000):
    k = int(rng.integers(2, 4))
    G = np.where(rng.random(1 << k) < 0.5, 1, -1).astype(np.int8)
    if len(set(G.tolist())) == 1:
        continue
    blocks = []
    for jj in range(k):
        m = int(rng.integers(1, 4))
        t = np.where(rng.random(1 << m) < rng.uniform(0.15, 0.85), -1, 1).astype(np.int8)
        if len(set(t.tolist())) == 1:
            t[0] = -t[0]
        blocks.append(t)
    F, sizes = compose(G, k, blocks)
    sF = stats(F)
    off = 0
    for jj, (b, s) in enumerate(zip(blocks, sizes)):
        sg = stats(b)
        for wl in range(s):
            w = off + wl
            if sg['Inf'][wl] < 1e-12 or sF['Inf'][w] < 1e-12:
                continue
            d = sF['Delta'][w] / sF['Inf'][w] - sg['Delta'][wl] / sg['Inf'][wl]
            cnt += 1
            if d < worst:
                worst = d
                ex = (G.copy(), [bb.copy() for bb in blocks], jj, wl, sF['Delta'][w] / sF['Inf'][w], sg['Delta'][wl] / sg['Inf'][wl])
        off += s
log('  %d leaf checks; min of [Delta_w(F)/Inf_w(F) - Delta_w(g_j)/Inf_w(g_j)] = %.6f' % (cnt, worst))
if ex is not None and worst < 0:
    G, bl, jj, wl, r1, r0 = ex
    log('  counterexample: G=%s blocks=%s j=%d w=%d : ratio in F %.6f < ratio in block %.6f' % (
        ''.join('1' if v == -1 else '0' for v in G), [''.join('1' if v == -1 else '0' for v in bb) for bb in bl], jj, wl, r1, r0))
OUT.close()
