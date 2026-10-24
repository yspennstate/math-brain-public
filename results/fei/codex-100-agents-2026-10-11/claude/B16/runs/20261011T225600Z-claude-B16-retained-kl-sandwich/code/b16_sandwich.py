"""B16 lead check: retained-KL sandwich, A076 tribes spectra, A077 point-defect ledger, majority Lambda_T.

Frozen spec (written before running): helper b16_sandwich v1; families: all Boolean functions on n<=4 variables
(65,536 at n=4, exhaustive, complete coordinate trees, lowest-bit-first order = every order up to relabelling),
tribes (w,t) in {(1,2),(2,2),(2,3),(3,2),(2,4),(3,3)}, point defects n=2..12, odd majority n in {5,9,17,33,65,129,257,513};
arithmetic: integer FWHT and exact integer/Fraction identities; logarithms in float64 (evidence only, tolerance 1e-11);
no randomness; memory estimate < 150 MB; max runtime 5 minutes. No escalation of n.
"""
import json, math, sys, time
from fractions import Fraction
from math import comb, log2
import numpy as np

LN2 = math.log(2.0)
TOL = 1e-11
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
t0 = time.time()
report = {}

def fwht(a):
    """integer Walsh-Hadamard along last axis; a: (N, 2^m) int64. Returns sum_x a(x)(-1)^{S.x}."""
    a = a.astype(np.int64).copy()
    n = a.shape[-1]
    h = 1
    while h < n:
        a = a.reshape(a.shape[0], -1, 2, h)
        x = a[:, :, 0, :].copy(); y = a[:, :, 1, :].copy()
        a[:, :, 0, :] = x + y; a[:, :, 1, :] = x - y
        a = a.reshape(a.shape[0], n)
        h *= 2
    return a

def ent_rows(p):
    """Shannon entropy in bits of each row of a probability array."""
    with np.errstate(divide="ignore", invalid="ignore"):
        t = np.where(p > 0, -p * np.log2(np.where(p > 0, p, 1.0)), 0.0)
    return t.sum(axis=1)

def node_stats(sub):
    """sub: (K, 2^m) +-1 truth tables; queried coordinate = lowest index bit. Returns dict of per-node arrays."""
    K, L = sub.shape
    m = int(round(math.log2(L)))
    g = sub[:, 0::2]; h = sub[:, 1::2]
    A = fwht(g); Bh = fwht(h)                   # = 2^{m-1} * child coefficients
    U2 = (A + Bh) ** 2; V2 = (A - Bh) ** 2       # = 2^{2m} * parent squares u_T^2, v_T^2
    scale = float(2 ** (2 * m))
    cnt = (g != h).sum(axis=1).astype(np.int64)  # Inf * 2^{m-1}
    mins = np.minimum(U2, V2)
    # exact identities (integers)
    pars = (U2 + V2).sum(axis=1)
    ok_pars = bool(np.all(pars == 2 ** (2 * m)))
    ok_M_identity = bool(np.all(2 * mins.sum(axis=1) == 2 ** (2 * m) - np.abs(U2 - V2).sum(axis=1)))
    jcnt = np.minimum(cnt, 2 ** (m - 1) - cnt)
    ok_M_le_j = bool(np.all(mins.sum(axis=1) <= (2 ** (m + 1)) * jcnt))
    # floats
    q = (U2 + V2) / scale; mm = mins / scale
    with np.errstate(divide="ignore", invalid="ignore"):
        Qterm = np.where(mm > 0, mm * np.log2(np.where(mm > 0, q / np.where(mm > 0, mm, 1.0), 1.0)), 0.0)
        rest = q - mm
        Rterm = np.where(rest > 0, rest * np.log2(np.where(rest > 0, q / np.where(rest > 0, rest, 1.0), 1.0)), 0.0)
    Qv = Qterm.sum(axis=1); Bv = Qv + Rterm.sum(axis=1)
    M = mins.sum(axis=1) / scale
    Inf = cnt / float(2 ** (m - 1)); j = jcnt / float(2 ** (m - 1))
    P = (A.astype(float) / 2 ** (m - 1)) ** 2; Qc = (Bh.astype(float) / 2 ** (m - 1)) ** 2
    Hg = ent_rows(P); Hh = ent_rows(Qc); Hmix = ent_rows((P + Qc) / 2)
    JS = Hmix - (Hg + Hh) / 2
    Fpar = np.concatenate([U2, V2], axis=1) / scale
    Hf = ent_rows(Fpar)
    Delta = Hf - (Hg + Hh) / 2
    kap = np.minimum(1 - P.max(axis=1), 1 - Qc.max(axis=1))
    with np.errstate(divide="ignore", invalid="ignore"):
        Lam = np.where(j > 0, j * np.log2(1 + kap / (2 * np.where(j > 0, j, 1.0))), 0.0)
        Rblind = np.where(M > 0, M * np.log2(1 / np.where(M > 0, M, 1.0)), 0.0)
    viol = {
        "Delta_minus_B_minus_JS_abs": float(np.max(np.abs(Delta - Bv - JS))) if K else 0.0,
        "Q_minus_B": float(np.max(Qv - Bv)) if K else 0.0,
        "B_minus_Q_minus_M_over_ln2": float(np.max(Bv - Qv - M / LN2)) if K else 0.0,
        "JS_minus_2M_over_ln2": float(np.max(JS - 2 * M / LN2)) if K else 0.0,
        "Q_minus_Delta": float(np.max(Qv - Delta)) if K else 0.0,
        "Delta_minus_Q_minus_3M_over_ln2": float(np.max(Delta - Qv - 3 * M / LN2)) if K else 0.0,
    }
    return dict(m=m, cnt=cnt, Q=Qv, B=Bv, M=M, Inf=Inf, j=j, JS=JS, Delta=Delta, Hf=Hf, Lam=Lam, R=Rblind,
                ok=dict(parseval=ok_pars, M_identity=ok_M_identity, M_le_j=ok_M_le_j), viol=viol)

