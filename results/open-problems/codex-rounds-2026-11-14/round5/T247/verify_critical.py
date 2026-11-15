"""Independent scalar, stopping, quadrature and actual-network checks."""
import os
THREADS = ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
           'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS')
for key in THREADS:
    os.environ[key] = '1'
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time
from decimal import Decimal as D, localcontext
from fractions import Fraction as R
signal.alarm(180)
START = time.monotonic()
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
import numpy as np
np.seterr(all='raise')


def matmul(a, b):
    return np.einsum('...ij,...jk->...ik', a, b, optimize=False)


def average(w, v):
    return math.fsum(float(x)*float(y) for x, y in zip(w, v))


def rising(x, k):
    return math.prod(x+j for j in range(k))


def exact_moments():
    records = []
    for n in (1, 2, 3, 4, 8, 64, 128, 10000):
        # Dirichlet(1/2,...,1/2), using rising factorials rather than
        # the double-factorial expression in the proof.
        alpha = R(1, 2)
        m4 = n*n*rising(alpha, 2)/rising(n*alpha, 2)
        m6 = n**3*rising(alpha, 3)/rising(n*alpha, 3)
        m44 = n*n*(n*rising(alpha, 4)
                    + n*(n-1)*rising(alpha, 2)**2)/rising(n*alpha, 4)
        assert m4 == R(3*n, n+2)
        assert m6 == R(15*n*n, (n+2)*(n+4))
        assert m44 == R(n*n*(9*n+96), (n+2)*(n+4)*(n+6))
        assert m6 <= 15 and m44 <= 9
        records.append({'n': n, 'E_M4': str(m4), 'E_M6': str(m6), 'E_M4_squared': str(m44)})
    assert R(17, 45)*15+2*9 == R(71, 3) < 24
    assert 15+24*4 == 111
    assert 36*4 == 144 and 2*111 == 222 and 222+16 == 238
    assert 15+24 == 39 and 4*39 == 156
    assert 2*1344+144//2 == 2760
    assert 2*1344+3*144//2 == 2904
    assert 4*2760 == 11040 and 4*2904 == 11616
    assert 8/64+238/4096+1/4 < math.log(2)
    return records


def decimal_scalar_checks():
    with localcontext() as ctx:
        ctx.prec = 110
        xs = ['0', '1e-12', '1e-8', '.0001', '.1', '.5', '1', '2', '10', '100']
        for value in xs:
            x = D(value)
            t = ((2*x).exp()-1)/((2*x).exp()+1)
            tol = D('1e-95')
            assert x/(1+x*x)-tol <= t <= x+tol
            rem = t*t-x*x+D(2)/3*x**4
            assert -tol <= rem <= D(17)/45*x**6+tol
            b = (1-t*t)**2
            rem_b = b-1+2*x*x
            assert -tol <= rem_b <= D(7)/3*x**4+tol
        # Rational unit vectors include a spike and the non-axis O(3) test.
        for unit in ([D(1), D(0), D(0)], [D(2)/3, D(1)/3, D(2)/3], [D('.5')]*4):
            n = len(unit)
            m4 = n*sum(x**4 for x in unit)
            m6 = n*n*sum(x**6 for x in unit)
            for val in ('1e-12', '.0002', '.01', '.25', '10'):
                q = D(val)
                f = D(0)
                for v in unit:
                    z = (n*q).sqrt()*v
                    t = ((2*z).exp()-1)/((2*z).exp()+1)
                    f += t*t/(n*q)
                log_f = f.ln()
                tol = D('1e-90')
                assert -log_f <= 2*q*m4+tol
                rem = abs(log_f+D(2)/3*q*m4)
                assert rem <= q*q*(D(17)/45*m6+2*m4*m4)+tol
    return {'precision_digits': 110, 'scalar_points': len(xs), 'forward_cases': 15}


def spherical_rule(n, nodes):
    lam = (n-2)/2
    k = np.arange(1, nodes, dtype=float)
    off = np.sqrt(k*(k+2*lam-1)/(4*(k+lam)*(k+lam-1)))
    jac = np.diag(off, 1)+np.diag(off, -1)
    t, vec = np.linalg.eigh(jac)
    w = vec[0]**2
    assert abs(average(w, t*t)-1/n) < 2e-14
    assert abs(average(w, t**4)-3/(n*(n+2))) < 2e-14
    return t, w


def gaussian_mu(q, nodes=96):
    t, w = np.polynomial.hermite.hermgauss(nodes)
    return average(w/math.sqrt(math.pi), np.cosh(np.sqrt(2*q)*t)**-4)


def spherical_mu(q, n, t, w):
    # q may be a batch vector; reduction has no BLAS call.
    q = np.asarray(q)
    return (np.cosh(np.sqrt(n*q[..., None])*t)**-4*w).sum(axis=-1)


