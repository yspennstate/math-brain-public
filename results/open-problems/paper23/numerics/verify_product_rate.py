"""Small-N test of the product min-over-supports least-singular-value rate.

Model: A_1, A_2 iid N x N, entries N(0,1/N). Supports S_0, S_1, S_2 of size n = N/2.
k=1 statistic: min over (S_0,S_1) of smin(A_1[S_1,S_0]).
k=2 statistic: min over (S_0,S_1,S_2) of smin(A_2[S_2,S_1] @ A_1[S_1,S_0]).

Rates rho_k = -(1/N) log min. Predictions: rho_1 -> 2H(1/2)=1.386;
conj:B4 (Shmalo, paper22) guessed rho_2 -> 2H = 1.386; the cascade theorem of this
paper says rho_k -> (k+1)H(alpha)/dF, so rho_2 -> 3H = 2.079.
Discriminator: rho_2/rho_1 -> 1.0 (B4) vs 1.5 (cascade).

For N=8 the exhaustive min over all support triples is computed directly.
For N=10 the exhaustive k=1 min is computed; for k=2 the min is estimated by the
greedy cascade (two-sided-optimal F_1, then one-sided-optimal S_2) which upper-bounds
the exhaustive min, plus a random sample of triples as a sanity floor. The theorem's
achievability is exactly the cascade, so cascade ~ exhaustive is the content.
"""

import itertools
import time

import numpy as np


def all_subsets(N, n):
    return np.array([c for c in itertools.combinations(range(N), n)])


def build_blocks(A, idx):
    # blocks[b_rows, b_cols] = A[idx[b_rows]][:, idx[b_cols]]  -> (m, m, n, n)
    R = A[idx, :]                      # (m, n, N)
    B = R[:, :, idx]                   # (m, n, m, n)
    return np.transpose(B, (0, 2, 1, 3))


def smin_stack(mats):
    return np.linalg.svd(mats, compute_uv=False)[..., -1]


def exhaustive_k1(blocks1, m, n):
    sv = smin_stack(blocks1.reshape(m * m, n, n)).reshape(m, m)  # [b1, b0]
    b1, b0 = np.unravel_index(sv.argmin(), sv.shape)
    return sv.min(), (b0, b1)


def cascade_k2(blocks1, A2, idx, arg1, n):
    b0, b1 = arg1
    F1 = blocks1[b1, b0]               # two-sided optimal single factor
    F2s = A2[idx, :][:, :, idx[b1]]    # (m, n, n): A2[S2, S1_opt] over all S2
    prods = np.einsum('aij,jk->aik', F2s, F1)
    return smin_stack(prods).min()


def exhaustive_k2(blocks1, A2, idx, m, n):
    R2 = A2[idx, :]                    # (m, n, N)
    best = np.inf
    for b1 in range(m):
        F1s = blocks1[b1]              # (b0, n, n)
        F2s = R2[:, :, idx[b1]]        # (b2, n, n)
        P = np.einsum('aij,bjk->abik', F2s, F1s).reshape(m * m, n, n)
        best = min(best, smin_stack(P).min())
    return best


def sample_k2(blocks1, A2, idx, m, n, nsamp, rng):
    R2 = A2[idx, :]
    best = np.inf
    for _ in range(nsamp):
        b0, b1, b2 = rng.integers(0, m, 3)
        P = A2[np.ix_(idx[b2], idx[b1])] @ blocks1[b1, b0]
        best = min(best, smin_stack(P))
    return best


def run(N, ntr, exhaustive_k2_flag, base_seed):
    H = np.log(2.0)
    n = N // 2
    idx = all_subsets(N, n)
    m = len(idx)
    r1, r2c, r2e = [], [], []
    for t in range(ntr):
        rng = np.random.default_rng(base_seed + t)
        A1 = rng.normal(0.0, 1.0 / np.sqrt(N), (N, N))
        A2 = rng.normal(0.0, 1.0 / np.sqrt(N), (N, N))
        blocks1 = build_blocks(A1, idx)
        min1, arg1 = exhaustive_k1(blocks1, m, n)
        casc = cascade_k2(blocks1, A2, idx, arg1, n)
        r1.append(-np.log(min1) / N)
        r2c.append(-np.log(casc) / N)
        if exhaustive_k2_flag:
            mine = exhaustive_k2(blocks1, A2, idx, m, n)
            r2e.append(-np.log(mine) / N)
    r1 = np.array(r1); r2c = np.array(r2c)
    print(f"N={N} m={m} trials={ntr}")
    print(f"  rho_1 (exhaustive)     mean {r1.mean():.3f}   2H={2*H:.3f}   {np.round(r1,3)}")
    print(f"  rho_2 (cascade, achiev) mean {r2c.mean():.3f}   3H={3*H:.3f}   {np.round(r2c,3)}")
    if exhaustive_k2_flag:
        r2e = np.array(r2e)
        print(f"  rho_2 (exhaustive)     mean {r2e.mean():.3f}   3H={3*H:.3f}   {np.round(r2e,3)}")
        print(f"  ratio rho2/rho1 (exh)  mean {(r2e/r1).mean():.3f}   (B4=1.0, cascade=1.5)")
        print(f"  cascade vs exhaustive gap (rate): mean {np.mean(r2c-r2e):.3f} (cascade <= exhaustive so >=0)")
    print(f"  ratio rho2/rho1 (casc) mean {(r2c/r1).mean():.3f}   (B4=1.0, cascade=1.5)")


def main():
    t0 = time.time()
    run(8, 8, True, 8000)
    print()
    run(10, 4, False, 10000)
    print(f"\ntotal {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
