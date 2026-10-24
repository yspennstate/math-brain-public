# B14 lead checks (Claude), written for run 20261011T224500Z-claude-B14-granularity-neutralization.
# Independent implementation: numpy integer FWHT, superset-max DP, Python Fractions. No agent code imported.
# Convention: index b, bit i of b = 1  <=>  x_i = -1 ; chi_S(x) = (-1)^{popcount(S & b)} ; W[S] = sum_b f[b] chi_S.
import sys, json, math, time, random, itertools
from fractions import Fraction as Fr
import numpy as np

T0 = time.time()
OUT = {}
ASSERTS = [0]

def ok(cond, msg):
    ASSERTS[0] += 1
    if not cond:
        raise AssertionError(msg)

def fwht(f):
    a = np.array(f, dtype=np.int64).copy()
    n = a.shape[-1]
    h = 1
    while h < n:
        a = a.reshape(a.shape[:-1] + (-1, 2, h))
        x = a[..., 0, :].copy(); y = a[..., 1, :].copy()
        a[..., 0, :] = x + y; a[..., 1, :] = x - y
        a = a.reshape(a.shape[:-3] + (n,))
        h *= 2
    return a

def popcounts(m):
    idx = np.arange(1 << m, dtype=np.int64)
    pc = np.zeros(1 << m, dtype=np.int64)
    for i in range(m):
        pc += (idx >> i) & 1
    return pc

def upmax_degree(W, m):
    """d[S] = max{|T| : T superset of S, W[T] != 0}; -1 if none.  Works on last axis."""
    pc = popcounts(m)
    d = np.where(W != 0, pc, -1).astype(np.int64)
    for i in range(m):
        h = 1 << i
        shp = d.shape[:-1] + (-1, 2, h)
        dd = d.reshape(shp)
        dd[..., 0, :] = np.maximum(dd[..., 0, :], dd[..., 1, :])
        d = dd.reshape(d.shape)
    return d

def v2(x):
    x = abs(int(x)); return (x & -x).bit_length() - 1

def influences_edges(f, m):
    f = np.asarray(f); idx = np.arange(1 << m)
    return [Fr(int(np.count_nonzero(f != f[idx ^ (1 << i)])), 1 << m) for i in range(m)]

def spectral_data(f, m):
    W = fwht(f); pc = popcounts(m); D = 1 << (2 * m)
    q = [Fr(int(w) * int(w), D) for w in W]
    return W, pc, q

# ---------------- R1: A067 local granularity, all tables n<=4 ----------------
r1 = {}
for n in range(0, 5):
    N = 1 << n
    tables = np.array(list(itertools.product([1, -1], repeat=N)), dtype=np.int64) if n < 4 else None
    if n == 4:
        ints = np.arange(1 << 16, dtype=np.int64)
        tables = np.stack([1 - 2 * ((ints >> j) & 1) for j in range(16)], axis=1)
    W = fwht(tables)
    d = upmax_degree(W, n)
    pc = popcounts(n)
    bad = 0; checked = 0
    absW = np.abs(W)
    low = absW & (-absW)
    for S in range(1, N):
        mask = W[:, S] != 0
        if not mask.any():
            continue
        lv = np.log2(low[mask, S]).astype(np.int64)
        cond = lv + d[mask, S] - 1 >= n
        bad += int((~cond).sum()); checked += int(mask.sum())
    ASSERTS[0] += checked
    ok(bad == 0, f"granularity fails n={n}")
    # sanity: termwise bound H <= 2I+2U-cv in floats
    q = (W.astype(np.float64) ** 2) / float(N * N)
    with np.errstate(divide='ignore', invalid='ignore'):
        H = -np.nansum(np.where(q > 0, q * np.log2(np.where(q > 0, q, 1)), 0.0), axis=1)
    I = (q * pc).sum(axis=1)
    dd = np.where(W != 0, d, 0)
    U = (np.where(np.arange(N) > 0, q * (dd - pc), 0.0)).sum(axis=1)
    v = 1 - q[:, 0]
    c = 2 - math.log2(math.e)
    gap = H - (2 * I + 2 * U - c * v)
    r1[n] = {"tables": int(tables.shape[0]), "nonzero_nonempty_coeffs_checked": checked, "violations": bad,
             "max_float_gap_H_minus_bound": float(gap.max())}
    ok(gap.max() < 1e-9, f"float bound gap n={n}")
