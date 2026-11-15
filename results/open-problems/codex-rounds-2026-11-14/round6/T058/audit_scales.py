"""Independent exact and log-space audits; no random graphs or large arrays."""

import json
import math
import os
import resource
import signal
import time
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(1150)
started = time.monotonic()
ell = math.log(2)


def e(k):
    return k*(k-1)//2


def log_fraction(value):
    assert value > 0
    return math.log(value.numerator)-math.log(value.denominator)


def at_phase(exponent, phase):
    with localcontext() as ctx:
        ctx.prec = 140
        d_ell = Decimal(2).ln()
        L = Decimal(exponent)*d_ell
        C = 1+d_ell.ln()
        target = int(2/d_ell*(L-L.ln()+C)-1)+Decimal(phase)
        for _ in range(15):
            L -= (2/d_ell*(L-L.ln()+C)-1-target)/(2/d_ell*(1-1/L))
        assert abs(2/d_ell*(L-L.ln()+C)-1-target) < Decimal('1e-110')
        n = int(L.exp().to_integral_value())
        actual = 2/d_ell*(Decimal(n).ln()-Decimal(n).ln().ln()+C)-1
        return n, int(actual), str(actual-int(actual))


def lse(values):
    maximum = max(values)
    return maximum+math.log(math.fsum(math.exp(x-maximum) for x in values))


def floating(L, k):
    log_mu = k*L-math.lgamma(k+1)-ell*e(k)
    h = []
    for j in range(1, k):
        r = k-j
        h.append(math.lgamma(k+1)-math.lgamma(j+1)-math.lgamma(r+1)
                 +r*L-math.lgamma(r+1)-ell*(e(k)-e(j)))
    return {'log10_Delta': (log_mu+lse(h[1:])-ell)/math.log(10),
            'log10_EY_over_sqrt_mu': (.5*log_mu+lse(h)-ell)/math.log(10),
            'log10_variance_bound_over_mu': (log_mu+2*math.log(k)-L)/math.log(10)}


def exact(exponent, phase):
    n, k, actual = at_phase(exponent, phase)
    N = math.comb(n, k)
    q = Fraction(1, 2**e(k))
    mu = N*q
    direct = [math.comb(k, j)*math.comb(n-k, k-j) for j in range(k+1)]
    # Independent hypergeometric recurrence from its opposite endpoint.
    descending = [0]*(k+1)
    descending[k] = 1
    for j in range(k, 0, -1):
        value, remainder = divmod(descending[j]*j*(n-2*k+j), (k-j+1)**2)
        assert remainder == 0
        descending[j-1] = value
    assert descending == direct and sum(direct) == N
    conditional = [Fraction(direct[j], 2**(e(k)-e(j))) for j in range(k+1)]
    Delta = mu*sum(conditional[2:k])/2
    EY = mu*sum(conditional[1:k])/2
    # Exact audits of the convexity-based bounds used in the proof.
    m, mp = k//2, (k+1)//2
    A = Fraction(k*k, n-k)
    v2, vm = 2*A*A, A**m*2**e(m)
    B = Fraction(k*n, 2**k)
    w1, wmp = 2*B, B**mp*2**(mp*(mp+1)//2)
    assert vm <= v2 and wmp <= w1
    assert sum(conditional[2:m+1]) <= mu*m*v2
    assert sum(conditional[m+1:k]) <= mp*w1
    Delta_bound = mu*(mu*m*v2+mp*w1)/2
    assert Delta <= Delta_bound
    # Exact one-vertex contribution and independent incidence count.
    EY1 = mu*conditional[1]/2
    common_vertex = Fraction(n*math.comb(n-1, k-1)*math.comb(n-k, k-1), 2)*q*q
    assert EY1 == common_vertex
    leading = mu*mu*Fraction(k*k, 2*n)
    ratio = Fraction(math.comb(n-k, k-1), math.comb(n-1, k-1))
    assert EY1 == leading*ratio
    assert 1-Fraction((k-1)**2, n-k+1) <= ratio <= 1
    normalized_var_bound = mu*Fraction(k*k, n)
    R = N-1-math.comb(n-k, k)
    exact_pair_variance_bound = N*q*q*(1-q)*R
    assert exact_pair_variance_bound <= mu*normalized_var_bound
    values = {'log10_Delta': log_fraction(Delta)/math.log(10),
              'log10_EY_over_sqrt_mu': (log_fraction(EY)-.5*log_fraction(mu))/math.log(10),
              'log10_variance_bound_over_mu': log_fraction(normalized_var_bound)/math.log(10)}
    independently = floating(math.log(n), k)
    errors = {key: abs(values[key]-independently[key]) for key in values}
    assert max(errors.values()) < 2e-7
    return {'log2_n': math.log2(n), 'phase': actual, 'k': k, **values,
            'log10_Delta_bound': log_fraction(Delta_bound)/math.log(10),
            'log_space_comparison_errors': errors}


rows = [exact(exponent, phase) for exponent in (80, 160, 320)
        for phase in ('.5', '.75', '.875')]
extended = []
for exponent in (640, 1280, 2560):
    for phase in (.75, .875):
        def f(u):
            return 2*u-2*math.log2(u)+2/ell-1
        target = math.floor(f(exponent))+phase
        u = float(exponent)
        for _ in range(8):
            u -= (f(u)-target)/(2-2/(ell*u))
        extended.append({'log2_n': u, 'phase': phase, 'k': math.floor(target),
                         **floating(u*ell, math.floor(target))})
result = {'status': 'all exact overlap and independent log-space audits passed',
          'nice': os.getpriority(os.PRIO_PROCESS, 0), 'exact_checks': rows,
          'floating_diagnostics': extended, 'elapsed_seconds': time.monotonic()-started,
          'peak_rss_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
assert result['elapsed_seconds'] < 1200
assert result['peak_rss_bytes'] < 1_000_000_000
Path('scale_audit.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
