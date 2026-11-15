"""Small deterministic independent checks using the actual infinite lattice Green kernel.

For SRW, Poissonizing gives G(0,x)=d integral_0^inf product_i ive(|x_i|,u) du.
We integrate using u=(z/(1-z))^2, z in (0,1). Hyperoctahedral symmetry
reduces a ball to sorted nonnegative coordinate tuples with exact multiplicities.
No code or data from claim_files/code or claim_files/data is used.
"""
import os
for name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
import csv
import json
import math
import resource
import time
from collections import Counter
from pathlib import Path
import numpy as np
from scipy.special import ive, roots_legendre
from scipy.optimize import minimize

ROOT = Path(__file__).resolve().parents[1]


def orbits(d, radius):
    def visit(prefix, left, bound, square_budget):
        if left == 0:
            yield prefix
            return
        for x in range(min(bound, math.isqrt(square_budget)) + 1):
            yield from visit(prefix + (x,), left - 1, x, square_budget - x*x)
    return list(visit((), d, radius, radius*radius))


def multiplicity(x):
    value = math.factorial(len(x)) * 2**sum(v != 0 for v in x)
    for count in Counter(x).values():
        value //= math.factorial(count)
    return value


def green(points, nodes):
    z, weight = roots_legendre(nodes)
    z = (z + 1)/2
    weight = weight/2
    u = (z/(1-z))**2
    jac = 2*z/(1-z)**3
    # AMOS (used by scipy.ive) returns NaN at very large arguments on this
    # platform. Above 1e6 use the elementary four-term large-u expansion.
    table = np.empty((int(points.max()) + 2, nodes))
    large = u > 1e6
    for j in range(len(table)):
        table[j, ~large] = ive(j, u[~large])
        v = u[large]
        series = np.ones_like(v)
        term = np.ones_like(v)
        for k in range(1, 5):
            term *= -(4*j*j-(2*k-1)**2)/(k*8*v)
            series += term
        table[j, large] = series/np.sqrt(2*math.pi*v)
    assert np.all(np.isfinite(table))
    d = points.shape[1]
    answer = np.empty(len(points))
    # Bound working memory by batches of at most 256 symmetry classes.
    for start in range(0, len(points), 256):
        x = points[start:start+256]
        integrand = np.ones((len(x), nodes))
        for i in range(d):
            integrand *= table[x[:,i]]
        answer[start:start+len(x)] = d*np.sum(integrand*(weight*jac), axis=1)
    return answer