def complete_tree(tt):
    """tt: (N, 2^n) +-1. Complete tree querying bit 0,1,...,n-1. Returns per-function sums and checks."""
    N, L = tt.shape
    n = int(round(math.log2(L)))
    F = fwht(tt)
    pf = (F.astype(float) / L) ** 2
    H = ent_rows(pf)
    deg = np.array([bin(s).count("1") for s in range(L)], dtype=np.int64)
    I2n = (F ** 2 * deg[None, :]).sum(axis=1)          # I * 2^{2n}, exact
    sums = {k: np.zeros(N) for k in ["Delta", "Q", "B", "M", "Lam", "R", "JS"]}
    cnt_sum = np.zeros(N, dtype=np.int64)               # sum over nodes of cnt -> I * 2^{n-1}
    okall = dict(parseval=True, M_identity=True, M_le_j=True)
    vmax = {}
    stopped_err = 0.0
    partial_Delta = np.zeros(N)
    for d in range(n):
        sub = tt.reshape(N, 2 ** (n - d), 2 ** d).transpose(0, 2, 1).reshape(N * 2 ** d, 2 ** (n - d))
        # stopped-tree identity at uniform depth d: H = sum_{depth<d} w Delta + E H(sub at depth d)
        Fs = fwht(sub); ps = (Fs.astype(float) / 2 ** (n - d)) ** 2
        EH = ent_rows(ps).reshape(N, 2 ** d).mean(axis=1)
        stopped_err = max(stopped_err, float(np.max(np.abs(H - partial_Delta - EH))))
        st = node_stats(sub)
        for k2, v in st["ok"].items():
            okall[k2] = okall[k2] and v
        for k2, v in st["viol"].items():
            vmax[k2] = max(vmax.get(k2, -1e9), v)
        w = 2.0 ** (-d)
        for k in sums:
            sums[k] += w * st[k].reshape(N, 2 ** d).sum(axis=1)
        partial_Delta += w * st["Delta"].reshape(N, 2 ** d).sum(axis=1)
        cnt_sum += st["cnt"].reshape(N, 2 ** d).sum(axis=1)
    ok_I_telescope = bool(np.all(cnt_sum * 2 ** (n + 1) == I2n))
    I = I2n / float(2 ** (2 * n))
    tele_err = float(np.max(np.abs(H - sums["Delta"])))
    sand_low = float(np.max(sums["Q"] - H))                         # must be <= 0
    sand_high = float(np.max(H - sums["Q"] - 3 * sums["M"] / LN2))   # must be <= 0
    M_le_I = bool(np.all(sums["M"] <= I + 1e-12))
    return dict(n=n, N=N, H=H, I=I, sums=sums, ok=okall, vmax=vmax, ok_I_telescope=ok_I_telescope,
                tele_err=tele_err, stopped_err=stopped_err, sand_low=sand_low, sand_high=sand_high, M_le_I=M_le_I)

