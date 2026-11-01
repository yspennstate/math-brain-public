"""Lemma 1 (per coordinate, per level) and the level-localization constant C(c).

Lemma 1: for coordinate i and level j >= 0, B^(i)_j := sum_{|U|=j, i notin U} phi(p(U), p(U+i)) <= d log2(e/d),
         d = d_{j,i} = sum_{|T| = j+1, T contains i} p(T)  (level-j Fourier weight of D_i f).
Localization: Loc_c(f) := sum_i sum_{j <= c ln(1/eps_i)} B^(i)_j <= C(c) I(f) for c < 1/2, where
         C(c) = sup_eps (1/eps) sum_{j=0}^{floor(c ln(1/eps))} psi(eps rho_{j+1}(eps)),  psi(x) = x log2(e/x).
Usage: python check_lemma1.py OUTJSON
"""
import os, sys, json, math, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import check_levels as CL
from per_level_constants import rho_hc

LOG2E = 1 / math.log(2)
QS = np.concatenate([2 + np.exp(np.linspace(-12, 0, 1500)), np.linspace(3, 200, 1500)])


def rho_j1(eps, j):
    """upper bound on d_{j,i}/eps_i for level j (= k-1)."""
    eps = np.atleast_1d(eps)
    if j == 0:
        return np.minimum(1.0, eps)
    r = rho_hc(eps, j + 1, QS)
    if j == 1:
        r = np.minimum(r, np.minimum(1.0, 2 * eps * np.log(2 / eps)))
    return r


def psi(x):
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    m = x > 0
    out[m] = x[m] * np.log2(math.e / x[m])
    return out


def log_rho_j1(L, j):
    """log of the upper bound on d_{j,i}/eps_i at ln(1/eps) = L (scalar), capped at log 1 = 0."""
    if j == 0:
        return -L
    lr = float(np.min(-L * (1 - 2 / QS) + j * np.log(QS - 1)))
    if j == 1 and L > 0:
        eps = math.exp(-L)
        lr = min(lr, math.log(2 * eps * math.log(2 / eps)))
    return min(0.0, lr)


def loc_constant(c):
    """C(c) = sup_eps sum_{j <= c ln(1/eps)} rho_j (log2 e + log2(1/eps) + log2(1/rho_j)), computed in log space."""
    best = (0.0, 0.0)
    for L in np.concatenate([np.linspace(0, 40, 8001), np.linspace(40, 400, 3601)]):
        J = int(math.floor(c * L + 1e-12))
        tot = 0.0
        for j in range(J + 1):
            lr = log_rho_j1(L, j)
            tot += math.exp(lr) * (LOG2E + L * LOG2E - lr * LOG2E)
        if tot > best[0]:
            best = (tot, float(L))
    return best


def per_coord_level(tt):
    R = CL.analyse(tt)
    p, n = R["p"], R["n"]
    pc, idx0 = CL.tables(n)
    M = p.shape[0]
    Bij = np.zeros((M, n, n))
    dij = np.zeros((M, n, n))
    for i in range(n):
        z0 = idx0[i]
        z1 = z0 | (1 << i)
        a, b = p[:, z0], p[:, z1]
        ph = CL.eta(a) + CL.eta(b) - CL.eta(a + b)
        ph[ph < 0] = 0
        lev = pc[z0]
        for j in range(n):
            s = lev == j
            Bij[:, i, j] = ph[:, s].sum(1)
            dij[:, i, j] = b[:, s].sum(1)
    return R, Bij, dij


def main():
    out = {}
    t0 = time.time()
    cs = (0.1, 0.2, 0.3, 0.4, 0.45)
    Cc = {}
    for c in cs:
        v, ln = loc_constant(c)
        Cc[c] = v
        out[f"C({c})"] = dict(value=v, at_ln_inv_eps=ln)
    rng = np.random.default_rng(7)
    batches = [CL.all_functions(n) for n in (2, 3, 4)]
    for n in (5, 6, 7, 8):
        batches.append((1 - 2 * rng.integers(0, 2, (200, 1 << n))).astype(np.int8))
        batches.append(CL.random_dt(n, 5, rng, 60))
        batches.append(CL.random_dnf(n, 2, 3, rng, 60))
        batches.append(CL.random_ltf(n, rng, 60))
        batches.append(np.where(rng.random((200, 1 << n)) < 0.1, -1, 1).astype(np.int8))
    for m in (2, 4, 6, 8):
        batches.append(CL.fam_bent_times_x0(m))
    for n in (8, 10):
        for t in range(n // 2 + 1):
            batches.append(CL.fam_threshold(n, t))
    for (w, s) in ((2, 3), (3, 2), (2, 4), (3, 3), (4, 2)):
        batches.append(CL.fam_tribes(w, s))
    worst_l1 = 0.0
    worst_l1_where = None
    worst_loc = {c: 0.0 for c in cs}
    worst_level = {}
    viol = 0
    count = 0
    for bt in batches:
        R, Bij, dij = per_coord_level(bt)
        count += bt.shape[0]
        bound = psi(dij)
        with np.errstate(divide="ignore", invalid="ignore"):
            r = np.where(bound > 1e-14, Bij / np.where(bound > 1e-14, bound, 1), 0)
        viol += int(np.sum(Bij > bound + 1e-10))
        if r.max() > worst_l1:
            worst_l1 = float(r.max())
            k = np.unravel_index(int(r.argmax()), r.shape)
            worst_l1_where = dict(n=int(R["n"]), coord=int(k[1]), level=int(k[2]),
                                  tt="".join("1" if v < 0 else "0" for v in bt[k[0]]))
        I = R["I"]
        eps = R["eps"]
        for c in cs:
            with np.errstate(divide="ignore"):
                J = np.floor(c * np.log(1 / np.where(eps > 0, eps, 1)) + 1e-12)
            levels = np.arange(R["n"])[None, None, :]
            mask = levels <= J[:, :, None]
            loc = (Bij * mask).sum((1, 2))
            rr = np.where(I > 1e-12, loc / np.where(I > 1e-12, I, 1), 0)
            worst_loc[c] = max(worst_loc[c], float(rr.max()))
        Bk = Bij.sum(1)
        for j in range(R["n"]):
            rr = np.where(I > 1e-12, Bk[:, j] / np.where(I > 1e-12, I, 1), 0)
            worst_level[j] = max(worst_level.get(j, 0.0), float(rr.max()))
    out.update(count=count, lemma1_violations=viol, lemma1_max_ratio=worst_l1, lemma1_max_where=worst_l1_where,
               loc_max_ratio={str(c): worst_loc[c] for c in cs}, max_Bj_over_I={str(j): v for j, v in worst_level.items()},
               seconds=time.time() - t0)
    json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), indent=1)
    print("count", count, "Lemma 1 violations", viol, "max B/bound", round(worst_l1, 4), worst_l1_where)
    print("C(c):", {c: round(Cc[c], 3) for c in cs})
    print("max Loc_c/I seen:", {c: round(worst_loc[c], 3) for c in cs})
    print("max B_j/I seen:", {j: round(v, 3) for j, v in worst_level.items()})


if __name__ == "__main__":
    main()
