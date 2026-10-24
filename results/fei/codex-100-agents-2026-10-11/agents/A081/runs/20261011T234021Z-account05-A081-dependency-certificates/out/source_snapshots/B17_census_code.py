# Exhaustive exact census of all 65,536 Boolean functions on 4 uniform bits.
# This covers every Boolean function with at most 4 relevant coordinates (an embedding
# into more bits changes no H, I_i, B_i or Delta_i H).  Units: bits, uniform measure,
# f: {0,1}^4 -> {-1,+1},  W_S = sum_x f(x) (-1)^{S.x} = 16 fhat(S),  q_S = W_S^2 (sum 256).
#   256 H       = 2048 - sum_S q_S log2 q_S
#   256 I_i     = sum_{S contains i} q_S
#   256 B_i     = sum_{T not i} [(a+b)log2(a+b) - a log2 a - b log2 b], a=q_T, b=q_{T+i}
#   256 Delta_i = 512 - sum q log2 q + 2 sum w0^2 log2 w0^2 + 2 sum w1^2 log2 w1^2,
#                 w0, w1 = (W_T +- W_{T+i})/2 the Walsh integers of the two restrictions.
# Certified quantities:  K_B(4) = max_f min_{i relevant} B_i/I_i,
#   K_D(4) = max_f min_{i relevant} Delta_i H / I_i,  C(4) = max_f H/I,  max_f B/I.
# Each comparison is the exact sign of an integer linear form in log2 p, p <= 256 prime.
import sys, os, json, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from certlog import LinLog
from fractions import Fraction

T0 = time.time()
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'out')
LL = LinLog(256); P = LL.P; NP = len(P); I2 = LL.idx[2]
Vtab = np.zeros((257, NP), dtype=np.int64)
for m in range(1, 257):
    Vtab[m] = np.array(LL.vexp(m), dtype=np.int64) * m

n, N = 4, 16
pc = np.array([bin(v).count('1') for v in range(N)])
Hm = np.array([[(-1) ** int(pc[x & S]) for S in range(N)] for x in range(N)], dtype=np.int64)
tt = np.arange(1 << N, dtype=np.int64)
F = 1 - 2 * ((tt[:, None] >> np.arange(N)[None, :]) & 1)
W = F @ Hm
q = W * W
assert (q.sum(1) == N * N).all()
VQ = np.zeros((len(tt), NP), dtype=np.int64)
for S in range(N):
    VQ += Vtab[q[:, S]]
EH = -VQ.copy(); EH[:, I2] += 2048
DI = q @ pc
nonconst = DI > 0
EB = np.zeros((4, len(tt), NP), dtype=np.int64); ED = np.zeros_like(EB)
D = np.zeros((4, len(tt)), dtype=np.int64)
for i in range(n):
    bit = 1 << i
    Ts = [T for T in range(N) if not T & bit]
    D[i] = q[:, [T | bit for T in Ts]].sum(1)
    acc = np.zeros((len(tt), NP), dtype=np.int64); c0 = np.zeros_like(acc); c1 = np.zeros_like(acc)
    for T in Ts:
        a, b = q[:, T], q[:, T | bit]
        acc += Vtab[a + b] - Vtab[a] - Vtab[b]
        s0 = W[:, T] + W[:, T | bit]; s1 = W[:, T] - W[:, T | bit]
        assert ((s0 % 2) == 0).all() and ((s1 % 2) == 0).all()
        w0 = s0 // 2; w1 = s1 // 2
        assert (np.abs(w0) <= 8).all() and (np.abs(w1) <= 8).all()
        c0 += Vtab[w0 * w0]; c1 += Vtab[w1 * w1]
    EB[i] = acc
    E = -VQ + 2 * c0 + 2 * c1; E[:, I2] += 512
    ED[i] = E
lf = LL.logf
Bv = EB @ lf; Dv = ED @ lf; Hv = EH @ lf
JS = Dv - Bv; Ii = D / 256.0
checks = {
    'min_JS_over_all (>= 0 expected)': float(JS.min() / 256),
    'max_JS_minus_2ln2_min(I,1-I) (<= 0 expected)': float((JS / 256 - (2 / np.log(2)) * np.minimum(Ii, 1 - Ii)).max()),
    'max_sumB_minus_H (<= 0 expected)': float(((Bv.sum(0) - Hv) / 256).max()),
    'max |B_i| on irrelevant i (0 expected)': float(np.abs(np.where(D == 0, Bv, 0)).max()),
}
rel = D > 0
rB = np.where(rel, Bv / np.where(rel, D, 1), np.inf)
rD = np.where(rel, Dv / np.where(rel, D, 1), np.inf)
minB = rB.min(0); minD = rD.min(0)
idx = np.nonzero(nonconst)[0]
HI = np.full(len(tt), -1.0); HI[idx] = Hv[idx] / DI[idx]
BI = np.full(len(tt), -1.0); BI[idx] = Bv.sum(0)[idx] / DI[idx]