# ---------------- Part 1: exhaustive n <= 4 ----------------
part1 = {}
for n in range(1, 5):
    L = 2 ** n
    N = 2 ** L
    idx = np.arange(N, dtype=np.int64)[:, None]
    bits = (idx >> np.arange(L, dtype=np.int64)[None, :]) & 1
    tt = (1 - 2 * bits).astype(np.int64)
    r = complete_tree(tt)
    ratio = np.where(r["I"] > 0, r["sums"]["Q"] / np.where(r["I"] > 0, r["I"], 1.0), 0.0)
    hratio = np.where(r["I"] > 0, r["H"] / np.where(r["I"] > 0, r["I"], 1.0), 0.0)
    part1[n] = dict(functions=int(N), exact_ok=r["ok"], I_telescope_exact=r["ok_I_telescope"],
                    max_violations_per_node=r["vmax"], H_telescope_err=r["tele_err"], stopped_tree_err=r["stopped_err"],
                    max_Qtree_minus_H=r["sand_low"], max_H_minus_Qtree_minus_3Mtree_over_ln2=r["sand_high"],
                    Mtree_le_I=r["M_le_I"], max_H_over_I=float(hratio.max()), max_Qtree_over_I=float(ratio.max()),
                    max_Lambda_over_I=float(np.max(np.where(r["I"] > 0, r["sums"]["Lam"] / np.where(r["I"] > 0, r["I"], 1.0), 0.0))))
report["part1_exhaustive"] = part1

# ---------------- Part 2: A076 tribes ----------------
part2 = []
for (w, t) in [(1, 2), (2, 2), (2, 3), (3, 2), (2, 4), (3, 3)]:
    n = w * t; L = 2 ** n
    xs = np.arange(L, dtype=np.int64)
    fires = np.zeros(L, dtype=bool)
    for jt in range(t):
        mask = ((1 << w) - 1) << (jt * w)
        fires |= (xs & mask) == mask
    f = np.where(fires, -1, 1).astype(np.int64)[None, :]
    F = fwht(f)[0]
    sq = sorted(Fraction(int(v) ** 2, L * L) for v in F)
    q = Fraction(1, 2 ** w); b = 1 - q; a = b ** t
    pred = [(2 * a - 1) ** 2]
    for k in range(1, t + 1):
        pred += [4 * q ** (2 * k) * b ** (2 * (t - k))] * (comb(t, k) * (2 ** w - 1) ** k)
    pred = sorted(pred)
    deg = np.array([bin(s).count("1") for s in range(L)])
    I = sum(Fraction(int(F[s]) ** 2 * int(deg[s]), L * L) for s in range(L))
    Ipred = 2 * t * w * q * b ** (t - 1)
    Hbf = -sum(float(c) * log2(float(c)) for c in sq if c > 0)
    Hf = -sum(float(c) * log2(float(c)) for c in pred if c > 0)
    part2.append(dict(w=w, t=t, n=n, multiset_exact=(sq == pred), I_exact=str(I), I_pred=str(Ipred), I_ok=(I == Ipred),
                      H_bruteforce=Hbf, H_formula=Hf, H_abs_diff=abs(Hbf - Hf)))
report["part2_tribes_A076"] = part2

# ---------------- Part 3: A077 point defect ----------------
part3 = []
for n in range(2, 13):
    L = 2 ** n
    f = np.ones((1, L), dtype=np.int64); f[0, 0] = -1
    r = complete_tree(f)
    R = float(r["sums"]["R"][0]); Q = float(r["sums"]["Q"][0]); I = float(r["I"][0]); H = float(r["H"][0])
    part3.append(dict(n=n, I=I, I_pred=2 * n * 2.0 ** (-n), R=R, R_pred=2.0 ** (-n) * n * (n - 1), R_over_I=R / I,
                      Q_over_I=Q / I, H_over_I=H / I, Q_le_2I=(Q <= 2 * I + 1e-12),
                      exact_ok=r["ok"], I_telescope_exact=r["ok_I_telescope"], vmax=r["vmax"]))
report["part3_point_defect_A077"] = part3

