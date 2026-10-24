"""Exhaustive referee checks for n <= 4 (all 2^(2^n) Boolean functions).

1. Lemma G-key, exact integers:  W_S^2 * 4^n <= 4^{|S|-1} * Pi_S^2  for every S != empty.
2. Theorem G (float): H <= 2(I-Var) + 2U - p0 log2(1/p0);  min slack and equality count.
3. The author's exhaustive maxima: H/I, B/I, K_loc, K_Delta, U/I, G/I.
4. Theorem U-loc identity  Delta_i U = sum_T m_T[s log(r/s) + (1-s)log(1/(1-s)) + D2]  (direct vs formula).
5. Delta_i U = B_i - Gamma_i + K_i with K_i = U(m) - avg U(f_+-), and the chain rules H = sum B, U = sum (B - Gamma).
6. Baseline facts used by the author: (E1) Delta_i H = B_i + JS_i, JS_i <= (2/ln2) min(Inf_i,1-Inf_i);
   (E3) L <= B <= L + I log2 e;  RM 2.2 variance-local bound Delta_i H <= Inf_i[log2(Var/Inf_i) + 6.0781626...].
7. GU' combinations at n <= 4: G <= 1.75 I + U, G <= 2.25 I + 0.5 U, G <= 0.75 I + H, G <= 1.5 H.
"""
import math, sys, json
import numpy as np
from rlib import Spec, all_tables, walsh, superset_sum, popcounts, restrict_tables, plogq, h2, LOG2E

out = {}
rng = np.random.default_rng(20261012)

def D2(a, b):
    """binary KL in bits, arrays, with 0 log 0 = 0; a,b in [0,1]."""
    return plogq(a, np.where(b > 0, a / np.where(b > 0, b, 1), 1)) + plogq(1 - a, np.where(1 - b > 0, (1 - a) / np.where(1 - b > 0, 1 - b, 1), 1))

