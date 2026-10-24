"""Exhaustive enumeration of the two-address class at n = 5 for the fixed address pair (y1, y2) = coordinates
(0, 1) and C = coordinates (2, 3, 4), by an independent row-based method:

  1. all v in {0,+-1,+-2}^8 (v = 2 g on the 3-bit cube); keep those whose squared Walsh law is product (exact
     integer test) - these are the only possible rows (Lemma 1 values; product hypothesis);
  2. a Boolean f with address pair (0,1) <-> a quadruple (g_0, g_1, g_2, g_12) that is pointwise a 2-bit fiber:
     at each x either one row is +-1 and the others 0, or all four are +-1/2 with sign product -1;
  3. group rows by (half-set Hm, one-set Om, sign pattern on Hm) and enumerate all compatible quadruples.

By coordinate permutation (which preserves H and I) this covers every f in K2 on 5 variables.
Outputs: the number of K2 functions with this address pair; max of H - c* I and of Phi over them (float),
exact sign checks at the maximisers; the max of H/I; and a random reconstruction cross-check."""
import sys, json, time, itertools, random
from fractions import Fraction
import numpy as np
from refk2 import walsh_int, LogLin, H_minus_cI_exact, in_K
from ref_rows import analyse_row

t0 = time.time()
m = 3
n = 5
NP = 1 << m
CST = 16 / 3 - 1.5 * np.log2(3)

# ---- step 1: candidate rows
vals = np.array([0, 1, -1, 2, -2], dtype=np.int64)
idx = np.array(list(itertools.product(range(5), repeat=NP)), dtype=np.int64)
Vrows = vals[idx]                     # (390625, 8) entries 2 g(x)
Vh = walsh_int(Vrows)                 # sum_x 2 g(x) chi_U(x) = 16 ghat(U)
A = Vh * Vh
Z = A.sum(axis=1)
s = np.stack([A[:, [u for u in range(NP) if (u >> i) & 1]].sum(axis=1) for i in range(m)], axis=1)
ok = np.ones(len(A), dtype=bool)
for u in range(NP):
    rhs = np.ones(len(A), dtype=np.int64)
    for i in range(m):
        rhs = rhs * (s[:, i] if (u >> i) & 1 else (Z - s[:, i]))
    ok &= (A[:, u] * Z * Z == rhs)
prod_rows = np.nonzero(ok)[0]
print("candidate product rows (incl. zero):", len(prod_rows), f"{time.time()-t0:.1f}s", flush=True)

# global Walsh coefficient of f at T u U is 32 ghat_T(U) = 2 Vh
rows = []
for k in prod_rows:
    v = Vrows[k]
    Hm = sum(1 << x for x in range(NP) if abs(v[x]) == 1)
    Om = sum(1 << x for x in range(NP) if abs(v[x]) == 2)
    neg = sum(1 << x for x in range(NP) if v[x] < 0)
    Wrow = [int(2 * t) for t in Vh[k]]
    # per-row float quantities: a = sum ghat^2 log2(1/ghat^2), w, wIU = sum ghat^2 |U|
    gh = np.array(Wrow, dtype=np.float64) / 32.0
    p = gh * gh
    nz = p > 0
    a = float(-(p[nz] * np.log2(p[nz])).sum())
    w = float(p.sum())
    wIU = float(sum(p[u] * bin(u).count("1") for u in range(NP)))
    rows.append(dict(v=v, Hm=Hm, Om=Om, neg=neg, W=Wrow, a=a, w=w, wIU=wIU))

# exact analysis of every nonzero row (Lemmas 1-6, identity, e_T <= ebar_T); web for t = 0
n_checked = 0
for R in rows:
    if R["w"] == 0:
        R["web0"] = 0.0
        R["an"] = None
        continue
    res = analyse_row(R["W"], m, n, 0)
    assert res is not False and res is not None
    R["an"] = res
    R["web0"] = float(res["web"])
    d = LogLin().add(res["web"]).add(res["we"], -1)
    assert d.sign() >= 0, "row with e_T > ebar_T"
    n_checked += 1
print("rows analysed exactly:", n_checked, f"{time.time()-t0:.1f}s", flush=True)

