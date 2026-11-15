"""Short consistency checks for PROOF.md; Python standard library only.

Floating-point checks are not certificates. The proof does not use these data.
"""

import json
import math
import os
from pathlib import Path
import resource
import sys
import time

ROOT = Path(__file__).resolve().parent
X, DELTA, P = 1.2, 0.4, 0.2
COND_A, COND_B = [0.2, 0.3, 0.5], [0.5, 0.25, 0.25]
WEIGHTS = [P * z for z in COND_A] + [(1 - P) * z for z in COND_B]


def simpson(f, lo, hi, n=32768):
    h = (hi - lo) / n
    return h / 3 * (f(lo) + f(hi)
                    + 4 * math.fsum(f(lo + i*h) for i in range(1, n, 2))
                    + 2 * math.fsum(f(lo + i*h) for i in range(2, n, 2)))


def atom_drift(beta, s, p=P):
    q = 1 - p
    e = math.exp(beta * (1 - math.cos(s)))
    return math.sin(s) * (q / (p*e + q) + p / (q*e + p))


def atom_time(beta, s=X, p=P):
    return simpson(lambda z: 1 / atom_drift(beta, z, p), DELTA, s)


def row(beta, theta, positions, weights):
    # The common exp(beta) factor is removed exactly.
    kernels = [m * math.exp(beta * (math.cos(phi-theta) - 1))
               for m, phi in zip(weights, positions)]
    z = math.fsum(kernels)
    alphas = [k / z for k in kernels]
    sins = [math.sin(phi-theta) for phi in positions]
    v = math.fsum(a*s for a, s in zip(alphas, sins))
    derivative = (-math.fsum(a*math.cos(phi-theta)
                            for a, phi in zip(alphas, positions))
                  + beta * (math.fsum(a*s*s for a, s in zip(alphas, sins)) - v*v))
    return v, derivative, kernels, z


def velocities(beta, positions, weights=WEIGHTS):
    return [row(beta, theta, positions, weights)[0] for theta in positions]


def gap(positions):
    return (math.fsum(m*z for m, z in zip(COND_B, positions[3:]))
            - math.fsum(m*z for m, z in zip(COND_A, positions[:3])))


def initial_positions(width):
    result = []
    for values, conditional, center in (([-0.5, -0.1, 0.4], COND_A, 0.0),
                                         ([-0.4, 0.15, 0.6], COND_B, X)):
        mean = math.fsum(a*b for a, b in zip(values, conditional))
        span = max(values) - min(values)
        result.extend(center + width*(v-mean)/span for v in values)
    assert abs(gap(result) - X) < 1e-14
    return result


def rk4_step(beta, positions, dt, weights=WEIGHTS):
    def shifted(k, factor):
        return [y + factor*dt*v for y, v in zip(positions, k)]
    k1 = velocities(beta, positions, weights)
    k2 = velocities(beta, shifted(k1, 0.5), weights)
    k3 = velocities(beta, shifted(k2, 0.5), weights)
    k4 = velocities(beta, shifted(k3, 1.0), weights)
    return [y + dt*(a+2*b+2*c+d)/6
            for y, a, b, c, d in zip(positions, k1, k2, k3, k4)]


def token_hitting_time(beta, width, dt):
    positions, t = initial_positions(width), 0.0
    max_width_excess = 0.0
    for step in range(100000):
        before = gap(positions)
        nxt = rk4_step(beta, positions, dt)
        after = gap(nxt)
        t += dt
        if t <= 20:
            diameter = max(max(nxt[:3])-min(nxt[:3]), max(nxt[3:])-min(nxt[3:]))
            max_width_excess = max(max_width_excess,
                                   diameter - width*math.exp(-t/2))
        if after <= DELTA:
            hitting = t-dt + dt*(before-DELTA)/(before-after)
            return hitting, max_width_excess
        positions = nxt
    raise AssertionError('time-step budget exceeded')


