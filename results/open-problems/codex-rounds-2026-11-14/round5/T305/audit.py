#!/usr/bin/env python3
"""Independent exact checks and a small streaming numerical audit."""
import json
import math
import os
from pathlib import Path
import random
import resource
import signal
import threading
import time
from fractions import Fraction as F

START = time.monotonic()
ROOT = Path(__file__).resolve().parent
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
assert threading.active_count() == 1
resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
signal.alarm(240)
AMP = F(1, 24)


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def bump(x):
    s = dot(x, x)
    return AMP*(1-s)**3 if s < 1 else s*0


def grad(x):
    s = dot(x, x)
    factor = 1-6*AMP*(1-s)**2 if s < 1 else 1
    return [factor*t for t in x]


def energy(x, p):
    return (dot(x, x)+dot(p, p))/2+bump(x)


def step(x, p, h):
    gx = grad(x)
    v = [pp-h*gg/2 for pp, gg in zip(p, gx)]
    q = [xx+h*vv for xx, vv in zip(x, v)]
    gq = grad(q)
    pp = [vv-h*gg/2 for vv, gg in zip(v, gq)]
    return q, pp


def exact_local_and_reversal():
    records = []
    for xx, pp, h in [([F(0)], [F(1, 3)], F(1, 5)),
                       ([F(9, 10)], [F(2)], F(1, 2)),
                       ([F(6, 5)], [F(-2)], F(1, 2)),
                       ([F(1, 3), F(1, 4)], [F(2, 3), F(-3, 4)], F(1, 4)),
                       ([F(2), F(0)], [F(-1), F(1, 5)], F(1))]:
        q, pn = step(xx, pp, h)
        direct = energy(q, pn)-energy(xx, pp)
        gx, gq = grad(xx), grad(q)
        displacement = [b-a for a, b in zip(xx, q)]
        algebra = ((dot(q, q)-dot(xx, xx))/2+bump(q)-bump(xx)
                   -dot(displacement, [a+b for a, b in zip(gx, gq)])/2
                   +h*h*(dot(gq, gq)-dot(gx, gx))/8)
        assert direct == algebra
        xr, pr = step(q, [-v for v in pn], h)
        assert xr == xx
        assert pr == [-v for v in pp]
        reverse_error = energy(xr, pr)-energy(q, pn)
        assert reverse_error == -direct
        records.append({'dimension': len(xx), 'h': str(h),
                        'initial_inside': dot(xx, xx) < 1,
                        'final_inside': dot(q, q) < 1,
                        'energy_error_float': float(direct),
                        'exact_identity_and_involution': True})
    return records


def mm(a, b):
    return [[sum(a[i][j]*b[j][k] for j in range(2)) for k in range(2)]
            for i in range(2)]


def gaussian_exact():
    records = []
    for h, n in [(F(1, 4), 4), (F(2, 7), 11), (F(1), 1), (F(1), 7)]:
        alpha = h*h/4
        c = [[1-h*h/2, h], [-h*(1-alpha), 1-h*h/2]]
        power = [[F(1), F(0)], [F(0), F(1)]]
        for _ in range(n):
            power = mm(c, power)
        aa, bb = power[0]
        cc, dd = power[1]
        e11 = (aa*aa+cc*cc-1)/2
        e22 = (bb*bb+dd*dd-1)/2
        e12 = (aa*bb+cc*dd)/2
        mu = e11+e22
        mu_alt = alpha*alpha*bb*bb/2
        assert mu == mu_alt
        var = 2*(e11*e11+2*e12*e12+e22*e22)
        assert var == 2*mu+2*mu*mu
        assert aa*dd-bb*cc == 1
        # Independent fourth-moment expansion, then tensorization.
        second_one = 3*e11*e11+4*e12*e12+3*e22*e22+2*e11*e22
        assert second_one == var+mu*mu
        for d in (1, 2, 13, 10000):
            second_direct = d*second_one+d*(d-1)*mu*mu
            second_claim = 2*d*mu+(d*d+2*d)*mu*mu
            assert second_direct == second_claim
            assert second_claim <= d*h**4/12+d*d*h**8/192
        phi = 2*n*math.asin(float(h)/2)
        prior = float(h)**4*math.sin(phi)**2/(32*(1-float(h)**2/4))
        assert abs(float(mu)-prior) < 3e-15
        records.append({'h': str(h), 'n': n, 'mean': float(mu),
                        'variance': float(var), 'prior_mean_residual': float(mu)-prior})
    return records