# slot values: d_t = a - c (t w + wIU);  phi_t = web0 - c t w
def dval(R, t):
    return R["a"] - CST * (t * R["w"] + R["wIU"])
def phival(R, t):
    return R["web0"] - CST * t * R["w"]

# ---- step 2/3: group and enumerate
from collections import defaultdict
group = defaultdict(list)    # (Hm, Om) -> row ids
for i, R in enumerate(rows):
    group[(R["Hm"], R["Om"])].append(i)
Hms = sorted(set(k[0] for k in group))
FULL = (1 << NP) - 1
TS = [0, 1, 1, 2]   # |T| for slots 0={}, 1={y1}, 2={y2}, 3={y1,y2}

count = 0
best_d = -1e9; best_d_combo = None
best_phi = -1e9; best_phi_combo = None
best_ratio = 0.0; best_ratio_combo = None
near_zero = []   # combos with H - c I > -1e-9 for exact checking
near_phi = []    # combos with Phi > -1e-9 for exact checking

def pattern(R, Hm):
    return R["neg"] & Hm

for Hm in Hms:
    comp = FULL & ~Hm
    Oms = sorted(set(k[1] for k in group if k[0] == Hm))
    Omset = set(Oms)
    # all ordered 4-tuples (O0,O1,O2,O3) of available one-sets partitioning comp
    for O0 in Oms:
        if O0 & ~comp:
            continue
        rest0 = comp & ~O0
        for O1 in Oms:
            if O1 & ~rest0:
                continue
            rest1 = rest0 & ~O1
            for O2 in Oms:
                if O2 & ~rest1:
                    continue
                O3 = rest1 & ~O2
                if O3 not in Omset:
                    continue
                L = [group[(Hm, O)] for O in (O0, O1, O2, O3)]
                if Hm == 0:
                    # no sign coupling: every choice valid
                    count += len(L[0]) * len(L[1]) * len(L[2]) * len(L[3])
                    # maxima are separable
                    for kind in ("d", "phi"):
                        tot = 0.0; combo = []
                        for slot in range(4):
                            fn = dval if kind == "d" else phival
                            bi = max(L[slot], key=lambda i: fn(rows[i], TS[slot]))
                            tot += fn(rows[bi], TS[slot]); combo.append(bi)
                        if kind == "d" and tot > best_d:
                            best_d, best_d_combo = tot, combo
                        if kind == "phi" and tot > best_phi:
                            best_phi, best_phi_combo = tot, combo
                    # near-zero and ratio: enumerate (sizes are small when Hm = 0? guard)
                    if len(L[0]) * len(L[1]) * len(L[2]) * len(L[3]) <= 200000:
                        for c4 in itertools.product(*L):
                            Hs = sum(rows[i]["a"] for i in c4)
                            Is = sum(TS[s_] * rows[i]["w"] + rows[i]["wIU"] for s_, i in enumerate(c4))
                            if Is > 0 and Hs / Is > best_ratio:
                                best_ratio, best_ratio_combo = Hs / Is, list(c4)
                            if Hs - CST * Is > -1e-9 and Is > 0:
                                near_zero.append(list(c4))
                            ps_ = sum(phival(rows[i], TS[s_]) for s_, i in enumerate(c4))
                            if ps_ > -1e-9 and Is > 0:
                                near_phi.append(list(c4))
                    else:
                        raise RuntimeError("unexpectedly large Hm = 0 block")
                    continue
                # Hm != 0: sign coupling p0 ^ p1 ^ p2 ^ p3 == Hm
                bypat = [defaultdict(list) for _ in range(4)]
                for slot in range(4):
                    for i in L[slot]:
                        bypat[slot][pattern(rows[i], Hm)].append(i)
                for P0, l0 in bypat[0].items():
                    for P1, l1 in bypat[1].items():
                        for P2, l2 in bypat[2].items():
                            P3 = P0 ^ P1 ^ P2 ^ Hm
                            l3 = bypat[3].get(P3)
                            if not l3:
                                continue
                            count += len(l0) * len(l1) * len(l2) * len(l3)
                            for c4 in itertools.product(l0, l1, l2, l3):
                                dsum = sum(dval(rows[i], TS[s_]) for s_, i in enumerate(c4))
                                psum = sum(phival(rows[i], TS[s_]) for s_, i in enumerate(c4))
                                Hs = sum(rows[i]["a"] for i in c4)
                                Is = sum(TS[s_] * rows[i]["w"] + rows[i]["wIU"] for s_, i in enumerate(c4))
                                if dsum > best_d:
                                    best_d, best_d_combo = dsum, list(c4)
                                if psum > best_phi:
                                    best_phi, best_phi_combo = psum, list(c4)
                                if Is > 0 and Hs / Is > best_ratio:
                                    best_ratio, best_ratio_combo = Hs / Is, list(c4)
                                if dsum > -1e-9:
                                    near_zero.append(list(c4))
                                if psum > -1e-9:
                                    near_phi.append(list(c4))
