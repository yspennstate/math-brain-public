"""Referee checks of Theorem C (criticality), Corollary C1/C2 ingredients and the random-restriction
inequality U-Han, exhaustively for n <= 4.

For every Boolean f (n <= 4):
  * all physical restrictions g = f_{J,X} (J live set, X assignment of the complement) are enumerated;
  * f is called ratio-critical if H(g)/I(g) <= H(f)/I(f) for every nonconstant restriction g;
  * U-Han: H(f) <= (1/t) E H(f_{J,X}) + (2/ln2)((1-t)/t) I(f), J ~ Binomial(t), X uniform, t in a grid;
  * Theorem C items that only use ratio-criticality are tested on every ratio-critical f:
      (iii) Delta_i H >= c Inf_i,  B_i >= (c - 2/ln2) Inf_i
      (iv)  DTC <= sum_i JS_i <= (2/ln2) J
      (v)   H(S_A|S_C) >= (c - 2/ln2) I_A  and  H(S_C) <= c I_C + (2/ln2) I_A   for every block A
      (viii) (c - 2/ln2) I <= beta(t) <= (c - 2/ln2) I + (2/ln2) I / t
      (ix)  E[c I(f_{J,X}) - H(f_{J,X})] <= (2/ln2)(1-t) I
      (vii) deg f >= 1 + c I/2 (granularity) -- for every f with c = H/I
  * (ii) Inf_i <= 1/2 and (vi) Inf_i <= Var 2^{6.0782-c} on the extremizers of c_n.
"""
import math, json, itertools
import numpy as np
from rlib import Spec, all_tables, walsh, popcounts, plogq, h2, LOG2E

C2 = 2 / math.log(2)
TGRID = [0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99]


def marg_entropies(p, n):
    """H(S_A) for every A (bitmask), batch. Marginal of the law on coordinates A."""
    N = 1 << n
    idx = np.arange(N)
    out = np.zeros((p.shape[0], N))
    for A in range(N):
        # map each S to S & A, sum masses
        key = idx & A
        q = np.zeros_like(p)
        np.add.at(q.T, key, p.T)   # q[:, key[S]] += p[:, S]
        out[:, A] = -plogq(q, q).sum(-1)
    return out


