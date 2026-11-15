"""Deterministic checks only; no random samples and no sandpile simulation.

Uses proxy radial Green weights, explicitly not exact lattice Green values.
The proofs in REPORT.md do not depend on this program.
"""
import csv
import itertools
import json
import math
import os
from pathlib import Path
import resource
import time

ROOT = Path(__file__).resolve().parents[1]
START = time.monotonic()
NICE = os.getpriority(os.PRIO_PROCESS, 0)
assert NICE >= 10, NICE
try:
    resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
    AS_LIMIT = 4 * 1024**3
except (ValueError, OSError) as error:
    # macOS in this sandbox rejects RLIMIT_AS. Arrays here have <=2401 entries;
    # record measured RSS instead of claiming that an OS limit was installed.
    AS_LIMIT = str(error)


def save_csv(name, rows):
    with (ROOT / 'data' / name).open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


# Finite Holder optimizer: exact formula checked by a separate direct sum.
holder_rows = []
for d in (3, 4, 5, 6, 8):
    p = d / 2
    q = p / (p - 1)
    for radius in (16, 64, 256, 1024):
        multiplicity = [1] + [(2*r+1)**d - (2*r-1)**d for r in range(1, radius+1)]
        weights = [(1+r)**(2-d) for r in range(radius+1)]
        power_sum = math.fsum(n*w**q for n, w in zip(multiplicity, weights))
        target = 37.0
        depths = [target*w**(q-1)/power_sum for w in weights]
        deficit = math.fsum(n*w*a for n, w, a in zip(multiplicity, weights, depths))
        cost = math.fsum(n*a**p for n, a in zip(multiplicity, depths))
        predicted = target**p / power_sum**(p-1)
        kkt = [p*a**(p-1)/w for a, w in zip(depths, weights)]
        assert abs(deficit/target - 1) < 2e-12
        assert abs(cost/predicted - 1) < 2e-12
        assert max(kkt)/min(kkt) - 1 < 2e-12
        holder_rows.append(dict(d=d, radius=radius, power_sum=power_sum,
                                power_sum_over_log_radius=power_sum/math.log(radius),
                                deficit=deficit, cost=cost, formula_ratio=cost/predicted,
                                one_site_cost=target**p))
save_csv('holder_optimizer.csv', holder_rows)


def optimal_depth(t, p):
    """Solve 2a + p*a**(p-1) = t by monotone bisection."""
    high = min(t/2, (t/p)**(1/(p-1)))
    low = 0.0
    for _ in range(55):
        middle = (low+high)/2
        if 2*middle + p*middle**(p-1) < t:
            low = middle
        else:
            high = middle
    return (low+high)/2


# Continuum radial quadrature for J(a)=a^2+a^p, plus a unit central site.
# The outer range is far beyond the predicted nonlinear-to-quadratic cutoff.
mixed_rows = []
for d in (5, 6, 8):
    p = d/2
    for amplitude in (1e2, 1e4, 1e6, 1e8):
        dual = amplitude**(p-1)
        tmax = 0.5*math.log(amplitude) + 14/(d-4)
        previous = None
        for bins in (1200, 2400):
            dt = tmax/bins
            center = optimal_depth(dual, p)
            deficit_terms = [center]
            cost_terms = [center**2+center**p]
            max_kkt_error = 0.0
            for i in range(bins):
                t = (i+0.5)*dt
                w = math.exp((2-d)*t)
                a = optimal_depth(dual*w, p)
                deficit_terms.append(math.exp(2*t)*a*dt)
                cost_terms.append(math.exp(d*t)*(a*a+a**p)*dt)
                max_kkt_error = max(max_kkt_error, abs((2*a+p*a**(p-1))/(dual*w)-1))
            deficit = math.fsum(deficit_terms)
            cost = math.fsum(cost_terms)
            normalized = cost/(deficit**p/math.log(math.e+deficit)**(p-1))
            if previous is not None:
                refinement_error = abs(cost/previous-1)
                assert refinement_error < 5e-5, (d, amplitude, refinement_error)
            previous = cost
        assert max_kkt_error < 2e-13
        mixed_rows.append(dict(d=d, amplitude=amplitude, cutoff=amplitude**0.5,
                               deficit=deficit, cost=cost,
                               cost_over_critical_prediction=normalized,
                               one_site_over_mixed_cost=(deficit**2+deficit**p)/cost,
                               quadrature_refinement_relative=refinement_error,
                               max_kkt_relative_error=max_kkt_error))
save_csv('mixed_radial.csv', mixed_rows)


# Direct finite-difference checks of the logarithmic barrier, also in low d.
barrier_rows = []
for d, radius in ((1, 100), (2, 12), (3, 6), (5, 3)):
    max_scaled_laplacian = -math.inf
    max_direct_difference = 0.0
    for x in itertools.product(range(-radius, radius+1), repeat=d):
        square = sum(t*t for t in x)
        s = 1+square
        direct = math.fsum(math.log(1+square+2*sign*xi+1)
                           for xi in x for sign in (-1, 1))/(2*d) - math.log(s)
        paired = math.log1p(1/s) + math.fsum(math.log1p(-4*xi*xi/(s+1)**2)
                                             for xi in x)/(2*d)
        max_direct_difference = max(max_direct_difference, abs(direct-paired))
        max_scaled_laplacian = max(max_scaled_laplacian, s*direct)
        assert direct <= 1/s + 2e-13
    barrier_rows.append(dict(d=d, checked_points=(2*radius+1)**d,
                             max_scaled_laplacian=max_scaled_laplacian,
                             max_direct_vs_paired_error=max_direct_difference))
save_csv('barrier_identity.csv', barrier_rows)


# Nonconvex finite variational problem for 0<gamma<1: one-site optimum.
subunit_rows = []
for gamma in (0.25, 0.5, 0.9):
    weights = [1, 0.5, 0.2, 0.05]
    target = 17.0
    for profile in ([17.0, 0, 0, 0], [8.5, 17.0, 0, 0], [0, 0, 85.0, 0]):
        deficit = math.fsum(a*w for a, w in zip(profile, weights))
        assert abs(deficit-target) < 1e-12
        cost = math.fsum(a**gamma for a in profile)
        optimum = (target/max(weights))**gamma
        assert cost >= optimum-1e-12
        subunit_rows.append(dict(gamma=gamma, profile=str(profile), deficit=deficit,
                                 cost=cost, one_site_optimum=optimum))
save_csv('subunit_one_site.csv', subunit_rows)

summary = dict(nice=NICE, threads=1, random_samples=0,
               elapsed_seconds=time.monotonic()-START,
               peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
               address_space_limit=AS_LIMIT,
               holder_rows=len(holder_rows), mixed_rows=len(mixed_rows),
               barrier_rows=len(barrier_rows), subunit_rows=len(subunit_rows))
(ROOT/'data'/'check_summary.json').write_text(json.dumps(summary, indent=2)+'\n')
print(json.dumps(summary, indent=2))
print('All deterministic checks passed.')
