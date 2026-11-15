"""Search over cyclically invariant Boolean functions for a large one-coordinate erasure ratio (FLOW 12(w), item 6).

For f invariant under the cyclic shift of its n variables all coordinates are equivalent, so
    G(f) = E_1 / Inf_1 = (sum_i E_i) / I(f) = min_i E_i / Inf_i  <=  H(f) / I(f),
with E_1 = H(U) - H(U - 1) = H(1[1 in U] | U - 1), U the spectral sample. A large G is a lower bound for the
good-coordinate constant G* and for A* = sup sum_i E_i / I.

The function is stored as one sign per rotation orbit of {0,1}^n. Simulated annealing on single-orbit flips.

Usage: python cyc_hill.py n objective seed sweeps init outdir [temperature factor, default 0.5]
    objective: G (E_1/Inf_1) or HI (H/I)
    init: random | maj | tribes<w> (OR over cyclic windows of width w) | best:<file>
A file named STOP in outdir ends the run at the next sweep.
"""
import os
import sys
import numpy as np


def wht(v):
    a = np.array(v, dtype=np.float64)
    n = a.size.bit_length() - 1
    h = 1
    while h < a.size:
        a = a.reshape(-1, 2, h)
        a = np.concatenate((a[:, 0, :] + a[:, 1, :], a[:, 0, :] - a[:, 1, :]), axis=1).reshape(-1)
        h *= 2
    return a / (1 << n)


def ent(p):
    p = p[p > 1e-300]
    return float(-(p * np.log2(p)).sum())


def orbits(n):
    idx = np.arange(1 << n, dtype=np.int64)
    rep = idx.copy()
    x = idx.copy()
    full = (1 << n) - 1
    for _ in range(n - 1):
        x = ((x << 1) & full) | (x >> (n - 1))
        rep = np.minimum(rep, x)
    reps, oid = np.unique(rep, return_inverse=True)
    return reps, oid


def stats(f, n, pc):
    mu = wht(f) ** 2
    var = 1.0 - mu[0]
    tot_i = float((pc * mu).sum())
    if tot_i < 1e-12:
        return None
    h = ent(mu)
    nu = mu.reshape(-1, 2).sum(axis=1)          # merge bit 0: the law of U - 1
    e1 = h - ent(nu)
    return {"G": e1 / (tot_i / n), "HI": h / tot_i, "I": tot_i, "var": var, "H": h}


def main():
    n = int(sys.argv[1])
    obj = sys.argv[2]
    seed = int(sys.argv[3])
    sweeps = int(sys.argv[4])
    init = sys.argv[5]
    outdir = sys.argv[6]
    os.makedirs(outdir, exist_ok=True)
    tag = f"n{n}_{obj}_{init.split(':')[0]}_s{seed}"
    rng = np.random.default_rng(seed)
    reps, oid = orbits(n)
    m = reps.size
    idx = np.arange(1 << n, dtype=np.int64)
    pc = np.zeros(1 << n)
    for j in range(n):
        pc += (idx >> j) & 1
    if init == "random":
        v = rng.choice([-1.0, 1.0], size=m)
    elif init == "maj":
        v = np.where(pc[reps] > n / 2, -1.0, 1.0)
    elif init.startswith("tribes"):
        w = int(init[6:])
        full = (1 << n) - 1
        win = (1 << w) - 1
        hit = np.zeros(m, dtype=bool)
        x = reps.copy()
        for _ in range(n):
            hit |= (x & win) == win
            x = ((x << 1) & full) | (x >> (n - 1))
        v = np.where(hit, -1.0, 1.0)
    elif init.startswith("best:"):
        with open(init[5:], encoding="utf-8") as fh:
            bits = fh.read().split()[-1]
        v = np.array([-1.0 if c == "1" else 1.0 for c in bits])
    else:
        raise SystemExit("unknown init")
    cur = stats(v[oid], n, pc)
    if cur is None:
        v[rng.integers(m)] *= -1
        cur = stats(v[oid], n, pc)
    best = dict(cur)
    best_v = v.copy()
    log = open(os.path.join(outdir, f"log_{tag}.txt"), "a", encoding="utf-8")
    print(f"start {tag}: orbits {m}; G {cur['G']:.6f} H/I {cur['HI']:.6f} I {cur['I']:.4f} var {cur['var']:.4f}",
          file=log, flush=True)
    # temperature scale: half the median size of a single-orbit move at the start (a fixed 0.02 accepted 95 percent
    # of the moves at n >= 14 and turned the run into a random walk)
    probe = []
    for o in rng.choice(m, size=min(m, 200), replace=False):
        v[o] *= -1
        new = stats(v[oid], n, pc)
        v[o] *= -1
        if new is not None:
            probe.append(abs(new[obj] - cur[obj]))
    t0 = (float(sys.argv[7]) if len(sys.argv) > 7 else 0.5) * float(np.median(probe))
    print(f"t0 {t0:.3e}", file=log, flush=True)
    for sw in range(sweeps):
        temp = t0 * (1 - sw / sweeps) ** 2 + 1e-9
        acc = 0
        for o in rng.permutation(m):
            v[o] *= -1
            new = stats(v[oid], n, pc)
            if new is not None and (new[obj] >= cur[obj] or rng.random() < np.exp((new[obj] - cur[obj]) / temp)):
                cur = new
                acc += 1
                if cur[obj] > best[obj] + 1e-12:
                    best = dict(cur)
                    best_v = v.copy()
            else:
                v[o] *= -1
        print(f"sweep {sw} temp {temp:.5f} accepted {acc}/{m}: cur G {cur['G']:.6f} H/I {cur['HI']:.6f}; "
              f"best {obj} {best[obj]:.9f} (G {best['G']:.6f} H/I {best['HI']:.6f} I {best['I']:.4f} "
              f"var {best['var']:.4f})", file=log, flush=True)
        with open(os.path.join(outdir, f"best_{tag}.txt"), "w", encoding="utf-8") as fh:
            fh.write(f"n {n} objective {obj} seed {seed} G {best['G']:.12f} HI {best['HI']:.12f} I {best['I']:.12f} "
                     f"var {best['var']:.12f} orbit signs (1 = true), orbit representatives in increasing order:\n")
            fh.write("".join("1" if s < 0 else "0" for s in best_v) + "\n")
        if os.path.exists(os.path.join(outdir, "STOP")):
            print("STOP file seen", file=log, flush=True)
            break
    print("done", file=log, flush=True)


if __name__ == "__main__":
    main()
