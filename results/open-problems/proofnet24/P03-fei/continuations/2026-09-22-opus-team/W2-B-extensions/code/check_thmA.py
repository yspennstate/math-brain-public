"""Tests of Theorem A (Boolean functions of k threshold functions, arbitrary weight orders).

For each instance f = F(h_1, ..., h_k), h_l = sgn(w^(l).x - theta_l):
  - H/I;
  - Phi = min over orderings of Sigma_r / I (exact, Hungarian method);
  - Sigma_{r*}/I for the round-robin interleaving r* of the k weight orders, against L_k = L1 + 3 ln k;
  - Lemma 3 quantity Q_i for r*, against L_k;
  - pointwise Lemma 2: max_x Pr[D_i f(y) != 0 | x] under re-randomisation of the predecessors of i
    with probability eta = c/N, against beta_f c^{-1/2}, beta_f = sqrt(k) * k * 2/sqrt(pi);
  - H <= C_k I with C_k = fei_constant(L_k).
Weight orders are deliberately not co-monotone (reversed, random).
"""
import sys, time
import numpy as np
from fei_lib import *

setup_process()


def gates(k, rng):
    out = {}
    if k == 2:
        out["AND"] = lambda v: np.where((v[0] > 0) & (v[1] > 0), 1.0, -1.0)
        out["XOR"] = lambda v: v[0] * v[1]
        out["OR"] = lambda v: np.where((v[0] > 0) | (v[1] > 0), 1.0, -1.0)
    if k == 3:
        out["AND3"] = lambda v: np.where((v[0] > 0) & (v[1] > 0) & (v[2] > 0), 1.0, -1.0)
        out["MAJ3"] = lambda v: sgn(v[0] + v[1] + v[2])
        out["XOR3"] = lambda v: v[0] * v[1] * v[2]
    tbl = rng.choice([-1.0, 1.0], size=1 << k)
    def rnd(v, tbl=tbl):
        key = np.zeros(v[0].shape[0], dtype=np.int64)
        for l in range(k):
            key |= ((v[l] < 0).astype(np.int64) << l)
        return tbl[key]
    out["RANDF"] = rnd
    return out


from math import comb


def erd_binom(s, eta):
    """E[C(m, floor(m/2)) 2^-m], m ~ Bin(s, eta) (Erdos bound averaged over the re-randomised set)."""
    tot = 0.0
    for m in range(s + 1):
        tot += comb(s, m) * eta ** m * (1 - eta) ** (s - m) * comb(m, m // 2) / 2.0 ** m
    return tot


stat = dict(cnt=0, nontriv=0, worst_nontriv=0.0)


def weight_family(kind, n, l, rng):
    g = np.abs(rng.standard_normal(n)) + 0.05
    if kind == "geom":
        base = 1.6 ** (-np.arange(n))
    elif kind == "pow":
        base = (1.0 + np.arange(n)) ** -0.7
    else:
        base = np.sort(g)[::-1]
    if l % 3 == 0:
        w = base
    elif l % 3 == 1:
        w = base[::-1].copy()
    else:
        w = base[rng.permutation(n)]
    w = w * (1 + 0.01 * rng.standard_normal(n)) * rng.choice([-1.0, 1.0], size=n)
    return w


def run(n, k, trials, seed, logf):
    rng = np.random.default_rng(seed)
    X = coords(n)
    Lk = L1 + 3 * np.log(k)
    Ck = fei_constant(Lk)
    beta = np.sqrt(k) * k * 2 / np.sqrt(np.pi)
    worst = dict(Q=0, sig=0, pw=0, thm=0, HI=0, phi=0)
    for t in range(trials):
        kind = ["geom", "pow", "gauss"][t % 3]
        W = [weight_family(kind, n, l, rng) for l in range(k)]
        th = [float(rng.normal(0, 0.6) * np.abs(w).sum() / np.sqrt(n)) for w in W]
        vals = [sgn(X @ W[l] - th[l]) for l in range(k)]
        for gname, G in gates(k, rng).items():
            f = G(vals)
            c = wht(f)
            H, I = HI(c, n)
            if I < 1e-9:
                continue
            orders = [list(np.argsort(-np.abs(W[l]), kind="stable")) for l in range(k)]
            rstar = round_robin(orders)
            sig = sigma_of_order(c, n, rstar) / I
            phi, _ = phi_min(c, n)
            phi /= I
            Q = lemma3_Q(c, n, rstar)
            qmax = np.nanmax(Q) if np.any(~np.isnan(Q)) else 0.0
            # pointwise lemma 2 on every coordinate with Inf > 0, three noise levels
            rank = {u: p + 1 for p, u in enumerate(rstar)}
            pw = 0.0
            infl = influences(c, n)
            for i in range(n):
                if infl[i] < 1e-12:
                    continue
                N = rank[i]
                if N < 2:
                    continue
                pred = [1 << u for u in rstar[: N - 1]]
                # s = number of complete rounds before i was placed: top_l(s) subset of pred for all l
                s = 0
                while all(set(orders[l][: s + 1]) <= set(rstar[: N - 1]) for l in range(k)):
                    s += 1
                act = [l for l in range(k) if abs(W[l][i]) > 0]
                for eta in (0.1, 0.3, 0.6, 1.0):
                    P, h = pointwise_exit(f, n, i, pred, eta)
                    bl = sum(erd_binom(s, eta) for l in act)
                    stat["cnt"] += 1
                    if bl < 1:
                        stat["nontriv"] += 1
                        stat["worst_nontriv"] = max(stat["worst_nontriv"], float(P.max()) / bl)
                    pw = max(pw, float(P.max()) / min(1.0, bl))
            worst["Q"] = max(worst["Q"], qmax / Lk)
            worst["sig"] = max(worst["sig"], sig / Lk)
            worst["pw"] = max(worst["pw"], pw)
            worst["thm"] = max(worst["thm"], (H / I) / Ck)
            worst["HI"] = max(worst["HI"], H / I)
            worst["phi"] = max(worst["phi"], phi)
            print("n=%d k=%d %-5s %-5s H/I=%.4f Phi=%.4f Sig(r*)/I=%.4f maxQ=%.4f (L_k=%.3f) pointwise/literal=%.4f"
                  % (n, k, kind, gname, H / I, phi, sig, qmax, Lk, pw), file=logf, flush=True)
    print("SUMMARY n=%d k=%d: max H/I=%.4f (C_k=%.4f, ratio %.4f); max Phi=%.4f; max Sig(r*)/I/L_k=%.4f; "
          "max Q/L_k=%.4f; max pointwise/literal=%.4f"
          % (n, k, worst["HI"], Ck, worst["thm"], worst["phi"], worst["sig"], worst["Q"], worst["pw"]), file=logf, flush=True)
    return worst


if __name__ == "__main__":
    t0 = time.time()
    with open("../logs/check_thmA.log", "w") as logf:
        print("L1=%.10f  C_2=%.6f  C_3=%.6f" % (L1, fei_constant(L1 + 3 * np.log(2)), fei_constant(L1 + 3 * np.log(3))), file=logf)
        for (n, k, tr) in [(8, 2, 6), (10, 2, 6), (12, 2, 6), (10, 3, 4), (12, 3, 4), (14, 2, 3)]:
            run(n, k, tr, 1000 * n + k, logf)
        print("pointwise tests: %d, with nontrivial literal bound (<1): %d, worst ratio among those: %.4f" % (stat["cnt"], stat["nontriv"], stat["worst_nontriv"]), file=logf)
        print("time %.1fs" % (time.time() - t0), file=logf)
