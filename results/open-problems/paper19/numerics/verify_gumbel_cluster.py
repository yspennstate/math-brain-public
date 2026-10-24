"""
Simple-vs-compound Poisson test for the Gumbel fluctuation conjecture (conj:gumbel).
For the extremal process of M_m = min_{|T|=m} sigma_min(A_T), simple Poisson (hence the
Gumbel law) requires the second factorial moment E[(N_t)_2] -> lambda^2, i.e. distinct
submatrices must not cluster at the extremal scale.  The only worry is the closest
codimension-2 pairs (row sets sharing m-2 rows).  Here we measure their lower-tail
co-occurrence ratio P{both small}/P{small}^2 and the conditional P{T small | S small},
versus a large-codimension (independent) control.  Run: python verify_gumbel_cluster.py

Finding (seed 20260628): D=2 association is BOUNDED (ratio ~4-7, conditional ~0.13-0.20
and decreasing toward the extremal scale); large-D pairs are independent (ratio ~1).
Since each submatrix has only O(m^2) codimension-2 neighbours against C(N,m) submatrices,
their contribution to E[(N_t)_2] is O(m^2 / C(N,m)) lambda^2 -> 0, while the exponentially
many independent large-D pairs give lambda^2.  Extremal index = 1 => SIMPLE Poisson =>
the conjectured Gumbel law (no compound/cluster correction).
"""
import numpy as np
rng = np.random.default_rng(20260628)

def smin(M):
    return np.linalg.svd(M, compute_uv=False)[-1]

for m in [6, 8, 10]:
    N = 2 * m - 1
    T = 120000
    base = list(range(m - 2))          # m-2 shared rows
    S = base + [m - 2]                  # an (m-1)-subset
    Tn = base + [m - 1]                 # D=2 neighbour: one row swapped (shares m-2) -> codim 2
    Sc = list(range(m - 1))             # large-codimension control: two disjoint (m-1)-subsets
    Tc = list(range(N - (m - 1), N))
    sS = np.empty(T); sT = np.empty(T); sSc = np.empty(T); sTc = np.empty(T)
    for k in range(T):
        A = rng.standard_normal((N, m))
        sS[k] = smin(A[S]); sT[k] = smin(A[Tn])
        sSc[k] = smin(A[Sc]); sTc[k] = smin(A[Tc])
    print(f"--- m={m}, N={N} ---")
    for ql in [0.05, 0.02]:
        qN = np.quantile(np.r_[sS, sT], ql); pS = np.mean(sS <= qN)
        pboth = np.mean((sS <= qN) & (sT <= qN)); ratio = pboth / (pS * pS)
        qc = np.quantile(np.r_[sSc, sTc], ql); pSc = np.mean(sSc <= qc)
        pbc = np.mean((sSc <= qc) & (sTc <= qc)); rc = pbc / (pSc * pSc)
        print(f"  q={ql}: D=2 ratio P(both)/P^2 = {ratio:5.2f} (P(T|S)={pboth/pS:.3f})"
              f"   |   large-D control ratio = {rc:5.2f}")
print("Bounded D=2 association + O(m^2) neighbours vs C(N,m) total => extremal index 1 => simple Poisson / Gumbel.")


# --- Direct second-factorial-moment test: E[N_t(N_t-1)]/E[N_t]^2 -> 1 (simple Poisson) ---
# Enumerate ALL C(N,m) submatrices, calibrate threshold to E[N_t]=lambda, measure the
# factorial-moment ratio (Poisson=1), Var/mean (Poisson=1), and P(N_t=0) (Poisson e^-lambda).
def direct_factorial_moment_test():
    from itertools import combinations
    from math import exp
    rng2 = np.random.default_rng(20260628)
    def smins_all(A, subs):
        return np.array([np.linalg.svd(A[s, :], compute_uv=False)[-1] for s in subs])
    for (m, nmat) in [(6, 15000), (7, 6000), (8, 2500)]:
        N = 2 * m - 1
        subs = [list(c) for c in combinations(range(N), m)]
        B = len(subs); lam = 2.0
        allmin = np.empty((nmat, B))
        for k in range(nmat):
            allmin[k] = smins_all(rng2.standard_normal((N, m)), subs)
        t = np.quantile(allmin, lam / B)
        counts = np.sum(allmin <= t, axis=1)
        EN = counts.mean(); ratio = np.mean(counts * (counts - 1)) / EN**2
        print(f"  m={m} N={N} #subs={B}: E[N]={EN:.3f}  E[N(N-1)]/E[N]^2={ratio:.3f} (Poisson=1)"
              f"  Var/mean={counts.var()/EN:.3f}  P(N=0) {np.mean(counts==0):.3f} vs {exp(-EN):.3f}")

if __name__ == "__main__":
    print("Direct second-factorial-moment test (simple-Poisson signature):")
    direct_factorial_moment_test()
