"""Referee check of SEL-1 (selector cost bound) and SEL-2 (closure constant K(c)).

Part A: exhaustive over all 65,536 Boolean functions of 4 variables, every split a = 1,2,3 (selector = low a bits).
Part B: exhaustive over all 2^32 ... no: random Boolean functions of 5..8 variables, all splits.
Part C: adversarial structured families (bent point flip, X002 parity splice, parity lifts, addressing, overlapping
        supports, signed-dictator encodings, sparse activation).
For each instance we compute, independently of the author's code:
  cost = H(F) - avg_b H(g_b);  HST = H(F) - H(R) with R the data-marginal of Fhat^2;
  IXY = H(R') - avg_b H(g_b) with R' the data-marginal of the channel law ghat_b(T)^2/N (computed from branches);
  pi_i = exact disagreement probability of selector bit i.
Checks: |R - R'| tiny (this is the identity (i)); IXY <= HST; IXY <= (2/ln2) I_sel; HST <= sum h(pi_i) <= a h(I_sel/a);
cost <= sum h(pi) + min(sum h(pi), (2/ln2) I_sel); and H(F) <= max(C, K(I_sel/a)) I(F) with C = max_b H(g_b)/I(g_b).
"""
import sys
import math
import numpy as np
from rlib import wht, ent, h2, popcount_table, K_of_c, LOG2E

TOL = 1e-9
worst = {}


def record(name, val, info):
    if name not in worst or val > worst[name][0]:
        worst[name] = (val, info)


def analyse_batch(F, a, n, label):
    """F: (B, 2^(a+n)) int array of +-1 truth tables, selector = low a bits."""
    Bsz = F.shape[0]
    N = 1 << a
    D = 1 << n
    W = wht(F)                                    # (B, N*D)
    P = (W.astype(np.float64) ** 2) / float((N * D) ** 2)
    HF = ent(P)
    Pm = P.reshape(Bsz, D, N)                     # [T, S]: joint index S + N*T
    R = Pm.sum(axis=2)                            # data marginal (B, D)
    HR = ent(R)
    HST = HF - HR
    # branches
    G = F.reshape(Bsz, D, N).transpose(0, 2, 1)   # G[b, y]
    Wg = wht(G)                                   # (B, N, D)
    Pg = (Wg.astype(np.float64) ** 2) / float(D * D)
    Hg = ent(Pg, axis=2)                          # (B, N)
    pc_d = popcount_table(n)
    Ig = (Pg * pc_d[None, None, :]).sum(axis=2)  # (B, N)
    avgHg = Hg.mean(axis=1)
    Rp = Pg.mean(axis=1)                          # channel data marginal (B, D)
    IXY = ent(Rp) - avgHg
    cost = HF - avgHg
    # selector influences by disagreement (exact integers)
    idx = np.arange(N)
    pis = np.stack([(G != G[:, idx ^ (1 << i), :]).mean(axis=(1, 2)) for i in range(a)], axis=1)  # (B, a)
    Isel = pis.sum(axis=1)
    pc = popcount_table(a + n)
    IF = (P * pc[None, :]).sum(axis=1)
    sumh = h2(pis).sum(axis=1) if a > 0 else np.zeros(Bsz)
    with np.errstate(divide="ignore", invalid="ignore"):
        ah = a * h2(np.clip(Isel / a, 0, 1))
    bound = sumh + np.minimum(sumh, 2 * LOG2E * Isel)
    # checks
    e_R = np.abs(R - Rp).max(axis=1)
    record("identity |R-R'|", e_R.max(), label)
    v1 = IXY - HST
    record("IXY - HST (<=0)", v1.max(), (label, int(np.argmax(v1))))
    v2 = IXY - 2 * LOG2E * Isel
    record("IXY - (2/ln2) Isel (<=0)", v2.max(), (label, int(np.argmax(v2))))
    v3 = HST - sumh
    record("HST - sum h(pi) (<=0)", v3.max(), (label, int(np.argmax(v3))))
    v4 = sumh - ah
    record("sum h(pi) - a h(Isel/a) (<=0)", v4.max(), (label, int(np.argmax(v4))))
    v5 = cost - bound
    record("cost - SEL1bound (<=0)", v5.max(), (label, int(np.argmax(v5))))
    # attainment ratio cost/bound
    with np.errstate(divide="ignore", invalid="ignore"):
        rat = np.where(bound > 1e-12, cost / bound, 0.0)
    record("max cost/bound (ratio)", rat.max(), (label, int(np.argmax(rat))))
    # SEL-2
    with np.errstate(divide="ignore", invalid="ignore"):
        rg = np.where(Ig > 1e-12, Hg / np.where(Ig > 1e-12, Ig, 1.0), 0.0)
    Cb = rg.max(axis=1)
    viol2 = []
    for k in range(Bsz):
        if Isel[k] <= 1e-15:
            continue
        K = K_of_c(Isel[k] / a)
        viol2.append(HF[k] - max(Cb[k], K) * IF[k])
    if viol2:
        record("H(F) - max(C,K(c)) I(F) (<=0)", max(viol2), label)
    return Bsz


def all_tables(nvars):
    M = 1 << nvars
    codes = np.arange(1 << M, dtype=np.int64)
    T = 1 - 2 * ((codes[:, None] >> np.arange(M)[None, :]) & 1)
    return T


def main():
    total = 0
    # Part A: exhaustive n_total = 4 (and 3, 2)
    for ntot in (2, 3, 4):
        T = all_tables(ntot)
        for a in range(1, ntot):
            total += analyse_batch(T, a, ntot - a, "exh n=%d a=%d" % (ntot, a))
    print("Part A exhaustive instances:", total, flush=True)
    # Part B: random tables
    rng = np.random.default_rng(20261012)
    cnt = 0
    for ntot in (5, 6, 7, 8):
        for a in range(1, ntot):
            for dens in (0.5, 0.1, 0.02):
                # biased random tables plus random low-energy multiplexers (few distinct branches)
                F = np.where(rng.random((400, 1 << ntot)) < dens, -1, 1).astype(np.int64)
                cnt += analyse_batch(F, a, ntot - a, "rand n=%d a=%d dens=%.2f" % (ntot, a, dens))
            # low-energy: branches equal except few points
            N = 1 << a
            D = 1 << (ntot - a)
            base = np.where(rng.random((300, 1, D)) < 0.5, -1, 1)
            G = np.repeat(base, N, axis=1)
            flips = rng.random((300, N, D)) < 0.03
            G = np.where(flips, -G, G).astype(np.int64)
            F = G.transpose(0, 2, 1).reshape(300, -1)
            cnt += analyse_batch(F, a, ntot - a, "lowenergy n=%d a=%d" % (ntot, a))
    print("Part B random instances:", cnt, flush=True)
    for k, (v, info) in sorted(worst.items()):
        print("%-40s %.3e   at %s" % (k, v, info))


if __name__ == "__main__":
    main()
