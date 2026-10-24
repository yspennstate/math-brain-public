"""B18 lead exhaustive n=4 audit (all 65536 Boolean sign tables on 4 uniform bits).
Checks, per function f and coordinate i:
  (A082) min over relevant i of B_i/Inf_i <= Kstar = 4 + 2.5 log2 5 - 4.5 log2 3, and Kstar attained.
  (A026) same with 7/2 (weaker).
  (A061) D_i = B_i + JS_i <= lambda_i + (3/ln2) Inf_i.
  (A031) p_R (H - ell_R)^2 <= J_R * E_log for every occupied R; sum_{U!=0} c_U^2 = Var_p(ell).
  (A067) fhat(S) * 2^(d_f(S)-1) integer; H <= 2I + 2U - (2 - log2 e) v.
  (A032) laws with support size <= 4: singleton, or uniform 1/4 on an affine 2-flat.
Floating point (float64) with an explicit error budget; near-extremal A082 cases are redone exactly
(rational coefficients of log2 of primes) so the extremal equality is exact.
Frozen spec: domain = all 2^16 tables on n=4; symmetry = none (full enumeration); memory < 200 MB; runtime < 2 min.
"""
import numpy as np, itertools, math, json, sys
from fractions import Fraction
n = 4; N = 1 << n
out = {}
# truth tables: row t of tables, bit x -> f(x) = (-1)^{bit}
tabs = ((np.arange(1 << N)[:, None] >> np.arange(N)[None, :]) & 1).astype(np.int64)
F = 1 - 2 * tabs                              # 65536 x 16 signs
# characters chi_S(x) = (-1)^{|S & x|}
pc = np.array([bin(i).count('1') for i in range(N)])
CH = np.array([[(-1) ** pc[s & x] for x in range(N)] for s in range(N)], dtype=np.int64)
W = F @ CH.T                                  # integer Walsh sums, fhat = W/16
a = W / N
p = a * a
nonconst = ~np.all(F == F[:, :1], axis=1)

def ent(P):
    with np.errstate(divide='ignore', invalid='ignore'):
        t = np.where(P > 0, -P * np.log2(np.where(P > 0, P, 1)), 0.0)
    return t.sum(axis=-1)

H = ent(p)
size = pc
I = (p * size[None, :]).sum(axis=1)
Kstar = 4 + 2.5 * math.log2(5) - 4.5 * math.log2(3)
LOG2E = 1 / math.log(2)
minratio = np.full(len(F), np.inf)
viol061 = 0; max061 = -np.inf
for i in range(n):
    bit = 1 << i
    T = np.array([s for s in range(N) if not s & bit])
    pa = p[:, T]; pb = p[:, T | bit]
    m = pa + pb
    with np.errstate(divide='ignore', invalid='ignore'):
        xb = np.where(m > 0, pb / np.where(m > 0, m, 1), 0)
        h2 = np.where((xb > 0) & (xb < 1), -xb * np.log2(np.where(xb > 0, xb, 1)) - (1 - xb) * np.log2(np.where(xb < 1, 1 - xb, 1)), 0)
        Bi = (m * h2).sum(axis=1)
        lam = np.where(pb > 0, pb * np.log2(np.where(pb > 0, m / np.where(pb > 0, pb, 1), 1)), 0).sum(axis=1)
    Inf = pb.sum(axis=1)
    aa = a[:, T]; bb = a[:, T | bit]
    JS = ent(m) - 0.5 * (ent((aa + bb) ** 2) + ent((aa - bb) ** 2))
    D = Bi + JS
    slack = lam + 3 * LOG2E * Inf - D
    viol061 += int((slack < -1e-9).sum()); max061 = max(max061, float((D - lam - 3 * LOG2E * Inf).max()))
    rel = Inf > 0
    r = np.where(rel, Bi / np.where(rel, Inf, 1), np.inf)
    minratio = np.minimum(minratio, r)
mr = minratio[nonconst]
out['A082_n4_max_min_ratio_float'] = float(mr.max())
out['A082_Kstar'] = Kstar
out['A082_max_minus_Kstar'] = float(mr.max() - Kstar)
out['A082_count_within_1e-8_of_Kstar'] = int((mr > Kstar - 1e-8).sum())
out['A082_count_above_Kstar_plus_1e-8'] = int((mr > Kstar + 1e-8).sum())
out['A026_count_min_ratio_above_3.5'] = int((mr > 3.5).sum())
srt = np.unique(np.round(mr, 9))[::-1][:6]
out['A082_top_distinct_values'] = [float(x) for x in srt]
out['A061_violations'] = viol061
out['A061_max_of_D_minus_bound'] = max061
# exact recheck of near-extremal functions for A082
def factor_log(q):  # q positive Fraction -> dict prime->exponent (log2 q = sum e*log2 p)
    d = {}
    for val, sgn in ((q.numerator, 1), (q.denominator, -1)):
        v = val; pr = 2
        while v > 1:
            while v % pr == 0:
                d[pr] = d.get(pr, 0) + sgn; v //= pr
            pr += 1
    return d