def moments_and_constants():
    # Derive chi-squared moments again by convolution of moments of 2d
    # independent squared normals, without using the rising factorial.
    records = []
    for d in (1, 2, 5, 11):
        square_moment = [1]
        for k in range(1, 7):
            square_moment.append(square_moment[-1]*(2*k-1))
        totals = [1]+[0]*6
        for _ in range(2*d):
            totals = [sum(math.comb(k, j)*totals[j]*square_moment[k-j]
                          for j in range(k+1)) for k in range(7)]
        rising = 1
        for k in range(7):
            if k:
                rising *= d+k-1
            assert totals[k] == 2**k*rising
        w12 = sum(math.comb(6, k)*totals[k] for k in range(7))
        assert w12 <= (2*d+11)**6
        records.append({'d': d, 'W12_exact': w12,
                        'upper_bound': (2*d+11)**6})
    c = 1/16+math.log(15/16)/2
    c0 = math.log(2)/2-1/4
    assert 0 < c < c0
    # Re-derive dot-product mgf using (X+P)/sqrt(2),(X-P)/sqrt(2).
    for t in (-0.4, -0.25, 0.25, 0.4):
        for d in (1, 3, 17):
            conditional = (1-t*t)**(-d/2)
            rotated = (1-t)**(-d/2)*(1+t)**(-d/2)
            assert abs(conditional/rotated-1) < 4e-15
    # Exact checks of Chernoff substitution, independently of exponentials.
    for root_v, b, root_s in [(F(2), F(1, 3), F(4)),
                               (F(1, 5), F(3), F(2))]:
        t = root_s/(root_v+b*root_s)
        threshold = 2*root_v*root_s+b*root_s**2
        assert t*threshold-root_v**2*t*t/(1-b*t) == root_s**2
    # The maximum in (25), checked both by its derivative and its value.
    maximizer = 4/c
    assert abs(2/maximizer-c/2) < 1e-15
    assert abs(maximizer**2*math.exp(-c*maximizer/2)/(16/(c*c*math.e**2))-1) < 1e-15
    return {'c': c, 'c0': c0, 'K_R_R1': 4*math.exp(5*c),
            'moments': records, 'polynomial_exponential_maximizer': maximizer}