def sphere3_integrals(qs, nt, nphi):
    t, wt = np.polynomial.legendre.leggauss(nt)
    z = np.repeat(t, nphi)
    phi = np.tile(2*np.pi*np.arange(nphi)/nphi, nt)
    weights = np.repeat(wt/(2*nphi), nphi)
    u = np.column_stack((np.sqrt(1-z*z)*np.cos(phi), np.sqrt(1-z*z)*np.sin(phi), z))
    results = []
    for q in qs:
        f = (np.tanh(np.sqrt(3*q)*u)**2).sum(1)/(3*q)
        m = average(weights, np.log(f))
        mu = average(weights, np.cosh(np.sqrt(3*q)*z)**-4)
        d = math.log(mu)-m
        assert abs(m+6*q/5) <= 24*q*q+2e-14
        assert abs(d) <= 4*q/5+39*q*q+2e-14
        var = average(weights, (np.log(f)-m)**2)
        assert var <= 36*q*q
        results.append({'q': q, 'E_log_F': m, 'log_mu_minus_E_log_F': d, 'variance_log_F': var})
    return results


def scalar_quadrature():
    qs = [1e-5, 2e-5, .001, .01, .25]
    low = sphere3_integrals(qs, 32, 64)
    high = sphere3_integrals(qs, 64, 128)
    diff = max(abs(x['E_log_F']-y['E_log_F']) for x, y in zip(low, high))
    assert diff < 1e-12
    der = (4*high[0]['log_mu_minus_E_log_F']-high[1]['log_mu_minus_E_log_F'])/(2*qs[0])
    assert abs(der+4/5) < 2e-7
    forward_der = (4*high[0]['E_log_F']-high[1]['E_log_F'])/(2*qs[0])
    assert abs(forward_der+6/5) < 2e-7
    gains = []
    for a in (1e-6, 1/4096, .01, .25):
        m96, m128 = gaussian_mu(a), gaussian_mu(a, 128)
        assert abs(m96-m128) < 2e-13
        for name, mu in [('gaussian', m128)]:
            assert abs(-math.log(mu)-2*a) <= 15*a*a+2e-15
            gains.append({'a': a, 'type': name, 'mu': mu})
        for n in (3, 64, 256):
            t, w = spherical_rule(n, 32)
            mu = float(spherical_mu(a, n, t, w))
            assert abs(-math.log(mu)-2*a) <= 15*a*a+2e-15
            gains.append({'a': a, 'type': f'spherical_n{n}', 'mu': mu})
    return {'sphere3': high, 'quadrature_difference': diff,
            'd_derivative_at_zero': der, 'predicted_derivative': -4/5,
            'forward_derivative_at_zero': forward_der, 'predicted_forward_derivative': -6/5,
            'gains': gains}


def crossing_check():
    rng = np.random.default_rng(2474001)
    r, step_bound = .1, .03
    for unused in range(1000):
        x = 0.
        m = 0.
        max_m = 0.
        for k in range(100):
            b = rng.uniform(-step_bound, step_bound)
            if x > r:
                b = -abs(b)
            if x < -r:
                b = abs(b)
            noise = rng.normal(scale=.04)
            m += noise
            max_m = max(max_m, abs(m))
            x += b+noise
            assert abs(x) <= r+step_bound+2*max_m+1e-13
    return {'paths': 1000, 'steps': 100, 'checks': 100000}


def radial_simulation():
    rng = np.random.default_rng(2474002)
    results = []
    samples = 48
    for n, depth, a in ((64, 10000, .0002), (256, 2000, .0002)):
        t, w = spherical_rule(n, 20)
        tr, wr = spherical_rule(n, 40)
        assert abs(float(spherical_mu(a, n, t, w))-float(spherical_mu(a, n, tr, wr))) < 1e-13
        gain2 = 1/gaussian_mu(a)
        q = np.full(samples, a)
        log_s = np.zeros(samples)
        x = np.zeros(samples)
        max_x = np.zeros(samples)
        proxy = np.zeros(samples)
        max_proxy = np.zeros(samples)
        sum_q2 = np.zeros(samples)
        for layer in range(depth):
            u = rng.normal(size=(samples, n))
            u /= np.sqrt((u*u).sum(1))[:, None]
            z = np.sqrt(n*q[:, None])*u
            f = (np.tanh(z)**2).sum(1)/(n*q)
            log_f = np.log(f)
            log_s += math.log(gain2)+np.log(spherical_mu(q, n, t, w))
            proxy += log_f+2*n/(n+2)*q
            max_proxy = np.maximum(max_proxy, np.abs(proxy))
            sum_q2 += q*q
            x += math.log(gain2)+log_f
            q *= gain2*f
            max_x = np.maximum(max_x, np.abs(x))
            assert np.all((q >= a/2) & (q <= 2*a))
        assert np.max(np.abs(x-np.log(q/a))) < 1e-12
        delta_path = max_proxy+24*sum_q2
        radius_bound = 8/n+238*a+2*delta_path
        scalar_bound = 8/n+238*a+8*depth*a/(n+2)+156*depth*a*a+3*delta_path
        assert np.all(max_x <= radius_bound+1e-12)
        assert np.all(np.abs(log_s) <= scalar_bound+1e-12)
        results.append({'n': n, 'L': depth, 'a': a, 'samples': samples,
                        'L_a': depth*a, 'gain_squared': gain2,
                        'max_abs_log_radius_ratio': float(max_x.max()),
                        'mean_final_radius_ratio': float((q/a).mean()),
                        'mean_S': float(np.exp(log_s).mean()),
                        'max_abs_log_S': float(np.abs(log_s).max()),
                        'max_pathwise_martingale_upper_bound': float(delta_path.max()),
                        'min_scalar_bound_margin': float((scalar_bound-np.abs(log_s)).min())})
        print(f'Radius n={n}, L={depth}, La={depth*a:g}: max |log(q/a)|={max_x.max():.6g}, mean S={np.exp(log_s).mean():.6g}')
    return results


