#!/usr/bin/env python3
"""Deterministic audits using only the Python standard library."""
import json
import math
import os
from pathlib import Path
import resource
import signal
import threading
import time
from fractions import Fraction as Q

START = time.monotonic()
ROOT = Path(__file__).resolve().parent
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
assert threading.active_count() == 1
resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
# macOS rejects a small RLIMIT_AS despite reporting an unlimited ceiling.
# Storage is bounded by an 801-entry momentum grid and scalar accumulators.
signal.alarm(240)


def multiply(a, b):
    return [[sum(a[i][j] * b[j][k] for j in range(2))
             for k in range(2)] for i in range(2)]


def gaussian_recheck():
    exact = []
    for h, lam, n in [(Q(1, 8), Q(1), 8),
                       (Q(2, 9), Q(7, 4), 5),
                       (Q(1, 2), Q(4), 2)]:
        a = h*h*lam/4
        step = [[1-h*h*lam/2, h], [-h*lam*(1-a), 1-h*h*lam/2]]
        power = [[Q(1), Q(0)], [Q(0), Q(1)]]
        for _ in range(n):
            power = multiply(step, power)
        # Physical covariance is diag(1/lambda,1). Compute E DeltaH
        # from endpoint kinetic and potential energies, not from R.
        aa, bb = power[0]
        cc, dd = power[1]
        mu_direct = (aa*aa+lam*bb*bb+cc*cc/lam+dd*dd-2)/2
        mu_invariant = a*a*lam*bb*bb/2
        assert mu_direct == mu_invariant
        assert aa*dd-bb*cc == 1
        # Quadratic-form coefficients in unstandardized coordinates.
        e11 = (lam*aa*aa+cc*cc-lam)/2
        e12 = (lam*aa*bb+cc*dd)/2
        e22 = (lam*bb*bb+dd*dd-1)/2
        second = 2*(e11*e11/lam**2+2*e12*e12/lam+e22*e22)+mu_direct**2
        assert second == 2*mu_direct+3*mu_direct**2
        assert mu_direct <= second/2
        # Compare against the prior report's trigonometric formula.
        hf, lf = float(h), float(lam)
        phi = 2*n*math.asin(hf*math.sqrt(lf)/2)
        prior = hf**4*lf**2*math.sin(phi)**2/(32*(1-hf*hf*lf/4))
        assert abs(float(mu_direct)-prior) < 2e-15
        exact.append({'h': str(h), 'lambda': str(lam), 'n': n,
                      'mean_exact': str(mu_direct),
                      'second_moment_exact': str(second),
                      'previous_mean_formula_error': float(mu_direct)-prior})
    critical = []
    for n in (8, 32, 128, 512):
        h = 1/n
        d = n**4  # Scalar multiplicity only.
        phi = 2*n*math.asin(h/2)
        a = h*h/4
        mu = d*a*a*math.sin(phi)**2/(2*(1-a))
        critical.append({'n': n, 'd': d, 'mean_R': mu,
                         'limit': math.sin(1)**2/32})
    # Expansion of phi=1+h^2/24+O(h^4) gives this independent h^2 bias.
    correction = math.sin(1)**2/128+math.sin(2)/768
    error = critical[-1]['mean_R']-critical[-1]['limit']
    assert abs(512**2*error-correction) < 1e-7
    assert 0 < error < 3e-8
    critical[-1]['scaled_bias'] = 512**2*error
    critical[-1]['bias_coefficient'] = correction
    return {'exact': exact, 'critical': critical}


A, BETA = 0.4, 0.15


def potential(x):
    r = abs(x)
    f = r**3/6 if r <= 1 else r*r/2-r/2+1/6
    return x*x/2+A*f+BETA*(math.sin(x)-x)


def gradient(x):
    r = abs(x)
    integ = r*r/2 if r <= 1 else r-0.5
    return x+A*math.copysign(integ, x)+BETA*(math.cos(x)-1)


def leap(x, p, h, n):
    for _ in range(n):
        p -= h*gradient(x)/2
        x += h*p
        p -= h*gradient(x)/2
    return x, p


