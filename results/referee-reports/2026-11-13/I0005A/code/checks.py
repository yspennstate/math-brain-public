"""Small checks only; none of these computations proves infinite-volume limits."""
import os
for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"
import csv
import json
import math
import resource
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.special import gammaln, logsumexp

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
assert os.getpriority(os.PRIO_PROCESS, 0) >= 10


def exact_divisible_check():
    # A subcritical cycle checks the deterministic implication without relying
    # on explosion. Fractions prevent loss of small positive masses by rounding.
    eta = [1, 1, -1, -1, -1, -1, -1, -1, -1]
    n = len(eta)
    u = [Fraction(0)] * n
    previous_q = None
    emitted = set()
    checks = 0
    for t in range(80):
        new = [max(Fraction(0), eta[x] + (u[(x-1) % n] + u[(x+1) % n]) / 2)
               for x in range(n)]
        q = [new[x] - u[x] for x in range(n)]
        residual = [eta[x] + (u[(x-1) % n] + u[(x+1) % n]) / 2 - u[x]
                    for x in range(n)]
        assert all(q[x] == max(residual[x], 0) for x in range(n))
        assert q[0] > 0 and q[1] > 0
        if previous_q is not None:
            for x in emitted:
                assert q[x] == (previous_q[(x-1) % n] + previous_q[(x+1) % n]) / 2
                checks += 1
        emitted.update(x for x in range(n) if new[x] > 0)
        previous_q, u = q, new
    result = {"rounds": 80, "identity_checks_at_emitted_sites": checks,
              "persistent_seed_pair": True,
              "last_seed_increment": str(previous_q[0]),
              "note": "Exact rational arithmetic; finite cycle, not a critical-scaling experiment."}
    (DATA / "divisible_exact.json").write_text(json.dumps(result, indent=2) + "\n")


def green_check():
    # Exact combinatorial return formula, evaluated with floating-point logs:
    # p_(2n)(0,0) = binom(2n,n)/8^(2n) *
    # sum_k binom(n,k)^2 binom(2k,k) binom(2n-2k,n-k).
    times = [32, 64, 128, 256, 512, 1024, 2048, 4096]
    max_n = max(times) - 1
    logfac = gammaln(np.arange(2 * max_n + 1) + 1)
    returns = np.empty(max_n + 1)
    for n in range(max_n + 1):
        k = np.arange(n + 1)
        logs = (2 * (logfac[n] - logfac[k] - logfac[n-k])
                + logfac[2*k] - 2*logfac[k]
                + logfac[2*(n-k)] - 2*logfac[n-k])
        returns[n] = np.exp(logfac[2*n] - 2*logfac[n]
                            + logsumexp(logs) - 2*n*np.log(8))
    assert abs(returns[1] - 1/8) < 1e-13
    assert abs(returns[2] - 168/4096) < 1e-13
    rows, last = [], None
    for t in times:
        s = 2 * np.arange(t)
        weights = np.where(s < t, s + 1, 2*t - 1 - s)
        # Scalar reduction avoids platform BLAS floating-point flag warnings.
        value = float(np.sum(weights * returns[:t]))
        rows.append({"t": t, "green_squared_norm": value,
                     "dyadic_log_slope": "" if last is None else (value-last)/np.log(2),
                     "limiting_coefficient": 4/math.pi**2})
        last = value
    with (DATA / "green_d4.csv").open("w") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)


def torus_distances(sources):
    if not sources.any():
        return np.full(sources.shape, 30000, dtype=np.int16)
    dist = np.where(sources, 0, 30000).astype(np.int16)
    while np.any(dist == 30000):
        nxt = dist.copy()
        for axis in range(dist.ndim):
            np.minimum(nxt, np.roll(dist, 1, axis) + 1, out=nxt)
            np.minimum(nxt, np.roll(dist, -1, axis) + 1, out=nxt)
        dist = nxt
    return dist


def parking_run(d, side, p, seed):
    rng = np.random.default_rng(seed)
    shape = (side,) * d
    volume = side**d
    initial = rng.random(volume)
    pos = np.flatnonzero(initial < p)
    holes = (initial >= p) & (initial < 2*p)
    initial_cars, initial_holes = len(pos), int(holes.sum())
    strides = side**np.arange(d-1, -1, -1, dtype=np.int64)
    rows = []
    steps_taken = 0
    for t in range(257):
        if t in (4, 16, 64, 256):
            active = np.bincount(pos, minlength=volume).reshape(shape) > 0
            dh = torus_distances(holes.reshape(shape))
            da = torus_distances(active)
            rows.append({"d": d, "L": side, "p_each_sign": p, "seed": seed, "t": t,
                         "cars": len(pos), "holes": int(holes.sum()),
                         "active_sites": int(active.sum()),
                         "hole_nearer_fraction": float(np.mean(dh < da)),
                         "tie_fraction": float(np.mean(dh == da)),
                         "median_D_h": float(np.median(dh)),
                         "median_D_a": float(np.median(da)),
                         "mean_U": steps_taken / volume})
        if t == 256:
            break
        steps_taken += len(pos)
        direction = rng.integers(0, 2*d, len(pos))
        axis, sign = direction // 2, 2*(direction % 2) - 1
        stride = strides[axis]
        coordinate = (pos // stride) % side
        dest = pos + sign * stride
        dest += np.where((sign == 1) & (coordinate == side-1), -side*stride, 0)
        dest += np.where((sign == -1) & (coordinate == 0), side*stride, 0)
        candidates = np.flatnonzero(holes[dest])
        # Shuffling then keeping one index per destination breaks all ties uniformly.
        rng.shuffle(candidates)
        unique_spots, first = np.unique(dest[candidates], return_index=True)
        keep = np.ones(len(dest), dtype=bool)
        keep[candidates[first]] = False
        holes[unique_spots] = False
        pos = dest[keep]
        assert len(pos) - int(holes.sum()) == initial_cars - initial_holes
    return rows


def distance_check():
    mask = np.zeros((5, 5), dtype=bool)
    mask[0, 0] = True
    mask[3, 2] = True
    calculated = torus_distances(mask)
    for x in np.ndindex(mask.shape):
        expected = min(sum(min(abs(x[k]-y[k]), 5-abs(x[k]-y[k])) for k in range(2))
                       for y in [(0, 0), (3, 2)])
        assert calculated[x] == expected
    return True


if __name__ == "__main__":
    exact_divisible_check()
    green_check()
    distance_check()
    rows = []
    for d, side in [(2, 128), (4, 24), (4, 32)]:
        for p in (0.5, 0.05):
            for seed in (5005, 5006):
                rows.extend(parking_run(d, side, p, seed))
                print(f"finished d={d}, L={side}, p={p}, seed={seed}", flush=True)
    with (DATA / "parking_tori.csv").open("w") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)
    (DATA / "check_environment.json").write_text(json.dumps({
        "nice": os.getpriority(os.PRIO_PROCESS, 0), "threads_per_library": 1,
        "numpy": np.__version__, "seed_list": [5005, 5006],
        "peak_rss_bytes_macos": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "boundary": "periodic; synchronous discrete-time walks; strict torus graph distance",
        "interpretation": "Checks only; spatial samples are dependent; no asymptotic fit."}, indent=2) + "\n")