def noise_bvp(beta, p, nu, n=8192):
    """Central finite differences for 2 nu u''-h u'=-1."""
    step = (math.pi - DELTA) / n
    low, diag, high, rhs = [], [], [], []
    for i in range(1, n):
        peclet = atom_drift(beta, DELTA+i*step, p)*step/(4*nu)
        assert peclet < 1
        low.append(1+peclet)
        diag.append(-2.0)
        high.append(1-peclet)
        rhs.append(-step*step/(2*nu))
    low.append(-1.0)
    diag.append(1.0)
    high.append(0.0)
    rhs.append(step*step/(4*nu))
    for i in range(1, n):
        f = low[i]/diag[i-1]
        diag[i] -= f*high[i-1]
        rhs[i] -= f*rhs[i-1]
    u = [0.0]*(n+1)
    u[n] = rhs[-1]/diag[-1]
    for i in range(n-2, -1, -1):
        u[i+1] = (rhs[i]-high[i]*u[i+2])/diag[i]
    pos = (X-DELTA)/step
    j = int(pos)
    return u[j]+(pos-j)*(u[j+1]-u[j])


def noise_kernel(beta, p, nu, n=1024):
    """Direct double Simpson integral, using a checked primitive."""
    ell = abs(math.log(p/(1-p)))
    def primitive(s):
        a = 1-math.cos(s)
        return (math.log1p(math.exp(ell-beta*a))
                + math.log1p(math.exp(-ell-beta*a)))/beta
    def inner(y):
        fy = primitive(y)
        return simpson(lambda z: math.exp(-(fy-primitive(z))/(2*nu)),
                       y, math.pi, n)
    return simpson(inner, DELTA, X, 128)/(2*nu)


