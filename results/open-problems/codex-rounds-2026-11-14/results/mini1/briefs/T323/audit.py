#!/usr/bin/env python3
"""Small independent checks for PROOF.md; standard library only."""

import json
import math
import os
import random
import resource
import signal
import sys
import time
from pathlib import Path

assert os.environ.get("OMP_NUM_THREADS") == "1"
PRIORITY = os.getpriority(os.PRIO_PROCESS, 0)
assert PRIORITY >= 15, f"process niceness {PRIORITY} is below 15"
resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
signal.alarm(120)
START = time.monotonic()
HERE = Path(__file__).resolve().parent


def cartesian_angular(theta, a, omega, kappa, beta, identity_key=False):
    """Construct Q,K,V, softmax, and tangent projection in Cartesian space."""
    x = [(math.cos(t), math.sin(t)) for t in theta]
    kx = x if identity_key else [(-kappa * y, kappa * u) for u, y in x]
    vx = [(a * u + omega * y, a * y - omega * u) for u, y in x]
    velocities = []
    radial_residual = 0.0
    for u, y in x:
        scores = [beta * (u * ku + y * ky) for ku, ky in kx]
        shift = max(scores)
        weights = [math.exp(s - shift) for s in scores]
        normalizer = sum(weights)
        fx = sum(w * v[0] for w, v in zip(weights, vx)) / normalizer
        fy = sum(w * v[1] for w, v in zip(weights, vx)) / normalizer
        radial = u * fx + y * fy
        px, py = fx - radial * u, fy - radial * y
        velocities.append(-y * px + u * py)
        radial_residual = max(radial_residual, abs(u * px + y * py))
    return velocities, radial_residual


def reduced_pair(theta, a, omega, kappa, beta, identity_key=False):
    delta = theta[1] - theta[0]
    s, c = math.sin(delta), math.cos(delta)
    if identity_key:
        p = 1.0 / (1.0 + math.exp(beta * (1.0 - c)))
        ddelta = -2.0 * a * p * s
        dmean = -omega + omega * p * (1.0 - c)
    else:
        t = math.tanh(beta * kappa * s / 2.0)
        ddelta = -a * s + omega * (1.0 - c) * t
        dmean = -omega * (1.0 + c) / 2.0 - a * t * s / 2.0
    return [dmean - ddelta / 2.0, dmean + ddelta / 2.0]


def rk4(fun, initial, duration, dt):
    steps = round(duration / dt)
    assert abs(steps * dt - duration) < 1e-10
    theta = list(initial)
    for _ in range(steps):
        k1 = fun(theta)
        k2 = fun([t + dt * k / 2 for t, k in zip(theta, k1)])
        k3 = fun([t + dt * k / 2 for t, k in zip(theta, k2)])
        k4 = fun([t + dt * k for t, k in zip(theta, k3)])
        theta = [t + dt * (v1 + 2 * v2 + 2 * v3 + v4) / 6
                 for t, v1, v2, v3, v4 in zip(theta, k1, k2, k3, k4)]
    return theta


def jacobian(theta, params, h=1e-5):
    n = len(theta)
    columns = []
    for j in range(n):
        plus, minus = list(theta), list(theta)
        plus[j] += h
        minus[j] -= h
        fp = cartesian_angular(plus, *params)[0]
        fm = cartesian_angular(minus, *params)[0]
        columns.append([(p - m) / (2 * h) for p, m in zip(fp, fm)])
    return [[columns[j][i] for j in range(n)] for i in range(n)]


def basin_h(delta, q):
    return math.tan(delta / 2.0) * math.tanh(q * math.sin(delta) / 2.0)


rng = random.Random(323)
random_error = 0.0
radial_error = 0.0
for _ in range(1000):
    theta = [rng.uniform(-6, 6), rng.uniform(-6, 6)]
    params = [rng.uniform(0.1, 3.0) for _ in range(4)]
    for identity in (False, True):
        original, radial = cartesian_angular(theta, *params, identity)
        reduced = reduced_pair(theta, *params, identity)
        random_error = max(random_error, *(abs(u-v) for u, v in zip(original, reduced)))
        radial_error = max(radial_error, radial)
assert random_error < 1e-12
assert radial_error < 1e-12

