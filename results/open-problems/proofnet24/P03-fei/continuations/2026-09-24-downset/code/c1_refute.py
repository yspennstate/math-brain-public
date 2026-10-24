"""The most-influential-coordinate step (C1) fails for monotone functions.

g_n(y, z) = Maj_n(y) OR (z AND [y = y*]), n odd, y* of weight (n-1)/2 (paper Remark 6.1).
Replace every y_j by a majority of k fresh variables. The inner functions are balanced, so the
spectral sample of the composition is: T ~ P_g, then an independent spectral sample of Maj_k for
every j in T. Hence Delta_z and Inf_z do not change, while every inner variable has influence
Inf_{y_j}(g_n) * Inf(Maj_k), which falls below Inf_z = 2^-n once k is large. Then z is the unique
coordinate of largest influence and Delta_z / Inf_z is that of g_n: 6.66 at n = 5, unbounded in n.

Part 1 checks the composition identities by brute force on 10- and 16-variable compositions.
Part 2 gives the exact ratio at z and the least k for which z is the unique most influential coordinate.
"""
import itertools
import sys
import functools
print = functools.partial(print, flush=True)
import math
import numpy as np


def wht(v):
    a = v.astype(np.float64).copy()
    h = 1
    n = a.size
    while h < n:
        a = a.reshape(-1, 2 * h)
        x = a[:, :h].copy()
        y = a[:, h:].copy()
        a[:, :h] = x + y
        a[:, h:] = x - y
        a = a.reshape(n)
        h *= 2
    return a / n


def spectrum(F):
    """F: array of +-1 values indexed by x with bit i of the index = x_i."""
    c = wht(F)
    return c * c


def ent(P):
    P = P[P > 1e-300]
    return float(-(P * np.log2(P)).sum())


def restrict(F, nvar, v, b):
    idx = np.arange(1 << nvar)
    keep = ((idx >> v) & 1) == b
    return F[keep]  # remaining coordinates keep their order


def step(F, nvar, v):
    H = ent(spectrum(F))
    H0 = ent(spectrum(restrict(F, nvar, v, 0)))
    H1 = ent(spectrum(restrict(F, nvar, v, 1)))
    return H - 0.5 * (H0 + H1)


def influences(F, nvar):
    idx = np.arange(1 << nvar)
    out = []
    for v in range(nvar):
        out.append(float(np.mean(F != F[idx ^ (1 << v)])))
    return out


def base_table(n):
    """g_n on n+1 variables: y_0..y_{n-1} then z (bit n)."""
    ystar = tuple([1] * ((n - 1) // 2) + [0] * ((n + 1) // 2))
    N = 1 << (n + 1)
    F = np.empty(N)
    for x in range(N):
        y = tuple((x >> j) & 1 for j in range(n))
        z = (x >> n) & 1
        f = (sum(y) > n // 2) or (z == 1 and y == ystar)
        F[x] = 1 - 2 * int(f)
    return F


def composed_table(n, k):
    """g_n with y_j = Maj_k(block j); variables: blocks then z."""
    ystar = tuple([1] * ((n - 1) // 2) + [0] * ((n + 1) // 2))
    nv = n * k + 1
    N = 1 << nv
    idx = np.arange(N)
    ys = []
    for j in range(n):
        s = np.zeros(N, dtype=np.int64)
        for i in range(k):
            s += (idx >> (j * k + i)) & 1
        ys.append((s > k // 2).astype(np.int64))
    Y = np.stack(ys, axis=1)
    z = (idx >> (n * k)) & 1
    maj = Y.sum(axis=1) > n // 2
    eq = np.all(Y == np.array(ystar), axis=1)
    f = maj | ((z == 1) & eq)
    return 1.0 - 2.0 * f.astype(np.float64), nv


def maj_inf(k):
    """Influence of one variable on Maj_k (k odd): C(k-1, (k-1)/2) / 2^(k-1), via lgamma."""
    h = (k - 1) // 2
    return math.exp(math.lgamma(k) - 2 * math.lgamma(h + 1) - (k - 1) * math.log(2))


def main():
    print("Part 1: brute-force check of the composition identities")
    for n, k in [(3, 3), (5, 3)]:
        Fb = base_table(n)
        infb = influences(Fb, n + 1)
        dz_b = step(Fb, n + 1, n)
        Fc, nv = composed_table(n, k)
        infc = influences(Fc, nv)
        dz_c = step(Fc, nv, nv - 1)
        pred_inner = [infb[j] * maj_inf(k) for j in range(n) for _ in range(k)]
        err_inf = max(abs(a - b) for a, b in zip(infc[:-1], pred_inner))
        print(f"  n={n} k={k} vars={nv}: Inf_z base {infb[-1]:.10f} comp {infc[-1]:.10f}; "
              f"Delta_z base {dz_b:.12f} comp {dz_c:.12f} (diff {abs(dz_b - dz_c):.2e}); "
              f"inner-influence formula max err {err_inf:.2e}; ratio {dz_c / infc[-1]:.6f}")
    print()
    print("Part 2: the ratio at z, and the least k making z the unique most influential coordinate")
    for n in [3, 5, 7, 9, 11, 13]:
        Fb = base_table(n)
        infb = influences(Fb, n + 1)
        dz = step(Fb, n + 1, n)
        infz = infb[-1]
        maxy = max(infb[:-1])
        lo, hi = 1, 3
        while maxy * maj_inf(hi) >= infz:
            lo, hi = hi, 2 * hi + 1
        while hi - lo > 2:  # maj_inf is decreasing in odd k; keep lo failing, hi passing, both odd
            mid = (lo + hi) // 2
            mid += 1 - mid % 2
            if mid >= hi:
                mid = hi - 2
            if maxy * maj_inf(mid) >= infz:
                lo = mid
            else:
                hi = mid
        k = hi
        print(f"  n={n:2d}: Inf_z = 2^-{n} = {infz:.3e}, max Inf_y(g_n) = {maxy:.6f}, "
              f"Delta_z/Inf_z = {dz / infz:.6f}; least odd k = {k} "
              f"(max inner influence {maxy * maj_inf(k):.4e} < Inf_z), total variables {n * k + 1}")


if __name__ == "__main__":
    main()
