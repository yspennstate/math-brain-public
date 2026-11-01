"""E4: cell selectors with pairwise ORTHOGONAL (not Fourier-disjoint) leaves.

F(x,y) = sum_k 1_{A_k}(x) G_k(y), arbitrary partition {A_k} of the selector cube, E[G_k G_l] = 0 (k != l).
 T1 (proved):        H(F) <= 2 H(p) + sum_k p_k [H(q_k) + H(G_k)]
 T1-sharp (open):    H(F) <=   H(p) + sum_k p_k [H(q_k) + H(G_k)]      (the Fourier-disjoint identity as a bound)
 marginal identity:  S-marginal of Fhat^2 = sum_k ahat_k^2 (checked), I_sel = (1/4) sum_k I(h_k).
Floating point evidence.
"""
import itertools
import numpy as np
from fei_lib import fwht_int, fwht_float, entropy_from_W, entropy_probs, popcounts


def leaf_family(kind, m, n, rng):
    N = 1 << n
    if kind == 'chi_shift':          # G_k = f * chi_{U_k}: pairwise orthogonal, spectra = shifts of fhat^2
        f = rng.choice([-1, 1], size=N)
        Us = rng.choice(N, size=m, replace=False)
        idx = np.arange(N)
        out = []
        for U in Us:
            par = np.zeros(N, dtype=np.int64)
            for j in range(n):
                if (U >> j) & 1:
                    par ^= (idx >> j) & 1
            out.append(f * (1 - 2 * par))
        return out
    if kind == 'bent_shift':         # maximal spectral overlap: bent * characters
        idx = np.arange(N)
        par = np.zeros(N, dtype=np.int64)
        for j in range(0, n - 1, 2):
            par ^= ((idx >> j) & 1) & ((idx >> (j + 1)) & 1)
        f = 1 - 2 * par
        Us = rng.choice(N, size=m, replace=False)
        out = []
        for U in Us:
            p2 = np.zeros(N, dtype=np.int64)
            for j in range(n):
                if (U >> j) & 1:
                    p2 ^= (idx >> j) & 1
            out.append(f * (1 - 2 * p2))
        return out
    # rejection sampling of random pairwise orthogonal functions
    out = []
    tries = 0
    while len(out) < m and tries < 200000:
        tries += 1
        g = rng.choice([-1, 1], size=N)
        if all(int(np.dot(g, h)) == 0 for h in out):
            out.append(g)
    return out if len(out) == m else None


def random_partition(a, m, rng):
    N = 1 << a
    lab = rng.integers(0, m, size=N)
    # make sure every label used
    perm = rng.permutation(N)
    for k in range(m):
        lab[perm[k]] = k
    return lab


def analyse(lab, leaves, a, n):
    N = 1 << a
    m = len(leaves)
    B = np.array([leaves[lab[b]] for b in range(N)])
    F = B.T.reshape(-1)
    W = fwht_int(F)
    HF = entropy_from_W(W, a + n)
    P = (W.astype(float) ** 2 / float(4 ** (a + n))).reshape(1 << n, N)
    mu = P.sum(axis=0)
    p = np.array([np.mean(lab == k) for k in range(m)])
    Hq = []
    mu_inc = np.zeros(N)
    for k in range(m):
        ak = (lab == k).astype(float)
        ah = fwht_float(ak) / N
        mu_inc += ah ** 2
        Hq.append(entropy_probs(ah ** 2 / p[k]))
    HG = [entropy_from_W(fwht_int(g), n) for g in leaves]
    Hp = entropy_probs(p)
    base = Hp + float(np.sum(p * (np.array(Hq) + np.array(HG))))
    return HF, base, Hp, float(np.max(np.abs(mu - mu_inc)))


if __name__ == '__main__':
    rng = np.random.default_rng(11)
    worst_sharp = -1e9
    worst_T1 = -1e9
    worst_mu = 0
    rec = None
    for trial in range(4000):
        a = int(rng.integers(1, 5))
        n = int(rng.integers(2, 6)) if a <= 3 else int(rng.integers(2, 5))
        m = int(rng.integers(2, min(1 << a, 1 << n) + 1))
        kind = ['chi_shift', 'bent_shift', 'random'][int(rng.integers(3))]
        if kind == 'bent_shift' and n % 2 == 1:
            kind = 'chi_shift'
        if kind == 'random' and (n > 4 or m > 6):
            kind = 'chi_shift'
        leaves = leaf_family(kind, m, n, rng)
        if leaves is None:
            continue
        lab = random_partition(a, m, rng)
        HF, base, Hp, dmu = analyse(lab, leaves, a, n)
        worst_mu = max(worst_mu, dmu)
        worst_T1 = max(worst_T1, HF - (base + Hp))
        if HF - base > worst_sharp:
            worst_sharp = HF - base
            rec = (a, n, m, kind, lab.tolist(), HF, base)
    print('max |mu - sum ahat^2| =', worst_mu)
    print('max H(F) - T1 bound   =', worst_T1)
    print('max H(F) - T1-sharp   =', worst_sharp)
    print('record:', rec)
