"""Checks for the small-Gaussian-bias theorem; writes only beside this script."""
import os
THREADS = ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
           'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS')
for name in THREADS:
    os.environ[name] = '1'
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
import numpy as np
import mpmath as mp
np.seterr(all='raise')


def mm(a, b):
    return np.einsum('...ij,...jk->...ik', a, b, optimize=False)


def weighted(w, x):
    return math.fsum(float(a)*float(b) for a, b in zip(w, x))


def multiply(a, b, order):
    c = [F(0)]*(order+1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i+j <= order:
                c[i+j] += x*y
    return c


def exact_series():
    # Solve t'=1-t^2, then integrate Gaussian powers. No numerical fitting.
    order = 14
    t = [F(0)]*(order+1)
    for k in range(order):
        square = multiply(t, t, order)
        t[k+1] = (F(k == 0)-square[k])/(k+1)
    t2 = multiply(t, t, order)
    derivative = [F(k == 0)-t2[k] for k in range(order+1)]
    sech4 = multiply(derivative, derivative, order)
    def gaussian_coeff(poly):
        return [poly[2*k]*math.prod(range(1, 2*k, 2)) for k in range(7)]
    activation = gaussian_coeff(t2)
    mu = gaussian_coeff(sech4)
    quotient = [F(0)]*7
    for k in range(7):
        quotient[k] = activation[k]-sum(mu[j]*quotient[k-j] for j in range(1, k+1))
    bias = [F(k == 1)-quotient[k] for k in range(7)]
    assert activation[:4] == [0, 1, -2, F(17, 3)]
    assert mu[:3] == [1, -2, 7]
    assert bias[:4] == [0, 0, 0, F(4, 3)]
    # Independent coefficient identity: a mu-A starts at 7-17/3=4/3.
    assert mu[2]-activation[3] == bias[3]
    return {'A_coefficients': list(map(str, activation)),
            'mu_coefficients': list(map(str, mu)),
            'bias_coefficients': list(map(str, bias))}


def high_precision_critical():
    mp.mp.dps = 70
    output = []
    density = lambda x: mp.exp(-x*x/2)/mp.sqrt(2*mp.pi)
    for val in ('0.000001', '0.00006103515625', '0.01'):
        a = mp.mpf(val)
        mu = 2*mp.quad(lambda x: mp.sech(mp.sqrt(a)*x)**4*density(x), [0, 1, 4, mp.inf])
        activation = 2*mp.quad(lambda x: mp.tanh(mp.sqrt(a)*x)**2*density(x), [0, 1, 4, mp.inf])
        bias = a-activation/mu
        assert 0 < bias <= 14*a**3
        assert abs(-mp.log(mu)-2*a) <= 15*a*a
        assert abs((activation/mu+bias)-a) < mp.mpf('1e-65')
        if a < mp.mpf('0.00001'):
            assert abs(bias/a**3-mp.mpf(4)/3) < mp.mpf('0.00001')
        output.append({'a': val, 'mu': str(mu), 'A': str(activation),
                       'b': str(bias), 'b_over_a_cubed': str(bias/a**3)})
    return output


def sphere_rule(n, order):
    if n == 3:
        t, w = np.polynomial.legendre.leggauss(order)
        return t, w/2
    lam = (n-2)/2
    k = np.arange(1, order, dtype=float)
    off = np.sqrt(k*(k+2*lam-1)/(4*(k+lam)*(k+lam-1)))
    vals, vectors = np.linalg.eigh(np.diag(off, 1)+np.diag(off, -1))
    w = vectors[0]**2
    assert abs(weighted(w, vals**2)-1/n) < 3e-14
    return vals, w


def gaussian_rule(order):
    x, w = np.polynomial.hermite.hermgauss(order)
    return x*math.sqrt(2), w/math.sqrt(math.pi)


def gate_averages(x, b, gaussian):
    v, w = gaussian
    z = np.asarray(x)[..., None]+math.sqrt(b)*v
    raw = np.cosh(z)**-4
    mean = (raw*w).sum(-1)
    second = (raw*raw*w).sum(-1)
    return mean, second


def mu_sphere(q, b, n, sphere, gaussian):
    t, w = sphere
    m, unused = gate_averages(np.sqrt(n*np.asarray(q)[..., None])*t, b, gaussian)
    return (m*w).sum(-1)


def bias_gate_bounds():
    gaussian = gaussian_rule(80)
    sphere = sphere_rule(3, 64)
    sphere2 = sphere_rule(3, 96)
    output = []
    for q, b in ((0., 0.), (0., .1), (.1, 0.), (.05, .15),
                 (.001, .002), (1e-6, 14e-18), (.2, .05)):
        r = q+b
        mu = float(mu_sphere(q, b, 3, sphere, gaussian))
        mu2 = float(mu_sphere(q, b, 3, sphere2, gaussian_rule(100)))
        assert abs(mu-mu2) < 2e-11
        max_ratio_r = 0.
        max_ratio_d = 0.
        for y in (0., .25, 1., 3., 100., 10000.):
            # These bounds are global in y, even beyond a sphere coordinate.
            x = math.sqrt(q*y)
            v, w = gaussian
            raw = np.cosh(x+math.sqrt(b)*v)**-4
            delta = raw/mu-1
            residual = weighted(w, delta)-2*q*(1-y)
            square = weighted(w, delta*delta)
            limit_r = 40*r*r*(1+y*y)
            limit_d = 128*r*r*(1+y*y)
            assert abs(residual) <= limit_r+3e-13, (q, b, y, residual, limit_r)
            assert square <= limit_d+3e-13
            if r:
                max_ratio_r = max(max_ratio_r, abs(residual)/limit_r)
                max_ratio_d = max(max_ratio_d, square/limit_d)
        output.append({'q': q, 'b': b, 'mu': mu,
                       'quadrature_difference': abs(mu-mu2),
                       'max_residual_over_bound': max_ratio_r,
                       'max_square_over_bound': max_ratio_d})
    return output


def haar3(q, b, X, nt, nphi, npsi=8):
    # Direct Euler integration of Haar O(3), independent Gaussian bias moments.
    z, wt = np.polynomial.legendre.leggauss(nt)
    phi = 2*np.pi*np.arange(nphi)/nphi
    z = np.repeat(z, nphi)
    phi = np.tile(phi, nt)
    weights = np.repeat(wt/(2*nphi), nphi)
    st = np.sqrt(1-z*z)
    cp, sp = np.cos(phi), np.sin(phi)
    u = np.column_stack((st*cp, st*sp, z))
    base = np.zeros((len(z), 3, 3))
    base[:, 0, 0] = cp*z
    base[:, 0, 1] = -sp
    base[:, 0, 2] = cp*st
    base[:, 1, 0] = sp*z
    base[:, 1, 1] = cp
    base[:, 1, 2] = sp*st
    base[:, 2, 0] = -st
    base[:, 2, 2] = z
    m, s = gate_averages(math.sqrt(3*q)*u, b, gaussian_rule(48))
    mu = weighted(weights, m[:, 2])
    m /= mu
    s /= mu*mu
    total = np.zeros(2)
    for psi in 2*np.pi*np.arange(npsi)/npsi:
        c, sn = math.cos(psi), math.sin(psi)
        rot = np.array([[c, -sn, 0], [sn, c, 0], [0, 0, 1.]])
        for sign in (-1, 1):
            o = mm(base, rot)
            o[:, :, 0] *= sign
            B = mm(mm(o, X), o.transpose(0, 2, 1))
            diag = np.diagonal(B, axis1=1, axis2=2)
            t = (m*diag).sum(1)
            second = (m[:, :, None]*m[:, None, :]*B*B).sum((1, 2))
            second += ((s-m*m)*diag*diag).sum(1)
            total += np.array([weighted(weights, t), weighted(weights, second)])/(2*npsi)
    return total, mu


def haar_checks():
    M = np.array([[1., 1/3, -.25], [0, 1.5, .2], [.5, 0, 4/3]])
    matrices = [('generic', mm(M, M.T)), ('identity', np.eye(3)),
                ('aligned_rank_one', np.diag([0., 0., 1.])),
                ('transverse_rank_one', np.diag([1., 0., 0.])),
                ('zero', np.zeros((3, 3)))]
    out = []
    pairs = [(0., .1), (.1, 0.), (.05, .1), (.2, .05), (.001, .002)]
    for name, X in matrices:
        T = np.trace(X)
        Q = np.sum(X*X)
        alpha = X[2, 2]
        gamma = np.sum(X[:, 2]**2)
        lin = np.array([-4*(3*alpha-T)/5, -8*(3*gamma-Q)/5])
        for q, b in pairs:
            values, mu = haar3(q, b, X, 20, 40)
            refined, unused = haar3(q, b, X, 32, 64)
            difference = float(np.max(np.abs(values-refined)))
            assert difference < 2e-8, (name, q, b, difference)
            remainder = np.abs(refined-np.array([T, Q])-q*lin)
            bounds = (q+b)**2*np.array([640*T, 3328*Q])
            assert np.all(remainder <= bounds+3e-11)
            if q == 0:
                assert abs(refined[0]-T) < 2e-12
                v, w = gaussian_rule(80)
                raw = np.cosh(math.sqrt(b)*v)**-4/mu
                variance = weighted(w, (raw-1)**2)
                expected_Q = Q+variance*(T*T+2*Q)/5
                assert abs(refined[1]-expected_Q) < 2e-9
            out.append({'matrix': name, 'q': q, 'b': b,
                        'moments': refined.tolist(), 'linear_coefficients': lin.tolist(),
                        'remainder': remainder.tolist(), 'bounds': bounds.tolist(),
                        'quadrature_difference': difference})
    # Extrapolation along total variance with a nonzero bias fraction.
    X = matrices[0][1]
    h = 1e-5
    v1, unused = haar3(.4*h, .6*h, X, 24, 48)
    v2, unused = haar3(.8*h, 1.2*h, X, 24, 48)
    base = np.array([np.trace(X), np.sum(X*X)])
    derivative = (4*v1-v2-3*base)/(2*h)
    pred = .4*np.array([-4*(3*X[2, 2]-base[0])/5,
                        -8*(3*np.sum(X[:, 2]**2)-base[1])/5])
    assert np.max(np.abs(derivative-pred)) < 3e-6
    return {'cases': out, 'derivative': derivative.tolist(), 'predicted_derivative': pred.tolist(),
            'max_derivative_error': float(np.max(np.abs(derivative-pred)))}


def sphere_y_moment(n, k, ell=0):
    numerator = n**(k+ell)*math.prod(range(1, 2*k, 2))*math.prod(range(1, 2*ell, 2))
    denominator = math.prod(n+2*j for j in range(k+ell))
    return F(numerator, denominator)


def exact_radial_bounds():
    count = 0
    max_ratio = F(0)
    for n in (64, 65, 128, 10000):
        for a in (F(1, 16384), F(1, 1000000)):
            for q in (a/2, a, 2*a):
                for b in (F(0), 14*a**3):
                    # Direct joint eighth moments, rather than Jensen's bound.
                    ez8 = sum(F(math.comb(8, 2*k))*q**k*b**(4-k)
                              *sphere_y_moment(n, k)*math.prod(range(1, 2*(4-k), 2))
                              for k in range(5))
                    cross = (q**4*sphere_y_moment(n, 2, 2)
                             +12*q**3*b*sphere_y_moment(n, 2, 1)
                             +6*q*q*b*b*sphere_y_moment(n, 2)
                             +36*q*q*b*b*sphere_y_moment(n, 1, 1)
                             +36*q*b**3+9*b**4)
                    mean_fourth_squared = ez8/n+F(n-1, n)*cross
                    exact_second_v = b*b+(4*q*b+2*b*b)/n
                    bound = 3*(16*a*a+4*(exact_second_v+F(4, 9)*mean_fourth_squared)/(q*q))
                    assert bound <= 12000*a*a
                    max_ratio = max(max_ratio, bound/(12000*a*a))
                    count += 1
    # Rebuild all accumulated constants from the one-layer coefficients.
    assert (2*40+128)*16 == 3328
    assert 40*16 == 640
    assert 2*3328+1280//2 == 7296
    assert 2*3328+3*1280//2 == 8576
    assert 9*7296 == 65664 and 9*8576 == 77184
    assert 32+16+56+1+1+153 == 259 < 300
    assert 48+1+21+11340 == 11410 < 12000
    assert 48000+12000 == 60000 and 600+14 == 614
    assert 2*614 == 1228 and 300+152 == 452
    assert F(8, 64)+F(614, 16384)+F(2, 16) < F(1, 2)
    return {'cases': count, 'max_exact_bound_over_coarse_bound': float(max_ratio)}


def radial_drift_checks():
    out = []
    for n in (64, 128):
        sphere = sphere_rule(n, 40)
        gaussian = gaussian_rule(40)
        t, wt = sphere
        v, w = gaussian
        for a in (1/16384, 1e-5):
            mu_g = weighted(w, np.cosh(math.sqrt(a)*v)**-4)
            AG = weighted(w, np.tanh(math.sqrt(a)*v)**2)
            critical_b = a-AG/mu_g
            for kind, gain2, b in [('lower_gain', math.exp(2*a-15*a*a), 0.),
                                   ('upper_gain_max_bias', math.exp(2*a+15*a*a), 14*a**3),
                                   ('critical', 1/mu_g, critical_b)]:
                assert b >= 0
                for ratio in (.5, 1., 2.):
                    q = a*ratio
                    z = math.sqrt(n*q)*t[:, None]+math.sqrt(b)*v
                    new_mean = gain2*float((np.tanh(z)**2*wt[:, None]*w).sum())
                    drift = (new_mean-q)/q
                    leading = 2*a-2*n*q/(n+2)
                    assert abs(drift-leading) <= 300*a*a+3e-14
                    mu = float(mu_sphere(q, b, n, sphere, gaussian))
                    scalar = math.log(gain2)+math.log(mu)
                    assert abs(scalar-drift) <= 8*a/(n+2)+452*a*a+3e-14
                    out.append({'n': n, 'a': a, 'q_over_a': ratio, 'parameters': kind,
                                'b': b, 'drift': drift, 'leading_drift': leading,
                                'scalar_minus_drift': scalar-drift})
    return out


def crossing_checks():
    rng = np.random.default_rng(2475002)
    checks = 0
    for unused in range(1000):
        r, step_bound = .12, .025
        x = rng.uniform(-r, r)
        M, maxM = 0., 0.
        active = True
        for k in range(100):
            if active:
                drift = rng.uniform(-step_bound, step_bound)
                if x >= r:
                    drift = -abs(drift)
                if x <= -r:
                    drift = abs(drift)
                noise = rng.normal(scale=.11)
                x += drift+noise
                M += noise
                maxM = max(maxM, abs(M))
                active = -.5 < x < 1.
            assert abs(x) <= r+step_bound+2*maxM+1e-13
            checks += 1
    return checks


def simulate():
    rng = np.random.default_rng(2475001)
    gaussian = gaussian_rule(24)
    v, w = gaussian
    n, depth, samples, a = 64, 180, 24, 1/16384
    mu_g = weighted(w, np.cosh(math.sqrt(a)*v)**-4)
    activation = weighted(w, np.tanh(math.sqrt(a)*v)**2)
    gain2 = 1/mu_g
    b = a-gain2*activation
    assert b > 0
    sphere = sphere_rule(n, 20)
    h = np.zeros((samples, n))
    h[:, 0] = math.sqrt(n*activation)
    J = np.broadcast_to(np.eye(n), (samples, n, n)).copy()
    logS = np.zeros(samples)
    sumU2 = np.zeros(samples)
    sumU = np.zeros(samples)
    M = np.zeros(samples)
    N = np.zeros(samples)
    maxM = np.zeros(samples)
    max_radius = np.zeros(samples)
    min_r, max_r = 1., 1.
    initial_ratio = gain2*activation/a
    for unused in range(depth):
        q = gain2*(h*h).sum(1)/n
        min_r = min(min_r, float((q/a).min()))
        max_r = max(max_r, float((q/a).max()))
        O, tri = np.linalg.qr(rng.normal(size=(samples, n, n)))
        signs = np.where(np.diagonal(tri, axis1=1, axis2=2) >= 0, 1., -1.)
        O *= signs[:, None, :]
        pre = math.sqrt(gain2)*np.einsum('bij,bj->bi', O, h, optimize=False)
        pre += math.sqrt(b)*rng.normal(size=(samples, n))
        J = math.sqrt(gain2)*np.cosh(pre)[:, :, None]**-2*mm(O, J)
        h = np.tanh(pre)
        qnext = gain2*(h*h).sum(1)/n
        U = (qnext-q)/q
        # Independently integrate the conditional forward mean on each path.
        st, sw = sphere
        prequad = np.sqrt(n*q[:, None, None])*st[None, :, None]+math.sqrt(b)*v
        forward_mean = gain2*(np.tanh(prequad)**2*sw[None, :, None]*w).sum((1, 2))
        drift = (forward_mean-q)/q
        N += U-drift
        M += (q/a)*(U-drift)
        maxM = np.maximum(maxM, abs(M))
        sumU += U
        sumU2 += U*U
        max_radius = np.maximum(max_radius, abs(qnext/a-1))
        logS += math.log(gain2)+np.log(mu_sphere(q, b, n, sphere, gaussian))
        assert np.all(max_radius <= 8/n+614*a+2*maxM+2e-12)
    S = np.exp(logS)
    gram = mm(J, J.transpose(0, 2, 1))
    Z = ((gram-np.eye(n))**2).sum((1, 2))/n
    Znorm = ((gram/S[:, None, None]-np.eye(n))**2).sum((1, 2))/n
    A = 24*depth*a/(n+2)+65664*depth*a*a
    B = 12*depth*a/(n+2)+77184*depth*a*a
    bound = B*math.exp(A)
    assert min_r >= .5 and max_r <= 2
    assert Znorm.mean()+6*Znorm.std(ddof=1)/math.sqrt(samples) < bound
    assert sumU2.mean() < 12000*depth*a*a
    assert np.all(np.sqrt(Z) <= S*np.sqrt(Znorm)+abs(S-1)+1e-12)
    final_ratio = gain2*(h*h).sum(1)/(n*a)
    log_ratio = np.log(final_ratio/initial_ratio)
    assert np.all(abs(sumU-log_ratio) <= 8*sumU2+3e-12)
    observed_delta = np.maximum(maxM, abs(N))
    K = (16/n+1228*a+28*a*a+5*observed_delta+8*sumU2
         +8*depth*a/(n+2)+452*depth*a*a)
    assert np.all(abs(logS) <= K+3e-12)
    network = {'n': n, 'L': depth, 'samples': samples, 'a': a, 'b': b,
               'b_over_a_cubed': b/a**3, 'gain_squared': gain2,
               'mean_S': float(S.mean()), 'min_radius_ratio': min_r,
               'max_radius_ratio': max_r, 'max_abs_radius_error': float(max_radius.max()),
               'mean_original_distortion': float(Z.mean()),
               'mean_normalized_distortion': float(Znorm.mean()),
               'stopped_distortion_bound': bound,
               'mean_sum_squared_relative_increments': float(sumU2.mean()),
               'max_radius_martingale': float(maxM.max()),
               'max_increment_martingale': float(abs(N).max()),
               'max_logarithm_remainder': float(abs(sumU-log_ratio).max()),
               'min_pathwise_scalar_margin': float((K-abs(logS)).min())}
    # A longer forward-only run exposes accumulated finite-width drift.
    n, depth, samples, a = 64, 10000, 32, .0002
    sphere = sphere_rule(n, 16)
    mu_g = weighted(w, np.cosh(math.sqrt(a)*v)**-4)
    activation = weighted(w, np.tanh(math.sqrt(a)*v)**2)
    gain2 = 1/mu_g
    b = a-gain2*activation
    q = np.full(samples, a-b)
    logS = np.zeros(samples)
    max_error = np.zeros(samples)
    for unused in range(depth):
        u = rng.normal(size=(samples, n))
        u /= np.sqrt((u*u).sum(1))[:, None]
        z = np.sqrt(n*q[:, None])*u+math.sqrt(b)*rng.normal(size=(samples, n))
        logS += math.log(gain2)+np.log(mu_sphere(q, b, n, sphere, gaussian))
        q = gain2*(np.tanh(z)**2).sum(1)/n
        max_error = np.maximum(max_error, abs(q/a-1))
    radial = {'n': n, 'L': depth, 'samples': samples, 'a': a, 'b': b,
              'La': depth*a, 'La_over_n': depth*a/n,
              'mean_S': float(np.exp(logS).mean()),
              'max_abs_radius_error': float(max_error.max())}
    return {'network': network, 'long_forward': radial}


def main():
    series = exact_series()
    critical = high_precision_critical()
    print('Exact critical bias series:', series['bias_coefficients'])
    print('70-digit critical b/a^3:', [x['b_over_a_cubed'][:18] for x in critical])
    gates = bias_gate_bounds()
    print(f'Global bias-averaged gate inequalities: {len(gates)*6} cases passed')
    haar = haar_checks()
    print(f'Direct biased Haar quadrature: {len(haar["cases"])} cases; '
          f'max refinement difference {max(x["quadrature_difference"] for x in haar["cases"]):.3g}')
    print(f'Biased linear-coefficient extrapolation error: {haar["max_derivative_error"]:.3g}')
    radial = exact_radial_bounds()
    print(f'Exact correlated eighth-moment radial bounds: {radial["cases"]} passed; '
          f'max ratio {radial["max_exact_bound_over_coarse_bound"]:.6g}')
    drift = radial_drift_checks()
    print(f'Forward drift/scalar quadrature: {len(drift)} cases passed')
    crossings = crossing_checks()
    print(f'Asymmetric stopped-radius crossing checks: {crossings} passed')
    simulations = simulate()
    net = simulations['network']
    long = simulations['long_forward']
    print(f'Actual biased critical network n={net["n"]}, L={net["L"]}: '
          f'mean Z={net["mean_original_distortion"]:.9g}, '
          f'normalized Z={net["mean_normalized_distortion"]:.9g}, '
          f'bound={net["stopped_distortion_bound"]:.9g}, mean S={net["mean_S"]:.9g}')
    print(f'Long biased forward n={long["n"]}, L={long["L"]}, La={long["La"]}: '
          f'mean S={long["mean_S"]:.9g}, max radius error={long["max_abs_radius_error"]:.9g}')
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        peak *= 1024
    assert peak < 10**9
    results = {'exact_series': series, 'high_precision_critical': critical,
               'gate_bounds': gates, 'haar': haar, 'exact_radial': radial,
               'radial_drift': drift, 'crossing_checks': crossings, 'simulations': simulations,
               'runtime_seconds': time.monotonic()-START, 'peak_rss_bytes': peak,
               'niceness': os.getpriority(os.PRIO_PROCESS, 0),
               'thread_environment': {k: os.environ[k] for k in THREADS}}
    Path(__file__).resolve().with_name('recheck_results.json').write_text(json.dumps(results, indent=2)+'\n')
    print(f'Niceness {results["niceness"]}; peak RSS {peak/1024**2:.1f} MiB; '
          f'runtime {results["runtime_seconds"]:.2f} s')
    print('All biased-network verification checks passed')


if __name__ == '__main__':
    main()
