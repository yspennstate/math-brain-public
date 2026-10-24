"""Composition law for the multiscale defect, and the tower recursion.

Theorem (composition law).  F = G(f_1,...,f_k) on disjoint variables, mu_i = E f_i, V_i = 1 - mu_i^2,
nu_i = mean of the delta-random restriction of f_i (a random variable with E nu_i = mu_i), W_i = 1 - nu_i^2,
Lambda_i(mu) = P_mu[i pivotal for G].  Then, with D_delta(f) = H(f) - E H(f_{J,x}),
    D_delta(F) = sum_i Lambda_i(mu) [D_delta(f_i) + E h2(nu_i^2) - h2(mu_i^2)] + Htilde_G(mu) - E Htilde_G(nu),
the nu_i independent with their own laws.  For the tower G_k = g(G_{k-1},...,G_{k-1}) of a balanced g:
    D_delta(G_k) = I(g) D_delta(G_{k-1}) + Xi_k,
    Xi_k = H(g) - E Htilde_g(nu) + sum_i Inf_i(g) E h2(nu_i^2),   nu_i iid ~ L_{k-1},
    L_0 = law of a restricted leaf: 0 w.p. delta, +-1 w.p. (1-delta)/2 each;  L_k = law of P_g(nu_1,...,nu_m),
    kappa_delta(G_k) = sum_{j<=k} Xi_j / ((1-delta) I(g)^j).
"""
import sys, os, json, time, itertools
import numpy as np
import numba as nb
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mslib import polite, fwht, entropy_bits, influences, restr_profile, restr_mean_hist, per_size_sums, size_weights


@nb.njit(cache=True)
def biased_H(ghat, mu):
    """Htilde_G(mu) (bits) and the output mean P_G(mu), from the uniform Fourier coefficients."""
    N = ghat.shape[0]
    n = mu.shape[0]
    a = ghat.copy()
    for i in range(n):
        bit = 1 << i
        m = mu[i]
        s = np.sqrt(max(0.0, 1.0 - m * m))
        for T in range(N):
            if (T & bit) == 0:
                u = a[T]
                v = a[T | bit]
                a[T] = u + m * v
                a[T | bit] = s * v
    H = 0.0
    for T in range(N):
        q = a[T] * a[T]
        if q > 1e-300:
            H -= q * np.log2(q)
    return H, a[0]


@nb.njit(cache=True)
def h2sq(nu):
    q = nu * nu
    if q <= 0.0 or q >= 1.0:
        return 0.0
    return -q * np.log2(q) - (1.0 - q) * np.log2(1.0 - q)


def compose_tt(g, ng, child, nc):
    """truth table of g(child(block_1),...,child(block_ng)), block j = variables j*nc..(j+1)*nc-1."""
    n = ng * nc
    N = 1 << n
    x = np.arange(N, dtype=np.int64)
    idx = np.zeros(N, dtype=np.int64)
    for j in range(ng):
        blk = (x >> (j * nc)) & ((1 << nc) - 1)
        out = child[blk]          # +-1 ; -1 = true -> bit 1
        idx |= ((out < 0).astype(np.int64)) << j
    return g[idx].astype(np.int64)


def law_from_hist(Hc, n, delta):
    """exact discrete law of the restricted mean nu from restr_mean_hist counts."""
    N = 1 << n
    vals, probs = [], []
    for s in range(n + 1):
        w = delta ** s * (1 - delta) ** (n - s) / 2.0 ** (n - s)
        row = Hc[s]
        ks = np.nonzero(row)[0]
        for k in ks:
            vals.append((k - N) / 2.0 ** s)
            probs.append(row[k] * w)
    vals = np.array(vals)
    probs = np.array(probs)
    # merge equal values
    key = np.round(vals * 2 ** 40).astype(np.int64)
    u, inv = np.unique(key, return_inverse=True)
    pv = np.bincount(inv, weights=probs)
    vv = np.bincount(inv, weights=vals * probs) / pv
    return vv, pv


def leaf_law(delta):
    return np.array([-1.0, 0.0, 1.0]), np.array([(1 - delta) / 2, delta, (1 - delta) / 2])


def exact_level(ghat, inf, vals, probs, n):
    """exact E Htilde_g(nu), E h2 term and the law of P_g(nu) for nu iid from a small discrete law."""
    EHt = 0.0
    out_v, out_p = [], []
    for combo in itertools.product(range(len(vals)), repeat=n):
        mu = vals[list(combo)]
        pr = np.prod(probs[list(combo)])
        Ht, m = biased_H(ghat, mu.astype(np.float64))
        EHt += pr * Ht
        out_v.append(m)
        out_p.append(pr)
    Eh2 = sum(p * h2sq(v) for v, p in zip(vals, probs))
    ov = np.array(out_v); op = np.array(out_p)
    key = np.round(ov * 2 ** 40).astype(np.int64)
    u, inv = np.unique(key, return_inverse=True)
    pv = np.bincount(inv, weights=op)
    vv = np.bincount(inv, weights=ov * op) / pv
    return EHt, Eh2, vv, pv


