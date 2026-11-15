"""Fast single-function evaluator (butterfly Walsh transform) for structured families up to n=16:
rho0 = min_i Delta_i H / Inf_i, H/I, and per-coordinate detail."""
import math, sys
import numpy as np

def fwht(a):
    a = a.copy(); h = 1; n = a.shape[-1]
    while h < n:
        a = a.reshape(-1, n // (2 * h), 2, h)
        x = a[:, :, 0, :].copy(); y = a[:, :, 1, :].copy()
        a[:, :, 0, :] = x + y; a[:, :, 1, :] = x - y
        a = a.reshape(-1, n); h *= 2
    return a

def stats(f, n):
    N = 1 << n
    fh = fwht(f.reshape(1, N))[0] / N
    p = fh * fh
    nz = p > 0
    H = float(-(p[nz] * np.log2(p[nz])).sum())
    pop = np.array([bin(S).count("1") for S in range(N)])
    I = float((p * pop).sum())
    rows = []
    idx = np.arange(N)
    for i in range(n):
        Inf = float(p[(idx >> i) & 1 == 1].sum())
        if Inf < 1e-12:
            continue
        Hc = []
        for b in (0, 1):
            sel = idx[((idx >> i) & 1) == b]
            g = f[sel]
            gh = fwht(g.reshape(1, N // 2))[0] / (N // 2); q = gh * gh; qz = q > 0
            Hc.append(float(-(q[qz] * np.log2(q[qz])).sum()))
        dH = H - 0.5 * (Hc[0] + Hc[1])
        rows.append((i, dH, Inf, dH / Inf))
    rho0 = min(r[3] for r in rows) if rows else float("inf")
    return H, I, rho0, rows

def make(n, kind):
    N = 1 << n; f = np.ones(N); c = 0
    on = {c}
    if kind in ("star", "star_matching", "ball2"):
        for i in range(n): on.add(c ^ (1 << i))
    if kind == "star_matching":
        for j in range(0, n - 1, 2): on.add(c ^ (1 << j) ^ (1 << (j + 1)))
    if kind == "ball2":
        for i in range(n):
            for j in range(i + 1, n): on.add(c ^ (1 << i) ^ (1 << j))
    if kind == "matching_only":
        on = {c} | {c ^ (1 << j) ^ (1 << (j + 1)) for j in range(0, n - 1, 2)}
    if kind == "point":
        on = {c}
    if kind == "edge":
        on = {c, c ^ 1}
    for x in on: f[x] = -1.0
    return f

if __name__ == "__main__":
    kinds = sys.argv[1].split(",") if len(sys.argv) > 1 else ["point", "star", "star_matching", "ball2"]
    ns = [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 else [4, 6, 8, 10, 12, 14]
    for kind in kinds:
        for n in ns:
            H, I, rho0, rows = stats(make(n, kind), n)
            ratios = sorted(set(round(r[3], 4) for r in rows))
            print(f"{kind:14s} n={n:2d} |ON|={int((make(n,kind)<0).sum()):4d} H={H:.4f} I={I:.4f} H/I={H/I:.4f} rho0={rho0:.4f} distinct coord ratios={ratios[:4]}")
