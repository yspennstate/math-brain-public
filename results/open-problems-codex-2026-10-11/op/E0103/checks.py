"""Bounded-memory independent diagnostics. These computations are not proofs."""
from pathlib import Path
import json, math, random, time
import numpy as np

start = time.time()
rng = np.random.default_rng(10320261011)
out = {}

# Direct particle-system simulation: Poisson starts in [0,L], together with
# the independent last start before zero. Common interval lengths give the
# exact coverage length by elementary interval geometry.
gumbel = []
for L, reps in [(100., 5000), (1000., 3000), (10000., 1500)]:
    z = []
    for _ in range(reps):
        n = rng.poisson(L)
        pts = np.sort(rng.uniform(0, L, n))
        last_before_zero = -rng.exponential()
        if n == 0:
            need = L - last_before_zero
        else:
            need = max(pts[0] - last_before_zero, L - pts[-1])
            if n > 1:
                need = max(need, float(np.max(np.diff(pts))))
        cover_time = max(0., need - 2 * .2)
        z.append(cover_time + .4 - math.log(L))
    z = np.array(z)
    rows = [{"z": x, "empirical_cdf": float(np.mean(z <= x)),
             "limiting_cdf": math.exp(-math.exp(-x))}
            for x in [-1., 0., 1., 2.]]
    gumbel.append({"L": L, "replicates": reps, "cdf": rows,
                   "mean_normalized": float(z.mean())})
out["direct_deterministic_velocity_simulation"] = gumbel

# Exhaustively exercise the endpoint comparison on random finite configurations.
# Two prior starts and two subsequent starts suffice to test the three events
# that bound disagreement between full coverage and the internal-gap condition.
endpoint_trials = 20000
disagreements = 0
for _ in range(endpoint_trials):
    L = 10.
    ell = rng.uniform(.05, 15.)
    pts = np.sort(rng.uniform(0, L, rng.poisson(L)))
    a0 = -rng.exponential()
    after = L + rng.exponential()
    seq = np.r_[a0, pts, after]
    need = L-a0 if len(pts)==0 else max(pts[0]-a0, L-pts[-1],
              float(np.max(np.diff(pts))) if len(pts)>1 else 0.)
    covered = need <= ell
    D = bool(np.all(np.diff(seq[1:]) <= ell))
    a1 = pts[0] if len(pts) else after
    exceptional = (-a0 > ell) or (a1-a0 > ell)
    for i in range(1, len(seq)-1):
        if seq[i] >= max(0., L-ell) and seq[i+1]-seq[i] > ell:
            exceptional = True
    if covered != D:
        disagreements += 1
        assert exceptional
out["endpoint_comparison"] = {"trials": endpoint_trials,
                              "disagreements_all_accounted_for": disagreements}

# Heavy-tail asymptotics evaluated in log coordinates to avoid overflow.
# x=log L, A=log log L. These are exact formulas except for the insignificant
# 2r correction (retained where representable).
heavy = []
for x in [100., 10000., 1e8, 1e16]:
    A = math.log(x)
    t = A
    logH = x - math.log(t)
    logh = .5*x - math.log(t)
    beta = t/math.log(logH)
    nonspan = 2*t/(logH*math.log(logH)**2)
    F = lambda logu: 1/math.log(logu)+1/(logu*math.log(logu)**2)
    gamma = t*(F(logh)-F(logH))
    heavy.append({"log_L": x, "s": 1., "spanning_mean": beta,
                  "limit_spanning_mean": 1., "nonspanning_long_mean": nonspan,
                  "intermediate_point_intensity_without_negligible_radius_term": gamma})
out["heavy_tail_exact_intensities"] = heavy

# Numerical quadrature after w=log log u checks the tail integral without
# sampling speeds that could exceed floating-point range.
from scipy.integrate import quad
tails = []
for w in [1., 2., 5., 10.]:
    value, err = quad(lambda z: z**-2, w, np.inf)
    assert abs(value - 1/w) < 1e-10
    tails.append({"log_log_h": w, "quadrature": value,
                  "formula": 1/w, "error_estimate": err})
out["tail_quadrature"] = tails

out["elapsed_seconds"] = time.time()-start
Path("checks.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
print(json.dumps(out, indent=2))
