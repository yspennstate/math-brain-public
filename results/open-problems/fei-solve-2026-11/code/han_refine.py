"""Numerical check of the fixed-order form of the relative step bound (FLOW 12(w), item 2).

Claim. Let f be Boolean on n variables and let k_1, ..., k_n be any order of the variables (k_1 queried first).
Put V_j = {k_j, ..., k_n} and W_j = sum of fhat(S)^2 over the sets S that MEET V_j (so W_1 = Var f and
W_j <= min(Var f, sum of the influences of V_j)). Then

    H(f) <= C0 * I(f) + sum_j Inf_{k_j} * log2(1 + W_j / Inf_{k_j}),        C0 = 6.94.

(Tree identity in the fixed order, the step bound of 12(v) item 1 at each node, and Jensen for the concave
homogeneous function (a, b) -> a log2(1 + b/a); E_rho Var(f_rho) = W_j and E_rho Inf(f_rho) = Inf.)

Prints, per family and per order rule, the largest H / right-hand side (must be <= 1) and, for comparison, the
largest H / Han's right-hand side (1/ln 2)(3 I + sum_k I_k ln(4/I_k)) (arXiv:2312.08271, Theorem 1).

Usage: python han_refine.py [seed]
"""
import sys
import numpy as np
from rand_restrict_identity import wht, ent
from relative_step import rand_dnf, C0


def data(f, n):
    mu = wht(f) ** 2
    idx = np.arange(1 << n)
    inf = np.array([mu[(idx >> i) & 1 == 1].sum() for i in range(n)])
    return mu, inf, idx


def rhs(mu, inf, idx, order):
    tot = C0 * inf.sum()
    mask = 0
    for k in reversed(order):                 # build V_j from the last queried variable upward
        mask |= 1 << k
        if inf[k] > 1e-15:
            w = mu[(idx & mask) != 0].sum()
            tot += inf[k] * np.log2(1 + w / inf[k])
    return tot


def han(inf):
    p = inf[inf > 1e-15]
    return (3 * p.sum() + (p * np.log(4 / p)).sum()) / np.log(2)


def run(fs, label, rng):
    worst = {"natural": 0.0, "decreasing": 0.0, "increasing": 0.0, "random": 0.0}
    worst_han = 0.0
    gain = []
    for f, n in fs:
        mu, inf, idx = data(f, n)
        if 1.0 - mu[0] < 1e-12:
            continue
        h = ent(mu)
        orders = {"natural": list(range(n)), "decreasing": list(np.argsort(-inf)),
                  "increasing": list(np.argsort(inf)), "random": list(rng.permutation(n))}
        vals = {}
        for name, od in orders.items():
            vals[name] = rhs(mu, inf, idx, [int(x) for x in od])
            worst[name] = max(worst[name], h / vals[name])
        worst_han = max(worst_han, h / han(inf))
        gain.append(min(vals.values()) / han(inf))
    print(f"{label}: " + "; ".join(f"{k} {v:.4f}" for k, v in worst.items())
          + f"; Han {worst_han:.4f}; best-order rhs / Han rhs: median {np.median(gain):.3f}, max {max(gain):.3f}",
          flush=True)


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    rng = np.random.default_rng(seed)
    fs = []
    for n in (4, 6, 8, 10):
        for _ in range(40):
            p = rng.choice([0.5, 0.2, 0.05, 0.01])
            fs.append((np.where(rng.random(1 << n) < p, -1.0, 1.0), n))
    run(fs, "random functions (160)", rng)
    fs = []
    for n in (6, 8, 10, 12):
        for w in (1, 2, 3, 4):
            for terms in (1, 2, 4, 8, 16, 40):
                for _ in range(2):
                    fs.append((rand_dnf(n, w, terms, rng)[0], n))
    run(fs, "random DNFs", rng)
    # structured: tribes, majority, dictator-heavy thresholds with geometric weights
    fs = []
    idx = np.arange(1 << 12)
    bits = ((idx[:, None] >> np.arange(12)) & 1).astype(float)
    tr = np.zeros(idx.size, dtype=bool)
    for b in range(4):
        tr |= bits[:, 3 * b:3 * b + 3].all(axis=1)
    fs.append((np.where(tr, -1.0, 1.0), 12))
    idx11 = np.arange(1 << 11)
    b11 = ((idx11[:, None] >> np.arange(11)) & 1).astype(float)
    fs.append((np.where(b11.sum(axis=1) > 5.5, -1.0, 1.0), 11))
    for r in (0.5, 0.7, 0.9):
        wts = r ** np.arange(12)
        fs.append((np.where(bits @ wts > wts.sum() / 2, -1.0, 1.0), 12))
    run(fs, "tribes(4x3), MAJ11, three geometric-weight thresholds", rng)


if __name__ == "__main__":
    main()