for n in [1, 2, 3, 4]:
    T = all_tables(n)
    N = 1 << n
    W = walsh(T)                       # exact ints
    P = W * W                          # exact ints, p = P / N^2
    Pi = superset_sum(P)
    sz = popcounts(n)
    # ---- 1. Lemma G-key exact
    viol = 0; eq = 0; tot = 0
    for S in range(1, N):
        lhs = P[:, S] * (N * N)            # W_S^2 * 4^n
        rhs = (4 ** (int(sz[S]) - 1)) * Pi[:, S] ** 2
        viol += int((lhs > rhs).sum()); eq += int(((lhs == rhs) & (P[:, S] > 0)).sum()); tot += lhs.size
    # sanity: the check must be able to fail - apply it to a non-Boolean normalized vector (X006 psi_n)
    sp = Spec(P.astype(np.float64) / (N * N))
    sp.W = W
    H = sp.H(); I = sp.I(); Var = sp.Var(); U = sp.U(); p0 = sp.p[:, 0]
    nc = I > 0
    rhsG = 2 * (I - Var) + 2 * U - plogq(p0, np.where(p0 > 0, 1 / np.where(p0 > 0, p0, 1), 1))
    slack = rhsG - H
    Binf = sp.B_i(); inf = sp.infl(); B = Binf.sum(-1)
    # Delta_i H and Delta_i U by direct restriction
    dH = np.zeros((T.shape[0], n)); dU = np.zeros((T.shape[0], n)); Uform = np.zeros((T.shape[0], n)); Ki = np.zeros((T.shape[0], n))
    JSi = np.zeros((T.shape[0], n))
    fhat = W.astype(np.float64) / N
    idx = np.arange(N)
    Gam = sp.Gamma_i()
    for i in range(n):
        sps = [Spec.from_tables(restrict_tables(T, i, s)) for s in (1, -1)]
        Hr = [s.H() for s in sps]; Ur = [s.U() for s in sps]
        dH[:, i] = H - 0.5 * (Hr[0] + Hr[1])
        dU[:, i] = U - 0.5 * (Ur[0] + Ur[1])
        lo = idx[((idx >> i) & 1) == 0]; hi = lo | (1 << i)
        u = fhat[:, lo]; v = fhat[:, hi]
        m = u * u + v * v
        with np.errstate(divide='ignore', invalid='ignore'):
            s = np.where(m > 0, v * v / np.where(m > 0, m, 1), 0.0)
            piT = sp.pi[:, lo]; V = sp.pi[:, hi]
            r = np.where(piT > 0, V / np.where(piT > 0, piT, 1), 0.0)
            eta = np.where(m > 0, 2 * u * v / np.where(m > 0, m, 1), 0.0)
            Z = np.zeros_like(fhat); Z[:, lo] = u * v
            C = superset_sum(Z)[:, lo]
            x = np.where(piT > 0, 2 * C / np.where(piT > 0, piT, 1), 0.0)
        x = np.clip(x, -1, 1)
        term = plogq(m * s, np.where(s > 0, r / np.where(s > 0, s, 1), 1)) + plogq(m * (1 - s), np.where(1 - s > 0, 1 / np.where(1 - s > 0, 1 - s, 1), 1)) + m * D2((1 + eta) / 2, (1 + x) / 2)
        Uform[:, i] = term.sum(-1)
        # K_i = U(law of S minus i) - avg U(f_+-)
        mlaw = np.zeros((T.shape[0], N >> 1))
        # law of S\i on the (n-1)-cube: index by compressing lo positions
        mlaw = m
        # upper sets of m in its own cube equal pi[lo]
        with np.errstate(divide='ignore', invalid='ignore'):
            Um = plogq(m, np.where(m > 0, piT / np.where(m > 0, m, 1), 1)).sum(-1)
        Ki[:, i] = Um - 0.5 * (Ur[0] + Ur[1])
        # JS term
        pp = (u + v) ** 2; pm = (u - v) ** 2
        JSi[:, i] = (-plogq(m, m) + 0.5 * plogq(pp, pp) + 0.5 * plogq(pm, pm)).sum(-1)
    errU = np.abs(dU - Uform).max()
    errBGK = np.abs(dU - (Binf - Gam + Ki)).max()
    errE1 = np.abs(dH - (Binf + JSi)).max()
    js_viol = (JSi > (2 / math.log(2)) * np.minimum(inf, 1 - inf) + 1e-12).sum()
    Ki_neg = (Ki < -1e-12).sum()
    # chain rules on a random order, for every function
    order = rng.permutation(n)
    Hch = np.zeros(T.shape[0]); Uch = np.zeros(T.shape[0]); Gch = np.zeros(T.shape[0])
    cur = sp.p.copy(); bits_left = list(range(n))
    for i in order:
        cs = Spec(cur)
        Hch += cs.B_i()[:, i]; Uch += cs.B_i()[:, i] - cs.Gamma_i()[:, i]; Gch += cs.Gamma_i()[:, i]
        # marginalize coordinate i: move mass of S+i onto S (keep indexing in the full cube)
        lo = idx[((idx >> i) & 1) == 0]; hi = lo | (1 << i)
        new = cur.copy(); new[:, lo] += cur[:, hi]; new[:, hi] = 0.0
        cur = new
    errChainH = np.abs(Hch - H).max(); errChainU = np.abs(Uch - U).max()
    with np.errstate(divide='ignore', invalid='ignore'):
        Elog1pi = plogq(sp.p, np.where(sp.pi > 0, 1 / np.where(sp.pi > 0, sp.pi, 1), 1)).sum(-1)
    errChainG = np.abs(Gch - Elog1pi).max()
    # (E3) and L
    L = sp.L_down()
    e3_viol = int(((L > B + 1e-12) | (B > L + I * LOG2E + 1e-12)).sum())
    # RM 2.2 variance-local bound for every relevant coordinate
    c622 = (3 + 2 / math.sqrt(math.e)) / math.log(2)
    with np.errstate(divide='ignore', invalid='ignore'):
        bound = inf * (np.log2(np.where(inf > 0, Var[:, None] / np.where(inf > 0, inf, 1), 1)) + c622)
    rm22_viol = int(((inf > 0) & (dH > bound + 1e-12)).sum())
    with np.errstate(divide='ignore', invalid='ignore'):
        rm22_ratio = np.where(inf > 0, dH / np.where(bound > 0, bound, 1), 0).max()
    # maxima
    with np.errstate(divide='ignore', invalid='ignore'):
        ratioB_loc = np.where(inf > 0, Binf / np.where(inf > 0, inf, 1), np.inf).min(-1)
        ratioD_loc = np.where(inf > 0, dH / np.where(inf > 0, inf, 1), np.inf).min(-1)
    G = dU.sum(-1)
    res = dict(
        n=n, functions=int(T.shape[0]),
        Gkey_pairs=tot, Gkey_violations=viol, Gkey_equalities_nonzero=eq,
        thmG_min_slack=float(slack[nc].min()), thmG_equal_count=int((np.abs(slack[nc]) < 1e-12).sum()),
        max_H_over_I=float((H[nc] / I[nc]).max()), max_B_over_I=float((B[nc] / I[nc]).max()),
        K_loc_n=float(ratioB_loc[nc].max()), K_Delta_n=float(ratioD_loc[nc].max()),
        max_U_over_I=float((U[nc] / I[nc]).max()), max_G_over_I=float((G[nc] / I[nc]).max()),
        min_G_over_I=float((G[nc] / I[nc]).min()),
        err_Uloc_identity=float(errU), err_B_minus_Gamma_plus_K=float(errBGK), Ki_negative=int(Ki_neg),
        err_E1=float(errE1), JS_bound_violations=int(js_viol),
        err_chain_H=float(errChainH), err_chain_U=float(errChainU), err_chain_H_minus_U=float(errChainG),
        E3_violations=e3_viol, RM22_violations=rm22_viol, RM22_max_ratio=float(rm22_ratio),
        GUp_1p75I_plus_U=float((G[nc] - 1.75 * I[nc] - U[nc]).max()),
        GUp_2p25I_plus_halfU=float((G[nc] - 2.25 * I[nc] - 0.5 * U[nc]).max()),
        GUp_0p75I_plus_H=float((G[nc] - 0.75 * I[nc] - H[nc]).max()),
        GUp_1p5H=float((G[nc] - 1.5 * H[nc]).max()),
        U_le_H_viol=int((U > H + 1e-12).sum()), U_neg=int((U < -1e-12).sum()),
    )
    # argmax info for the H/I maximizer
    k = int(np.argmax(np.where(nc, H / np.where(nc, I, 1), -1)))
    res['argmax_HI_table'] = [int(v) for v in T[k]]
    print(json.dumps(res))
    out[n] = res

with open('ex_n4_results.json', 'w', encoding='utf-8') as fh:
    json.dump(out, fh, indent=1)
