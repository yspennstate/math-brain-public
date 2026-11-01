"""G0013 (Catalano-Lavenant) exhaustive discrete search, lane claude-q2-attack-0912, 2026-09-12.

Same discrete problem as prob1000_lean_20260908/g0013_permutation_search.py: marginals uniform on
{(k+1/2)/n}, couplings = doubly stochastic / n, and since W_2^2(.,Q) is convex the maximum over the
Birkhoff polytope sits at a permutation matrix.  W_2^2(pi_sigma, U_n (x) U_n) = T(sigma)/n^4 with

    T(sigma) = min over maps f from the n^2 grid cells onto the n atoms, n cells per atom, of
               sum over cells of (i - f)^2 + (j - sigma(f))^2 ,

an integer transportation problem with unit sources and capacity n, so its LP optimum is attained at
an integral f and equals a linear assignment on the n^2 x n^2 matrix that repeats each atom n times.
That is ~10^3 times faster than the n^3-variable LP, which is what puts n = 8 and n = 9 in reach.

Identity used for the cross-check (derived in the memo, not assumed here):
    T(sigma) = 4 n S2 - 2 M(sigma),  S2 = sum_{k<n} k^2,
    M(sigma) = max over the same f of sum over cells of (i f + j sigma(f)),
because sum |z|^2 over cells and sum |a_k|^2 over atoms, each counted n times, are both independent
of sigma (sigma is a bijection).  The script reports both routes and asserts they agree.
"""
import itertools, sys, time
import numpy as np
from scipy.optimize import linear_sum_assignment


def cells_of(n):
    idx = np.arange(n)
    I, J = np.meshgrid(idx, idx, indexing="ij")
    return np.stack([I.ravel(), J.ravel()], 1)


SKIP_M = False


def T_and_M(sigma, cells, n):
    atoms = np.stack([np.arange(n), np.asarray(sigma, dtype=np.int64)], 1)
    D = ((cells[:, None, :] - atoms[None, :, :]) ** 2).sum(-1)          # n^2 x n, squared distances
    P = cells @ atoms.T                                                  # n^2 x n, inner products
    Dfull = np.repeat(D, n, axis=1)
    r, c = linear_sum_assignment(Dfull)
    T = int(Dfull[r, c].sum())
    if SKIP_M:
        return T, None
    Pfull = np.repeat(P, n, axis=1)
    r2, c2 = linear_sum_assignment(-Pfull)
    M = int(Pfull[r2, c2].sum())
    return T, M


def canonical(sigma, n):
    """Lexicographically least element of the orbit of sigma under the 8 symmetries of the square
    that fix the grid and the product measure: transpose (sigma -> inverse), i -> n-1-i, j -> n-1-j."""
    s = tuple(sigma)
    inv = [0] * n
    for i, v in enumerate(s):
        inv[v] = i
    orbit = []
    for base in (s, tuple(inv)):
        for hflip in (False, True):
            for vflip in (False, True):
                t = list(base)
                if hflip:
                    t = t[::-1]
                if vflip:
                    t = [n - 1 - v for v in t]
                orbit.append(tuple(t))
    return min(orbit)


def main(n, use_symmetry):
    t0 = time.time()
    cells = cells_of(n)
    S2 = sum(k * k for k in range(n))
    ident = tuple(range(n)); rev = tuple(range(n - 1, -1, -1))
    best = -1; argbest = []; second = -1; argsecond = []
    count = 0
    for sigma in itertools.permutations(range(n)):
        if use_symmetry and canonical(sigma, n) != sigma:
            continue
        count += 1
        T, M = T_and_M(sigma, cells, n)
        if M is not None:
            assert T == 4 * n * S2 - 2 * M, (sigma, T, M)
        if T > best:
            second, argsecond = best, argbest
            best, argbest = T, [sigma]
        elif T == best:
            argbest.append(sigma)
        elif T > second:
            second, argsecond = T, [sigma]
        elif T == second:
            argsecond.append(sigma)
    Ti, _ = T_and_M(ident, cells, n)
    Tr, _ = T_and_M(rev, cells, n)
    n4 = n ** 4
    print(f"n={n}: {count} permutations tested"
          f"{' (canonical reps of the 8-fold symmetry)' if use_symmetry else ''}, "
          f"{time.time()-t0:.0f}s", flush=True)
    print(f"   max T={best} -> W2^2={best/n4:.8f}, attained by {len(argbest)}: {argbest[:8]}", flush=True)
    print(f"   identity T={Ti} ({Ti/n4:.8f})   reversal T={Tr} ({Tr/n4:.8f})", flush=True)
    canon_max = {canonical(ident, n)} if use_symmetry else {ident, rev}
    print(f"   conjecture holds at this n: {set(argbest) <= canon_max}", flush=True)
    print(f"   runner-up T={second} ({second/n4:.8f}), gap {best-second}, at {argsecond[:5]}", flush=True)


if __name__ == "__main__":
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    ns = [int(a) for a in sys.argv[1:2]] or [3, 4, 5, 6, 7]

    sym = (len(sys.argv) > 2 and "sym" in sys.argv[2:])
    SKIP_M = ("skipm" in sys.argv[2:])
    for n in ns:
        main(n, sym)