print("K2 functions with address pair (0,1) at n=5:", count, f"{time.time()-t0:.1f}s", flush=True)
print("max (H - c* I) float:", best_d, " max Phi float:", best_phi, " max H/I:", best_ratio, flush=True)

def build_f(c4):
    """reconstruct f(y,x) from the four rows; index z = y1 + 2 y2 + 4 x  (bits)"""
    f = []
    for z in range(1 << n):
        y1 = -1 if z & 1 else 1
        y2 = -1 if (z >> 1) & 1 else 1
        x = z >> 2
        val = Fraction(0)
        chis = [1, y1, y2, y1 * y2]
        for s_, i in enumerate(c4):
            val += Fraction(int(rows[i]["v"][x]), 2) * chis[s_]
        f.append(val)
    return f

# exact checks of the near-zero combos
exact_zero = 0
for c4 in near_zero:
    f = build_f(c4)
    assert all(v in (1, -1) for v in f)
    W = walsh_int(np.array([int(v) for v in f], dtype=np.int64))
    Q, _ = H_minus_cI_exact(W, n)
    sg = Q.sign()
    assert sg <= 0, ("VIOLATION", c4)
    if sg == 0:
        exact_zero += 1
print("near-zero combos:", len(near_zero), " exact equality cases:", exact_zero, flush=True)

# exact Phi at the Phi maximiser and at every combo with float Phi > -1e-9
def exact_phi(c4):
    Phi = LogLin()
    for s_, i in enumerate(c4):
        R = rows[i]
        if R["an"] is None:
            continue
        Phi.add(R["an"]["web"])
        Phi.add(LogLin(Fraction(16, 3), {3: Fraction(-3, 2)}), -TS[s_] * R["an"]["w"])
    return Phi
Phi = exact_phi(best_phi_combo)
print("exact sign of Phi at its maximiser:", Phi.sign(), " value", float(Phi), flush=True)
phi_pos = 0
phi_zero = 0
for c4 in near_phi:
    sg = exact_phi(c4).sign()
    if sg > 0:
        phi_pos += 1
    elif sg == 0:
        phi_zero += 1
print("combos with float Phi > -1e-9:", len(near_phi), " exact Phi > 0:", phi_pos, " exact Phi = 0:", phi_zero, flush=True)

# random reconstruction cross-check: rebuild f, check Boolean, recheck K2 membership with the generic test
random.seed(1)
samples = 0
for Hm in random.sample(Hms, min(len(Hms), 40)):
    pass
allrows_ids = list(range(len(rows)))
for c4 in random.sample(near_zero, min(50, len(near_zero))) + [best_d_combo, best_phi_combo, best_ratio_combo]:
    f = build_f(c4)
    W = walsh_int(np.array([int(v) for v in f], dtype=np.int64))
    assert in_K(W, n, (0, 1)), "reconstructed function not in K2"
    samples += 1
print("reconstruction cross-checks passed:", samples, f"{time.time()-t0:.1f}s", flush=True)
out = dict(product_rows=len(prod_rows), count=count, max_HmcI=best_d, max_Phi=best_phi, max_ratio=best_ratio,
           near_zero=len(near_zero), exact_equalities=exact_zero, argmax_ratio_f=[int(v) for v in build_f(best_ratio_combo)])
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "ref_enum_n5.json", "w", encoding="utf-8"), indent=1)