def exact_Bi_over_Inf(wrow, i):
    bit = 1 << i
    tot = {}; Inf = Fraction(0)
    for s in range(N):
        if s & bit: continue
        pa = Fraction(int(wrow[s]) ** 2, N * N); pb = Fraction(int(wrow[s | bit]) ** 2, N * N)
        Inf += pb
        mm = pa + pb
        for x in (pa, pb):
            if x > 0 and x < mm:  # x log2(m/x)
                for pr, e in factor_log(mm / x).items():
                    tot[pr] = tot.get(pr, Fraction(0)) + x * e
    return tot, Inf
near = np.where(nonconst & (minratio > Kstar - 1e-8))[0]
exact_list = []
Kd = {2: Fraction(4), 5: Fraction(5, 2), 3: Fraction(-9, 2)}
for idx in near[:200]:
    best = None
    for i in range(n):
        tot, Inf = exact_Bi_over_Inf(W[idx], i)
        if Inf == 0: continue
        ratio = {k: v / Inf for k, v in tot.items() if v != 0}
        val = sum(float(v) * math.log2(k) for k, v in ratio.items())
        if best is None or val < best[0]: best = (val, ratio, i)
    eq = {k: v for k, v in best[1].items()} == {k: v for k, v in Kd.items()}
    exact_list.append({'table': int(idx), 'truth': ''.join('1' if b else '0' for b in tabs[idx]), 'coord': best[2], 'ratio_coeffs': {str(k): str(v) for k, v in best[1].items()}, 'equals_Kstar_exactly': bool(eq)})
out['A082_near_extremal_exact'] = exact_list[:12]
out['A082_near_extremal_all_equal_Kstar'] = all(e['equals_Kstar_exactly'] for e in exact_list)
# A031
xorix = np.array([[s ^ u for s in range(N)] for u in range(N)])
with np.errstate(divide='ignore'):
    ell = np.where(p > 0, -np.log2(np.where(p > 0, p, 1)), 0.0)
L = a * ell
c = np.stack([(L * a[:, xorix[u]]).sum(axis=1) for u in range(N)], axis=1)
Elog = (c[:, 1:] ** 2 * size[None, 1:]).sum(axis=1)
var_ell = (p * ell ** 2).sum(axis=1) - H ** 2
out['A031_parseval_identity_max_abs_err'] = float(np.abs((c[:, 1:] ** 2).sum(axis=1) - var_ell).max())
out['A031_c_empty_equals_H_max_err'] = float(np.abs(c[:, 0] - H).max())
worst031 = -np.inf; viol031 = 0
for R in range(N):
    JR = sum(p[:, R ^ u] / size[u] for u in range(1, N))
    lhs = p[:, R] * (H - ell[:, R]) ** 2
    rhs = JR * Elog
    occ = p[:, R] > 0
    diff = np.where(occ, lhs - rhs, -np.inf)
    viol031 += int((diff > 1e-9).sum()); worst031 = max(worst031, float(diff.max()))
out['A031_violations'] = viol031; out['A031_max_lhs_minus_rhs'] = worst031
# A067
gran_viol = 0; bound_viol = 0; worst067 = -np.inf
sup = p > 0
for S in range(N):
    sups = [T for T in range(N) if T & S == S]
    dS = np.max(np.stack([np.where(sup[:, T], size[T], -1) for T in sups], axis=1), axis=1)
    ok = ~sup[:, S] | (np.mod(W[:, S] * (2.0 ** (dS - 1)) / N, 1.0) == 0)
    gran_viol += int((~ok).sum())
U = np.zeros(len(F))
for S in range(1, N):
    sups = [T for T in range(N) if T & S == S]
    dS = np.max(np.stack([np.where(sup[:, T], size[T], -1) for T in sups], axis=1), axis=1)
    U += np.where(sup[:, S], p[:, S] * (dS - size[S]), 0)
v = 1 - p[:, 0]
b067 = 2 * I + 2 * U - (2 - LOG2E) * v
d067 = np.where(nonconst, H - b067, -np.inf)
out['A067_granularity_violations'] = gran_viol
out['A067_bound_violations'] = int((d067 > 1e-9).sum()); out['A067_max_H_minus_bound'] = float(d067.max())
# A032
spars = sup.sum(axis=1)
laws = {}
bad032 = 0
for idx in np.where(spars <= 4)[0]:
    S = np.where(sup[idx])[0]
    vals = sorted(set(np.round(p[idx, S], 12)))
    k = len(S)
    if k == 1: kind = 'singleton'
    elif k == 4 and vals == [0.25] and (S[0] ^ S[1] ^ S[2] ^ S[3]) == 0: kind = 'uniform_affine_2flat'
    else: kind = 'OTHER'; bad032 += 1
    laws[kind] = laws.get(kind, 0) + 1
out['A032_sparsity_le4_kinds'] = laws; out['A032_other_count'] = bad032
out['sparsity_histogram'] = {int(k): int(v) for k, v in zip(*np.unique(spars, return_counts=True))}
json.dump(out, open(sys.argv[1], 'w'), indent=1)
print(json.dumps({k: v for k, v in out.items() if k != 'A082_near_extremal_exact'}, indent=0))
print(json.dumps(out['A082_near_extremal_exact'][:3]))
