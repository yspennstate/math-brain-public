"""Core routines: truth tables of linear threshold functions, Walsh transform, H and I.

Conventions. Index x in [0, 2^n); bit i of x equal to 1 means x_i = -1, bit 0 means x_i = +1.
f(x) = +1 if w.x > theta else -1 (ties are avoided by the caller: integer weights with
half-integer theta, or generic real weights).  H is in bits.
"""
import numpy as np
import numba as nb

try:
    import psutil
    _p = psutil.Process()
    _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    _p.cpu_affinity([2, 3, 14, 15])
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
    """Return Fourier coefficients c (c[S] = E f chi_S) of a +-1 table."""
    a = f.copy()
    wht_inplace(a)
    N = a.shape[0]
    for i in range(N):
        a[i] /= N
    return a


@nb.njit(cache=True)
def HI(c):
    """Entropy (bits) and total influence from coefficients."""
    N = c.shape[0]
    H = 0.0
    I = 0.0
    for S in range(N):
        w = c[S] * c[S]
        if w > 1e-300:
            H -= w * np.log2(w)
            I += popcount(S) * w
    return H, I


@nb.njit(cache=True)
def levels(c, n):
    W = np.zeros(n + 1)
    for S in range(c.shape[0]):
        W[popcount(S)] += c[S] * c[S]
    return W


@nb.njit(cache=True)
def influences(f, n):
    N = f.shape[0]
    inf = np.zeros(n)
    for i in range(n):
        b = 1 << i
        cnt = 0
        for x in range(N):
            if (x & b) == 0:
                if f[x] != f[x | b]:
                    cnt += 1
        inf[i] = cnt / (N // 2)
    return inf


@nb.njit(cache=True)
def restriction_step(c, n, i):
    """Delta_i H = H(f) - (H(f0)+H(f1))/2 and its parts, from the spectrum c of f.
    Returns (DeltaH, JS, split, Inf_i)."""
    N = c.shape[0]
    b = 1 << i
    Hf = 0.0
    H0 = 0.0
    H1 = 0.0
    Hmix = 0.0
    inf = 0.0
    for S in range(N):
        if S & b:
            continue
        s = c[S]
        d = c[S | b]
        a0 = s + d  # restriction x_i=+1
        a1 = s - d  # restriction x_i=-1
        w0 = a0 * a0
        w1 = a1 * a1
        m = 0.5 * (w0 + w1)
        ws = s * s
        wd = d * d
        inf += wd
        if ws > 1e-300:
            Hf -= ws * np.log2(ws)
        if wd > 1e-300:
            Hf -= wd * np.log2(wd)
        if w0 > 1e-300:
            H0 -= w0 * np.log2(w0)
        if w1 > 1e-300:
            H1 -= w1 * np.log2(w1)
        if m > 1e-300:
            Hmix -= m * np.log2(m)
    JS = Hmix - 0.5 * (H0 + H1)
    split = Hf - Hmix
    return Hf - 0.5 * (H0 + H1), JS, split, inf


def ltf_HI(w, theta):
    w = np.asarray(w, dtype=np.float64)
    f = ltf_table(w, float(theta))
    c = spectrum(f)
    H, I = HI(c)
    return H, I, f, c


def distinct_thresholds(w):
    """Sorted distinct values of w.x; a threshold strictly between consecutive values
    gives each distinct LTF with this weight vector exactly once."""
    v = np.unique(np.round(linform(np.asarray(w, np.float64)), 9))
    return v