def local_identity():
    max_residual = 0.0
    max_fine_ratio = 0.0
    m, L, M = 1-BETA, 1+A+BETA, A+BETA
    cv = 1+L/2
    fine_a = M*cv**3/12
    fine_b = L*L*cv*(2+cv)/8
    coarse = L*cv*cv/4+fine_b
    for x, p in [(0.0, 0.0), (0.01, -0.3), (-0.01, 0.3),
                 (0.95, 1.2), (-1.05, 0.6), (3.0, -5.0), (50.0, -20.0)]:
        for h in (0.001, 0.03, 0.2, 1.0):
            v = p-h*gradient(x)/2
            q = x+h*v
            pp = v-h*gradient(q)/2
            direct = potential(q)-potential(x)+(pp*pp-p*p)/2
            algebra = (potential(q)-potential(x)
                       -(q-x)*(gradient(q)+gradient(x))/2
                       +h*h*(gradient(q)**2-gradient(x)**2)/8)
            max_residual = max(max_residual, abs(direct-algebra))
            assert abs(direct-algebra) < 2e-12
            w = math.hypot(x, p)
            fine = h**3*(fine_a*w**3+fine_b*w*w)
            rough = coarse*h*h*w*w
            assert abs(algebra) <= fine+2e-12
            assert abs(algebra) <= rough+2e-12
            if fine:
                max_fine_ratio = max(max_fine_ratio, abs(algebra)/fine)
    # Sharp trapezoidal constant 1/12 in a region of constant U'''.
    x, q = Q(1, 5), Q(4, 5)
    amp = Q(2, 5)
    f = lambda t: t*t/2+amp*t**3/6
    g = lambda t: t+amp*t*t/2
    defect = f(q)-f(x)-(q-x)*(g(q)+g(x))/2
    assert defect == -amp*(q-x)**3/12
    # Check the coefficient condition in the entropy inequality separately.
    for t in (-100.0, -10.0, -1.0, -0.001, 0.0, 0.001, 1.0, 10.0, 100.0):
        assert t*math.tanh(t/2) <= t*t/2+1e-14
    # Independent combinatorial check of the radial moment constants.
    for k in (1, 2, 7):
        dim = 2*k
        fourth = 3*dim+dim*(dim-1)
        sixth = 15*dim+9*dim*(dim-1)+dim*(dim-1)*(dim-2)
        assert fourth == 4*k*(k+1)
        assert sixth == 8*k*(k+1)*(k+2)
    # Exact substitution in the tail calculation, with rational roots.
    for root_v, bh, root_s in [(Q(3), Q(2), Q(2)),
                               (Q(1, 2), Q(1, 7), Q(4)),
                               (Q(9), Q(1, 3), Q(1, 5))]:
        v, s = root_v**2, root_s**2
        tt = root_s/(root_v+bh*root_s)
        threshold = 2*root_v*root_s+bh*s
        assert tt*threshold-v*tt**2/(1-bh*tt) == s
    return {'m': m, 'L': L, 'M': M,
            'max_direct_vs_local_identity_error': max_residual,
            'max_fine_bound_ratio': max_fine_ratio,
            'exact_cubic_trapezoid_defect': str(defect)}


class Sum:
    def __init__(self):
        self.value = 0.0
        self.correction = 0.0

    def add(self, val):
        y = val-self.correction
        total = self.value+y
        self.correction = (total-self.value)-y
        self.value = total


