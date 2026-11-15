#!/usr/bin/env python3
"""Small deterministic checks of the finite-step remainder theorem."""
import json
import math
import os
from pathlib import Path
import resource
import threading
import time
from fractions import Fraction as Q

START = time.monotonic()
ROOT = Path(__file__).resolve().parent
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert threading.active_count() == 1
resource.setrlimit(resource.RLIMIT_CPU, (120, 120))


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def trace(a):
    return a[0][0] + a[1][1]


def det(a):
    return a[0][0]*a[1][1] - a[0][1]*a[1][0]


def matrix_power(a, n):
    b = [[1, 0], [0, 1]]
    for _ in range(n):
        b = mm(a, b)
    return b


def quad(a, x):
    return sum(x[i]*a[i][j]*x[j] for i in range(2) for j in range(2))


def difference(a, b, factor=1):
    return [[factor*(a[i][j]-b[i][j]) for j in range(2)] for i in range(2)]


def direct_leapfrog(x, p, h, n, lam):
    for _ in range(n):
        p -= h*lam*x/2
        x += h*p
        p -= h*lam*x/2
    return x, p


def rational_audit():
    rows = []
    for h, lam, n in [(Q(1, 7), Q(3, 2), 7),
                       (Q(1, 5), Q(2, 3), 9),
                       (Q(1, 2), Q(3), 3)]:
        a = h*h*lam/4
        c = [[1-h*h*lam/2, h], [-h*lam*(1-a), 1-h*h*lam/2]]
        b = matrix_power(c, n)
        inv = [[lam*(1-a), 0], [0, 1]]
        physical = [[lam, 0], [0, 1]]
        assert mm(mm(transpose(b), inv), b) == inv
        assert det(b) == 1
        dmat = difference(mm(mm(transpose(b), physical), b), physical, Q(1, 2))
        cov = [[1/lam, 0], [0, 1]]
        dcov = mm(dmat, cov)
        mu = trace(dcov)
        mu_alt = a*a*lam*b[0][1]**2/2
        var = 2*trace(mm(dcov, dcov))
        assert mu == mu_alt
        assert var == 2*mu + 2*mu*mu
        assert det([[1+2*dcov[0][0], 2*dcov[0][1]],
                    [2*dcov[1][0], 1+2*dcov[1][1]]]) == 1
        for x, p in [(Q(2, 5), Q(-3, 4)), (Q(-7, 3), Q(1, 8))]:
            xn, pn = direct_leapfrog(x, p, h, n, lam)
            assert [xn, pn] == [b[0][0]*x+b[0][1]*p, b[1][0]*x+b[1][1]*p]
            dh = (lam*(xn*xn-x*x)+pn*pn-p*p)/2
            assert dh == a*lam*(xn*xn-x*x)/2
        var_a = 2*(lam/12)**2 + 2*(lam*lam/24)**2/(lam*lam)
        assert var_a == 5*lam*lam/288
        rows.append({'h': str(h), 'lambda': str(lam), 'n': n,
                     'mean_energy_error': str(mu),
                     'variance_energy_error': str(var),
                     'variance_A_over_lambda_squared': str(var_a/(lam*lam)),
                     'exact_checks': 'invariant, determinant, direct iteration, two means, variance, exponential identity'})
    return rows


