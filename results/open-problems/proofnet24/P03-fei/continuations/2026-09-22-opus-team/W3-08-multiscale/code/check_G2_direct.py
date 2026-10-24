"""Independent Monte Carlo check of kappa_delta(G_2) for Numaro's g (324 variables).

Each sample draws a delta-random restriction of G_2 = g(g,...,g): for every child i an independent (J_i, x_i),
the restricted child r_i (exact truth table, exact H(r_i), mean nu_i), and then
    H(G_2 restricted) = Htilde_g(nu) + sum_i Lambda_i(nu) (H(r_i) - h2(nu_i^2)),   Lambda_i(nu) = It_i(nu)/W_i,
evaluated at the realized nu (no multilinearity, no population).  Compared with H(G_2) - D_delta(G_2) from the recursion.
usage: python check_G2_direct.py NSAMP DELTA
"""
import sys, os, time
import numpy as np
import numba as nb
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mslib import polite, fwht, entropy_bits, influences

polite()
nsamp = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
delta = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
g = np.load(os.path.join(HERE, "..", "..", "inputs", "numaro18_pm1_table.npy")).astype(np.int64)
n = 18
N = 1 << n
ghat = fwht(g)
Hg = entropy_bits(ghat * ghat)
Ig = influences(ghat, n).sum()


@nb.njit(cache=True)
def biased_coeffs(ghat, mu):
    N = ghat.shape[0]
    n = mu.shape[0]
    a = ghat.copy()
    for i in range(n):
        bit = 1 << i
        m = mu[i]
        s = np.sqrt(max(0.0, 1.0 - m * m))
        for T in range(N):
            if (T & bit) == 0:
                u = a[T]
                v = a[T | bit]
                a[T] = u + m * v
                a[T | bit] = s * v
    return a


@nb.njit(cache=True)
def restrict_child(g, freemask, xbits, n):
    """truth table of g restricted: free coords = bits of freemask (in increasing order), others fixed to xbits."""
    free = np.empty(n, dtype=np.int64)
    nf = 0
    for i in range(n):
        if (freemask >> i) & 1:
            free[nf] = i
            nf += 1
    M = 1 << nf
    sub = np.empty(M, dtype=np.int64)
    base = xbits & ~freemask
    for y in range(M):
        idx = base
        for k in range(nf):
            if (y >> k) & 1:
                idx |= 1 << free[k]
        sub[y] = g[idx]
    return sub


@nb.njit(cache=True)
def sample_many(g, ghat, n, delta, nsamp, seed):
    np.random.seed(seed)
    out = np.empty(nsamp)
    Hr = np.empty(n)
    nu = np.empty(n)
    for t in range(nsamp):
        for i in range(n):
            fm = 0
            for j in range(n):
                if np.random.random() < delta:
                    fm |= 1 << j
            xb = np.random.randint(0, 1 << n)
            sub = restrict_child(g, fm, xb, n)
            fh = fwht(sub)
            nu[i] = fh[0]
            h = 0.0
            for q in fh:
                w = q * q
                if w > 1e-300:
                    h -= w * np.log2(w)
            Hr[i] = h
        a = biased_coeffs(ghat, nu)
        Ht = 0.0
        It = np.zeros(n)
        for T in range(a.shape[0]):
            w = a[T] * a[T]
            if w > 1e-300:
                Ht -= w * np.log2(w)
                for i in range(n):
                    if (T >> i) & 1:
                        It[i] += w
        tot = Ht
        for i in range(n):
            W = 1.0 - nu[i] * nu[i]
            if W > 1e-15:
                q = nu[i] * nu[i]
                h2 = 0.0
                if q > 0.0:
                    h2 = -q * np.log2(q) - (1 - q) * np.log2(1 - q)
                tot += It[i] / W * (Hr[i] - h2)
        out[t] = tot
    return out


t0 = time.time()
vals = sample_many(g, ghat, n, delta, nsamp, 2026)
EH = vals.mean()
se = vals.std() / np.sqrt(nsamp)
H2 = Hg + Ig * Hg
I2 = Ig ** 2
print(f"delta={delta} nsamp={nsamp}: E H(G_2 restricted) = {EH:.5f} +- {se:.5f}  ->  kappa_delta(G_2) = {(H2 - EH) / ((1 - delta) * I2):.5f} +- {se / ((1 - delta) * I2):.5f}   [{time.time() - t0:.0f}s]")
