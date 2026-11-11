"""Monte Carlo evaluation of the dimension of harmonic measure of the biased walk on a Galton-Watson tree.

For an offspring law and a bias lam, the escape probability beta of the walk on a Galton-Watson tree with an added
parent of the root satisfies beta = C / (lam + C), where C is the sum of the escape probabilities of the subtrees of
the children of the root.  The dimension is

    d(lam) = E[W L] / E[W],   W = B C / (lam - 1 + B + C),   L = log(lam + C),

with B an independent copy of beta (Lin, Bernoulli 25 (2019), formulas (7) and (8)).  The program iterates the
recursion on a pool of samples of (beta, d beta / d lam), then evaluates d(lam) and its derivative in lam.  Every
bias is run with the same random numbers, so that differences between biases are much less noisy than the values.

usage: python dim_check.py POOL ITER SEEDS out.json [stopfile]
"""
import json
import math
import os
import sys
import time

import numpy as np

GRID = [0.0, 0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]   # bias as a fraction of the mean m


def finite_law(values, probs):
    values = np.array(values)
    probs = np.array(probs, dtype=float)

    def sample(rng, size):
        return rng.choice(values, size=size, p=probs)

    pairs = list(zip(values.tolist(), probs.tolist()))
    return sample, pairs


def geometric_law():
    def sample(rng, size):
        return rng.geometric(0.5, size=size)

    pairs = [(k, 0.5 ** k) for k in range(1, 400)]
    return sample, pairs


LAWS = {
    "half_1_2": finite_law([1, 2], [0.5, 0.5]),
    "half_2_4": finite_law([2, 4], [0.5, 0.5]),
    "third_1_2_3": finite_law([1, 2, 3], [1 / 3, 1 / 3, 1 / 3]),
    "geometric_half": geometric_law(),
}


def exact(pairs):
    m = sum(k * p for k, p in pairs)
    a = sum(p / k for k, p in pairs)
    ell = sum(p * math.log(k) for k, p in pairs)
    c = sum(p * math.log(k) / k for k, p in pairs)
    return {"m": m, "a": a, "d0": ell, "slope0": (1 - a) * (a * ell - c), "k0": min(k for k, p in pairs if p > 0)}


def draw(rng, sample, beta, dbeta, pool):
    n = sample(rng, pool)
    starts = np.concatenate(([0], np.cumsum(n)[:-1]))
    idx = rng.integers(0, pool, size=int(n.sum()))
    return np.add.reduceat(beta[idx], starts), np.add.reduceat(dbeta[idx], starts)


def run(sample, lam, pool, iters, seed):
    rng = np.random.default_rng(seed)
    beta = np.ones(pool)
    dbeta = np.zeros(pool)
    for _ in range(iters):
        c, dc = draw(rng, sample, beta, dbeta, pool)
        beta = c / (lam + c)
        dbeta = (lam * dc - c) / (lam + c) ** 2
    c, dc = draw(rng, sample, beta, dbeta, pool)
    j = rng.integers(0, pool, size=pool)
    b, db = beta[j], dbeta[j]
    den = lam - 1 + b + c
    w = b * c / den
    dw = (db * c + b * dc) / den - b * c * (1 + db + dc) / den ** 2
    lg = np.log(lam + c)
    dlg = (1 + dc) / (lam + c)
    d = float(np.mean(w * lg) / np.mean(w))
    dd = float((np.mean(dw * lg + w * dlg) - d * np.mean(dw)) / np.mean(w))
    return d, dd


def main():
    pool, iters, seeds, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    stop = sys.argv[5] if len(sys.argv) > 5 else None
    res = {"pool": pool, "iters": iters, "seeds": seeds, "grid": GRID, "laws": {}}
    t0 = time.time()
    for name, (sample, pairs) in LAWS.items():
        ex = exact(pairs)
        rows = []
        for frac in GRID:
            lam = frac * ex["m"]
            vals = [run(sample, lam, pool, iters, 1000 + s) for s in range(seeds)]
            rows.append({"frac": frac, "lam": lam, "d": [v[0] for v in vals], "dd": [v[1] for v in vals]})
            print(name, frac, round(float(np.mean([v[0] for v in vals])), 6), round(time.time() - t0), flush=True)
            if stop and os.path.exists(stop):
                print("stop file", flush=True)
                return
        res["laws"][name] = {"exact": ex, "rows": rows}
        with open(out + ".tmp", "w") as f:
            json.dump(res, f)
        os.replace(out + ".tmp", out)
    print("done", round(time.time() - t0), flush=True)


if __name__ == "__main__":
    main()