OUT["R1_granularity_all_n_le_4"] = r1

# ---------------- R2: structured random functions n=5..9 ----------------
rng = random.Random(20261011)
def rand_dtree(n, depth, avail):
    if depth == 0 or not avail or rng.random() < 0.25 * (1 + (n - len(avail)) / max(1, n)):
        s = rng.choice([1, -1]); return lambda b: s
    i = rng.choice(sorted(avail)); a2 = avail - {i}
    L = rand_dtree(n, depth - 1, a2); R = rand_dtree(n, depth - 1, a2)
    return lambda b, i=i, L=L, R=R: (R(b) if (b >> i) & 1 else L(b))
def rand_struct(n):
    k = rng.randrange(5)
    if k == 0:
        t = rand_dtree(n, n, set(range(n))); return [t(b) for b in range(1 << n)]
    if k == 1:
        w = [rng.randint(-5, 5) for _ in range(n)]; th = rng.randint(-6, 6)
        return [1 if sum(w[i] * (1 - 2 * ((b >> i) & 1)) for i in range(n)) - th >= 0 else -1 for b in range(1 << n)]
    if k == 2:
        vs = list(range(n)); rng.shuffle(vs); A = vs[: n // 2]; B = vs[n // 2:]
        ta = [rng.choice([1, -1]) for _ in range(1 << len(A))]; tb = [rng.choice([1, -1]) for _ in range(1 << len(B))]
        def sub(b, V): return sum(((b >> v) & 1) << j for j, v in enumerate(V))
        return [ta[sub(b, A)] * tb[sub(b, B)] for b in range(1 << n)]
    if k == 3:
        V = rng.sample(range(n), min(n, rng.randint(1, 4))); tt = [rng.choice([1, -1]) for _ in range(1 << len(V))]
        return [tt[sum(((b >> v) & 1) << j for j, v in enumerate(V))] for b in range(1 << n)]
    g = rand_struct(n); A = rng.randrange(1 << n)
    return [g[b] * (1 - 2 * (bin(A & b).count("1") % 2)) for b in range(1 << n)]
r2 = {}
for n in range(5, 10):
    cnt = 0; checked = 0
    per = 400 if n <= 7 else 150
    for _ in range(per):
        f = rand_struct(n); W = fwht(f); d = upmax_degree(W, n)
        for S in range(1, 1 << n):
            if W[S] != 0:
                ok(v2(W[S]) + int(d[S]) - 1 >= n, f"granularity R2 n={n}"); checked += 1
        cnt += 1
    r2[n] = {"functions": cnt, "coeffs_checked": checked}
OUT["R2_granularity_structured_random_n5_9"] = r2

# ---------------- R3: dictator surgery ----------------
r3 = {}
for n in range(2, 13):
    m = n; p = Fr(1, 1 << m)
    f = [(1 - 2 * (b & 1)) for b in range(1 << m)]; f[0] = -1   # x1 except at all+, where -1
    W, pc, q = spectral_data(f, m)
    a = [Fr(int(w), 1 << m) for w in W]
    ok(a[1] == 1 - 2 * p, "dict a1")
    ok(all(a[S] == -2 * p for S in range(1 << m) if S != 1), "dict others")
    I = sum(q[S] * int(pc[S]) for S in range(1 << m))
    Ie = sum(influences_edges(f, m))
    ok(I == Ie == 1 + (2 * n - 4) * p, "dict I")
    v = 1 - q[0]; ok(v == 1 - 4 * p * p, "dict v")
    d = upmax_degree(W, m)
    U = sum(q[S] * (int(d[S]) - int(pc[S])) for S in range(1, 1 << m))
    ok(U == n - 1 - (2 * n - 4) * p - 4 * n * p * p, "dict U")
    r3[n] = {"I": str(I), "U": str(U), "U_over_I": float(U / I)}
OUT["R3_dictator_surgery_exact"] = r3

# ---------------- R4: Maj3 x point defect, all anchors ----------------
r4 = {}
for n in range(2, 6):
    m = n + 3
    def F(b):
        z = [1 - 2 * ((b >> i) & 1) for i in range(3)]
        maj = 1 if sum(z) > 0 else -1
        y = b >> 3
        return maj * (-1 if y == 0 else 1)
    f = [F(b) for b in range(1 << m)]
    W = fwht(f)
    idx = np.arange(1 << m)
    Wh = np.stack([W[idx ^ A] for A in range(1 << m)])     # row A: spectrum of F*chi_A
    d = upmax_degree(Wh, m)
    num = (Wh.astype(object) ** 2 * (d - 1).astype(object))[:, 1:].sum(axis=1)   # sum_{R != empty} W^2 (d-1)
    # E_sum(A) = 2*num/4^m ; claim E_sum >= 3n/2  <=>  4*num >= 3n*4^m
    mins = min(int(x) for x in num)
    ok(all(4 * int(x) >= 3 * n * (1 << (2 * m)) for x in num), f"Maj3 anchor n={n}")
    W1, pc, q = spectral_data(f, m)
    I = sum(q[S] * int(pc[S]) for S in range(1 << m))
    ok(I == Fr(3, 2) + Fr(2 * n, 1 << n), "Maj3 I")
    ok(I == sum(influences_edges(f, m)), "Maj3 I edges")
    r4[n] = {"anchors": 1 << m, "min_A_Esum": str(Fr(2 * mins, 1 << (2 * m))), "three_n_over_2": str(Fr(3 * n, 2)), "I": str(I)}
OUT["R4_maj3_pointdefect_all_anchors"] = r4

# ---------------- R5: addressing ----------------
r5 = {}
for a in range(1, 5):
    m = a + (1 << a)
    b = np.arange(1 << m, dtype=np.int64)
    u = b & ((1 << a) - 1)
    f = 1 - 2 * ((b >> (a + u)) & 1)
    W = fwht(f)
    pc = popcounts(m)
    d = upmax_degree(W, m)
    supp = np.nonzero(W)[0]
    ok(len(supp) == 4 ** a, "addr support size")
    ok(bool(np.all(np.abs(W[supp]) == (1 << (m - a)))), "addr magnitude")
    ok(bool(np.all(d[supp] == a + 1)), "addr d")
    Unum = int((W[supp].astype(object) ** 2 * (d[supp] - pc[supp]).astype(object)).sum())
    U = Fr(Unum, 1 << (2 * m))
    ok(U == Fr(a, 2), "addr U")
    Inum = int((W[supp].astype(object) ** 2 * pc[supp].astype(object)).sum())
    ok(Fr(Inum, 1 << (2 * m)) == 1 + Fr(a, 2), "addr I")
    r5[a] = {"N": m, "U": str(U), "I": str(Fr(Inum, 1 << (2 * m))), "H_exact": 2 * a}
OUT["R5_addressing_exact"] = r5

# ---------------- R6: A066 point-defect heat formulas ----------------
r6 = {}
from math import comb
for n in range(2, 11):
    m = n
    f = [1] * (1 << m); f[0] = -1
    W, pc, q = spectral_data(f, m)
    ok(all(q[S] == Fr(4, 1 << (2 * m)) for S in range(1, 1 << m)), "pd spectrum")
    ok(q[0] == (1 - Fr(2, 1 << m)) ** 2, "pd empty")
    I = sum(q[S] * int(pc[S]) for S in range(1 << m)); ok(I == Fr(2 * n, 1 << n), "pd I")
    # J/I as polynomial in z (ln2 formal): coefficient of z^k
    for k in range(0, n + 1):
        lhs = Fr(2 * n - 2) * Fr(4, 1 << (2 * n)) * k * comb(n, k) / I
        rhs = Fr(2 * n - 2) * (comb(n - 1, k - 1) if k >= 1 else 0) / Fr(1 << (n - 1))
        ok(lhs == rhs, "heat poly")
    area = (n - 1) * sum(Fr(comb(n - 1, k), (1 << (n - 1)) * (k + 1)) for k in range(n))   # times ln2
    ok(area == 2 * (1 - Fr(1, n)) * (1 - Fr(1, 1 << n)), "heat area")
    r6[n] = {"area_over_ln2": str(area)}
OUT["R6_A066_point_defect_heat"] = r6

# ---------------- N1: point-defect neutralization ----------------
def base_funcs():
    yield "x1", 1, [1, -1]
    yield "AND2", 2, [1, 1, 1, -1]
    yield "Maj3", 3, [1 if sum(1 - 2 * ((b >> i) & 1) for i in range(3)) > 0 else -1 for b in range(8)]
    a = 2; m = a + (1 << a)
    yield "addr2", m, [1 - 2 * ((b >> (a + (b & 3))) & 1) for b in range(1 << m)]
n1 = {}
for name, n, f0 in base_funcs():
    rows = []
    Wb, pcb, qb = spectral_data(f0, n)
    for Nn in range(n + 1, 15):
        if Nn - n > 6 and name != "x1":
            continue
        fpad = [f0[b & ((1 << n) - 1)] for b in range(1 << Nn)]
        fp = list(fpad); fp[0] = -fp[0]
        W, pc, q = spectral_data(fp, Nn)
        Wpad = fwht(fpad); qpad = [Fr(int(w) * int(w), 1 << (2 * Nn)) for w in Wpad]
        d = upmax_degree(W, Nn)
        ok(all(int(d[S]) == Nn for S in range(1 << Nn) if W[S] != 0), "neutral d=N")
        inf_p = influences_edges(fp, Nn); inf_0 = influences_edges(fpad, Nn)
        ok(all(abs(x - y) <= Fr(2, 1 << Nn) for x, y in zip(inf_p, inf_0)), "neutral dInf")
        Ip = sum(inf_p); I0 = sum(inf_0)
        ok(Ip == sum(q[S] * int(pc[S]) for S in range(1 << Nn)), "neutral I fourier=edges")
        p = Fr(1, 1 << Nn)
        L1 = sum(abs(x - y) for x, y in zip(q, qpad))
        sumabs = sum(Fr(abs(int(w)), 1 << Nn) for w in Wpad)
        ok(L1 <= 4 * p * sumabs + 4 * p * p * (1 << Nn), "neutral L1")
        ok(sumabs * sumabs <= (1 << Nn), "neutral CS")
        vp = 1 - q[0]
        Up = sum(q[S] * (int(d[S]) - int(pc[S])) for S in range(1, 1 << Nn))
        ok(Up == Nn * vp - Ip, "neutral U=Nv-I")
        Hp = -sum(float(x) * math.log2(float(x)) for x in q if x > 0)
        H0 = -sum(float(x) * math.log2(float(x)) for x in qpad if x > 0)
        rows.append({"N": Nn, "I_f": str(I0), "I_fprime": float(Ip), "H_f": H0, "H_fprime": Hp, "U_fprime": float(Up),
                     "U_over_I": float(Up / Ip), "L1_spectral_change": float(L1)})
    n1[name] = rows
OUT["N1_point_defect_neutralization"] = n1

# ---------------- N2: hybrid granularity / code bounds ----------------
LOG2E = math.log2(math.e); C_A067 = 2 - LOG2E
def h2(x):
    return 0.0 if x <= 0 or x >= 1 else -(x * math.log2(x) + (1 - x) * math.log2(1 - x))
def hybrid_report(f, m):
    W = fwht(np.array(f, dtype=np.int64)); D = float(1 << (2 * m))
    q = W.astype(np.float64) ** 2 / D
    pc = popcounts(m); d = upmax_degree(W, m)
    I_i = np.array([q[(np.arange(1 << m) >> i) & 1 == 1].sum() for i in range(m)])
    I = float(I_i.sum())
    nz = q > 0
    H = float(-(q[nz] * np.log2(q[nz])).sum())
    v = 1 - q[0]
    U = float((q[1:] * np.where(W[1:] != 0, d[1:] - pc[1:], 0)).sum())
    a = np.where(np.arange(1 << m) > 0, 2.0 * (d - 1), 0.0)
    a[0] = -math.log2(q[0]) if q[0] > 0 else 0.0
    # influence code
    cost = np.zeros(1 << m)
    idx = np.arange(1 << m)
    for i in range(m):
        ci = math.log2(I / I_i[i]) if I_i[i] > 0 else 1e9
        cost += ((idx >> i) & 1) * ci
    linf = LOG2E + cost
    # level code, uniform prior on levels 0..m
    lgC = np.array([math.log2(math.comb(m, k)) for k in range(m + 1)])
    llev = lgC[pc] + math.log2(m + 1)
    lmix = 1.0 + np.minimum(llev, linf)
    out = {"m": m, "H": H, "I": I, "A067_bound": 2 * I + 2 * U - C_A067 * v}
    for nm, l in (("inf", linf), ("mix", lmix)):
        K = nz & (l < a)
        Pm = nz & ~K
        hyb = h2(float(q[K].sum())) + float((q[Pm] * a[Pm]).sum()) + float((q[K] * l[K]).sum())
        out["hyb_" + nm] = hyb
        ok(H <= hyb + 1e-9, "hybrid sanity")
    out["H_over_I"] = H / I; out["hyb_inf_over_I"] = out["hyb_inf"] / I; out["hyb_mix_over_I"] = out["hyb_mix"] / I
    out["A067_over_I"] = out["A067_bound"] / I
    return out
n2 = {"dictator_surgery": [], "maj3_x_pointdefect": [], "addressing": [], "pd_addressing": []}
for n in range(3, 15):
    f = [(1 - 2 * (b & 1)) for b in range(1 << n)]; f[0] = -1
    n2["dictator_surgery"].append(dict(n=n, **hybrid_report(f, n)))
for n in range(2, 11):
    m = n + 3
    f = [((1 if sum(1 - 2 * ((b >> i) & 1) for i in range(3)) > 0 else -1) * (-1 if (b >> 3) == 0 else 1)) for b in range(1 << m)]
    n2["maj3_x_pointdefect"].append(dict(n=n, **hybrid_report(f, m)))
for a in range(1, 5):
    m = a + (1 << a)
    b = np.arange(1 << m, dtype=np.int64); u = b & ((1 << a) - 1)
    f = 1 - 2 * ((b >> (a + u)) & 1)
    n2["addressing"].append(dict(a=a, **hybrid_report(f, m)))
    fp = f.copy(); fp[0] = -fp[0]
    n2["pd_addressing"].append(dict(a=a, **hybrid_report(fp, m)))
OUT["N2_hybrid_support_values"] = n2

# ---------------- N3: heavy-block restriction bound (support) ----------------
def H_I_U_var(f, m):
    W = fwht(np.array(f, dtype=np.int64)); D = float(1 << (2 * m)) if m > 0 else 1.0
    q = W.astype(np.float64) ** 2 / D
    pc = popcounts(m); d = upmax_degree(W, m)
    nz = q > 0
    H = float(-(q[nz] * np.log2(q[nz])).sum())
    I = float((q * pc).sum())
    U = float((q[1:] * np.where(W[1:] != 0, d[1:] - pc[1:], 0)).sum()) if m > 0 else 0.0
    return H, I, U, 1 - q[0]
n3 = {"functions": 0, "blocks_checked": 0, "max_gap_H_minus_rhs": -1e9}
for _ in range(300):
    n = rng.randint(2, 6)
    f = rand_struct(n)
    if rng.random() < 0.5:   # add a point defect half the time
        f = list(f); f[rng.randrange(1 << n)] *= -1
    H, I, U, v = H_I_U_var(f, n)
    W = fwht(np.array(f)); q = W.astype(np.float64) ** 2 / float(1 << (2 * n))
    Ii = [float(q[(np.arange(1 << n) >> i) & 1 == 1].sum()) for i in range(n)]
    for Bmask in range(1 << n):
        B = [i for i in range(n) if (Bmask >> i) & 1]; R = [i for i in range(n) if not (Bmask >> i) & 1]
        EU = 0.0; EV = 0.0; ER = 0.0
        for y in range(1 << len(B)):
            sub = []
            for xr in range(1 << len(R)):
                bb = 0
                for j, i in enumerate(B): bb |= ((y >> j) & 1) << i
                for j, i in enumerate(R): bb |= ((xr >> j) & 1) << i
                sub.append(f[bb])
            Hy, Iy, Uy, vy = H_I_U_var(sub, len(R))
            EU += Uy; EV += vy
        EU /= (1 << len(B)); EV /= (1 << len(B))
        IB = sum(Ii[i] for i in B); IR = I - IB
        rhs = sum(h2(Ii[i]) for i in B) + (2 / math.log(2)) * IB + 2 * IR + 2 * EU - C_A067 * EV
        n3["max_gap_H_minus_rhs"] = max(n3["max_gap_H_minus_rhs"], H - rhs)
        ok(H <= rhs + 1e-9, "heavy block sanity")
        n3["blocks_checked"] += 1
    n3["functions"] += 1
OUT["N3_heavy_block_support"] = n3

OUT["exact_assertions"] = ASSERTS[0]
OUT["seconds"] = time.time() - T0
OUT["status"] = "PASS"
json.dump(OUT, open(sys.argv[1], "w"), indent=1, default=str)
print("PASS", ASSERTS[0], "assertions", round(OUT["seconds"], 1), "s")
