"""D0007: bin-occupation LP relaxation and rearrangement experiments.

Run: OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 numerics.py
Only one process is used. LP feasibility is an outer relaxation, not a proof
of complete mixability of the continuous law.
"""
import os
for _key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_key] = "1"
import argparse
import csv
import json
import math
from pathlib import Path
import resource
import time
import warnings
import numpy as np
from scipy.integrate import quad
from scipy.optimize import linprog, OptimizeWarning
from scipy.special import expn
from scipy.stats import beta
from threadpoolctl import threadpool_limits


class Law:
    def __init__(self, name, cdf, ppf, mean):
        self.name, self.cdf, self.ppf, self.mean = name, cdf, ppf, mean


def laws():
    z = float(expn(2, 1.0))
    # Integral_0^x exp(-1/t)dt = x E_2(1/x).
    def thin_cdf(x):
        x = np.asarray(x, float)
        y = np.zeros_like(x)
        mask = x > 0
        y[mask] = x[mask] * expn(2, 1 / x[mask]) / z
        return np.clip(y, 0, 1)
    def thin_ppf(u):
        u = np.asarray(u, float)
        lo, hi = np.zeros_like(u), np.ones_like(u)
        for _ in range(50):
            mid = (lo + hi) / 2
            left = thin_cdf(mid) < u
            lo = np.where(left, mid, lo)
            hi = np.where(left, hi, mid)
        return (lo + hi) / 2
    return [
        Law("power4", lambda x: np.clip(x, 0, 1)**5,
            lambda u: np.asarray(u)**.2, 5/6),
        Law("beta_3_5", lambda x: beta.cdf(x, 3, 5),
            lambda u: beta.ppf(u, 3, 5), 3/8),
        Law("thin_exp", thin_cdf, thin_ppf, float(expn(3, 1.0)/z)),
        Law("two_bands", lambda x: .5*np.clip(np.asarray(x)/.1, 0, 1)
            + .5*np.clip((np.asarray(x)-.9)/.1, 0, 1),
            lambda u: np.where(np.asarray(u) < .5, .2*np.asarray(u),
                               .9+.2*(np.asarray(u)-.5)), .5),
        Law("beta_3_3", lambda x: beta.cdf(x, 3, 3),
            lambda u: beta.ppf(u, 3, 3), .5),
    ]


def price(cost, n, indices, lo, hi):
    """Exact combinatorial pricing by min-plus DP (floating costs)."""
    top = n*int(indices[-1])
    dp = np.full((n+1, top+1), np.inf)
    arg = np.full((n+1, top+1), -1, dtype=np.int16)
    dp[0, 0] = 0
    for k in range(1, n+1):
        previous_top = (k-1)*int(indices[-1])
        for j, value in enumerate(indices):
            value = int(value)
            candidate = dp[k-1, :previous_top+1]+cost[j]
            dest = dp[k, value:value+previous_top+1]
            take = candidate < dest
            dest[take] = candidate[take]
            arg[k, value:value+previous_top+1][take] = j
    lo, hi = max(0, lo), min(top, hi)
    if lo > hi or not np.isfinite(dp[n, lo:hi+1]).any():
        return math.inf, None
    total = lo+int(np.argmin(dp[n, lo:hi+1]))
    optimum = float(dp[n, total])
    count = np.zeros(len(cost))
    for k in range(n, 0, -1):
        j = int(arg[k, total])
        assert j >= 0
        count[j] += 1
        total -= int(indices[j])
    assert total == 0 and count.sum() == n
    return optimum, count/n


def occupation_lp(law, n, bins, max_iter=1500):
    """Minimum marginal L1 error over bin-compatible n-tuples.

    Each column is c/n, c an occupation vector. The bin-sum restriction is
    sum(j c_j) in [n*mu*bins-n, n*mu*bins]. Thus a continuous constant-sum
    coupling induces a feasible LP. Uniform random permutation recovers
    identical discrete marginals from an occupation-vector distribution.
    """
    edges = np.linspace(0, 1, bins+1)
    masses = np.maximum(0, np.diff(law.cdf(edges)))
    masses /= masses.sum()
    indices = np.flatnonzero(masses > 0)
    p = masses[indices]
    d = len(p)
    low = math.ceil(n*law.mean*bins-n-1e-10)
    high = math.floor(n*law.mean*bins+1e-10)
    _, first = price(np.zeros(d), n, indices, low, high)
    if first is None:
        return dict(lp_status="infeasible_support", lp_l1=2.,
                    lp_lower=2., lp_iterations=0, lp_residual=0.)
    cols = [first]
    keys = {tuple(np.rint(first*n).astype(int))}
    identity = np.eye(d)
    for iteration in range(max_iter):
        a = np.column_stack(cols)
        # a*w + positive - negative = p, sum(w)=1.
        matrix = np.column_stack([a, identity, -identity])
        norm_row = np.r_[np.ones(len(cols)), np.zeros(2*d)]
        # SciPy forwards this native HiGHS option but warns that it is not
        # in SciPy's public options list. Limit the native scheduler as well
        # as BLAS; dual simplex itself is serial.
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=OptimizeWarning,
                                    message="Unrecognized options detected:.*threads")
            result = linprog(np.r_[np.zeros(len(cols)), np.ones(2*d)],
                             A_eq=np.vstack([matrix, norm_row]),
                             b_eq=np.r_[p, 1.], bounds=(0, None),
                             method="highs-ds", options={
                                 "threads": 1,
                                 "dual_feasibility_tolerance": 1e-9,
                                 "primal_feasibility_tolerance": 1e-9})
        if not result.success:
            raise RuntimeError(result.message)
        residual = float(np.max(np.abs(result.eqlin.residual)))
        dual, gamma = result.eqlin.marginals[:-1], result.eqlin.marginals[-1]
        priced, column = price(-dual/n, n, indices, low, high)
        reduced = priced-gamma
        lower = float(result.fun+min(0., reduced))
        if result.fun < 1e-8 or reduced >= -1e-9:
            status = "outer_feasible" if result.fun < 1e-8 else "outer_infeasible"
            return dict(lp_status=status, lp_l1=float(result.fun),
                        lp_lower=lower, lp_iterations=iteration+1,
                        lp_residual=residual)
        key = tuple(np.rint(column*n).astype(int))
        if key in keys:
            raise RuntimeError("Duplicate column with negative reduced cost")
        cols.append(column)
        keys.add(key)
    raise RuntimeError("Column-generation limit")


