"""Product condition behind the level witness for threshold functions.

For f = sgn(w.x - theta) and i the coordinate of largest weight, with A_k = W^k(E_i f), B_k = W^k(D_i f) (level weights
on the other n-1 variables) and delta = Inf_i = sum_k B_k, prints
  M = max_K  A_{>=K} * B_{<=K} / delta^2      (K >= 1; at K = 0 the ratio is A_total <= 1)
  L/Inf = sum_k Phi(A_k, B_k) / delta
and the median level of B.  If M stays bounded over all threshold functions, L <= C(M) Inf, hence FEI for the class.

usage: python ltf_product.py n family param seed reps [theta/sd]
"""
import sys
import numpy as np
from ltf_level import wht, phi, weights


def levels(w, theta):
    n = len(w)
    N = 1 << n
    idx = np.arange(N, dtype=np.int64)
    s = np.full(N, -float(theta))
    for j in range(n):
        s += w[j] * (1 - 2 * ((idx >> j) & 1))
    if np.any(np.abs(s) < 1e-12):
        return None
    mu = wht(np.sign(s)) ** 2
    pc = np.zeros(N, dtype=np.int64)
    for j in range(n):
        pc += (idx >> j) & 1
    i = int(np.argmax(w))
    lo = idx[((idx >> i) & 1) == 0]
    lev = pc[lo]
    A = np.bincount(lev, weights=mu[lo], minlength=n)
    B = np.bincount(lev, weights=mu[lo | (1 << i)], minlength=n)
    return A, B


def main():
    n = int(sys.argv[1])
    fam = sys.argv[2]
    param = float(sys.argv[3])
    seed = int(sys.argv[4])
    reps = int(sys.argv[5])
    thfix = float(sys.argv[6]) if len(sys.argv) > 6 else None
    rng = np.random.default_rng(seed)
    for r in range(reps):
        w, th = weights(n, fam, param, rng)
        sd = float(np.sqrt((w * w).sum()))
        if th is None:
            m = thfix if thfix is not None else rng.choice([0.0, 0.5, 1.0, 1.5, 2.0])
            th = m * sd + 1e-3 * rng.standard_normal()
        out = levels(w, th)
        if out is None:
            print('tie, skipped')
            continue
        A, B = out
        d = float(B.sum())
        if d <= 0:
            print('largest weight has no influence')
            continue
        Atail = np.cumsum(A[::-1])[::-1]
        Bhead = np.cumsum(B)
        prod = Atail * Bhead / d ** 2
        K = int(np.argmax(prod[1:])) + 1
        med = int(np.searchsorted(Bhead, d / 2))
        L = float(phi(A, B).sum())
        print('n=%d %s p=%g th/sd=%.2f Inf=%.3e L/Inf=%.3f M=%.3f at K=%d  median level of B=%d  A_tail(med)/Inf=%.3f'
              % (n, fam, param, th / sd, d, L / d, float(prod[K]), K, med, float(Atail[med]) / d))
        sys.stdout.flush()


if __name__ == '__main__':
    main()
