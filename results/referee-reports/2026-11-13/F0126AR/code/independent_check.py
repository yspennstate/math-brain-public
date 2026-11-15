"""Independent finite checks for the referee; no submitted code is imported.

Standard library only; fixed quenched, nonuniform scenery; both independent
Monte Carlo samples and exhaustive path counts. Run from any directory.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))

from collections import Counter
from itertools import product
from math import comb, log, sqrt
from pathlib import Path
import hashlib
import json
import random
import resource
import time

START = time.monotonic()
ROOT = Path(__file__).resolve().parents[1]
F = ((1, 0), (-1, 0), (1, 1), (-1, -1))
B = ((1, 1), (0, 1))
BI = ((1, -1), (0, 1))
R = ((0, -1), (1, 0))
A = ((1, -2), (1, -1))
AI = ((-1, 2), (-1, 1))
I = ((1, 0), (0, 1))

def mv(m, x):
    return tuple(sum(m[i][j] * x[j] for j in range(2)) for i in range(2))

def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def transpose(m):
    return tuple(zip(*m))

def det(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]

assert mm(mm(B, R), BI) == A
assert mm(A, AI) == I and det(A) == 1
assert mm(A, A) == ((-1, 0), (0, -1))
assert mm(transpose(A), A) == ((2, -3), (-3, 5)) != I
assert Counter(mv(A, f) for f in F) == Counter(F)
assert mv(B, (1, 0)) == F[0] and mv(B, (0, 1)) == F[2]
assert det(B) == 1

# Every linear automorphism preserving the kernel is determined by images of
# u=(1,0), v=(1,1). Enumerate those images directly from F.
automorphisms = []
for u, v in product(F, repeat=2):
    m = ((u[0], v[0] - u[0]), (u[1], v[1] - u[1]))
    if abs(det(m)) == 1 and Counter(mv(m, f) for f in F) == Counter(F):
        automorphisms.append(m)
euclidean = [m for m in automorphisms if mm(transpose(m), m) == I]
assert len(automorphisms) == 8 and len(euclidean) == 2
# Four representatives modulo the Euclidean intersection {I,-I}.
D = ((1, -2), (0, -1))
representatives = [I, A, D, mm(A, D)]
def inv_unimodular(m):
    d = det(m)
    return ((m[1][1] // d, -m[0][1] // d), (-m[1][0] // d, m[0][0] // d))
for i, g in enumerate(representatives):
    assert g in automorphisms
    for h in representatives[i + 1:]:
        ratio = mm(h, inv_unimodular(g))
        assert mm(transpose(ratio), ratio) != I

# A second recurrence check: integer spatial path-count recursion, independent
# of the diagonal-coordinate argument in the submitted proof.
counts = Counter({(0, 0): 1})
returns = []
for n in range(1, 25):
    nxt = Counter()
    for (x, y), k in counts.items():
        for dx, dy in F:
            nxt[x + dx, y + dy] += k
    counts = nxt
    if n % 2 == 0:
        expected = comb(n, n // 2) ** 2
        assert counts[(0, 0)] == expected
        returns.append({"time": n, "return_paths": expected, "total_paths": 4 ** n})
    else:
        assert counts[(0, 0)] == 0

def total_variation(p, q, zp, zq):
    return sum(abs(p[k] / zp - q[k] / zq) for k in p.keys() | q.keys()) / 2

def enumerate_records(color, h, weights=None):
    hist = Counter()
    for steps in product(range(4), repeat=h):
        x = y = 0
        rec = [color((0, 0))]
        weight = 1
        for j in steps:
            dx, dy = F[j]
            x, y = x + dx, y + dy
            rec.append(color((x, y)))
            if weights is not None:
                weight *= weights[j]
        hist[tuple(rec)] += weight
    return hist

def simulate_records(color, h, n, seed):
    rng = random.Random(seed)
    hist = Counter()
    origin_color = color((0, 0))
    for _ in range(n):
        x = y = 0
        rec = [origin_color]
        for _ in range(h):
            dx, dy = F[rng.randrange(4)]
            x, y = x + dx, y + dy
            rec.append(color((x, y)))
        hist[tuple(rec)] += 1
    return hist

experiments = []
for q, probabilities, seed in [(2, (0.8, 0.2), 12617), (3, (0.7, 0.2, 0.1), 12619)]:
    rng = random.Random(seed)
    # Covers all queried coordinates, including A^-1 times a reachable site.
    radius = 40
    scenery = {(x, y): rng.choices(range(q), weights=probabilities)[0]
               for x in range(-radius, radius + 1) for y in range(-radius, radius + 1)}
    color = scenery.__getitem__
    transformed = lambda x: color(mv(AI, x))
    h = 7
    exact = enumerate_records(color, h)
    exact_transformed = enumerate_records(transformed, h)
    assert exact == exact_transformed
    assert sum(exact.values()) == 4 ** h
    n = 120000
    mc1 = simulate_records(color, h, n, seed + 1)
    mc2 = simulate_records(transformed, h, n, seed + 2)
    keys = exact.keys() | mc1.keys() | mc2.keys()
    # Union Hoeffding bound for both histograms; fixed before looking at data.
    alpha = 1e-6
    eps = sqrt(log(4 * len(keys) / alpha) / (2 * n))
    max_errors = [max(abs(mc[k] / n - exact[k] / (4 ** h)) for k in keys)
                  for mc in (mc1, mc2)]
    assert max(max_errors) < eps
    # Exact paired identity along long forward-only trajectories.
    paired_rng = random.Random(seed + 3)
    for _ in range(10000):
        x = y = 0
        for _ in range(13):
            assert color((x, y)) == transformed(mv(A, (x, y)))
            dx, dy = paired_rng.choice(F)
            x, y = x + dx, y + dy
    # Negative control: retain F but break its symmetry by unequal weights.
    weights = (4, 1, 3, 2)
    bad1 = enumerate_records(color, h, weights)
    bad2 = enumerate_records(transformed, h, weights)
    bad_tv = total_variation(bad1, bad2, 10 ** h, 10 ** h)
    assert bad_tv > 0
    experiments.append({
        "alphabet_size": q, "scenery_law": probabilities, "seed": seed,
        "scenery_sha256": hashlib.sha256(json.dumps(sorted(scenery.items())).encode()).hexdigest(),
        "horizon_increments": h, "record_length": h + 1,
        "exact_paths": 4 ** h, "exact_record_support": len(exact),
        "exact_tv": 0, "independent_samples_each": n,
        "empirical_tv_between_records": total_variation(mc1, mc2, n, n),
        "empirical_tv_vs_exact": [total_variation(mc, exact, n, 4 ** h) for mc in (mc1, mc2)],
        "max_cell_errors": max_errors, "union_hoeffding_tolerance": eps,
        "hoeffding_failure_bound": alpha,
        "paired_paths": 10000, "paired_forward_record_length": 13,
        "broken_kernel_symmetry_control_tv": bad_tv,
        "histogram_original": {"".join(map(str,k)):v for k,v in sorted(mc1.items())},
        "histogram_transformed": {"".join(map(str,k)):v for k,v in sorted(mc2.items())},
        "histogram_exact_path_counts": {"".join(map(str,k)):v for k,v in sorted(exact.items())},
    })

result = {"status": "PASS", "nice": os.getpriority(os.PRIO_PROCESS, 0),
          "threads": 1, "matrix": A, "kernel_image": [mv(A, f) for f in F],
          "linear_kernel_automorphisms": automorphisms,
          "euclidean_linear_kernel_automorphisms": euclidean,
          "four_inequivalent_kernel_representatives": representatives,
          "return_count_checks": returns, "experiments": experiments,
          "seconds": time.monotonic() - START,
          "max_rss_native_units": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
          "rss_unit_note": "bytes on macOS; KiB on Linux"}
data = ROOT / "data"
data.mkdir(exist_ok=True)
(data / "independent_check.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k:v for k,v in result.items() if k != "experiments"}, indent=2))
for e in experiments:
    print(json.dumps({k:v for k,v in e.items() if not k.startswith("histogram")}))