def describe(t):
    f = [int(1 - 2 * ((int(t) >> x) & 1)) for x in range(N)]
    return {'truth_table_int': int(t), 'points_x_with_f_minus1': [x for x in range(N) if f[x] == -1],
            'relevant_coords': [i for i in range(4) if D[i, t] > 0],
            'walsh_W_S_for_S_0_to_15': [int(v) for v in W[t]]}

def certify_max(Esel, Dsel, Estar, Dstar, idx_sel):
    """For every row: Esel.log/Dsel <= Estar.log/Dstar, i.e. Dstar*Esel - Dsel*Estar <= 0."""
    e = Dstar * Esel - Dsel[:, None] * Estar[None, :]
    sg, val = LL.float_screen(e)
    sgn = sg.astype(np.int64)
    und = np.nonzero(sg == 0)[0]
    for k in und:
        sgn[k] = LL.sign(e[k])
    viol = np.nonzero(sgn > 0)[0]; eq = np.nonzero(sgn == 0)[0]
    return {'rows_checked': int(len(e)), 'violations': int(len(viol)), 'equality_cases': int(len(eq)),
            'rows_needing_exact_fallback': int(len(und)),
            'equality_truth_tables_first12': [int(idx_sel[k]) for k in eq[:12]]}

def form_str(Estar, Dstar):
    return {str(P[k]): str(Fraction(int(Estar[k]), Dstar)) for k in range(NP) if Estar[k] != 0}

out = {}
for name, rmat, Emats, best in [('K_B', rB, EB, minB), ('K_D', rD, ED, minD)]:
    tstar = int(idx[np.argmax(best[idx])])
    istar = int(np.argmin(rmat[:, tstar]))
    Estar = Emats[istar, tstar]; Dstar = int(D[istar, tstar])
    sel = np.argmin(rmat[:, idx], axis=0)
    Esel = Emats[sel, idx]; Dsel = D[sel, idx]
    assert (Dsel > 0).all()
    cert = certify_max(Esel, Dsel, Estar, Dstar, idx)
    att = [LL.sign(Emats[i, tstar] * Dstar - D[i, tstar] * Estar) for i in range(4) if D[i, tstar] > 0]
    out[name] = {'float_value': float(best[tstar]), 'argmax': describe(tstar), 'coord': istar,
                 'value_as_sum_coeff_times_log2_p': form_str(Estar, Dstar),
                 'certificate_upper_bound_all_functions': cert,
                 'attained_exactly(all relevant coords of argmax >= value)': all(s >= 0 for s in att),
                 'functions_within_1e-12_of_max': int((np.abs(best[idx] - best[tstar]) < 1e-12).sum())}
for name, vals, Emat_all in [('C_FEI4=max_H/I', HI, EH), ('max_B/I', BI, EB.sum(0))]:
    tstar = int(idx[np.argmax(vals[idx])])
    Estar = Emat_all[tstar]; Dstar = int(DI[tstar])
    cert = certify_max(Emat_all[idx], DI[idx], Estar, Dstar, idx)
    out[name] = {'float_value': float(vals[tstar]), 'argmax': describe(tstar),
                 'value_as_sum_coeff_times_log2_p': form_str(Estar, Dstar),
                 'certificate_upper_bound_all_functions': cert,
                 'functions_within_1e-12_of_max': int((np.abs(vals[idx] - vals[tstar]) < 1e-12).sum())}
kb = out['K_B']; t0 = kb['argmax']['truth_table_int']; i0 = kb['coord']
Estar = EB[i0, t0]; Dstar = int(D[i0, t0])
target = np.zeros(NP, dtype=np.int64); target[LL.idx[2]] = 8; target[LL.idx[5]] = 5; target[LL.idx[3]] = -9
out['K_B']['equals_4+(5/2)log2(5)-(9/2)log2(3)_exactly'] = bool((2 * Estar == Dstar * target).all())
# K_B(4) < 107/40 exactly:  40*Estar.log - 107*Dstar*log2(2) < 0
e = 40 * Estar.copy(); e[I2] -= 107 * Dstar
out['K_B']['strictly_below_107/40'] = LL.sign(e) < 0
# distribution of min_i B_i/I_i (float, for orientation only)
mb = minB[idx]
out['distribution_min_B_ratio_float'] = {thr: int((mb >= thr).sum()) for thr in [0.5, 1.0, 1.5, 2.0, 2.5, 2.6]}
out['functions_with_some_relevant_B_i_equal_0'] = int((np.where(rel, Bv, 1.0)[:, idx] < 1e-12).any(0).sum())
res = {'domain': 'all 65536 truth tables on 4 uniform bits (no symmetry reduction); the 2 constants excluded',
       'nonconstant': int(nonconst.sum()), 'float_sanity_checks': checks, 'results': out,
       'exact_fallback_calls': LL.exact_calls, 'seconds': round(time.time() - T0, 2)}
with open(os.path.join(OUT, 'census_n4.json'), 'w', encoding='utf-8') as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res, indent=1))
