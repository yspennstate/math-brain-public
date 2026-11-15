"""Independent checks of the log-volume law; writes only beside this script."""
import os
THREADS = ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
           'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS')
for key in THREADS:
    os.environ[key] = '1'
import json
import math
from fractions import Fraction as F
from pathlib import Path
import resource
import signal
import sys
import time
signal.alarm(180)
START = time.monotonic()
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
import mpmath as mp
import numpy as np
np.seterr(all='raise')
# Local copy of the previous verification, imported without running its main.
import recheck_bias as prior
signal.alarm(180)


def scalar_checks():
    mp.mp.dps = 75
    points = ['0', '1e-20', '1e-12', '.0001', '.1', '1', '2', '10', '100', '-2']
    for value in points:
        x = mp.mpf(value)
        rem = x*x/2-mp.log(mp.cosh(x))
        assert -mp.mpf('1e-70') <= rem <= x**4/12+mp.mpf('1e-70')
    count = 0
    for n in (3, 4, 16, 64, 256, 10000):
        # Dirichlet moment computation, independent of double factorials.
        rising = lambda x, k: math.prod(x+j for j in range(k))
        fourth = n*n*rising(F(1, 2), 2)/rising(F(n, 2), 2)
        assert fourth == F(3*n, n+2)
        cn = F(2, 3)*fourth
        for k in (F(1, 2), F(1), F(2)):
            assert (2-2*k)-(2-cn*k) == -F(4, n+2)*k
            count += 1
        equilibrium = F(2)/cn
        assert 2-2*equilibrium == -F(4, n)
    assert 4*2*14+2*14**2*F(1, 16384)**2 < 113
    assert 2*math.sqrt(113/64)+16*9 < 150
    assert 2*614 == 1228 and 2*8 == 16
    assert 300+152 == 452 and 48000+12000 == 60000
    return {'log_cosh_points': len(points), 'rational_coefficients': count,
            'precision_digits': mp.mp.dps}


def high_precision_sphere():
    mp.mp.dps = 65
    records = []
    for n in (3, 64, 256):
        # Marginal density of y=sqrt(n)u_1, rather than the full sphere grid.
        norm = mp.gamma(mp.mpf(n)/2)/(mp.sqrt(mp.pi*n)*mp.gamma(mp.mpf(n-1)/2))
        top = mp.sqrt(n)
        breaks = [mp.mpf(0), min(mp.mpf(1), top), min(mp.mpf(3), top), top]
        breaks = sorted(set(breaks))
        def integrate(f):
            return 2*norm*mp.quad(lambda y: f(y)*(1-y*y/n)**(mp.mpf(n-3)/2), breaks)
        assert abs(integrate(lambda y: y*y)-1) < mp.mpf('1e-55')
        for ratio in (mp.mpf('.5'), mp.mpf(1), mp.mpf(2)):
            vals = []
            for a in (mp.mpf('1e-8'), mp.mpf('2e-8')):
                q = ratio*a
                gain2 = mp.exp(2*a)
                mean_activation = integrate(lambda y: mp.tanh(mp.sqrt(q)*y)**2)
                mu = integrate(lambda y: mp.sech(mp.sqrt(q)*y)**4)
                mean_log_gate = integrate(lambda y: -4*mp.log(mp.cosh(mp.sqrt(q)*y)))
                drift = gain2*mean_activation/q-1
                s = 2*a+mp.log(mu)
                h = 2*a+mean_log_gate
                vals.append(((s-drift)/a, (h-drift)/a))
            extrapolated = [2*vals[0][j]-vals[1][j] for j in range(2)]
            predicted = -4*ratio/(n+2)
            error = max(abs(x-predicted) for x in extrapolated)
            assert error < mp.mpf('2e-12'), (n, ratio, error)
            records.append({'n': n, 'q_over_a': str(ratio), 'predicted': str(predicted),
                            'scalar_extrapolation': str(extrapolated[0]),
                            'volume_extrapolation': str(extrapolated[1]), 'error': str(error)})
    return records


