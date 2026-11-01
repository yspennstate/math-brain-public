"""Joint-activation reference for read-k DNFs.
Q1(A) = Z^-1 sum_U lam^|U| 2^-|V(U)| 2^-|V(U)| [A in V(U)],  Z = E_x (1+lam)^{N'(x)}
(N' = number of terms whose variable set is all ones).  Finner: log Z <= mu((1+lam)^k-1)/k * log e.
Bound: H <= h(Var) + Var log Z + sum_{A!=0} P(A) min_{B = V(U) >= A} (|U| log(1/lam) + 2|B|).
Reports the bound over I next to H/I, lam = 1/k, and E[min |V(U)|]/I."""
import numpy as np, numba as nb
from feicore import spectrum, popcounts, polite, entropy
from mincover import random_readk, tt_dnf
polite()

@nb.njit(cache=True)
def min_terms_closure(masks, n):
    N = 1 << n
    m = np.full(N, 1 << 30, dtype=np.int64)
    m[0] = 0
    frontier = np.zeros(N, dtype=np.int64); nf = 1; frontier[0] = 0
    nxt = np.zeros(N, dtype=np.int64)
    d = 0
    while nf > 0:
        d += 1; nn = 0
        for f in range(nf):
            B = frontier[f]
            for mk in masks:
                C = B | mk
                if m[C] > d:
                    m[C] = d; nxt[nn] = C; nn += 1
        for f in range(nn):
            frontier[f] = nxt[f]
        nf = nn
    return m

@nb.njit(cache=True)
def min_superset(best, n):
    a = best.copy()
    for i in range(n):
        bit = 1 << i
        for A in range(1 << n):
            if (A & bit) == 0:
                if a[A | bit] < a[A]:
                    a[A] = a[A | bit]
    return a

def h2(v):
    return 0.0 if v <= 0 or v >= 1 else -(v*np.log2(v) + (1-v)*np.log2(1-v))

if __name__ == "__main__":
    rng = np.random.default_rng(12)
    for n in (14, 16):
        pc = popcounts(n); xs = np.arange(1 << n)
        for k in (2, 3, 4, 6, 8, 10):
            for rep in range(3):
                terms = random_readk(n, k, rng)
                masks = np.array([sum(1 << int(v) for v in V) for V, _ in terms], dtype=np.int64)
                tt = tt_dnf(n, terms); P = spectrum(tt)
                H = entropy(P); I = float((P * pc).sum()); Var = 1 - P[0]
                lam = 1.0 / k
                Np = np.zeros(1 << n)
                for mk in masks:
                    Np += ((xs & mk) == mk)
                logZ = float(np.log2(np.mean((1 + lam) ** Np)))
                mu = float(sum(2.0 ** -popcounts(n)[mk] for mk in masks))
                finner = mu * ((1 + lam) ** k - 1) / k * np.log2(np.e)
                mt = min_terms_closure(masks, n)
                reach = mt < (1 << 30)
                best = np.where(reach, mt * np.log2(1 / lam) + 2.0 * pc, np.inf)
                ms = min_superset(best, n)
                bestV = np.where(reach, pc.astype(float), np.inf)
                msV = min_superset(bestV, n)
                nz = np.nonzero(P[1:] > 0)[0] + 1
                cov = float((P[nz] * ms[nz]).sum()); covV = float((P[nz] * msV[nz]).sum())
                bound = h2(Var) + Var * logZ + cov
                print(f"n={n} k={k:2d} H/I={H/I:5.2f} bound/I={bound/I:6.2f} [h(V)/I={h2(Var)/I:5.2f} VlogZ/I={Var*logZ/I:5.2f} (Finner {Var*finner/I:5.2f}) cover/I={cov/I:6.2f}] E|V(U)|/I={covV/I:5.2f}", flush=True)
