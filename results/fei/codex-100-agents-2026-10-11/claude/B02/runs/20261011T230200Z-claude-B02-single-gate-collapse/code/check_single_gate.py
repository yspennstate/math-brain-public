# B02 lead check: single-gate collapse of thm:posteriorforest and the tribes obstruction.
# Exact integer FWHT for spectra; floating point only for logarithms (evidence, not proof).
import itertools, math, random, sys
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 40
GAMMA = 6 / 5
KREF = 3 + 2 * math.log2(3) + math.log2(6 * math.e)
C = GAMMA / math.log(2)  # coefficient of the nat-valued rank term


def fwht_int(a):
    a = list(a)
    h = 1
    n = len(a)
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def spectrum(tt, n):
    # tt: list of +-1 values indexed by x (bit j = coordinate j true when 1)
    co = fwht_int(tt)  # 2^n * fhat(A), A as bitmask
    N = 1 << n
    return [Fraction(c * c, N * N) for c in co]


def h2(p):
    p = float(p)
    if p <= 0 or p >= 1:
        return 0.0
    return -p * math.log2(p) - (1 - p) * math.log2(1 - p)


def stats(P, n):
    H = -sum(float(p) * math.log2(float(p)) for p in P if p > 0)
    inf = [sum(P[A] for A in range(len(P)) if A >> j & 1) for j in range(n)]
    I = sum(inf)
    v = 1 - P[0]
    Elnfact = sum(float(P[A]) * math.lgamma(bin(A).count('1') + 1) for A in range(len(P)) if P[A] > 0)
    return H, inf, I, v, Elnfact


def sord_direct(P, n, rank):
    # E sum_{j in A} ln( r(j) / (|A cap U_j|+1) ), one ordered piece (M=1)
    tot = 0.0
    for A in range(1, len(P)):
        if P[A] == 0:
            continue
        els = sorted((rank[j] for j in range(n) if A >> j & 1))
        s = sum(math.log(r) - math.log(i + 1) for i, r in enumerate(els))
        tot += float(P[A]) * s
    return tot


def sord_formula(inf, n, Elnfact, rank):
    return sum(float(inf[j]) * math.log(rank[j]) for j in range(n)) - Elnfact


def tribes_tt(m, w):
    n = m * w
    tt = []
    for x in range(1 << n):
        anyblock = any(((x >> (i * w)) & ((1 << w) - 1)) == (1 << w) - 1 for i in range(m))
        tt.append(-1 if anyblock else 1)
    return tt


out = []
def say(s):
    print(s)
    out.append(s)

