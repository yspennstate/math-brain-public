"""Location term on towers.  L_delta(f) = E_J H(S minus J | S cap J) = H(f) - E_J H(S cap J).

Composition law (balanced children): with q_i = P(S_i cap J_i = empty | J_i) (a function of J_i only),
T ~ spectral law of G and R an independent random set with P(i in R) = 1 - q_i,
    L_delta(F) = sum_i Inf_i(G) [L_delta(f_i) + E h2(q_i)] + H(G) - E H(T cap R),
and q_F = sum_T p_G(T) prod_{i in T} q_i.  Tower: L(G_k) = I(g) L(G_{k-1}) + Y_k.
The mixing term is M = D - L.
"""
import sys, os, json, time, itertools
import numpy as np
import numba as nb
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mslib import polite, fwht, entropy_bits, influences, size_weights, per_size_sums


@nb.njit(cache=True)
def thin_H(pg, q):
    """entropy of T cap R (T ~ pg, P(i in R) = 1 - q_i) and P(T cap R empty) = sum_T pg(T) prod_{i in T} q_i."""
    N = pg.shape[0]
    n = q.shape[0]
    a = pg.copy()
    for i in range(n):
        bit = 1 << i
        qi = q[i]
        for T in range(N):
            if (T & bit) == 0:
                u = a[T]
                v = a[T | bit]
                a[T] = u + qi * v
                a[T | bit] = (1.0 - qi) * v
    H = 0.0
    for T in range(N):
        w = a[T]
        if w > 1e-300:
            H -= w * np.log2(w)
    return H, a[0]


@nb.njit(cache=True)
def h2(q):
    if q <= 0.0 or q >= 1.0:
        return 0.0
    return -q * np.log2(q) - (1 - q) * np.log2(1 - q)


@nb.njit(cache=True)
def zeta_empty_trace(p, n):
    """q[J] = sum_{S subset of J^c} p_S for every mask J."""
    N = p.shape[0]
    a = p.copy()                        # a[U] <- sum_{S subset U} p_S
    for i in range(n):
        bit = 1 << i
        for U in range(N):
            if U & bit:
                a[U] += a[U ^ bit]
    q = np.empty(N)
    full = N - 1
    for J in range(N):
        q[J] = a[full ^ J]
    return q


@nb.njit(cache=True)
def mc_loc_level(pg, n, pop, target, nsamp, seed):
    np.random.seed(seed)
    P = pop.shape[0]
    # tilt the population of q to its exact mean
    lam = 0.0
    for it in range(60):
        m0 = 0.0; m1 = 0.0; m2 = 0.0
        for t in range(P):
            e = np.exp(lam * pop[t]); m0 += e; m1 += e * pop[t]; m2 += e * pop[t] * pop[t]
        mean = m1 / m0; var = m2 / m0 - mean * mean
        if abs(mean - target) < 1e-15 or var <= 0.0:
            break
        lam -= (mean - target) / var
    w = np.empty(P); tot = 0.0
    for t in range(P):
        w[t] = np.exp(lam * pop[t]); tot += w[t]
    for t in range(P):
        w[t] /= tot
    cw = np.cumsum(w)
    Ht = np.empty(nsamp); newpop = np.empty(nsamp); q = np.empty(n)
    for t in range(nsamp):
        for i in range(n):
            j = np.searchsorted(cw, np.random.random() * cw[P - 1])
            if j >= P:
                j = P - 1
            q[i] = pop[j]
        H, Q = thin_H(pg, q)
        Ht[t] = H; newpop[t] = Q
    Eh2 = 0.0
    for t in range(P):
        Eh2 += w[t] * h2(pop[t])
    return Ht, Eh2, newpop


def phi_gen(pg, pc, x):
    return float(np.sum(pg * x ** pc))


def exact_loc_level(pg, vals, probs, n):
    EH = 0.0; ov = []; op = []
    for combo in itertools.product(range(len(vals)), repeat=n):
        q = vals[list(combo)].astype(np.float64); pr = float(np.prod(probs[list(combo)]))
        H, Q = thin_H(pg, q); EH += pr * H; ov.append(Q); op.append(pr)
    Eh2 = float(sum(p * h2(v) for v, p in zip(vals, probs)))
    ov = np.array(ov); op = np.array(op)
    key = np.round(ov * 2 ** 40).astype(np.int64)
    u, inv = np.unique(key, return_inverse=True)
    pv = np.bincount(inv, weights=op); vv = np.bincount(inv, weights=ov * op) / pv
    return EH, Eh2, vv, pv


