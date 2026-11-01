"""Tests of Propositions 2 and 3 (block-separable thresholds, separable functions of block sums,
Boolean combinations over a common unit partition) and of Theorem 1 on these classes.

For every instance and every coordinate i and every initial segment P of the unit order preceding
u(i) (all t = |P| >= 1), and eta in {0.25, 0.5, 1}, the exact function
    x -> Pr[D_i f(y) != 0],  y = x with each unit of P re-randomised with probability eta,
is computed by a Walsh transform, and its maximum over x is compared with the bound that the
proof actually establishes (before the final Jensen step):
    block-separable threshold:          E Erd(M),  M ~ Poisson-binomial(eta 2^{1-|u|}, u in P)
    separable kappa-function (m groups): kappa * E Erd(Bin(s, eta)),  s = complete rounds in P
    Boolean combination of components:  sum over components of the component bound on its prefix.
Erd(m) = C(m, floor(m/2)) 2^{-m}.  Also recorded: H/I, Phi (exact minimum over unit orders),
max_i Q_i (Lemma B) and Sigma/I for the order used, against L of Theorem 1.
"""
import time
from math import comb
import numpy as np
from fei_lib import *

setup_process()

ERD = [comb(m, m // 2) / 2.0 ** m for m in range(64)]


def pb_erd(ps):
    """E Erd(M) for M a sum of independent Bernoulli(p) with the given list of p."""
    dist = np.zeros(len(ps) + 1)
    dist[0] = 1.0
    for p in ps:
        dist[1:] = dist[1:] * (1 - p) + dist[:-1] * p
        dist[0] *= (1 - p)
    return float(sum(dist[m] * ERD[m] for m in range(len(ps) + 1)))


def random_partition(n, d, rng):
    perm = rng.permutation(n)
    units = np.empty(n, dtype=int)
    u, pos = 0, 0
    while pos < n:
        size = int(rng.integers(1, d + 1))
        for j in perm[pos: pos + size]:
            units[j] = u
        pos += size
        u += 1
    return units


def block_values(X, members, kind, rng):
    """Real function P_u on the block, evaluated on all points; returns (values, range)."""
    b = len(members)
    Xb = X[:, members]
    key = np.zeros(X.shape[0], dtype=np.int64)
    for t in range(b):
        key |= ((Xb[:, t] < 0).astype(np.int64) << t)
    if kind == "gauss":
        tbl = rng.standard_normal(1 << b)
    elif kind == "and":
        tbl = np.where(np.arange(1 << b) == 0, 1.0, -1.0)
    elif kind == "xor":
        tbl = np.array([(-1.0) ** bin(z).count("1") for z in range(1 << b)])
    else:  # random boolean
        tbl = rng.choice([-1.0, 1.0], size=1 << b)
    return tbl[key], float(tbl.max() - tbl.min())


def block_sep_instance(n, d, units, kind, profile, rng, X):
    m = units.max() + 1
    vals, ranges = [], []
    scale = {"geom": 1.5 ** (-rng.permutation(m)), "pow": (1.0 + rng.permutation(m)) ** -0.8,
             "flat": np.ones(m) + 0.05 * rng.random(m)}[profile]
    for u in range(m):
        members = list(np.where(units == u)[0])
        v, r = block_values(X, members, kind, rng)
        vals.append(scale[u] * v)
        ranges.append(scale[u] * r)
    Q = np.sum(vals, axis=0)
    return Q, np.array(ranges)


def unit_masks(units):
    m = units.max() + 1
    masks = [0] * m
    for i, u in enumerate(units):
        masks[u] |= (1 << int(i))
    return masks


def check_instance(name, f, n, units, order, bound_fn, Lval, d, logf, stats):
    c = wht(f)
    H, I = HI(c, n)
    if I < 1e-9:
        return
    masks = unit_masks(units)
    phi, _ = phi_min(c, n, units)
    sig = sigma_of_order(c, n, order, units) / I
    Q = lemma3_Q(c, n, order, units)
    qmax = float(np.nanmax(Q)) if np.any(~np.isnan(Q)) else 0.0
    rank = {u: p for p, u in enumerate(order)}
    worst = 0.0
    infl = influences(c, n)
    for i in range(n):
        if infl[i] < 1e-12:
            continue
        N = rank[units[i]]  # number of units before u(i)
        for t in range(1, N + 1):
            P = order[:t]
            for eta in (0.25, 0.5, 1.0):
                Pw, _ = pointwise_exit(f, n, i, [masks[u] for u in P], eta)
                bnd = bound_fn(i, P, eta)
                stats["tests"] += 1
                if bnd < 1:
                    stats["nontriv"] += 1
                    r = float(Pw.max()) / bnd
                    worst = max(worst, r)
                    if r > 1 + 1e-9:
                        stats["viol"] += 1
    C = fei_constant(Lval, d)
    stats["worst"] = max(stats["worst"], worst)
    stats["thm"] = max(stats["thm"], (H / I) / C)
    stats["Q"] = max(stats["Q"], qmax / Lval)
    stats["sig"] = max(stats["sig"], sig / Lval)
    print("%-34s n=%d H/I=%.4f Phi=%.4f Sigma/I=%.4f maxQ=%.4f L=%.3f C=%.3f worst pointwise/bound=%.4f"
          % (name, n, H / I, phi / I, sig, qmax, Lval, C, worst), file=logf, flush=True)


def main():
    rng = np.random.default_rng(2026)
    stats = dict(tests=0, nontriv=0, viol=0, worst=0.0, thm=0.0, Q=0.0, sig=0.0)
    t0 = time.time()
    with open("../logs/check_thmB.log", "w") as logf:
        # 1. block-separable thresholds (Proposition 3), d = 2, 3
        for n in (10, 12):
            X = coords(n)
            for d in (2, 3):
                for kind in ("gauss", "and", "xor", "rbool"):
                    for profile in ("geom", "pow", "flat"):
                        units = random_partition(n, d, rng)
                        Qv, ranges = block_sep_instance(n, d, units, kind, profile, rng, X)
                        th = rng.normal(0, 0.5) * np.sqrt((ranges ** 2).sum())
                        f = sgn(Qv - th)
                        order = list(np.argsort(-ranges, kind="stable"))
                        sizes = np.bincount(units)

                        def bnd(i, P, eta, sizes=sizes):
                            return pb_erd([eta * 2.0 ** (1 - sizes[u]) for u in P])
                        dmax = int(sizes.max())
                        Lval = L1 + (dmax - 1) * np.log(2)
                        check_instance("blocksep d=%d %s %s" % (d, kind, profile), f, n, units, order, bnd,
                                       Lval, dmax, logf, stats)
        # 2. separable functions of two linear forms on disjoint halves (Theorem C type)
        for n in (10, 12):
            X = coords(n)
            h = n // 2
            units = np.arange(n)
            for wk in ("geom", "pow"):
                base = 1.5 ** (-np.arange(h)) if wk == "geom" else (1.0 + np.arange(h)) ** -0.8
                wa = base * rng.choice([-1, 1], size=h)
                wb = base[rng.permutation(h)] * rng.choice([-1, 1], size=h)
                La = X[:, :h] @ wa
                Lb = X[:, h:] @ wb
                order_a = list(np.argsort(-np.abs(wa), kind="stable"))
                order_b = [h + j for j in np.argsort(-np.abs(wb), kind="stable")]
                order = round_robin([order_a, order_b])
                for (fname, f, kappa) in [("hyperbola th=0.3", sgn(La * Lb - 0.3), 1),
                                          ("hyperbola th=-0.1", sgn(La * Lb + 0.1), 1),
                                          ("disc th=1", sgn(La ** 2 + Lb ** 2 - 1.0), 2),
                                          ("annulus-ish", sgn((La ** 2 + Lb ** 2 - 0.6) * (La ** 2 + Lb ** 2 - 2.0)), 4)]:
                    def bnd(i, P, eta, kappa=kappa):
                        grp = order_a if i < h else order_b
                        s = 0
                        while s < len(grp) and grp[s] in P[: len(P)]:
                            s += 1
                        # s = length of the longest prefix of i's group order inside P
                        tot = 0.0
                        for mm in range(s + 1):
                            tot += comb(s, mm) * eta ** mm * (1 - eta) ** (s - mm) * ERD[mm]
                        return kappa * tot
                    Lval = L1 + 2 * np.log(kappa) + np.log(2)
                    check_instance("sep2 %s %s" % (fname, wk), f, n, units, order, bnd, Lval, 1, logf, stats)
        # 3. Boolean combinations of two block-separable thresholds on a common partition
        for n in (10, 12):
            X = coords(n)
            for d in (1, 2):
                for gate in ("AND", "XOR"):
                    units = random_partition(n, d, rng)
                    Q1, r1 = block_sep_instance(n, d, units, "gauss", "geom", rng, X)
                    Q2, r2 = block_sep_instance(n, d, units, "gauss", "pow", rng, X)
                    h1 = sgn(Q1 - rng.normal(0, 0.3) * np.sqrt((r1 ** 2).sum()))
                    h2 = sgn(Q2 - rng.normal(0, 0.3) * np.sqrt((r2 ** 2).sum()))
                    f = np.where((h1 > 0) & (h2 > 0), 1.0, -1.0) if gate == "AND" else h1 * h2
                    o1 = list(np.argsort(-r1, kind="stable"))
                    o2 = list(np.argsort(-r2, kind="stable"))
                    order = round_robin([o1, o2])
                    sizes = np.bincount(units)

                    def bnd(i, P, eta, o1=o1, o2=o2, sizes=sizes):
                        tot = 0.0
                        for ol in (o1, o2):
                            s = 0
                            while s < len(ol) and ol[s] in P:
                                s += 1
                            tot += pb_erd([eta * 2.0 ** (1 - sizes[u]) for u in ol[:s]])
                        return tot
                    dmax = int(sizes.max())
                    Lval = L1 + 3 * np.log(2) + (dmax - 1) * np.log(2)
                    check_instance("bool2 %s d=%d" % (gate, d), f, n, units, order, bnd, Lval, dmax, logf, stats)
        print("TOTAL pointwise tests %d, nontrivial %d, violations %d, worst ratio %.4f; max (H/I)/C %.4f; "
              "max Q/L %.4f; max (Sigma/I)/L %.4f; time %.1fs"
              % (stats["tests"], stats["nontriv"], stats["viol"], stats["worst"], stats["thm"], stats["Q"],
                 stats["sig"], time.time() - t0), file=logf, flush=True)


if __name__ == "__main__":
    main()
