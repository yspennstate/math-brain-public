"""Finite observation laws and finite-cycle inference; no infinite reconstruction claim.

Run: OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/experiments.py
All law calculations retain the origin and Y_0. Horizon n means n increments.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))

import hashlib
import itertools
import json
from pathlib import Path
import resource
import time
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)


def bit_at(x, y=0, seed=126):
    """A fixed reproducible scenery realization; not a cryptographic randomness claim."""
    return hashlib.sha256(f"{seed}:{x}:{y}".encode()).digest()[0] & 1


def laws_1d(colors, steps, probs, horizon):
    radius = (len(colors) - 1) // 2
    a = np.zeros((2, len(colors)))
    a[int(colors[radius]), radius] = 1.0
    laws = [a.sum(axis=1)]
    for _ in range(horizon):
        prop = np.zeros_like(a)
        for step, p in zip(steps, probs):
            if step > 0:
                prop[:, step:] += p * a[:, :-step]
            elif step < 0:
                prop[:, :step] += p * a[:, -step:]
            else:
                prop += p * a
        a = np.empty((2 * len(prop), len(colors)))
        a[::2] = prop * (colors == 0)
        a[1::2] = prop * (colors == 1)
        laws.append(a.sum(axis=1))
    return laws


def brute_1d(colors, steps, probs, horizon):
    radius = (len(colors) - 1) // 2
    out = np.zeros(2 ** (horizon + 1))
    for seq in itertools.product(range(len(steps)), repeat=horizon):
        x, word, weight = 0, int(colors[radius]), 1.0
        for j in seq:
            x += steps[j]
            weight *= probs[j]
            word = 2 * word + int(colors[radius + x])
        out[word] += weight
    return out


def hit_probability(steps, probs, target, horizon):
    radius = horizon * max(abs(s) for s in steps)
    a = np.zeros(2 * radius + 1)
    a[radius] = 1.0
    out = [float(target == 0)]
    if target == 0:
        return [1.0] * (horizon + 1)
    for _ in range(horizon):
        b = np.zeros_like(a)
        for step, p in zip(steps, probs):
            if step > 0:
                b[step:] += p * a[:-step]
            elif step < 0:
                b[:step] += p * a[-step:]
            else:
                b += p * a
        b[radius + target] = 0.0
        a = b
        out.append(float(1.0 - a.sum()))
    return out


def laws_2d_counts(colors, horizon):
    """Integer path counts for simple square walk in B-basis coordinates."""
    side = len(colors)
    center = side // 2
    a = np.zeros((2, side, side), dtype=np.int64)
    a[int(colors[center, center]), center, center] = 1
    laws = [a.sum(axis=(1, 2))]
    for _ in range(horizon):
        b = np.zeros_like(a)
        b[:, 1:, :] += a[:, :-1, :]
        b[:, :-1, :] += a[:, 1:, :]
        b[:, :, 1:] += a[:, :, :-1]
        b[:, :, :-1] += a[:, :, 1:]
        a = np.empty((2 * len(b), side, side), dtype=np.int64)
        a[::2] = b * (colors == 0)
        a[1::2] = b * (colors == 1)
        laws.append(a.sum(axis=(1, 2)))
    return laws


def tv_experiments():
    h = 14
    xs = np.arange(-2 * h, 2 * h + 1)
    colors = np.array([bit_at(int(x)) for x in xs])
    rows = []
    for label, steps, probs in [
        ("sublattice", [-2, 2], [0.5, 0.5]),
        ("symmetric_five", [-2, -1, 0, 1, 2], [0.2] * 5),
        ("asymmetric_five", [-2, -1, 0, 1, 2], [0.1, 0.3, 0.25, 0.2, 0.15]),
    ]:
        altered = colors.copy()
        altered[2 * h + 1] ^= 1
        a = laws_1d(colors, steps, probs, h)
        b = laws_1d(altered, steps, probs, h)
        np.testing.assert_allclose(a[5], brute_1d(colors, steps, probs, 5), atol=2e-15)
        np.testing.assert_allclose(b[5], brute_1d(altered, steps, probs, 5), atol=2e-15)
        hits = hit_probability(steps, probs, 1, h)
        prev = -1.0
        for n, (p, q) in enumerate(zip(a, b)):
            distance = float(0.5 * np.abs(p - q).sum())
            assert abs(p.sum() - 1.0) < 2e-12
            assert abs(q.sum() - 1.0) < 2e-12
            assert distance >= prev - 2e-12
            assert distance <= hits[n] + 2e-12
            rows.append(dict(model=label, increments=n, tv=distance, coupling_hit_upper=hits[n]))
            prev = distance
    # B=[[1,1],[0,1]], R=[[0,-1],[1,0]], A=B R B^-1.
    B = np.array([[1, 1], [0, 1]], dtype=np.int64)
    R = np.array([[0, -1], [1, 0]], dtype=np.int64)
    A = np.array([[1, -2], [1, -1]], dtype=np.int64)
    np.testing.assert_array_equal(A @ B, B @ R)
    np.testing.assert_array_equal(A @ A, -np.eye(2, dtype=np.int64))
    support = {(1, 0), (-1, 0), (1, 1), (-1, -1)}
    assert {tuple(A @ x) for x in support} == support
    assert not np.array_equal(A.T @ A, np.eye(2))
    h2 = 12
    c = np.array([[bit_at(u + v, v, 127) for v in range(-h2, h2 + 1)]
                  for u in range(-h2, h2 + 1)])
    # A^-1 B(u,v) = B(v,-u).
    cA = np.array([[bit_at(v - u, -u, 127) for v in range(-h2, h2 + 1)]
                   for u in range(-h2, h2 + 1)])
    p = laws_2d_counts(c, h2)
    q = laws_2d_counts(cA, h2)
    for n, (pn, qn) in enumerate(zip(p, q)):
        assert int(pn.sum()) == 4 ** n
        assert np.array_equal(pn, qn)
        rows.append(dict(model="sheared_square_symmetry", increments=n, tv=0.0,
                         exact_integer_equality=True, total_paths=4 ** n))
    (DATA / "tv_results.json").write_text(json.dumps(rows, indent=2) + "\n")
    (DATA / "tv_scenery.json").write_text(json.dumps(dict(seed_1d=126, seed_2d=127,
         coordinates_1d=xs.tolist(), colors_1d=colors.tolist(), local_flip_site=1,
         B=B.tolist(), A=A.tolist()), indent=2) + "\n")
    return rows


def cycle_inference(trials=8, size=11, length=2000):
    """Enumerate all binary cycle sceneries and sum over all hidden walk paths.

    Origin is fixed at zero. The estimator gets only the colors and known step law.
    The true scenery and trajectory are used exclusively for generation and scoring.
    """
    steps = np.array([-2, -1, 0, 1, 2])
    probs = np.array([0.1, 0.3, 0.25, 0.2, 0.15])
    assert abs(float(steps @ probs)) < 1e-15
    candidates = ((np.arange(2 ** size)[:, None] >> np.arange(size)) & 1).astype(np.int8)
    checkpoints = {100, 500, length}
    results = []
    for seed in range(12600, 12600 + trials):
        rng = np.random.default_rng(seed)
        truth = rng.integers(0, 2, size=size)
        path = np.r_[0, np.cumsum(rng.choice(steps, size=length, p=probs))] % size
        record = truth[path]
        alpha = np.zeros((len(candidates), size))
        alpha[:, 0] = candidates[:, 0] == record[0]
        loglike = np.where(alpha.sum(axis=1) > 0, 0.0, -np.inf)
        equivalent = np.zeros(len(candidates), dtype=bool)
        for direction in (1, -1):
            for shift in range(size):
                shifted = truth[(direction * np.arange(size) + shift) % size]
                equivalent |= np.all(candidates == shifted, axis=1)
        for t, color in enumerate(record[1:], 1):
            propagated = sum(p * np.roll(alpha, int(k), axis=1) for k, p in zip(steps, probs))
            propagated *= candidates == color
            norms = propagated.sum(axis=1)
            live = norms > 0
            alpha.fill(0.0)
            alpha[live] = propagated[live] / norms[live, None]
            loglike[live] += np.log(norms[live])
            loglike[~live] = -np.inf
            if t in checkpoints:
                weights = np.exp(loglike - np.max(loglike))
                weights /= weights.sum()
                map_id = int(np.argmax(weights))
                results.append(dict(seed=seed, increments=t, cycle_size=size,
                    map_equivalent=bool(equivalent[map_id]),
                    posterior_true_dihedral_orbit=float(weights[equivalent].sum()),
                    posterior_map=float(weights[map_id]),
                    truth=truth.tolist(), estimate=candidates[map_id].tolist()))
        np.savez_compressed(DATA / f"cycle_record_{seed}.npz", observations=record)
    (DATA / "cycle_results.json").write_text(json.dumps(results, indent=2) + "\n")
    return results


def main():
    start = time.monotonic()
    tv = tv_experiments()
    cycles = cycle_inference()
    summary = dict(priority=os.getpriority(os.PRIO_PROCESS, 0), threads=1,
        elapsed_seconds=time.monotonic() - start,
        max_rss_bytes_macos=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        tv_at_final_horizons={label: [r for r in tv if r["model"] == label][-1]
                             for label in sorted({r["model"] for r in tv})},
        cycle_by_horizon={str(t): dict(trials=sum(r["increments"] == t for r in cycles),
            map_successes=sum(r["increments"] == t and r["map_equivalent"] for r in cycles),
            mean_true_orbit_posterior=float(np.mean([r["posterior_true_dihedral_orbit"]
                    for r in cycles if r["increments"] == t]))) for t in (100, 500, 2000)},
        caution="Finite horizons and a finite-cycle surrogate do not prove infinite-lattice reconstruction.")
    (DATA / "experiment_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == "__main__":
    main()