def main():
    started = time.monotonic()
    summary = {'nice': os.getpriority(os.PRIO_PROCESS, 0), 'threads_requested': 1,
               'kernel': 'infinite-lattice SRW, Bessel product quadrature', 'checks': []}
    assert summary['nice'] >= 10
    rows = []
    optrows = []
    profilerows = []
    for d in (5, 6):
        points = np.array(orbits(d, 16), dtype=int)
        mult = np.array([multiplicity(x) for x in points], dtype=float)
        radii2 = (points*points).sum(axis=1)
        g = green(points, 256)
        fine = green(points, 512)
        rel = float(np.max(np.abs(g-fine)/fine))
        assert rel < 2e-7, rel
        q = d/(d-2)
        p = d/2
        # Harmonicity checks at small representatives, computed with fresh kernels.
        testpoints = points[radii2 <= 9]
        nbs = []
        for x in testpoints:
            for j in range(d):
                for direction in (-1,1):
                    y = x.copy()
                    y[j] += direction
                    nbs.append(np.abs(y))
        neighbor_g = green(np.array(nbs), 512).reshape(len(testpoints), 2*d).mean(axis=1)
        residual = fine[radii2 <= 9]-neighbor_g-(radii2[radii2 <= 9] == 0)
        assert np.max(np.abs(residual)) < 1e-9
        sums = {}
        # The actual admissible hole event charges one unit per constrained site.
        for a in (4.,16.,64.,256.):
            radius = math.ceil(math.sqrt(a))
            mask = radii2 < radius**2
            depths = 2*a/(1+radii2[mask])
            deficit = float(np.sum(mult[mask]*fine[mask]*depths))
            event_cost = float(np.sum(mult[mask]*(1+depths**p)))
            profilerows.append(dict(d=d,a=a,radius=radius,deficit=deficit,
                deficit_over_a_log=deficit/(a*math.log(a)),
                event_cost=event_cost,cost_over_a_power_log=event_cost/(a**p*math.log(a)),
                min_depth=float(depths.min())))
        # Discrete supersolution checked on all symmetry classes in the test ball.
        f = np.log1p(radii2)
        Pf = np.zeros(len(points))
        for j in range(d):
            Pf += np.log1p(radii2+1+2*points[:,j])/(2*d)
            Pf += np.log1p(radii2+1-2*points[:,j])/(2*d)
        assert np.max(Pf-f-1/(1+radii2)) <= 1e-12
        for radius in (1, 2, 4, 8, 16):
            mask = radii2 <= radius**2
            S = float(np.sum(mult[mask]*fine[mask]**q))
            sums[radius] = S
            rows.append(dict(d=d, radius=radius, orbits=int(mask.sum()),
                             sites=int(mult[mask].sum()), S=S,
                             S_over_log=S/math.log(2+radius),
                             doubling_increment=S-sums.get(radius//2, 0) if radius > 1 else '',
                             quadrature_max_relative_error=rel))
            # Check exact Holder optimizer directly for several levels.
            for m in (3., 30., 300.):
                a = (m/S)*fine[mask]**(1/(p-1))
                deficit = float(np.sum(mult[mask]*fine[mask]*a))
                cost = float(np.sum(mult[mask]*a**p))
                predicted = m**p/S**(p-1)
                assert abs(deficit/m-1) < 1e-12
                assert abs(cost/predicted-1) < 1e-12
                optrows.append(dict(d=d,radius=radius,m=m,deficit=deficit,cost=cost,
                                    predicted=predicted,min_depth=float(a.min()),max_depth=float(a.max())))
        # A generic constrained numerical optimizer, independent of the Holder formula.
        mask = radii2 <= 2**2
        weights, counts = fine[mask], mult[mask]
        m = 10.
        result = minimize(lambda a: np.sum(counts*a**p),
                          np.full(len(weights), m/np.sum(counts*weights)),
                          jac=lambda a: p*counts*a**(p-1),
                          bounds=[(0,None)]*len(weights),
                          constraints=[{'type':'eq','fun': lambda a: np.dot(counts*weights,a)-m,
                                        'jac': lambda a: counts*weights}],
                          method='SLSQP', options={'ftol':1e-10,'maxiter':300})
        target = m**p/(np.sum(counts*weights**q)**(p-1))
        assert result.success, result.message
        assert abs(result.fun/target-1) < 1e-7
        area = 2*math.pi**(d/2)/math.gamma(d/2)
        asymptotic_G = 2*d/((d-2)*area)
        expected_slope = area*asymptotic_G**q
        summary['checks'].append(dict(d=d,classes=len(points),G00=float(fine[radii2==0][0]),
            quadrature_relative_error=rel,harmonicity_error=float(np.max(np.abs(residual))),
            optimizer_relative_error=float(abs(result.fun/target-1)),
            annular_slope_8_16=(sums[16]-sums[8])/math.log(2),
            continuum_predicted_slope=expected_slope))
    for name, output in (('green_sums.csv', rows), ('finite_variational.csv', optrows),
                         ('hole_profile.csv', profilerows)):
        with (ROOT/'data'/name).open('w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=list(output[0]))
            writer.writeheader()
            writer.writerows(output)
    summary['elapsed_seconds'] = time.monotonic()-started
    summary['peak_rss_bytes'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert summary['peak_rss_bytes'] < 4_000_000_000
    (ROOT/'data'/'referee_checks.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__ == '__main__':
    main()