# ---------------- Part 4: odd majority Lambda_T ----------------
def thr_stats(t, mp, pref):
    """child c(y)=sign(t+sum_{mp} y), parity t+mp odd. Returns (Ec as Fraction, max_j Inf_j as Fraction).
    pref[W] = sum_{w<=W} C(mp,w)."""
    if mp == 0:
        return Fraction(1 if t > 0 else -1), Fraction(0)
    assert (t + mp) % 2 == 1
    # Pr[sum > -t] - Pr[sum < -t]; sum = mp - 2w (w = number of -1's); sum > -t  <=>  w <= (mp+t-1)/2
    W = (mp + t - 1) // 2
    pos = 0 if W < 0 else ((1 << mp) if W >= mp else pref[W])
    neg = (1 << mp) - pos
    Ec = Fraction(pos - neg, 1 << mp)
    if abs(t) <= mp - 1 and (mp - 1 - t) % 2 == 0:
        infc = Fraction(comb(mp - 1, (mp - 1 - t) // 2), 1 << (mp - 1))
    else:
        infc = Fraction(0)
    return Ec, infc

def kraw_table(m):
    """E[k][w] = sum_{|x|=w} chi_S(x) for |S|=k: coefficients of (1-z)^k (1+z)^(m-k)."""
    rows = []
    poly = [comb(m, w) for w in range(m + 1)]  # k=0
    rows.append(poly[:])
    for k in range(1, m + 1):
        # divide by (1+z), multiply by (1-z)
        r = [0] * m
        r[0] = poly[0]
        for i in range(1, m):
            r[i] = poly[i] - r[i - 1]
        newp = [0] * (m + 1)
        for i in range(m):
            newp[i] += r[i]; newp[i + 1] -= r[i]
        poly = newp
        rows.append(poly[:])
    return rows

def thr_maxcoef_exact(t, mp, E):
    vals = [1 if (mp - 2 * ww + t) > 0 else -1 for ww in range(mp + 1)]
    best = Fraction(0)
    for k in range(mp + 1):
        s = sum(vals[ww] * E[k][ww] for ww in range(mp + 1))
        c = Fraction(s * s, 1 << (2 * mp))
        if c > best:
            best = c
    return best

part4 = []
kr_cache = {}
for n in [5, 9, 17, 33, 65, 129, 257, 513]:
    exact_kappa = n <= 33
    Lam_lo = Lam_hi = Lam_skip_lo = 0.0
    Isum = Fraction(0)
    Iskip = Fraction(0)
    kappa_checks = 0; kappa_level01 = 0
    for d in range(n):
        m = n - d
        pref = []; acc = 0
        for ww in range(m):
            acc += comb(m - 1, ww); pref.append(acc)
        for s in range(-d, d + 1, 2):
            if abs(s) > m - 1:
                continue
            Pds = Fraction(comb(d, (d + s) // 2), 1 << d)
            Inf = Fraction(comb(m - 1, (m - 1 - s) // 2), 1 << (m - 1))
            if Inf == 0:
                continue
            j = min(Inf, 1 - Inf)
            Isum += Pds * Inf
            kl = []; ku = []
            for tch in (s + 1, s - 1):
                Ec, infc = thr_stats(tch, m - 1, pref)
                lo = 1 - max(Ec * Ec, infc)          # rigorous lower bound on kappa(child)
                hi = 1 - max(Ec * Ec, infc * infc)   # value if the max coefficient sits at level <= 1
                if exact_kappa:
                    if (m - 1) not in kr_cache:
                        kr_cache[m - 1] = kraw_table(m - 1)
                    kex = 1 - thr_maxcoef_exact(tch, m - 1, kr_cache[m - 1])
                    kappa_checks += 1
                    assert lo <= kex <= hi, (n, d, s, tch)
                    if kex == hi:
                        kappa_level01 += 1
                kl.append(lo); ku.append(hi)
            kmin_lo = max(Fraction(0), min(kl)); kmin_hi = min(ku)
            wj = float(Pds * j); jf = float(j)
            if j == 0:   # Inf = 1 (a dictator node, children are -+ each other): epsilon = 0, Lambda term 0
                term_lo = term_hi = 0.0
            else:
                term_lo = wj * log2(1 + float(kmin_lo) / (2 * jf))
                term_hi = wj * log2(1 + float(kmin_hi) / (2 * jf))
            Lam_lo += term_lo; Lam_hi += term_hi
            if s != 0:
                Lam_skip_lo += term_lo
            else:
                Iskip += Pds * Inf
    Iex = Fraction(n * comb(n - 1, (n - 1) // 2), 1 << (n - 1))
    # exact spectrum of Maj_n via Krawtchouk at the root
    E = kraw_table(n)
    vals = [1 if (n - 2 * ww) > 0 else -1 for ww in range(n + 1)]
    H = 0.0; Wtot = Fraction(0)
    for k in range(n + 1):
        s_ = sum(vals[ww] * E[k][ww] for ww in range(n + 1))
        c = Fraction(s_ * s_, 1 << (2 * n))
        Wtot += comb(n, k) * c
        if c > 0:
            H -= comb(n, k) * float(c) * log2(float(c))
    If = float(Iex)
    part4.append(dict(n=n, I=If, I_telescope_exact=(Isum == Iex), parseval_exact=(Wtot == 1), H_over_I=H / If,
                      Lambda_lower_over_I=Lam_lo / If, Lambda_upper_over_I=Lam_hi / If,
                      Lambda_skip_lower_over_I=Lam_skip_lo / If, isospectral_skip_share_of_I=float(Iskip / Iex),
                      Lambda_lower_over_I_minus_half_log2n=Lam_lo / If - 0.5 * log2(n),
                      kappa_exact_checked_nodes=kappa_checks, kappa_max_at_level_le_1=kappa_level01))
report["part4_majority_Lambda"] = part4
report["runtime_s"] = time.time() - t0

with open(f"{OUT}/b16_sandwich_results.json", "w", encoding="utf-8") as fh:
    json.dump(report, fh, indent=1, default=str)
print(json.dumps(report, indent=1, default=str))