def rearrange(law, n, rows, restarts=3, sweeps=80):
    q = law.ppf((np.arange(rows)+.5)/rows)
    target = n*law.mean
    rng = np.random.default_rng(701000+n)
    best = None
    for restart in range(restarts):
        x = np.column_stack([rng.permutation(q) for _ in range(n)])
        sums = x.sum(axis=1)
        old_var = np.inf
        for sweep in range(sweeps):
            for j in rng.permutation(n):
                other = sums-x[:, j]
                order = np.argsort(other, kind="stable")
                x[order, j] = q[::-1]
                sums = other+x[:, j]
            variance = float(np.var(sums))
            if old_var-variance < 1e-15:
                break
            old_var = variance
        rms = float(np.sqrt(np.mean((sums-target)**2)))
        candidate = dict(ra_rms=rms, ra_max=float(np.max(np.abs(sums-target))),
                         ra_range=float(np.ptp(sums)), ra_sweeps=sweep+1,
                         ra_mean_bias=float(sums.mean()-target))
        if best is None or rms < best["ra_rms"]:
            best = candidate
    return best


def self_check():
    from itertools import product
    # Compare pricing against complete tuple enumeration on tiny instances.
    rng = np.random.default_rng(10)
    for n in range(2, 5):
        inds = np.array([0, 1, 3, 4])
        cost = rng.normal(size=4)
        for low, high in [(0, 4*n), (n, 2*n), (2*n, 2*n)]:
            expected = min(sum(cost[j] for j in t) for t in product(range(4), repeat=n)
                           if low <= sum(inds[j] for j in t) <= high)
            got, _ = price(cost, n, inds, low, high)
            assert abs(expected-got) < 1e-10
    uniform = Law("uniform", lambda x: np.clip(x, 0, 1), lambda u: u, .5)
    for n in [3, 4, 5]:
        assert occupation_lp(uniform, n, 10)["lp_status"] == "outer_feasible"
    power = laws()[0]
    assert occupation_lp(power, 3, 80)["lp_status"] == "outer_infeasible"
    assert abs(quad(lambda x: math.exp(-1/x), 0, 1)[0]-expn(2, 1)) < 1e-12
    assert abs(quad(lambda x: x*math.exp(-1/x), 0, 1)[0]-expn(3, 1)) < 1e-12
    print("self checks passed", flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--bins", type=int, default=80)
    parser.add_argument("--rows", type=int, default=2048)
    parser.add_argument("--law", default="all")
    parser.add_argument("--n", type=int, nargs="+", default=list(range(3, 21)))
    args = parser.parse_args()
    threadpool_limits(1)
    if args.self_check:
        self_check()
        return
    Path("data").mkdir(exist_ok=True)
    suffix = "" if args.n == list(range(3, 21)) else "_n"+"-".join(map(str, args.n))
    output = Path("data")/f"results_b{args.bins}_r{args.rows}_{args.law}{suffix}.csv"
    start = time.monotonic()
    with output.open("w", newline="") as f:
        writer = None
        for law in laws():
            if args.law not in ("all", law.name):
                continue
            for n in args.n:
                record = dict(law=law.name, mean=law.mean, n=n, bins=args.bins,
                              rows=args.rows)
                record.update(occupation_lp(law, n, args.bins))
                record.update(rearrange(law, n, args.rows))
                if writer is None:
                    writer = csv.DictWriter(f, fieldnames=list(record))
                    writer.writeheader()
                writer.writerow(record)
                f.flush()
                print(law.name, n, record['lp_status'],
                      f"L1={record['lp_l1']:.3g}",
                      f"RA_RMS={record['ra_rms']:.3g}", flush=True)
    metadata = dict(seconds=time.monotonic()-start,
                    peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                    platform=os.uname().sysname, threads=1, processes=1,
                    numpy=np.__version__, seed="701000+n")
    output.with_suffix(".json").write_text(json.dumps(metadata, indent=2)+'\n')
    print(metadata, flush=True)


if __name__ == "__main__":
    main()