def bump_regularities():
    # Radial Hessian is also obtained as d/dr of the radial gradient:
    # g_rad=r-6 AMP*r*(1-r^2)^2.
    max_hessian_abs, max_operator_derivative_bound = F(0), F(0)
    for i in range(101):
        r = F(i, 100)
        s = r*r
        tangential = -6*AMP*(1-s)**2
        radial = AMP*(-6+36*s-30*s*s)
        radial_from_gradient = -6*AMP*((1-s)**2-4*s*(1-s))
        assert radial == radial_from_gradient
        assert abs(tangential) <= F(1, 4)
        assert abs(radial) <= F(1, 4)
        bound = 72*AMP*r*(1-r*r)+48*AMP*r**3
        assert bound == 24*AMP*(3*r-r**3)
        assert bound <= 2
        max_hessian_abs = max(max_hessian_abs, abs(tangential), abs(radial))
        max_operator_derivative_bound = max(max_operator_derivative_bound, bound)
    # Exact polynomial differentiation of the tangential Hessian at r=1/2.
    r = F(1, 2)
    derivative_poly = 24*AMP*r-24*AMP*r**3
    derivative_factored = 24*AMP*r*(1-r*r)
    assert derivative_poly == derivative_factored == F(3, 8)
    radial_derivative = 72*AMP*r-120*AMP*r**3
    assert radial_derivative == F(7, 8)
    # A C3 sibling removes third-derivative discontinuity as an explanation
    # of the regularity gap. Its fourth derivative jumps at the boundary.
    amp4 = F(1, 32)
    for i in range(101):
        rr = F(i, 100)
        ss = rr*rr
        tang4 = -8*amp4*(1-ss)**3
        rad4 = 8*amp4*(1-ss)**2*(7*ss-1)
        rad4_from_gradient = -8*amp4*((1-ss)**3-6*ss*(1-ss)**2)
        assert rad4 == rad4_from_gradient
        assert max(abs(tang4), abs(rad4)) <= F(1, 4)
        bound4 = 144*amp4*rr*(1-ss)**2+192*amp4*rr**3*(1-ss)
        assert bound4 == 48*amp4*rr*(1-ss)*(3+ss)
        assert bound4 <= 3
    assert 48*amp4*r*(1-r*r)**2 == F(27, 64)
    assert 144*amp4*r-480*amp4*r**3+336*amp4*r**5 == F(45, 64)
    assert 8*amp4*(1-F(3, 7))**2*(7*F(3, 7)-1) == 256*amp4/49
    return {'m': 0.75, 'L_safe': 1.25, 'M_safe': 2,
            'max_grid_hessian_abs': str(max_hessian_abs),
            'max_grid_operator_derivative_bound': str(max_operator_derivative_bound),
            'Frobenius_derivative_squared_exact': '(49+9*(d-1))/64',
            'Frobenius_Lipschitz_lower_bound': '3*sqrt(d-1)/8',
            'C3_sibling': {'m': 0.75, 'L_safe': 1.25, 'M_safe': 3,
                           'Frobenius_Lipschitz_lower_bound': '27*sqrt(d-1)/64'}}


def leap_float(x, p, h, n, perturbed=True):
    x, p = list(x), list(p)
    for _ in range(n):
        s = math.fsum(t*t for t in x)
        f = 1-(1-s)**2/4 if perturbed and s < 1 else 1
        p = [pp-h*f*xx/2 for xx, pp in zip(x, p)]
        x = [xx+h*pp for xx, pp in zip(x, p)]
        s = math.fsum(t*t for t in x)
        f = 1-(1-s)**2/4 if perturbed and s < 1 else 1
        p = [pp-h*f*xx/2 for xx, pp in zip(x, p)]
    return x, p


def float_energy(x, p):
    s = math.fsum(t*t for t in x)
    return (s+math.fsum(t*t for t in p))/2+max(0, 1-s)**3/24


def smallest_gram_eigenvalue(x, p):
    xx, pp, xp = dot(x, x), dot(p, p), dot(x, p)
    return max(0.0, (xx+pp-math.hypot(xx-pp, 2*xp))/2)


def avoidance_audit():
    max_endpoint_error = 0.0
    min_ratio = float('inf')
    cases = 0
    # Includes nonorthogonal, unequal-length columns and long resonant runs.
    for x, p in [([2., 0.], [0., 3.]), ([3., 1., 0.], [1., 3., 2.]),
                 ([2., 0., 0.], [0., 2., 0.])]:
        lower = math.sqrt(smallest_gram_eigenvalue(x, p))
        assert lower > 1
        for h, n in [(1., 1), (1., 7), (0.25, 4), (0.125, 80)]:
            a, b = leap_float(x, p, h, n, True)
            ag, bg = leap_float(x, p, h, n, False)
            err = max(abs(u-v) for u, v in zip(a+b, ag+bg))
            max_endpoint_error = max(max_endpoint_error, err)
            assert err == 0
            theta, rh = 2*math.asin(h/2), math.sqrt(1-h*h/4)
            for j in range(n+1):
                pos = [math.cos(j*theta)*u+math.sin(j*theta)*v/rh
                       for u, v in zip(x, p)]
                ratio = math.sqrt(dot(pos, pos))/lower
                min_ratio = min(min_ratio, ratio)
                assert ratio >= 1-1e-14
            cases += 1
    # A path starting outside can enter. This refutes a comparison using
    # only the initial radius, and must be caught by the Gram event.
    x, p = [2., 0.], [-1., 0.]
    assert smallest_gram_eigenvalue(x, p) < 1
    out, mom = leap_float(x, p, 1/16, 16, True)
    og, pg = leap_float(x, p, 1/16, 16, False)
    entered_difference = max(abs(u-v) for u, v in zip(out+mom, og+pg))
    assert entered_difference > 0.01
    return {'cases': cases, 'max_perturbed_vs_Gaussian_endpoint_error': max_endpoint_error,
            'minimum_position_over_singular_value': min_ratio,
            'outside_start_that_enters_endpoint_difference': entered_difference}


