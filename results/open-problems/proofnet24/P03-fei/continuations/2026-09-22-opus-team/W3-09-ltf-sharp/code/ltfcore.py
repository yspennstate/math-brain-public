"""Core routines for W3-09: truth tables of threshold functions, Walsh transform, H and I.

Convention: index x in [0, 2^n); bit i of x equal to 1 means x_i = -1 ("true").
f(x) = +1 if w.x > theta else -1.  H is in bits.
"""
import numpy as np
import numba as nb

try:
    import psutil
    _p = psutil.Process()
    _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    _p.cpu_affinity([2, 3, 10, 11, 12, 13, 14, 15])
except Exception:  # pragma: no cover
    pass


@nb.njit(cache=True)
def linform(w):
    n = w.shape[0]
    N = 1 << n
    v = np.empty(N, np.float64)
    s = 0.0
    for i in range(n):
        s += w[i]
    v[0] = s
    for k in range(n):
        step = 1 << k
        for x in range(step):
            v[x + step] = v[x] - 2.0 * w[k]
    return v


@nb.njit(cache=True)
def ltf_table(w, theta):
    v = linform(w)
    N = v.shape[0]
    f = np.empty(N, np.float64)
    for x in range(N):
        f[x] = 1.0 if v[x] > theta else -1.0
    return f


@nb.njit(cache=True)
def wht_inplace(a):
    N = a.shape[0]
    h = 1
    while h < N:
        for i in range(0, N, 2 * h):
            for j in range(i, i + h):
                u = a[j]
                t = a[j + h]
                a[j] = u + t
                a[j + h] = u - t
        h *= 2


@nb.njit(cache=True)
def popcount(x):
    c = 0
    while x:
        x &= x - 1
        c += 1
    return c


@nb.njit(cache=True)
def spectrum(f):
    a = f.copy()
    wht_inplace(a)
    N = a.shape[0]
    for i in range(N):
        a[i] /= N
    return a


@nb.njit(cache=True)
def HI(c):
    N = c.shape[0]
    H = 0.0
    I = 0.0
    for S in range(N):
        w = c[S] * c[S]
        if w > 1e-300:
            H -= w * np.log2(w)
            I += popcount(S) * w
    return H, I


def ltf_HI(w, theta):
    w = np.asarray(w, dtype=np.float64)
    f = ltf_table(w, float(theta))
    c = spectrum(f)
    H, I = HI(c)
    return H, I, f, c