# ---------- Part A: tribes exhaustive small cases ----------
say("PART A: tribes(m,w) exhaustive, exact spectrum vs closed form; single-gate identity")
for (m, w) in [(2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (2, 3), (3, 3), (4, 3), (2, 4), (3, 4)]:
    n = m * w
    tt = tribes_tt(m, w)
    P = spectrum(tt, n)
    q = Fraction(2 ** w - 1, 2 ** w)
    ok = True
    for A in range(1, 1 << n):
        k = sum(1 for i in range(m) if (A >> (i * w)) & ((1 << w) - 1))
        if P[A] != 4 * q ** (2 * (m - k)) * Fraction(1, 4 ** (w * k)):
            ok = False
            break
    ok0 = (P[0] == (2 * q ** m - 1) ** 2)
    H, inf, I, v, Elnf = stats(P, n)
    Ek = Fraction(4 * m) * q ** m / 2 ** w
    I_cf = Fraction(2 * m * w) * q ** (m - 1) / 2 ** w
    v_cf = 4 * q ** m * (1 - q ** m)
    lq = math.log2(float(q))
    P0 = float((2 * q ** m - 1) ** 2)
    H_cf = (-P0 * math.log2(P0) if P0 > 0 else 0.0) - 2 * float(v_cf) * (1 + m * lq) + 2 * float(Ek) * (w + lq)
    rank_nat = list(range(1, n + 1))
    rnd = list(range(1, n + 1)); random.Random(m * 100 + w).shuffle(rnd)
    d1 = sord_direct(P, n, rank_nat); f1 = sord_formula(inf, n, Elnf, rank_nat)
    d2 = sord_direct(P, n, rnd); f2 = sord_formula(inf, n, Elnf, rnd)
    LB = float(q ** (m - 1)) * float(I) * (math.log(m) - 1)
    boundSG = h2(v) + KREF * float(I) + C * d1
    say(f" m={m} w={w} n={n}: spectrum formula {ok and ok0}; I exact {I == I_cf}; v exact {v == v_cf}; "
        f"H={H:.6f} H_closed={H_cf:.6f}; H/I={H/float(I):.4f}; SORD nat direct={d1:.6f} formula={f1:.6f}; "
        f"rand direct={d2:.6f} formula={f2:.6f}; LB q^(m-1) I (ln m-1)={LB:.6f} <= SORD {LB <= d1 + 1e-12}; "
        f"single-gate bound={boundSG:.4f} >= H {boundSG >= H}")

# ---------- Part B: rearrangement and validity on random functions ----------
say("PART B: random f on n<=7: identity for every order, min over all orders = influence-sorted order, bound >= H")
rng = random.Random(20261011)
worst_id = 0.0; worst_gap = 0.0; viol = 0; cnt = 0
for trial in range(60):
    n = rng.choice([4, 5, 6, 7])
    p1 = rng.choice([0.5, 0.25, 0.1])
    tt = [(-1 if rng.random() < p1 else 1) for _ in range(1 << n)]
    if all(t == tt[0] for t in tt):
        continue
    P = spectrum(tt, n)
    H, inf, I, v, Elnf = stats(P, n)
    order = sorted(range(n), key=lambda j: -inf[j])
    rank_sorted = [0] * n
    for pos, j in enumerate(order):
        rank_sorted[j] = pos + 1
    fs = sord_formula(inf, n, Elnf, rank_sorted)
    best = None
    perms = itertools.permutations(range(1, n + 1)) if n <= 6 else (tuple(rng.sample(range(1, n + 1), n)) for _ in range(300))
    for perm in perms:
        r = list(perm)
        fo = sord_formula(inf, n, Elnf, r)
        if rng.random() < 0.02:
            d = sord_direct(P, n, r)
            worst_id = max(worst_id, abs(d - fo))
        best = fo if best is None else min(best, fo)
    worst_gap = max(worst_gap, fs - best)
    bound = h2(v) + KREF * float(I) + C * fs
    cnt += 1
    if bound < H - 1e-9:
        viol += 1
say(f" functions={cnt}; max |direct - formula| = {worst_id:.2e}; max (sorted - min over orders) = {worst_gap:.2e}; bound<H violations = {viol}")

# ---------- Part C: tribes m=2^w, closed forms, large w ----------
say("PART C: tribes m=2^w: H/I, one-gate-per-block forest bound / I (closed form), single-gate lower bound / I")
say("  w        H/I     blockforest/I    singlegate_LB/I")
for w in list(range(2, 13)) + [16, 20, 24, 28, 32, 40, 48, 60]:
    m = mp.mpf(2) ** w
    q = 1 - mp.mpf(2) ** (-w)
    qm = q ** m
    Ek = 4 * m * qm * mp.mpf(2) ** (-w)
    I = 2 * m * w * q ** (m - 1) * mp.mpf(2) ** (-w)
    v = 4 * qm * (1 - qm)
    P0 = (2 * qm - 1) ** 2
    lq = mp.log(q, 2)
    H = (-P0 * mp.log(P0, 2) if P0 > 0 else 0) - 2 * v * (1 + m * lq) + 2 * Ek * (w + lq)
    h2v = -v * mp.log(v, 2) - (1 - v) * mp.log(1 - v, 2)
    Lam = m * mp.log(1 + mp.mpf(2) ** (-w), 2)
    Z = 1 - mp.mpf(2) ** (-Lam)
    # phibar(w) = E over uniform nonempty S in [w] of sum_{j in S} ln pos(j) - ln |S|!
    s1 = mp.mpf(2) ** (w - 1) * mp.loggamma(w + 1)
    s2 = mp.fsum(mp.binomial(w, s) * mp.loggamma(s + 1) for s in range(1, w + 1))
    phibar = (s1 - s2) / (mp.mpf(2) ** w - 1)
    block = h2v + v * (Lam + mp.log(Z, 2)) + KREF * I + Ek * (w + C * phibar)
    sg_lb = h2v + KREF * I + GAMMA * q ** (m - 1) * I * (w - mp.log(mp.e, 2))
    say(f" {w:3d}   {float(H/I):8.4f}   {float(block/I):10.4f}     {float(sg_lb/I):10.4f}")

open(sys.argv[1], 'w', encoding='utf-8').write("\n".join(out) + "\n")
