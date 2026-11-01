"""Core spectral quantities for the F4 group (FEI, 22-23 September 2026).

Conventions: a Boolean function on n variables is a +-1 truth table of length 2^n, entry x
(bit i of x = coordinate i).  Fourier coefficients fhat(S) = 2^-n sum_x f(x) (-1)^{|x & S|}.
Entropies in bits.  All routines accept a batch: array of shape (B, 2^n).
"""
import numpy as np

LOG2E = 1.0 / np.log(2.0)


def set_polite():
    try:
        import psutil
        p = psutil.Process()
        p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        cpus = [c for c in (2, 3, 14, 15) if c < psutil.cpu_count()]
        if cpus:
            p.cpu_affinity(cpus)
    except Exception as e:  # never fail on politeness
        print("[polite] could not set priority/affinity:", e)


def wht(tt):
    """Normalised Walsh-Hadamard transform along the last axis (length 2^n)."""
    a = np.array(tt, dtype=np.float64, copy=True)
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
    return a / N


def popcounts(N):
    return np.array([bin(s).count("1") for s in range(N)], dtype=np.int64)


def phi(p):
    """p log2(1/p) with phi(0)=0 (elementwise)."""
    p = np.asarray(p, dtype=np.float64)
    out = np.zeros_like(p)
    m = p > 0
    out[m] = -p[m] * np.log2(p[m])
    return out


def h2(q):
    q = np.clip(np.asarray(q, dtype=np.float64), 0.0, 1.0)
    return phi(q) + phi(1.0 - q)


def spectra(tt):
    fh = wht(tt)
    return fh, fh * fh


def entropy(p):
    return phi(p).sum(axis=-1)


def influence_vector(p, n):
    N = 1 << n
    S = np.arange(N)
    return np.stack([p[..., (S >> i) & 1 == 1].sum(axis=-1) for i in range(n)], axis=-1)


def total_influence(p, n):
    return (p * popcounts(1 << n)).sum(axis=-1)


def pair_arrays(fh, i, n):
    """For coordinate i return u = fhat(T), v = fhat(T+i) over T not containing i (shape (..., 2^(n-1)))."""
    N = 1 << n
    S = np.arange(N)
    low = S[((S >> i) & 1) == 0]
    return fh[..., low], fh[..., low | (1 << i)]


def coord_quantities(fh, n):
    """Per-coordinate: Inf, eta (Hellinger), B (erasure), JS (bits), Delta (restriction drop).

    u = E_i f coefficient, v = D_i f coefficient.  Restrictions have coefficients u+v, u-v.
    """
    out = {k: [] for k in ("Inf", "eta", "B", "JS", "Delta")}
    for i in range(n):
        u, v = pair_arrays(fh, i, n)
        a, b = u * u, v * v
        m = a + b
        mn = np.minimum(a, b)
        Inf = b.sum(axis=-1)
        eta = mn.sum(axis=-1)
        B = (phi(a) + phi(b) - phi(m)).sum(axis=-1)
        p1 = (u + v) ** 2
        p0 = (u - v) ** 2
        # JS(p0,p1) = H(m) - (H(p0)+H(p1))/2 where m=(p0+p1)/2 = a+b
        JS = (phi(m) - 0.5 * (phi(p0) + phi(p1))).sum(axis=-1)
        Delta = JS + B
        out["Inf"].append(Inf)
        out["eta"].append(eta)
        out["B"].append(B)
        out["JS"].append(JS)
        out["Delta"].append(Delta)
    return {k: np.stack(v, axis=-1) for k, v in out.items()}


def restrict(tt, i, bit, n):
    """Restriction x_i = bit (bit 0 -> +1 coordinate value index 0) ; returns table on n-1 vars."""
    N = 1 << n
    x = np.arange(N)
    sel = x[((x >> i) & 1) == bit]
    return tt[..., sel]


# ---------------------------------------------------------------- families
def tt_from_func(n, fn):
    N = 1 << n
    x = np.arange(N)
    bits = ((x[:, None] >> np.arange(n)[None, :]) & 1).astype(np.int64)
    return np.array([fn(bits[k]) for k in range(N)], dtype=np.int8)


def bent_ip(m2):
    """Inner product mod 2 on 2*m2 variables, +-1 valued."""
    n = 2 * m2
    return tt_from_func(n, lambda b: 1 - 2 * (int(np.dot(b[:m2], b[m2:])) & 1))


def one_point(n):
    return tt_from_func(n, lambda b: -1 if b.sum() == n else 1)


def tribes(w, s):
    """OR of s ANDs of width w ( -1 = true )."""
    n = w * s
    return tt_from_func(n, lambda b: -1 if any(b[j * w:(j + 1) * w].all() for j in range(s)) else 1)


def majority(n):
    return tt_from_func(n, lambda b: -1 if b.sum() * 2 > n else 1)


def rec_maj3(depth):
    n = 3 ** depth

    def ev(b):
        vals = list(b)
        while len(vals) > 1:
            vals = [1 if (vals[3 * k] + vals[3 * k + 1] + vals[3 * k + 2]) >= 2 else 0 for k in range(len(vals) // 3)]
        return -1 if vals[0] else 1
    return tt_from_func(n, ev)


def addressing(k):
    n = k + (1 << k)

    def ev(b):
        a = int(sum(int(b[j]) << j for j in range(k)))
        return -1 if b[k + a] else 1
    return tt_from_func(n, ev)


def bent_plus_flip(m2):
    """bent IP on 2*m2 vars plus a new variable z (last); flip the point y=all-ones when z=1."""
    n = 2 * m2 + 1
    base = bent_ip(m2)
    N = 1 << n
    tt = np.empty(N, dtype=np.int8)
    for x in range(N):
        y = x & ((1 << (2 * m2)) - 1)
        z = (x >> (2 * m2)) & 1
        v = base[y]
        if z == 1 and y == (1 << (2 * m2)) - 1:
            v = -v
        tt[x] = v
    return tt