@nb.njit(cache=True)
def mc_level(ghat, inf, pop, nsamp, seed):
    """Monte Carlo: nu_i iid uniform from the population sample; returns Xi samples parts and new population."""
    np.random.seed(seed)
    n = inf.shape[0]
    P = pop.shape[0]
    Ht = np.empty(nsamp)
    newpop = np.empty(nsamp)
    mu = np.empty(n)
    for t in range(nsamp):
        for i in range(n):
            mu[i] = pop[np.random.randint(P)]
        H, m = biased_H(ghat, mu)
        Ht[t] = H
        newpop[t] = m
    Eh2 = 0.0
    for t in range(P):
        Eh2 += h2sq(pop[t])
    Eh2 /= P
    return Ht, Eh2, newpop


@nb.njit(cache=True)
def tilt_weights(pop, target):
    """exponential tilting w_t ~ exp(lam nu_t) with weighted mean = target (the exact mean of the law)."""
    lam = 0.0
    P = pop.shape[0]
    w = np.ones(P)
    for it in range(60):
        m0 = 0.0
        m1 = 0.0
        m2 = 0.0
        for t in range(P):
            e = np.exp(lam * pop[t])
            m0 += e
            m1 += e * pop[t]
            m2 += e * pop[t] * pop[t]
        mean = m1 / m0
        var = m2 / m0 - mean * mean
        if abs(mean - target) < 1e-15 or var <= 0.0:
            break
        lam -= (mean - target) / var
    tot = 0.0
    for t in range(P):
        w[t] = np.exp(lam * pop[t])
        tot += w[t]
    for t in range(P):
        w[t] /= tot
    return w


@nb.njit(cache=True)
def mc_level_tilted(ghat, inf, pop, nsamp, seed, target):
    """as mc_level, but the parent population is first tilted to its exact mean (removes the unstable mode)."""
    np.random.seed(seed)
    n = inf.shape[0]
    P = pop.shape[0]
    w = tilt_weights(pop, target)
    cw = np.cumsum(w)
    Ht = np.empty(nsamp)
    newpop = np.empty(nsamp)
    mu = np.empty(n)
    for t in range(nsamp):
        for i in range(n):
            u = np.random.random() * cw[P - 1]
            j = np.searchsorted(cw, u)
            if j >= P:
                j = P - 1
            mu[i] = pop[j]
        H, m = biased_H(ghat, mu)
        Ht[t] = H
        newpop[t] = m
    Eh2 = 0.0
    for t in range(P):
        Eh2 += w[t] * h2sq(pop[t])
    return Ht, Eh2, newpop


def sample_law(vals, probs, size, rng):
    return rng.choice(vals, size=size, p=probs / probs.sum())


def tower_kappa(g, ng, delta, depth, npop=20000, seed=1, exact_levels=2, verbose=True):
    """kappa_delta(G_k), k = 1..depth.  Level 1 exact; levels <= exact_levels exact if feasible; else Monte Carlo."""
    g = np.asarray(g, dtype=np.int64)
    ghat = fwht(g)
    p = ghat * ghat
    Hg = entropy_bits(p)
    inf = influences(ghat, ng)
    Ig = inf.sum()
    vals, probs = leaf_law(delta)
    rows = []
    kap = 0.0
    pop = None
    rng = np.random.default_rng(seed)
    for k in range(1, depth + 1):
        use_exact = (pop is None) and (len(vals) ** ng <= 3e6) and (k <= exact_levels or len(vals) ** ng <= 2e5)
        if use_exact:
            EHt, Eh2, nv, npb = exact_level(ghat, inf, vals, probs, ng)
            Xi = Hg - EHt + Ig * Eh2
            se = 0.0
            vals, probs = nv, npb
        else:
            if pop is None:
                pop = sample_law(vals, probs, npop, rng)
            Ht, Eh2, newpop = mc_level_tilted(ghat, inf, pop, npop, seed + 17 * k, 0.0)
            Xi = Hg - Ht.mean() + Ig * Eh2
            se = Ht.std() / np.sqrt(len(Ht))
            pop = newpop
        kap += Xi / ((1 - delta) * Ig ** k)
        HI = Hg * (Ig ** k - 1) / ((Ig - 1) * Ig ** k)
        rows.append({"k": k, "Xi": float(Xi), "Xi_se": float(se), "kappa": float(kap),
                     "kappa_se_level": float(se / ((1 - delta) * Ig ** k)), "H_over_I": float(HI)})
        if verbose:
            print(f"  k={k:2d} Xi={Xi:.6f} (+-{se:.1e})  kappa_delta(G_k)={kap:.6f}  H/I(G_k)={HI:.6f}", flush=True)
    return rows, Hg, Ig