def critical(a):
    mp.mp.dps = 65
    a = mp.mpf(str(a))
    density = lambda x: mp.exp(-x*x/2)/mp.sqrt(2*mp.pi)
    mu = 2*mp.quad(lambda x: mp.sech(mp.sqrt(a)*x)**4*density(x), [0, 1, 4, mp.inf])
    ag = 2*mp.quad(lambda x: mp.tanh(mp.sqrt(a)*x)**2*density(x), [0, 1, 4, mp.inf])
    return float(-mp.log(mu)), float(a-ag/mu), float(ag)


def one_layer_bias():
    rng = np.random.default_rng(2476001)
    records = []
    samples = 4096
    for n in (64, 128):
        sphere = prior.sphere_rule(n, 36)
        gauss = prior.gaussian_rule(40)
        for a in (1/16384, 1e-6):
            for ratio in (.5, 1., 2.):
                q = a*ratio
                for b in (0., 14*a**3):
                    r = q+b
                    u = rng.normal(size=(samples, n))
                    u /= np.sqrt((u*u).sum(1))[:, None]
                    z = math.sqrt(n*q)*u+math.sqrt(b)*rng.normal(size=(samples, n))
                    h2 = np.tanh(z)**2
                    mean_log_gate = (2*np.log1p(-h2)).mean(1)
                    mu = float(prior.mu_sphere(q, b, n, sphere, gauss))
                    R = mean_log_gate-math.log(mu)
                    v = (z*z).mean(1)
                    assert np.all(abs(R) <= 2*abs(v-r)+(z**4).mean(1)/3+15*r*r+3e-14)
                    analytical_bound = 2*math.sqrt((4*q*b+2*b*b)/n)+16*r*r
                    assert analytical_bound <= 150*a*a
                    assert abs(R).mean() <= analytical_bound+5e-13
                    # This variance uses the whole sphere vector: it is not n
                    # independent Gaussian signal coordinates.
                    variance = (4*q*b+2*b*b)/n
                    if variance:
                        measured = ((v-r)**2).mean()
                        assert abs(measured/variance-1) < .12
                    else:
                        assert np.max(abs(v-r)) < 1e-17
                    records.append({'n': n, 'a': a, 'q_over_a': ratio, 'b': b,
                                    'mean_absolute_R': float(abs(R).mean()),
                                    'analytical_bound': analytical_bound,
                                    'bound_150_a_squared': 150*a*a})
    return records


