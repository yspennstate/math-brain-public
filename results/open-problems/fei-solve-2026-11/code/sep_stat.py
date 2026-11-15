"""How many bits of log2(1/delta) does a coarse statistic of the spectral sample recover? (FLOW 12(y))

For a coordinate i write p_T = ghat(T)^2, q_T = hhat(T)^2 (g = E_i f, h = D_i f), delta = Inf_i, rho_h = q/delta,
nu = p + q. By 12(x)(A), E_i/delta = log2(1/delta) - D(rho_h || nu) + r with 0 <= r <= 1/ln 2, so the coordinate is
good exactly when the deficit  log2(1/delta) - D(rho_h || nu)  is bounded. For a statistic s(T) the data-processing
inequality gives D(rho_h || nu) >= D(s(rho_h) || s(nu)), so
    deficit_s := log2(1/delta) - D(s(rho_h) || s(nu))  >=  deficit_full >= 0,
and a bounded deficit_s proves the coordinate good by reading only s.

Statistics:
  size     |T|
  lowcnt   |T n L|,  L = coordinates j != i with Inf_j <= Inf_i
  lowproj  T n L
  hiproj   T n (complement of L)
  g1..g4   T n S for the best S of 1..4 coordinates found greedily (largest divergence at each step)

One row per class of coordinates (coordinates with the same Inf and E are printed once, with their count).

Usage: python sep_stat.py [seed]
"""
import sys
import numpy as np
from rand_restrict_identity import wht
import mono_hidden
import graph_pendant
from step_info import tribes, maj


def kl_keys(q, nu, key, size, delta):
    a = np.bincount(key, weights=q, minlength=size) / delta
    b = np.bincount(key, weights=nu, minlength=size)
    ok = a > 1e-300
    return float((a[ok] * np.log2(a[ok] / b[ok])).sum())


def phi_sum(p, q):
    s = p + q
    out = 0.0
    for a in (p, q):
        m = a > 0
        out -= float((a[m] * np.log2(a[m] / s[m])).sum())
    return out


def rows(f, n):
    mu = wht(f) ** 2
    N = 1 << n
    idx = np.arange(N)
    inf = np.array([mu[(idx >> j) & 1 == 1].sum() for j in range(n)])
    pc = np.zeros(N, dtype=np.int64)
    for j in range(n):
        pc += (idx >> j) & 1
    out = {}
    for i in range(n):
        d = inf[i]
        if d < 1e-15:
            continue
        lo = idx[(idx >> i) & 1 == 0]
        p, q = mu[lo], mu[lo | (1 << i)]
        nu = p + q
        E = phi_sum(p, q)
        cls = (round(d, 10), round(E, 10))
        if cls in out:
            out[cls]["count"] += 1
            continue
        lg = float(np.log2(1 / d))
        lowmask = sum(1 << j for j in range(n) if j != i and inf[j] <= d + 1e-12)
        himask = (N - 1) & ~lowmask & ~(1 << i)
        lowcnt = np.zeros(lo.size, dtype=np.int64)
        for j in range(n):
            if (lowmask >> j) & 1:
                lowcnt += (lo >> j) & 1
        r = {"i": i, "count": 1, "inf": d, "ratio": E / d, "lg": lg,
             "full": lg - kl_keys(q, nu, lo, N, d),
             "size": lg - kl_keys(q, nu, pc[lo], n + 1, d),
             "lowcnt": lg - kl_keys(q, nu, lowcnt, n + 1, d),
             "lowproj": lg - kl_keys(q, nu, lo & lowmask, N, d),
             "hiproj": lg - kl_keys(q, nu, lo & himask, N, d),
             "nlow": bin(lowmask).count("1")}
        S = 0
        gs = []
        for step in range(4):
            best, bj = -1.0, None
            for j in range(n):
                if j == i or (S >> j) & 1:
                    continue
                v = kl_keys(q, nu, lo & (S | (1 << j)), N, d)
                if v > best:
                    best, bj = v, j
            if bj is None:
                gs.append(float("nan"))
                continue
            S |= 1 << bj
            gs.append(lg - best)
        r["g"] = gs
        out[cls] = r
    return sorted(out.values(), key=lambda r: r["inf"])


def ip(k):
    idx = np.arange(1 << k)
    s = np.zeros(idx.size, dtype=np.int64)
    for j in range(0, k, 2):
        s += ((idx >> j) & 1) * ((idx >> (j + 1)) & 1)
    return np.where(s % 2 == 1, -1.0, 1.0)


def bent_hidden(k, m):
    """ip(y) on k variables times prod_j x_j^{1[y = y_j]} for m distinct points y_j: m hidden coordinates."""
    b = ip(k)
    n = k + m
    idx = np.arange(1 << n)
    y = idx & ((1 << k) - 1)
    f = b[y].copy()
    pts = [(1 << k) - 1 - 37 * j for j in range(m)]
    for j, pt in enumerate(pts):
        flip = (y == pt) & (((idx >> (k + j)) & 1) == 1)
        f[flip] *= -1.0
    return n, f


def show(name, f, n):
    for r in rows(f, n):
        g = r["g"]
        print("%-22s i=%2d x%-2d Inf=%.3e E/Inf=%7.4f lg=%6.3f | full %6.3f size %6.3f lowcnt %6.3f lowproj %6.3f "
              "hiproj %6.3f (nlow %2d) | g1 %6.3f g2 %6.3f g3 %6.3f g4 %6.3f" % (
                  name, r["i"], r["count"], r["inf"], r["ratio"], r["lg"], r["full"], r["size"], r["lowcnt"],
                  r["lowproj"], r["hiproj"], r["nlow"], g[0], g[1], g[2], g[3]), flush=True)


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    rng = np.random.default_rng(seed)
    for m, w in ((3, 3), (4, 3), (3, 4), (2, 6)):
        f, n = tribes(m, w)
        show("tribes %dx%d" % (m, w), f, n)
    f, n = maj(11)
    show("majority 11", f, n)
    for k in (7, 9, 11):
        n, f = mono_hidden.build(k)
        show("mono_hidden k=%d" % k, f, n)
    for k in (6, 9, 11):
        n, f = graph_pendant.build(k)
        show("graph_pendant k=%d" % k, f, n)
    for k, m in ((8, 1), (10, 1), (12, 1), (8, 4), (10, 3)):
        n, f = bent_hidden(k, m)
        show("bent_hidden k=%d m=%d" % (k, m), f, n)
    for n in (10, 12):
        f = rng.choice([-1.0, 1.0], size=1 << n)
        show("random n=%d" % n, f, n)


if __name__ == "__main__":
    main()