if __name__ == "__main__":
    polite()
    mode = sys.argv[1] if len(sys.argv) > 1 else "validate"
    maj3 = np.array([1 if bin(x).count("1") < 2 else -1 for x in range(8)], dtype=np.int64)
    seed4 = np.array([1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1], dtype=np.int64)
    res = {}
    if mode == "validate":
        from mslib import multiscale_summary
        for name, g, ng in (("maj3", maj3, 3), ("seed4", seed4, 4)):
            for delta in (0.25, 0.5, 0.75):
                print(f"{name} delta={delta}")
                rows, Hg, Ig = tower_kappa(g, ng, delta, 3 if ng == 3 else 2, exact_levels=3)
                G2 = compose_tt(g, ng, g, ng)
                out, *_ = multiscale_summary(G2, ng * ng, (delta,), need_trace=False)
                print(f"  brute force kappa_delta(G_2) = {out[f'kappa_{delta}']:.12f}  recursion = {rows[1]['kappa']:.12f}")
                res[f"{name}_{delta}"] = {"rows": rows, "brute_G2": out[f"kappa_{delta}"]}
        # biased children: F = maj3(and2, or2, x) on 5 variables, law of children exact
        and2 = np.array([1, 1, 1, -1], dtype=np.int64)
        or2 = np.array([1, -1, -1, -1], dtype=np.int64)
        N = 1 << 5
        x = np.arange(N)
        c1 = and2[x & 3]; c2 = or2[(x >> 2) & 3]; c3 = np.where((x >> 4) & 1, -1, 1)
        idx = (c1 < 0).astype(int) | ((c2 < 0).astype(int) << 1) | ((c3 < 0).astype(int) << 2)
        F = maj3[idx].astype(np.int64)
        for delta in (0.3, 0.5, 0.8):
            out, *_ = multiscale_summary(F, 5, (delta,), need_trace=False)
            DF = out[f"kappa_{delta}"] * (1 - delta) * out["I"]
            ghat = fwht(maj3)
            kids = [(and2, 2), (or2, 2), (np.array([1, -1], dtype=np.int64), 1)]
            laws, mus, Ds = [], [], []
            for tt, nn in kids:
                Hc = restr_mean_hist(tt, nn)
                laws.append(law_from_hist(Hc, nn, delta))
                fh = fwht(tt)
                mus.append(fh[0])
                o, *_ = multiscale_summary(tt, nn, (delta,), need_trace=False)
                Ds.append(o[f"kappa_{delta}"] * (1 - delta) * o["I"])
            mu = np.array(mus)
            Ht_mu, _ = biased_H(ghat, mu)
            EHt = 0.0
            for combo in itertools.product(*[range(len(l[0])) for l in laws]):
                nu = np.array([laws[i][0][c] for i, c in enumerate(combo)])
                pr = np.prod([laws[i][1][c] for i, c in enumerate(combo)])
                EHt += pr * biased_H(ghat, nu)[0]
            # Lambda_i(mu) = P_mu[i pivotal]
            Lam = []
            for i in range(3):
                tot = 0.0
                for y in range(8):
                    if (y >> i) & 1:
                        continue
                    piv = maj3[y] != maj3[y | (1 << i)]
                    pr = 1.0
                    for j in range(3):
                        if j == i:
                            continue
                        bitj = (y >> j) & 1
                        pr *= (1 + mu[j]) / 2 if bitj == 0 else (1 - mu[j]) / 2
                    tot += pr * piv
                Lam.append(tot)
            rhs = Ht_mu - EHt
            for i in range(3):
                Eh = sum(pp * h2sq(v) for v, pp in zip(*laws[i]))
                rhs += Lam[i] * (Ds[i] + Eh - h2sq(mu[i]))
            print(f"biased composition maj3(and2,or2,x) delta={delta}: brute D = {DF:.14f}  composition law = {rhs:.14f}")
            res[f"biased_{delta}"] = [DF, rhs]
        with open(os.path.join(HERE, "..", "logs", "tower_validate.json"), "w") as fo:
            json.dump(res, fo, indent=1)
    elif mode == "small":
        for name, g, ng in (("maj3", maj3, 3), ("seed4", seed4, 4)):
            for delta in (0.5, 0.25, 0.125, 0.0625, 0.03125, 0.75, 0.9):
                print(f"{name} delta={delta}", flush=True)
                rows, Hg, Ig = tower_kappa(g, ng, delta, 16 if ng == 4 else 22, npop=200000, exact_levels=2 if ng == 4 else 3)
                res[f"{name}_{delta}"] = rows
        with open(os.path.join(HERE, "..", "logs", "tower_small.json"), "w") as fo:
            json.dump(res, fo, indent=1)