def tower_location(g, ng, delta, depth, npop=20000, seed=5, level1=None, qlaw1=None, exact_levels=3, verbose=True):
    g = np.asarray(g, dtype=np.int64)
    ghat = fwht(g); pg = ghat * ghat
    Hg = entropy_bits(pg); Ig = influences(ghat, ng).sum()
    pc = np.array([bin(T).count("1") for T in range(1 << ng)])
    vals, probs = np.array([0.0, 1.0]), np.array([delta, 1 - delta])       # leaf: q = 0 if free, 1 if fixed
    Eq = 1 - delta
    rows = []; lam = 0.0; pop = None
    rng = np.random.default_rng(seed)
    for k in range(1, depth + 1):
        target_parent = Eq
        if k == 1 and level1 is not None:
            Y = level1                              # exact L_delta(g) supplied
            vals, probs = qlaw1
            se = 0.0
        else:
            use_exact = pop is None and len(vals) ** ng <= 3e6 and (k <= exact_levels or len(vals) ** ng <= 2e5)
            if use_exact:
                EH, Eh2, vals2, probs2 = exact_loc_level(pg, vals, probs, ng)
                Y = Hg - EH + Ig * Eh2; se = 0.0
                vals, probs = vals2, probs2
            else:
                if pop is None:
                    pop = rng.choice(vals, size=npop, p=probs / probs.sum())
                Ht, Eh2, newpop = mc_loc_level(pg, ng, pop, target_parent, npop, seed + 31 * k)
                if k == 2 and qlaw1 is not None:
                    Eh2 = float(sum(p * h2(v) for v, p in zip(*qlaw1)))
                Y = Hg - Ht.mean() + Ig * Eh2; se = Ht.std() / np.sqrt(npop)
                pop = newpop
        Eq = phi_gen(pg, pc, Eq)
        lam += Y / ((1 - delta) * Ig ** k)
        rows.append({"k": k, "Y": float(Y), "se": float(se), "lambda": float(lam)})
        if verbose:
            print(f"  k={k:2d} Y={Y:.6f} (se {se:.1e})  L/((1-d)I)(G_k) = {lam:.6f}", flush=True)
    return rows


if __name__ == "__main__":
    polite()
    mode = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if mode == "validate":
        from mslib import multiscale_summary
        from tower import compose_tt
        maj3 = np.array([1 if bin(x).count("1") < 2 else -1 for x in range(8)], dtype=np.int64)
        seed4 = np.array([1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1], dtype=np.int64)
        for name, g, ng in (("maj3", maj3, 3), ("seed4", seed4, 4)):
            for d in (0.3, 0.5, 0.8):
                rows = tower_location(g, ng, d, 2, verbose=False)
                G2 = compose_tt(g, ng, g, ng)
                out, *_ = multiscale_summary(G2, ng * ng, (d,), need_trace=True)
                out1, *_ = multiscale_summary(g, ng, (d,), need_trace=True)
                print(f"{name} delta={d}: L(G_1) recursion {rows[0]['lambda']:.12f} brute {out1[f'L_{d}']:.12f} | "
                      f"L(G_2) recursion {rows[1]['lambda']:.12f} brute {out[f'L_{d}']:.12f}")
    elif mode == "numaro":
        npop = int(sys.argv[2]); depth = int(sys.argv[3]); d = float(sys.argv[4])
        gt = np.load(os.path.join(HERE, "..", "..", "inputs", "numaro18_pm1_table.npy")).astype(np.int64)
        n = 18
        fh = fwht(gt); p = fh * fh
        prof = np.load(os.path.join(HERE, "..", "logs", "numaro18_profile.npz"))
        w = size_weights(n, d)
        L1 = float(prof["H"] - (w * prof["cHT"]).sum())
        q = zeta_empty_trace(p, n)
        pcJ = np.array([bin(J).count("1") for J in range(1 << n)])
        wJ = d ** pcJ * (1 - d) ** (n - pcJ)
        key = np.round(q * 2 ** 40).astype(np.int64)
        u, inv = np.unique(key, return_inverse=True)
        pv = np.bincount(inv, weights=wJ); vv = np.bincount(inv, weights=q * wJ) / pv
        print(f"delta={d}: L_delta(g) exact = {L1:.9f}; q-law {len(vv)} atoms, E q = {np.dot(vv, pv):.9f}", flush=True)
        rows = tower_location(gt, n, d, depth, npop=npop, level1=L1, qlaw1=(vv, pv))
        json.dump(rows, open(os.path.join(HERE, "..", "logs", f"location_numaro_{d}.json"), "w"), indent=1)
