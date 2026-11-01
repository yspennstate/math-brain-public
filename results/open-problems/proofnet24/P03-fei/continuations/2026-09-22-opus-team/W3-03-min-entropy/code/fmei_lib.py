"""Core quantities for the Fourier min-entropy / influence problem.

Conventions (as in CONTEXT.md): f : {-1,1}^n -> {-1,1}, entry x of a truth table is f(x),
bit i of the integer x is coordinate i, value -1 means "true".
fhat(S) = 2^-n sum_x f(x) (-1)^{popcount(x & S)}.

    Hinf(f) = min_S log2(1/fhat(S)^2)            (min-entropy of the spectral distribution)
    H2(f)   = log2(1/sum_S fhat(S)^4)             (collision entropy)
    H(f)    = sum_S fhat(S)^2 log2(1/fhat(S)^2)
    I(f)    = sum_S |S| fhat(S)^2
"""
import numpy as np


def popcounts(n):
    idx = np.arange(1 << n, dtype=np.int64)
    pc = np.zeros(1 << n, dtype=np.int64)
    for b in range(n):
        pc += (idx >> b) & 1
    return pc


def wht(a):
    """Unnormalised Walsh-Hadamard transform along the last axis (length 2^n), in place on a float copy."""
    a = np.array(a, dtype=np.float64, copy=True)
    N = a.shape[-1]
    h = 1
    shp = a.shape[:-1]
    while h < N:
        a = a.reshape(shp + (N // (2 * h), 2, h))
        x = a[..., 0, :].copy()
        y = a[..., 1, :]
        a[..., 0, :] = x + y
        a[..., 1, :] = x - y
        a = a.reshape(shp + (N,))
        h *= 2
    return a


def coeffs(tt_pm):
    """Fourier coefficients of +-1 truth tables (last axis)."""
    tt_pm = np.asarray(tt_pm, dtype=np.float64)
    return wht(tt_pm) / tt_pm.shape[-1]


def stats(tt_pm):
    """Return dict of arrays: Hinf, H2, H, I, maxsq, mean, for a batch of +-1 truth tables."""
    c = coeffs(tt_pm)
    N = c.shape[-1]
    n = N.bit_length() - 1
    pc = popcounts(n).astype(np.float64)
    p = c * c
    I = p @ pc
    maxsq = p.max(axis=-1)
    with np.errstate(divide="ignore", invalid="ignore"):
        Hinf = -np.log2(maxsq)
        H2 = -np.log2((p * p).sum(axis=-1))
        lp = np.where(p > 0, -np.log2(np.where(p > 0, p, 1.0)), 0.0)
        H = (p * lp).sum(axis=-1)
    return dict(Hinf=Hinf, H2=H2, H=H, I=I, maxsq=maxsq, mean=c[..., 0], coeffs=c)


def bits_to_pm(masks, n):
    """Integer truth-table masks (bit x = 1 means f(x) = true = -1) -> +-1 arrays."""
    masks = np.asarray(masks, dtype=np.uint64)
    xs = np.arange(1 << n, dtype=np.uint64)
    bits = (masks[..., None] >> xs) & np.uint64(1)
    return 1.0 - 2.0 * bits.astype(np.float64)


def influences(tt_pm):
    """Per-coordinate influences Pr[f(x) != f(x^i)] of a single +-1 truth table."""
    tt = np.asarray(tt_pm)
    N = tt.shape[-1]
    n = N.bit_length() - 1
    xs = np.arange(N)
    return np.array([np.mean(tt != tt[xs ^ (1 << i)]) for i in range(n)])


def hinf_I(tt_pm):
    s = stats(tt_pm)
    return float(s["Hinf"]), float(s["I"])