def previous_identity_audit(n):
    # Asymmetric non-Gaussian scalar target; 0.45 <= V'' <= 1.55.
    # Integrate out momentum by its exact second and fourth moments.
    dx = 24/n
    terms = [[] for _ in range(8)]
    for j in range(n+1):
        x = -12 + j*dx
        v = x*x/2 + 0.3*(1-math.cos(x)) + 0.25*(math.sin(x)-x)
        g = x + 0.3*math.sin(x) + 0.25*(math.cos(x)-1)
        k = 1 + 0.3*math.cos(x) - 0.25*math.sin(x)
        weight = (1 if j in (0, n) else 4 if j % 2 else 2)*math.exp(-v)
        s = g*g
        ca = k/12-s/24
        ca2 = k*k/48-k*s/144+s*s/576
        for target, value in zip(terms, [1, ca, ca2, k*k, g*g*k, s, s*s, k]):
            target.append(weight*value)
    vals = [math.fsum(t)/math.fsum(terms[0]) for t in terms]
    _, ea, ea2, ek2, egkg, es, es2, ek = vals
    direct = ea2-ea*ea
    identity = (12*ek2-4*egkg+(es2-es*es))/576
    assert abs(direct-identity) < 1e-12
    assert abs(es-ek) < 1e-12
    assert ek2/72 <= direct <= ek2/48
    return {'grid_intervals': n, 'box': [-12, 12],
            'variance_A_direct': direct, 'variance_A_identity': identity,
            'identity_residual': direct-identity,
            'ibp_residual': es-ek, 'proved_interval': [ek2/72, ek2/48]}


def remainder_block(h, n, lam):
    a = h*h*lam/4
    r = math.sqrt(1-a)
    phi = 2*n*math.asin(h*math.sqrt(lam)/2)
    tau = n*h*math.sqrt(lam)
    v = [math.cos(phi), math.sin(phi)/r]
    w = [math.cos(tau), math.sin(tau)]
    e = [[a*(v[i]*v[j]-w[i]*w[j])/2 for j in range(2)] for i in range(2)]
    return e, a*a*math.sin(phi)**2/(2*(1-a)), phi


def opnorm_symmetric(e):
    mid = trace(e)/2
    spread = math.hypot((e[0][0]-e[1][1])/2, e[0][1])
    return max(abs(mid+spread), abs(mid-spread))


def finite_step_audit():
    rows = []
    max_norm_ratio = 0
    max_pointwise_error = 0
    max_mean_error = 0
    for lam in (0.25, 1.0, 1.7, 4.0):
        for n in (1, 2, 7, 16, 31):
            for T in (0.3, 1.0, math.pi, 6.0):
                h = T/n
                if h*math.sqrt(lam) > 1:
                    continue
                e, mu, phi = remainder_block(h, n, lam)
                bound = h**4*lam**2*(1+T*math.sqrt(lam))/8
                norm = opnorm_symmetric(e)
                max_norm_ratio = max(max_norm_ratio, norm/bound)
                assert norm <= bound*(1+1e-10)
                for x, p in ((0.7, -1.1), (-1.3, 0.2)):
                    xn, pn = direct_leapfrog(x, p, h, n, lam)
                    tau = T*math.sqrt(lam)
                    xt = x*math.cos(tau)+p*math.sin(tau)/math.sqrt(lam)
                    pt = p*math.cos(tau)-x*math.sqrt(lam)*math.sin(tau)
                    a0 = lam*p*p/12-lam*lam*x*x/24
                    at = lam*pt*pt/12-lam*lam*xt*xt/24
                    dh = (lam*(xn*xn-x*x)+pn*pn-p*p)/2
                    residual = dh-h*h*(a0-at)-quad(e, (math.sqrt(lam)*x, p))
                    max_pointwise_error = max(max_pointwise_error, abs(residual))
                    assert abs(residual) < 1e-11
                eta = h*math.sqrt(lam)
                c = [[1-eta*eta/2, eta], [-eta*(1-eta*eta/4), 1-eta*eta/2]]
                bp = matrix_power(c, n)
                raw = mm(transpose(bp), bp)
                mu_from_entropy = (trace(raw)-2)/2-math.log(det(bp))
                max_mean_error = max(max_mean_error, abs(mu-mu_from_entropy))
                assert abs(mu-mu_from_entropy) < 1e-12
                assert abs(mu-trace(e)) < 1e-12
                rows.append({'lambda': lam, 'n': n, 'T': T, 'mu': mu,
                             'matrix_norm_over_bound': norm/bound})
    return {'cases': len(rows), 'max_matrix_norm_over_bound': max_norm_ratio,
            'max_pointwise_residual': max_pointwise_error,
            'max_mean_vs_entropy_residual': max_mean_error, 'rows': rows}