def streaming_audit():
    # Fixed-seed samples are numerical audits, not probability enclosures.
    rng = random.Random(30505)
    rows = []
    sample_count = 2000
    for d in (1, 2, 4, 8, 16, 64):
        accum = {n: [0., 0., 0.] for n in (4, 8, 16)}
        exceptional = 0
        accepted = 0
        while accepted < sample_count:
            x = [rng.gauss(0, 1) for _ in range(d)]
            sx = math.fsum(t*t for t in x)
            u = max(0, 1-sx)**3/24
            if rng.random() > math.exp(-u):
                continue
            accepted += 1
            p = [rng.gauss(0, 1) for _ in range(d)]
            if smallest_gram_eigenvalue(x, p) <= 1:
                exceptional += 1
            initial = float_energy(x, p)
            for n, values in accum.items():
                xn, pn = leap_float(x, p, 1/n, n, True)
                delta = float_energy(xn, pn)-initial
                # Reflection formula follows from the independently checked
                # exact involution. Its integrand is positive of order h^4.
                reflected = -delta*math.expm1(-delta)/2
                values[0] += delta*delta
                values[1] += reflected
                values[2] += delta
        for n, values in accum.items():
            scaled_second = values[0]*n**4/(sample_count*d)
            scaled_reflected = values[1]*n**4/(sample_count*d)
            # Broad sanity limits only, no claimed Monte Carlo accuracy.
            assert 0.01 < scaled_second < 0.12
            assert 0.005 < scaled_reflected < 0.06
            rows.append({'d': d, 'n': n, 'samples': sample_count,
                         'exceptional_count': exceptional,
                         'second_over_dh4': scaled_second,
                         'reflected_mean_over_dh4': scaled_reflected,
                         'direct_mean_over_dh4': values[2]*n**4/(sample_count*d)})
        print('stream d=%d exceptional=%d/%d second/(dh4)=%s' %
              (d, exceptional, sample_count,
               ','.join('%.6g' % r['second_over_dh4'] for r in rows if r['d'] == d)),
              flush=True)
    return rows


def main():
    data = {'exact_local_and_reversal': exact_local_and_reversal(),
            'exact_Gaussian': gaussian_exact(),
            'moments_and_constants': moments_and_constants(),
            'regularity': bump_regularities(), 'avoidance': avoidance_audit()}
    print('PASS: exact rational local energy identity and reversible involution', flush=True)
    print('PASS: Gaussian second moments by two exact expansions', flush=True)
    print('PASS: Gaussian moments, dot-product Chernoff constant, and tail substitution', flush=True)
    print('PASS: operator regularity and growing Frobenius lower bound', flush=True)
    print('PASS: pathwise avoidance, including an outside start that enters the ball', flush=True)
    data['streaming'] = streaming_audit()
    data['resources'] = {'elapsed_seconds': time.monotonic()-START,
                         'max_rss_bytes_macos': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                         'nice': os.getpriority(os.PRIO_PROCESS, 0),
                         'python_threads': threading.active_count()}
    assert data['resources']['max_rss_bytes_macos'] < 1024**3
    assert data['resources']['elapsed_seconds'] < 240
    (ROOT/'audit_data.json').write_text(json.dumps(data, indent=2)+'\n')
    print('Resources:', json.dumps(data['resources']), flush=True)


if __name__ == '__main__':
    main()
