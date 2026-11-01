"""Direct 2D particle simulation and orientation-uniform packing diagnostics."""
import json, math, time
from pathlib import Path
import numpy as np
rng = np.random.default_rng(202610110103)
start = time.time()
results = {}

# Generate every possibly relevant germ from an enclosing square, give each
# a random velocity of unit speed, and compute distances to actual segments.
# This independently tests the point law and its disputed capsule constant.
lam, r = .4, .5
rows = []
for t in [0., 1., 2., 5.]:
    R = r+t
    miss = 0
    reps = 12000
    for _ in range(reps):
        n = rng.poisson(lam*(2*R)**2)
        x = rng.uniform(-R, R, (n, 2))
        th = rng.uniform(0, 2*math.pi, n)
        v = np.column_stack((np.cos(th), np.sin(th)))
        closest_time = np.clip(-np.sum(x*v, axis=1), 0., t)
        closest = x + closest_time[:, None]*v
        hit = np.any(np.sum(closest**2, axis=1) <= r*r)
        miss += not hit
    q = math.exp(-lam*(math.pi*r*r+2*r*t))
    empirical = miss/reps
    se = math.sqrt(q*(1-q)/reps)
    assert abs(empirical-q) <= 5*se
    rows.append({"t": t, "replicates": reps, "empirical_void": empirical,
                 "exact_void": q, "standard_error": se,
                 "source_printed_constant_void": math.exp(-lam*(math.pi*r*r+2*math.pi*r*t))})
results["pointwise_direct_particle_simulation"] = rows

# Test the geometric obstruction with arbitrary orientations, including exact
# lattice-axis alignment where the largest number of correlated pairs occurs.
counts = []
for side_points in [10, 20, 40]:
    s = 10.
    coords = np.arange(side_points)*s
    points = np.array(np.meshgrid(coords, coords)).reshape(2, -1).T
    ratios = []
    max_count = 0
    for theta in np.r_[0., math.pi/2, rng.uniform(0, math.pi, 100)]:
        normal = np.array([-math.sin(theta), math.cos(theta)])
        proj = points@normal
        for i in rng.choice(len(points), min(30, len(points)), replace=False):
            count = int(np.count_nonzero(np.abs(proj-proj[i]) <= 2.)) - 1
            max_count = max(max_count, count)
            ratios.append(count/side_points)
    counts.append({"side_points": side_points,
                   "max_other_centers_in_radius_2_tube": max_count,
                   "max_count_divided_by_L_over_spacing": max(ratios)})
results["tube_packing_diagnostics"] = counts
results["elapsed_seconds"] = time.time()-start
Path('spatial_checks.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
print(json.dumps(results, indent=2))