linearizations = []
for n in (2, 4, 6, 10):
    for params in ((1., 1., 1., 2.), (1., 1., 1., 1.), (1., 1., 1., .5),
                   (.7, 1.3, .8, 2.1)):
        a, omega, kappa, beta = params
        b = omega * kappa * beta
        sigma = [1] * (n//2) + [-1] * (n//2)
        phase = .371
        for kind in ("antipodal", "consensus"):
            theta = [phase + (math.pi if s == -1 else 0) for s in sigma]
            if kind == "consensus":
                theta = [phase] * n
            actual = jacobian(theta, params)
            expected = [[(-b if i == j else 0) + b/n + a*sigma[i]*sigma[j]/n
                         for j in range(n)] for i in range(n)]
            rates = [0., a-b] + [-b] * (n-2)
            if kind == "consensus":
                expected = [[(-a if i == j else 0) + a/n for j in range(n)] for i in range(n)]
                rates = [0.] + [-a] * (n-1)
            error = max(abs(actual[i][j]-expected[i][j]) for i in range(n) for j in range(n))
            assert error < 2e-8
            linearizations.append(dict(n=n, params=params, kind=kind,
                                       max_error=error, predicted_eigenvalues=rates,
                                       cartesian_finite_difference_matrix=actual))

# Bisection uses the scalar formula; a second root is found using only the
# original projected Cartesian vector field at symmetric token angles.
def bisect(fun, lo, hi):
    assert fun(lo) < 0 < fun(hi)
    for _ in range(70):
        mid = (lo + hi) / 2
        if fun(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

root_scalar = bisect(lambda d: basin_h(d, 2.)-1., 1e-5, math.pi-1e-5)
def direct_gap_velocity(d):
    v, _ = cartesian_angular([-d/2, d/2], 1., 1., 1., 2.)
    return v[1]-v[0]
root_original = bisect(direct_gap_velocity, 1e-5, math.pi-1e-5)
assert abs(root_scalar-root_original) < 1e-12

# A finite scan checks numerical signs but is not a substitute for (11).
threshold_signs = []
for q in (.1, .5, 1., 2., 10.):
    values = [basin_h(math.pi*i/2000, q) for i in range(1, 2000)]
    assert all(u < v for u, v in zip(values, values[1:]))
    assert max(values) < q
    threshold_signs.append(dict(q=q, maximum_sampled_h=max(values),
                               minimum_increment=min(v-u for u,v in zip(values, values[1:]))))

trajectories = []
for name, initial, identity in (
    ("pair_consensus", [-root_scalar/4, root_scalar/4], False),
    ("pair_antipodal", [-(root_scalar+math.pi)/4, (root_scalar+math.pi)/4], False),
    ("pair_identity_key", [-1.3, 1.3], True),
    ("four_consensus", [.1, .04, -.04, -.08], False),
    ("four_antipodal", [.02, -.03, math.pi+.025, math.pi-.015], False),
):
    fun = lambda theta: cartesian_angular(theta, 1., 1., 1., 2., identity)[0]
    duration = 60. if identity else 20.
    final = rk4(fun, initial, duration, .01)
    finer = rk4(fun, initial, duration, .005)
    dt_error = max(abs(u-v) for u,v in zip(final, finer))
    assert dt_error < 2e-7
    if "antipodal" in name:
        target = [0.] * (len(final)//2) + [math.pi] * (len(final)//2)
        residuals = [t-s for t,s in zip(final, target)]
    else:
        residuals = final
    spread = max(residuals)-min(residuals)
    assert spread < 5e-6
    row = dict(name=name, initial=initial, final_angles=final,
               duration=duration, dt=.01, half_step_error=dt_error, target_spread=spread)
    if len(initial) == 2:
        reduced = rk4(lambda theta: reduced_pair(theta, 1., 1., 1., 2., identity), initial, duration, .01)
        reduction_error = max(abs(u-v) for u,v in zip(final, reduced))
        assert reduction_error < 1e-9
        row["independent_reduced_trajectory_error"] = reduction_error
    trajectories.append(row)

peak_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
peak_rss_bytes = peak_rss if sys.platform == "darwin" else peak_rss * 1024
assert peak_rss_bytes < 1_000_000_000
results = dict(
    process_niceness=PRIORITY, peak_rss_bytes=peak_rss_bytes,
    random_cases=1000, random_two_token_velocity_max_error=random_error,
    projection_radial_max_error=radial_error,
    linearizations=linearizations,
    root_scalar=root_scalar, root_original_cartesian=root_original,
    uniform_antipodal_basin_probability=1.-root_scalar/math.pi,
    monotonicity_scan=threshold_signs, trajectories=trajectories,
    wall_seconds=time.monotonic()-START,
)
(HERE / "audit_data.json").write_text(json.dumps(results, indent=2)+"\n")
print(f"process niceness: {PRIORITY}; peak RSS bytes: {peak_rss_bytes}")
print("PASS: 1000 random parameter/angle cases, both query-key choices")
print(f"maximum angular-velocity discrepancy: {random_error:.3e}")
print(f"maximum projection radial residual: {radial_error:.3e}")
print(f"PASS: {len(linearizations)} full Jacobian comparisons (n=2,4,6,10)")
print("maximum Jacobian discrepancy: " + f"{max(r['max_error'] for r in linearizations):.3e}")
print(f"separatrix (a=omega=kappa=1, beta=2): {root_scalar:.15f}")
print(f"independent Cartesian root discrepancy: {abs(root_scalar-root_original):.3e}")
print(f"uniform antipodal basin probability: {1.-root_scalar/math.pi:.15f}")
print("PASS: 5 monotonicity scans, including threshold endpoint bound H<q")
print("PASS: 5 original-system RK4 trajectories, each repeated at half step")
for row in trajectories:
    print(f"  {row['name']}: target spread={row['target_spread']:.3e}, half-step error={row['half_step_error']:.3e}")
print(f"elapsed seconds: {results['wall_seconds']:.3f}")
print("data: audit_data.json")