def critical_audit():
    rows = []
    for n in (4, 8, 16, 32, 64, 128, 256):
        # d=n^4 is represented only by a scalar; no d-dimensional array.
        h, d = 1/n, n**4
        e, mu_one, phi = remainder_block(h, n, 1)
        mu = d*mu_one
        var_r = 2*d*trace(mm(e, e))
        a = h*h/4
        w = [math.cos(1), math.sin(1)]
        leading = [[a*(w[i]*w[j]-(1 if i == j == 0 else 0))/2
                    for j in range(2)] for i in range(2)]
        exact_energy = [[leading[i][j]+e[i][j] for j in range(2)] for i in range(2)]
        var_dh = 2*d*trace(mm(exact_energy, exact_energy))
        var_dh_alt = d*(2*mu_one+2*mu_one*mu_one)
        assert abs(var_dh-var_dh_alt) < 1e-12
        rows.append({'n': n, 'd': d, 'h': h, 'mean_R': mu,
                     'sd_R': math.sqrt(var_r),
                     'mean_limit': math.sin(1)**2/32,
                     'variance_energy_error': var_dh,
                     'variance_limit': math.sin(1)**2/16})
    assert abs(rows[-1]['mean_R']-rows[-1]['mean_limit']) < 2e-7
    assert rows[-1]['sd_R'] < rows[0]['sd_R']/1000
    # Resonance: the positive-limit conclusion must exclude T in pi Z.
    resonant = []
    for n in (8, 32, 128):
        h = math.pi/n
        d = max(1, round(h**-4))
        _, mu_one, _ = remainder_block(h, n, 1)
        resonant.append({'n': n, 'd': d, 'mean_R': d*mu_one})
    assert resonant[-1]['mean_R'] < resonant[0]['mean_R']/1000
    return {'nonresonant': rows, 'resonant_T_pi': resonant}


def main():
    data = {'rational_audit': rational_audit(),
            'earlier_identity': [previous_identity_audit(4096), previous_identity_audit(8192)],
            'finite_step': finite_step_audit(), 'critical_scale': critical_audit()}
    assert abs(data['earlier_identity'][0]['variance_A_direct']-
               data['earlier_identity'][1]['variance_A_direct']) < 1e-13
    data['resources'] = {'nice': os.getpriority(os.PRIO_PROCESS, 0),
                         'python_threads': threading.active_count(),
                         'elapsed_seconds': time.monotonic()-START,
                         'max_rss_bytes_macos': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    assert data['resources']['max_rss_bytes_macos'] < 1024**3
    assert data['resources']['elapsed_seconds'] < 120
    (ROOT/'audit_data.json').write_text(json.dumps(data, indent=2)+'\n')
    print('PASS: earlier variance identity by independent asymmetric 1D quadrature')
    print('  max residual:', max(abs(r['identity_residual']) for r in data['earlier_identity']))
    print('PASS: exact rational invariant, direct leapfrog, two drift formulas, energy variance, exponential identity')
    f = data['finite_step']
    print('PASS: finite-step matrix theorem in', f['cases'], 'cases')
    print('  max pointwise residual:', f['max_pointwise_residual'])
    print('  max drift/entropy residual:', f['max_mean_vs_entropy_residual'])
    print('  max operator norm / proved bound:', f['max_matrix_norm_over_bound'])
    print('Critical scale T=1, h=1/n, d=n^4:')
    print('n d mean_R sd_R variance_DeltaH')
    for row in data['critical_scale']['nonresonant']:
        print(row['n'], row['d'], f"{row['mean_R']:.12g}", f"{row['sd_R']:.6g}",
              f"{row['variance_energy_error']:.12g}")
    print('mean limit:', math.sin(1)**2/32)
    print('PASS: T=pi resonance tends to zero; positive-limit exception checked')
    print('Resources:', json.dumps(data['resources']))


if __name__ == '__main__':
    main()