def actual_network():
    rng = np.random.default_rng(2474003)
    n, depth, samples, a = 64, 120, 24, .0002
    gain2 = 1/gaussian_mu(a)
    t, w = spherical_rule(n, 20)
    h = np.zeros((samples, n))
    h[:, 0] = math.sqrt(n*a/gain2)
    j = np.broadcast_to(np.eye(n), (samples, n, n)).copy()
    log_s = np.zeros(samples)
    max_ratio = 1.
    min_ratio = 1.
    for layer in range(depth):
        q = gain2*(h*h).sum(1)/n
        max_ratio = max(max_ratio, float((q/a).max()))
        min_ratio = min(min_ratio, float((q/a).min()))
        o, tri = np.linalg.qr(rng.normal(size=(samples, n, n)))
        signs = np.where(np.diagonal(tri, axis1=1, axis2=2) >= 0, 1., -1.)
        o *= signs[:, None, :]
        z = math.sqrt(gain2)*np.einsum('bij,bj->bi', o, h, optimize=False)
        j = math.sqrt(gain2)*np.cosh(z)[:, :, None]**-2*matmul(o, j)
        h = np.tanh(z)
        log_s += math.log(gain2)+np.log(spherical_mu(q, n, t, w))
    assert min_ratio >= .5 and max_ratio <= 2
    s = np.exp(log_s)
    gram = matmul(j, j.transpose(0, 2, 1))
    identity = np.eye(n)
    z_orig = ((gram-identity)**2).sum((1, 2))/n
    z_norm = ((gram/s[:, None, None]-identity)**2).sum((1, 2))/n
    A = 24*depth*a/(n+2)+11040*depth*a*a
    B = 12*depth*a/(n+2)+11616*depth*a*a
    bound = B*math.exp(A)
    assert z_norm.mean()+6*z_norm.std(ddof=1)/math.sqrt(samples) < bound
    assert np.all(np.sqrt(z_orig) <= s*np.sqrt(z_norm)+abs(s-1)+1e-13)
    print(f'Actual critical tanh n={n}, L={depth}: mean Z={z_orig.mean():.6g}, mean normalized Z={z_norm.mean():.6g}, bound={bound:.6g}')
    return {'n': n, 'L': depth, 'samples': samples, 'a': a, 'gain_squared': gain2,
            'mean_original_distortion': float(z_orig.mean()),
            'mean_normalized_distortion': float(z_norm.mean()),
            'normalized_distortion_bound': bound, 'mean_S': float(s.mean()),
            'radius_ratio_min': min_ratio, 'radius_ratio_max': max_ratio}


def main():
    moments = exact_moments()
    scalar = decimal_scalar_checks()
    quad = scalar_quadrature()
    crossing = crossing_check()
    print(f'Exact spherical moment cases: {len(moments)}; all constant checks passed')
    print(f'110-digit global scalar inequalities: {scalar["scalar_points"]} points; forward log inequalities: {scalar["forward_cases"]} cases')
    print(f'Sphere O(3) scalar quadrature difference: {quad["quadrature_difference"]:.3g}')
    print(f'Normalizer/radius linear coefficient: {quad["d_derivative_at_zero"]:.10g}, predicted -0.8')
    print(f'Forward log-radius linear coefficient: {quad["forward_derivative_at_zero"]:.10g}, predicted -1.2')
    print(f'Discrete last-crossing inequalities: {crossing["checks"]} passed')
    radial = radial_simulation()
    network = actual_network()
    examples = []
    for n in (100, 1000, 10000, 1000000):
        a = n**-2
        depth = math.isqrt(n**5)
        examples.append({'n': n, 'L': depth, 'a': a, 'La': depth*a,
                         'La_squared': depth*a*a, 'La_over_n': depth*a/n})
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        peak *= 1024
    assert peak < 10**9
    result = {'exact_spherical_moments': moments, 'scalar_inequalities': scalar,
              'quadrature': quad, 'last_crossing': crossing, 'radial_simulation': radial,
              'actual_network': network, 'diverging_La_examples': examples,
              'runtime_seconds': time.monotonic()-START, 'peak_rss_bytes': peak,
              'niceness': os.getpriority(os.PRIO_PROCESS, 0), 'numpy_version': np.__version__,
              'thread_environment': {key: os.environ[key] for key in THREADS}}
    Path('earlier_critical_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(f'Niceness {result["niceness"]}; peak RSS {peak/1024**2:.1f} MiB; runtime {result["runtime_seconds"]:.2f} s')
    print('All critical-gain verification checks passed')


if __name__ == '__main__':
    main()