def main():
    started = time.monotonic()
    resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    for name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS',
                 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
        assert os.environ.get(name) == '1'
    results = {}

    # Round 3: direct row coefficients versus a different coordinate integral.
    prior = []
    for p in (0.5, 0.2, 0.01):
        for beta in (20, 80, 160):
            scale = math.exp(-beta*(1-math.cos(X)))
            angular = simpson(lambda s: scale/atom_drift(beta, s, p), DELTA, X)
            def cosine_integrand(c):
                e = math.exp(beta*(1-c))
                w = (1-p)/(p*e+1-p)+p/((1-p)*e+p)
                return scale/(w*(1-c*c))
            cosine = simpson(cosine_integrand, math.cos(X), math.cos(DELTA))
            err = abs(angular/cosine-1)
            assert err < 2e-8
            prefactor_ratio = angular*(p/(1-p)+(1-p)/p)*beta*math.sin(X)**2
            prior.append(dict(p=p, beta=beta, coordinate_error=err,
                              exact_over_prefactor=prefactor_ratio))
    results['prior_deterministic'] = prior
    kernel = noise_kernel(4, 0.2, 0.03)
    bvp = noise_bvp(4, 0.2, 0.03)
    noise_error = abs(kernel/bvp-1)
    assert noise_error < 2e-6
    results['prior_noise'] = dict(kernel=kernel, bvp=bvp, relative_error=noise_error)
    print('Prior deterministic coordinate error:', f'{max(z["coordinate_error"] for z in prior):.3e}')
    print('Prior noise kernel / BVP:', f'{kernel:.12g}', f'{bvp:.12g}',
          'relative error', f'{noise_error:.3e}', flush=True)

    # Identity (10) checked by finite differences, and (12) by direct sums.
    identities = []
    for beta in (20, 80, 320):
        positions = initial_positions(0.2/math.sqrt(beta))
        w = max(max(positions[:3])-min(positions[:3]),
                max(positions[3:])-min(positions[3:]))
        eps = max(P/(1-P), (1-P)/P)*math.exp(
            -beta*(math.cos(w)-math.cos(DELTA/2)))
        for group, mass in ((range(3), P), (range(3, 6), 1-P)):
            group = list(group)
            direct, symmetric = 0.0, 0.0
            denominators = {i: row(beta, positions[i], positions, WEIGHTS)[3]
                            for i in group}
            for i in group:
                v, deriv, kernels, z = row(beta, positions[i], positions, WEIGHTS)
                step = 1e-6
                finite_diff = (row(beta, positions[i]+step, positions, WEIGHTS)[0]
                               - row(beta, positions[i]-step, positions, WEIGHTS)[0])/(2*step)
                assert abs(deriv-finite_diff) < 1e-7
                assert deriv < -0.5
                for j in group:
                    k = math.exp(beta*(math.cos(positions[j]-positions[i])-1))
                    pair = WEIGHTS[i]*WEIGHTS[j]*k*math.sin(positions[j]-positions[i])/mass
                    direct += pair/z
                    symmetric += 0.5*pair*(1/z-1/denominators[j])
            identity_error = abs(direct-symmetric)
            bound = 0.5*beta*math.exp(1/16)*(w**3+eps*w*w)
            assert identity_error < 2e-16
            assert abs(direct) <= bound
            identities.append(dict(beta=beta, group=group, internal_drift=direct,
                                   symmetrized=symmetric, identity_error=identity_error,
                                   bound=bound))
    results['identities'] = identities
    print('Internal symmetrization max absolute error:',
          f'{max(z["identity_error"] for z in identities):.3e}', flush=True)

    full = []
    for beta in (6, 10, 14, 18):
        width = 0.2/beta
        coarse, excess_c = token_hitting_time(beta, width, 0.1)
        fine, excess_f = token_hitting_time(beta, width, 0.05)
        err = abs(coarse/fine-1)
        assert err < 2e-4
        atom = atom_time(beta)
        prefactor = math.exp(beta*(1-math.cos(X)))/(
            (P/(1-P)+(1-P)/P)*beta*math.sin(X)**2)
        full.append(dict(beta=beta, width=width, time=fine, scalar_time=atom,
                         token_over_scalar=fine/atom, token_over_prefactor=fine/prefactor,
                         mesh_relative_error=err, max_width_bound_excess=max(excess_c, excess_f)))
        print('Full six-token solve:', beta, f'{fine:.9g}',
              'token/scalar', f'{fine/atom:.9f}', 'mesh error', f'{err:.3e}', flush=True)
    results['full_token_solve'] = full

    concentration = []
    for beta in (500, 1000, 2000):
        width = 0.2/math.sqrt(beta)
        epsilon = max(P/(1-P), (1-P)/P)*math.exp(
            -beta*(math.cos(width)-math.cos(DELTA/2)))
        derivative_bound = -1+(beta+0.5)*width**2+(beta+2)*epsilon
        assert derivative_bound < -0.5
        positions, excess = initial_positions(width), 0.0
        for i in range(400):
            positions = rk4_step(beta, positions, 0.05)
            t = (i+1)*0.05
            measured = max(max(positions[:3])-min(positions[:3]),
                           max(positions[3:])-min(positions[3:]))
            excess = max(excess, measured-width*math.exp(-t/2))
            assert gap(positions) > DELTA
        assert excess < 2e-14
        concentration.append(dict(beta=beta, sufficient_derivative_bound=derivative_bound,
                                  width=width, max_width_bound_excess=excess))
    results['concentration'] = concentration
    print('Concentration sufficient derivative bounds:',
          [(z['beta'], round(z['sufficient_derivative_bound'], 9)) for z in concentration], flush=True)

    # Breaking the prefactor extrapolation: isolate one skew group so that its
    # initial relaxation can be measured without any cross attraction.
    relaxation = []
    for beta in (20, 80, 320):
        for power in (0.5, 1.0):
            width = 0.2/beta**power
            positions = initial_positions(width)[:3]
            for _ in range(400):
                positions = rk4_step(beta, positions, 0.05, COND_A)
            shift = math.fsum(m*z for m, z in zip(COND_A, positions))
            relaxation.append(dict(beta=beta, width_power=power, center_shift=shift,
                                   beta_times_shift=beta*shift,
                                   shift_over_beta_width_cubed=shift/(beta*width**3)))
    results['isolated_group_relaxation'] = relaxation
    print('Isolated skew group: beta, width power, beta*center shift')
    for z in relaxation:
        print(z['beta'], z['width_power'], f'{z["beta_times_shift"]:.9g}')

    elapsed = time.monotonic()-started
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform == 'darwin' else 1024)
    assert peak < 1024
    results['resources'] = dict(elapsed_seconds=elapsed, peak_rss_mib=peak,
                               effective_nice=os.getpriority(os.PRIO_PROCESS, 0))
    (ROOT/'verification.json').write_text(json.dumps(results, indent=2)+'\n')
    print(f'All checks passed. elapsed={elapsed:.3f}s; peak RSS={peak:.2f} MiB; nice={os.getpriority(os.PRIO_PROCESS, 0)}')


if __name__ == '__main__':
    main()