def full_products():
    rng = np.random.default_rng(2476002)
    records = []
    for n, depth, a in ((8, 1000, .001), (16, 800, .001), (32, 240, 1/16384)):
        lam, b, ag = critical(a)
        gain2 = math.exp(lam)
        samples = 8
        sphere, gaussian = prior.sphere_rule(n, 32), prior.gaussian_rule(32)
        h = np.zeros((samples, n))
        h[:, 0] = math.sqrt(n*ag)
        J = np.broadcast_to(np.eye(n), (samples, n, n)).copy()
        H = np.zeros(samples)
        logS = np.zeros(samples)
        comparison_bound = np.zeros(samples)
        qsum = np.zeros(samples)
        maxradius = np.zeros(samples)
        qinitial = gain2*ag
        for _ in range(depth):
            q = gain2*(h*h).sum(1)/n
            qsum += q
            maxradius = np.maximum(maxradius, abs(q/a-1))
            O, tri = np.linalg.qr(rng.normal(size=(samples, n, n)))
            O *= np.where(np.diagonal(tri, axis1=1, axis2=2) >= 0, 1., -1.)[:, None, :]
            z = math.sqrt(gain2)*np.einsum('bij,bj->bi', O, h, optimize=False)
            z += math.sqrt(b)*rng.normal(size=(samples, n))
            h = np.tanh(z)
            J = math.sqrt(gain2)*(1-h*h)[:, :, None]*prior.mm(O, J)
            H += lam+(2*np.log1p(-h*h)).mean(1)
            mu = prior.mu_sphere(q, b, n, sphere, gaussian)
            logS += lam+np.log(mu)
            r = q+b
            comparison_bound += 2*abs((z*z).mean(1)-r)+(z**4).mean(1)/3+15*r*r
        # Independent scalar partial-pivot elimination. The platform's NumPy
        # slogdet raised a floating-point exception on the first run; retain
        # exception checks and avoid that backend rather than masking errors.
        def logabsdet(matrix):
            rows = matrix.tolist()
            ans = 0.
            for i in range(n):
                pivot = max(range(i, n), key=lambda k: abs(rows[k][i]))
                rows[i], rows[pivot] = rows[pivot], rows[i]
                diag = rows[i][i]
                assert math.isfinite(diag) and abs(diag) > 1e-12
                ans += math.log(abs(diag))
                for k in range(i+1, n):
                    factor = rows[k][i]/diag
                    for j in range(i+1, n):
                        rows[k][j] -= factor*rows[i][j]
            return ans
        H_direct = 2*np.array([logabsdet(x) for x in J])/n
        error = float(np.max(abs(H-H_direct)))
        assert error < 1e-9, error
        assert np.all(abs(H-logS) <= comparison_bound+1e-11)
        qfinal = gain2*(h*h).sum(1)/n
        compensated = H-np.log(qfinal/qinitial)+4*qsum/(n+2)
        gram = prior.mm(J, J.transpose(0, 2, 1))
        Z = ((gram-np.eye(n))**2).sum((1, 2))/n
        records.append({'n': n, 'L': depth, 'a': a, 'b': b, 'samples': samples,
                        'La_squared': depth*a*a, 'La_over_n': depth*a/n,
                        'mean_H': float(H.mean()), 'mean_log_S': float(logS.mean()),
                        'max_direct_determinant_error': error,
                        'max_absolute_H_minus_logS': float(abs(H-logS).max()),
                        'min_determinant_comparison_margin': float((comparison_bound-abs(H-logS)).min()),
                        'mean_compensated_H': float(compensated.mean()),
                        'mean_distortion_Z': float(Z.mean()),
                        'max_abs_radius_error': float(maxradius.max())})
    return records


def logical_counterexample():
    out = []
    for n in (10, 100, 1000):
        t = .25
        # Work with logs so the test also covers singular values below the
        # floating point representable range.
        logmean = (-4*t*n)/n
        Z = (-math.expm1(-4*t*n))**2/n
        assert logmean == -4*t and Z <= 1/n
        out.append({'n': n, 'log_geometric_mean': logmean, 'distortion': Z})
    return out


def main():
    scalar = scalar_checks()
    print(f'75-digit log-cosh inequalities: {scalar["log_cosh_points"]}; exact signed coefficients: {scalar["rational_coefficients"]}')
    coeff = high_precision_sphere()
    err = max(mp.mpf(x['error']) for x in coeff)
    print(f'Independent 65-digit sphere quadratures: {len(coeff)}; max extrapolation error {float(err):.3g}')
    biased = one_layer_bias()
    print(f'Whole-vector biased determinant comparisons: {len(biased)} passed')
    products = full_products()
    for x in products:
        print(f'Full Jacobian n={x["n"]}, L={x["L"]}: H={x["mean_H"]:.9g}, log S={x["mean_log_S"]:.9g}, determinant error={x["max_direct_determinant_error"]:.3g}')
    logical = logical_counterexample()
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        peak *= 1024
    assert peak < 10**9
    results = {'scalar': scalar, 'coefficient_quadrature': coeff, 'biased_comparison': biased,
               'full_products': products, 'logical_counterexample': logical,
               'runtime_seconds': time.monotonic()-START, 'peak_rss_bytes': peak,
               'niceness': os.getpriority(os.PRIO_PROCESS, 0),
               'thread_environment': {k: os.environ[k] for k in THREADS}}
    Path(__file__).resolve().with_name('results.json').write_text(json.dumps(results, indent=2)+'\n')
    print(f'Niceness {results["niceness"]}; peak RSS {peak/1024**2:.1f} MiB; runtime {results["runtime_seconds"]:.2f} s')
    print('All log-volume verification checks passed')


if __name__ == '__main__':
    main()
