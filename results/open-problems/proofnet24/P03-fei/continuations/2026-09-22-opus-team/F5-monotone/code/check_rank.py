"""Stress test of the rank argument (Theorem B, FEI for all LTFs).

For f = sign(w.x - theta), rank coordinates by |w| (1 = heaviest), U_i = {j != i : |w_j| >= |w_i|},
N_i = |U_i| + 1, g_i = D_i f.  The proof uses, for every i,
  (P1) Stab^{U_i}_{1-c/N_i}[g_i] <= (2/sqrt(pi)) c^{-1/2} Inf_i   (0 < c <= N_i)
  (P2) E_{T ~ g_i^2/Inf_i} ln(N_i/(|T cap U_i|+1)) <= 2 ln B + 2 = 4.1511,  B = 3 sqrt(3/pi)
and then Sigma := sum_S fhat(S)^2 sum_{i in S} ln+(r(i)/|S|) <= 4.1511 I,
H(S | |S|) <= [ln(e a/(a-1)) I + a Sigma]/ln 2, H(|S|) <= 3 I.
Prints worst value/bound ratios; each must be <= 1.
"""
import sys, math
import numpy as np
import numba as nb
from ltf_core import ltf_table, spectrum, HI, popcount

GAMMA = 1.0   # U_i = {j != i : |w_j| >= GAMMA |w_i|}; covering number kappa = ceil(1/GAMMA)
KAPPA = math.ceil(1 / GAMMA - 1e-12)
B = 3 * math.sqrt(3 / math.pi) * KAPPA   # final constant of Theorem 1 (choice c = N/(3K) in Lemma 3)
LOGB = 2 * math.log(B) + 2


@nb.njit(cache=True)
def per_coord(c, n, i, umask, N, cs):
    b = 1 << i
    stab = np.zeros(cs.shape[0])
    elog = 0.0
    inf = 0.0
    for T in range(c.shape[0]):
        if T & b:
            continue
        v = c[T | b]
        w = v * v
        if w < 1e-300:
            continue
        k = popcount(T & umask)
        inf += w
        elog += w * np.log(N / (k + 1.0))
        for q in range(cs.shape[0]):
            stab[q] += w * (1.0 - cs[q] / N) ** k
    return stab, elog, inf


@nb.njit(cache=True)
def sigma_and_cond(c, n, rank):
    """Sigma = sum_S c_S^2 sum_{i in S} ln+(rank_i/|S|); H(|S|) (bits); H(S | |S|) (bits)."""
    N = c.shape[0]
    Wk = np.zeros(n + 1)
    Hjoint = 0.0
    sig = 0.0
    for S in range(N):
        w = c[S] * c[S]
        if w < 1e-300:
            continue
        k = popcount(S)
        Wk[k] += w
        Hjoint -= w * np.log2(w)
        if k > 0:
            s = 0.0
            for i in range(n):
                if S & (1 << i):
                    r = rank[i]
                    if r > k:
                        s += np.log(r / k)
            sig += w * s
    Hlev = 0.0
    for k in range(n + 1):
        if Wk[k] > 1e-300:
            Hlev -= Wk[k] * np.log2(Wk[k])
    return sig, Hlev, Hjoint - Hlev


def analyse(w, theta, alpha=None, cs=np.array([0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0])):
    if alpha is None:
        alpha = (1 + math.sqrt(1 + 4 / LOGB)) / 2
    w = np.asarray(w, float)
    n = len(w)
    f = ltf_table(w, theta)
    c = spectrum(f)
    H, I = HI(c)
    if I < 1e-14:
        return None
    a = np.abs(w)
    order = np.argsort(-a, kind="stable")
    rank = np.empty(n, np.int64)
    rank[order] = np.arange(1, n + 1)
    worst_p1 = 0.0
    worst_p2 = 0.0
    for i in range(n):
        if a[i] == 0:
            continue
        U = [j for j in range(n) if j != i and a[j] >= GAMMA * a[i] - 1e-12]
        N = len(U) + 1
        if N < 2:
            continue
        um = sum(1 << j for j in U)
        ok = cs[cs <= N].astype(np.float64)
        stab, elog, inf = per_coord(c, n, i, um, float(N), ok)
        if inf < 1e-15:
            continue
        for q, cc in enumerate(ok):
            worst_p1 = max(worst_p1, stab[q] / ((2 * KAPPA / math.sqrt(math.pi)) / math.sqrt(cc) * inf))
        worst_p2 = max(worst_p2, (elog / inf) / LOGB)
    sig, Hlev, Hcond = sigma_and_cond(c, n, rank)
    bound_cond = (math.log(math.e * alpha / (alpha - 1)) * I + alpha * sig) / math.log(2)
    total_bound = 3 * I + (math.log(math.e * alpha / (alpha - 1)) + alpha * LOGB) / math.log(2) * I
    return dict(H=H, I=I, p1=worst_p1, p2=worst_p2, sig=sig / (LOGB * I), lev=Hlev / (3 * I),
                cond=Hcond / bound_cond, tot=H / total_bound, ratio=H / I)


if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    ntr = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    rng = np.random.default_rng(seed)
    keys = ["p1", "p2", "sig", "lev", "cond", "tot"]
    worst = {k: (0.0, None) for k in keys}
    for tr in range(ntr):
        n = int(rng.integers(3, 16))
        kind = tr % 7
        if kind == 0:
            w = rng.uniform(1, 2, n)
        elif kind == 1:
            w = 2.0 ** (-np.arange(n)) * rng.uniform(0.9, 1.1, n)       # chain-like
        elif kind == 2:
            w = rng.exponential(size=n) ** 3                             # heavy tail
        elif kind == 3:
            w = np.abs(rng.standard_normal(n)) + 1e-3
        elif kind == 4:
            w = np.concatenate([rng.uniform(3, 6, max(1, n // 4)), rng.uniform(0.2, 0.3, n - max(1, n // 4))])
        elif kind == 5:
            w = rng.integers(1, 6, n).astype(float)
        else:
            w = 1.5 ** (-np.arange(n)) * rng.uniform(0.95, 1.05, n)
        s = np.linalg.norm(w)
        theta = float(rng.normal() * s * rng.choice([0.1, 0.7, 1.5, 2.5])) + 1e-9
        r = analyse(w, theta)
        if r is None:
            continue
        for k in keys:
            if r[k] > worst[k][0]:
                worst[k] = (r[k], (np.round(w, 4).tolist(), round(theta, 4), round(r['ratio'], 4)))
    for k in keys:
        print("worst %-4s value/bound = %.4f  at %s" % (k, worst[k][0], worst[k][1]), flush=True)