report = {}
for n in [2, 3, 4]:
    T = all_tables(n).astype(np.int8)
    M, N = T.shape
    sp = Spec.from_tables(T)
    H = sp.H(); I = sp.I(); Var = sp.Var(); inf = sp.infl(); Bi = sp.B_i(); B = Bi.sum(-1)
    nc = I > 1e-15
    c = np.where(nc, H / np.where(nc, I, 1), 0.0)
    idx = np.arange(N)
    # ---- all restrictions: live set J (bitmask), assignment of complement
    EH = {t: np.zeros(M) for t in TGRID}
    EI = {t: np.zeros(M) for t in TGRID}
    max_restr_ratio = np.zeros(M)
    for J in range(N):
        live = [i for i in range(n) if (J >> i) & 1]
        fixed = [i for i in range(n) if not (J >> i) & 1]
        for X in itertools.product([0, 1], repeat=len(fixed)):
            base = 0
            for b, i in zip(X, fixed):
                base |= (b << i)
            keep = []
            for y in range(1 << len(live)):
                x = base
                for k, i in enumerate(live):
                    x |= (((y >> k) & 1) << i)
                keep.append(x)
            g = T[:, keep]
            if len(live) == 0:
                Hg = np.zeros(M); Ig = np.zeros(M)
            else:
                sg = Spec.from_tables(g)
                Hg = sg.H(); Ig = sg.I()
            if len(fixed) > 0:  # proper restriction
                with np.errstate(divide='ignore', invalid='ignore'):
                    rr = np.where(Ig > 1e-15, Hg / np.where(Ig > 1e-15, Ig, 1), 0.0)
                max_restr_ratio = np.maximum(max_restr_ratio, rr)
            for t in TGRID:
                w = (t ** len(live)) * ((1 - t) ** len(fixed)) / (2 ** len(fixed))
                EH[t] += w * Hg; EI[t] += w * Ig
    # ---- U-Han for every f
    han_worst = -1e9; tower_I_err = 0.0
    for t in TGRID:
        rhs = EH[t] / t + C2 * ((1 - t) / t) * I
        han_worst = max(han_worst, float((H - rhs).max()))
        tower_I_err = max(tower_I_err, float(np.abs(EI[t] - t * I).max()))   # E I(f_{J,X}) = t I
    # ---- ratio-critical functions
    crit = nc & (max_restr_ratio <= c + 1e-12)
    # ---- Delta_i H and JS
    dH = np.zeros((M, n))
    for i in range(n):
        lo = idx[((idx >> i) & 1) == 0]; hi = lo | (1 << i)
        sps = [Spec.from_tables(T[:, lo]), Spec.from_tables(T[:, hi])]
        dH[:, i] = H - 0.5 * (sps[0].H() + sps[1].H())
    JS = dH - Bi
    Jchar = np.minimum(inf, 1 - inf).sum(-1)
    ok = {}
    ok['iii_Delta'] = int((crit[:, None] & (dH < c[:, None] * inf - 1e-12)).sum())
    ok['iii_B'] = int((crit[:, None] & (Bi < (c[:, None] - C2) * inf - 1e-12)).sum())
    DTC = H - B
    ok['iv'] = int((crit & ((DTC > JS.sum(-1) + 1e-12) | (JS.sum(-1) > C2 * Jchar + 1e-12))).sum())
    # ---- marginal entropies for blocks and profile
    HA = marg_entropies(sp.p, n)
    full = N - 1
    v_viol = 0
    for A in range(1, N):
        Cset = full ^ A
        IA = sum(inf[:, i] for i in range(n) if (A >> i) & 1)
        IC = I - IA
        Hcond = H - HA[:, Cset]
        v_viol += int((crit & (Hcond < (c - C2) * IA - 1e-12)).sum())
        v_viol += int((crit & (HA[:, Cset] > c * IC + C2 * IA + 1e-12)).sum())
    ok['v'] = v_viol
    # beta(t) = sum_i sum_{A subset [n]\i} t^|A| (1-t)^{n-1-|A|} [H(S_{A+i}) - H(S_A)]
    pc = popcounts(n)
    viii_lo = 0; viii_hi = 0; ix = 0
    for t in TGRID + [1.0]:
        beta = np.zeros(M)
        for i in range(n):
            for A in range(N):
                if (A >> i) & 1:
                    continue
                w = (t ** pc[A]) * ((1 - t) ** (n - 1 - pc[A]))
                beta += w * (HA[:, A | (1 << i)] - HA[:, A])
        if t == 1.0:
            ok['beta1_equals_B_err'] = float(np.abs(beta - B).max())
        viii_lo += int((crit & (beta < (c - C2) * I - 1e-9)).sum())
        viii_hi += int((crit & (beta > (c - C2) * I + C2 * I / t + 1e-9)).sum())
        if t < 1.0:
            ix += int((crit & (c * EI[t] - EH[t] > C2 * (1 - t) * I + 1e-9)).sum())
    ok['viii_lower'] = viii_lo; ok['viii_upper'] = viii_hi; ok['ix'] = ix
    # ---- (vii) granularity / degree for every f
    W = sp.W
    deg = np.array([max([int(pc[S]) for S in range(N) if W[k, S] != 0]) for k in range(M)])
    ok['vii_violations_all_f'] = int((nc & (deg < 1 + c * I / 2 - 1e-12)).sum())
    ok['granularity_H_le_2deg_minus_2_viol'] = int((nc & (H > 2 * (deg - 1) + 1e-12)).sum())
    # ---- extremizers of c_n
    cn = c[nc].max()
    ext = nc & (c >= cn - 1e-12)
    ok['c_n'] = float(cn); ok['num_extremizers'] = int(ext.sum())
    ok['ii_violations_on_extremizers'] = int((ext[:, None] & (inf > 0.5 + 1e-12)).sum())
    ok['vi_violations_on_extremizers'] = int((ext[:, None] & (inf > Var[:, None] * 2 ** (6.078162672495945 - cn) + 1e-12)).sum())
    ok['extremizers_ratio_critical'] = int((ext & crit).sum())
    ok['num_ratio_critical'] = int(crit.sum())
    ok['han_worst_H_minus_rhs'] = han_worst
    ok['tower_E_I_restriction_err'] = tower_I_err
    print(n, json.dumps(ok))
    report[n] = ok

with open('thmC_results.json', 'w', encoding='utf-8') as fh:
    json.dump(report, fh, indent=1)