def quadrature(grid, steps):
    radius = 10.0
    dx = 2*radius/grid
    h = 1/steps
    totals = [Sum() for _ in range(8)]
    pgrid = []
    for j in range(grid+1):
        p = -radius+j*dx
        simpson = 1 if j in (0, grid) else 4 if j % 2 else 2
        pgrid.append((p, simpson*math.exp(-p*p/2)))
    for i in range(grid+1):
        x = -radius+i*dx
        ux = potential(x)
        simpson = 1 if i in (0, grid) else 4 if i % 2 else 2
        wx = simpson*math.exp(-ux)
        for p, wp in pgrid:
            xn, pn = leap(x, p, h, steps)
            delta = potential(xn)-ux+(pn*pn-p*p)/2
            negexp = math.exp(-delta)
            # The reflected mean follows from reversibility and is
            # computed separately to expose quadrature bias in E Delta.
            reflected = -delta*math.expm1(-delta)/2
            values = (1.0, delta, delta*delta, math.expm1(-delta),
                      delta*negexp, delta*delta*negexp, reflected,
                      math.exp(delta)-1-delta)
            weight = wx*wp
            for acc, value in zip(totals, values):
                acc.add(weight*value)
    norm = totals[0].value
    vals = [s.value/norm for s in totals]
    _, mu, second, exp_minus_one, reverse_first, reverse_second, reflected, exp_rem = vals
    assert abs(exp_minus_one) < 2e-6
    assert abs(mu-reflected) < 2e-6
    assert abs(second-reverse_second) < 2e-6
    assert reflected <= second/2*(1+1e-3)+1e-12
    return {'grid': grid, 'steps': steps, 'h': h,
            'mean_direct': mu, 'mean_reversibility': reflected,
            'second_moment': second, 'mean_over_h4': mu/h**4,
            'reflected_mean_over_h4': reflected/h**4,
            'second_over_h4': second/h**4,
            'exp_minus_one': exp_minus_one,
            'reverse_first_identity_residual': mu+reverse_first,
            'reverse_second_identity_residual': second-reverse_second,
            'mean_second_moment_bound_ratio': 2*reflected/second,
            'positive_mgf_remainder': exp_rem}


def main():
    data = {'gaussian_recheck': gaussian_recheck(),
            'local_checks': local_identity()}
    print('PASS: independent rational Gaussian mean, second moment, and prior critical drift', flush=True)
    print('PASS: exact local energy identity and sharp cubic trapezoid constant', flush=True)
    rows = []
    for grid in (200, 400):
        for steps in (4, 8, 16, 32):
            row = quadrature(grid, steps)
            rows.append(row)
            print('grid=%d n=%d mean/h4=%.9g reflected/h4=%.9g second/h4=%.9g exp_res=%.3g'
                  % (grid, steps, row['mean_over_h4'], row['reflected_mean_over_h4'],
                     row['second_over_h4'], row['exp_minus_one']), flush=True)
    data['nonquadratic_C21_quadrature'] = rows
    coarse, fine = rows[:4], rows[4:]
    data['refinement'] = [{'steps': x['steps'],
                           'direct_mean_change': y['mean_direct']-x['mean_direct'],
                           'reflected_mean_change': y['mean_reversibility']-x['mean_reversibility'],
                           'second_moment_change': y['second_moment']-x['second_moment']}
                          for x, y in zip(coarse, fine)]
    # The stable reflected mean and second moment should display h^4.
    ratio = fine[-1]['reflected_mean_over_h4']/fine[-2]['reflected_mean_over_h4']
    assert 0.8 < ratio < 1.2
    refined = quadrature(800, 32)
    data['extra_refinement_n32'] = refined
    print('grid=800 n=32 mean/h4=%.9g reflected/h4=%.9g second/h4=%.9g exp_res=%.3g'
          % (refined['mean_over_h4'], refined['reflected_mean_over_h4'],
             refined['second_over_h4'], refined['exp_minus_one']), flush=True)
    assert abs(refined['mean_direct']-refined['mean_reversibility']) < abs(fine[-1]['mean_direct']-fine[-1]['mean_reversibility'])
    assert abs(refined['mean_reversibility']-fine[-1]['mean_reversibility']) < 1e-10
    data['resources'] = {'nice': os.getpriority(os.PRIO_PROCESS, 0),
                         'python_threads': threading.active_count(),
                         'elapsed_seconds': time.monotonic()-START,
                         'max_rss_bytes_macos': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    assert data['resources']['max_rss_bytes_macos'] < 1024**3
    assert data['resources']['elapsed_seconds'] < 240
    (ROOT/'audit_data.json').write_text(json.dumps(data, indent=2)+'\n')
    print('PASS: C2,1 nonquadratic entropy/second-moment scaling and fluctuation identities', flush=True)
    print('Resources: '+json.dumps(data['resources'], sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
