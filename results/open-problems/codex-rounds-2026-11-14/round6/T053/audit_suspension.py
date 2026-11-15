"""Independent finite checks of the collision suspension; no Lorentz simulation.
Run: OMP_NUM_THREADS=1 nice -n 15 python3 audit_suspension.py
"""
from fractions import Fraction as F
import math
import os
import resource
import sys
import time

started = time.monotonic()
assert os.environ.get('OMP_NUM_THREADS') == '1'
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 15
print('nice', priority)

E = (F(1), F(0))
N = (F(0), F(1))
W = (F(-1), F(0))
S = (F(0), F(-1))
Q = (F(-3, 5), F(4, 5))
cycles = (
    ((F(1), F(3)), (E, W)),
    ((F(1, 2), F(1, 2), F(1, 2), F(3, 2)), (E, N, Q, S)),
    ((F(3, 7),), ((F(3, 5), F(4, 5)),)),
)


def dot(u, v):
    return sum((a*b for a, b in zip(u, v)), F(0))


def epochs(gaps):
    out = []
    t = F(0)
    for gap in gaps:
        out.append(t)
        t += gap
    return out


def state_at(gaps, t):
    """Locate a time phase in a physical period, without a Palm law."""
    phase = t % sum(gaps)
    for i, (a, gap) in enumerate(zip(epochs(gaps), gaps)):
        if a <= phase < a+gap:
            return i, phase-a
    raise AssertionError('uncovered phase')


def direct_correlation(gaps, velocities, t):
    """Integrate over one time period, split at all physical breakpoints."""
    period = sum(gaps)
    cuts = {F(0), period}
    for e in epochs(gaps):
        cuts.add(e)
        cuts.add((e-t) % period)
    cuts = sorted(cuts)
    total = F(0)
    for a, b in zip(cuts, cuts[1:]):
        phase = (a+b)/2
        i, _ = state_at(gaps, phase)
        j, _ = state_at(gaps, phase+t)
        total += (b-a)*dot(velocities[i], velocities[j])
    return total/period


def collision_overlap(gaps, velocities, t, initial):
    """Integrate the age overlaps in equation (11), starting at one event."""
    m = len(gaps)
    ell0 = gaps[initial]
    left = F(0)
    total = mass = F(0)
    limit = int((t+ell0)/min(gaps))+3
    for n in range(limit):
        j = (initial+n) % m
        right = left+gaps[j]
        overlap = max(F(0), min(ell0, right-t)-max(F(0), left-t))
        total += overlap*dot(velocities[initial], velocities[j])
        mass += overlap
        left = right
        if left >= t+ell0:
            break
    assert mass == ell0, (gaps, t, mass, ell0)
    return total


checks = 0
observation_times = tuple(map(F, (0, 1, 4, 13))) + (F(1, 7), F(1, 2), F(5, 4), F(17, 3))
for gaps, velocities in cycles:
    assert all(g > 0 for g in gaps)
    assert all(dot(v, v) == 1 for v in velocities)
    m, period = len(gaps), sum(gaps)
    intensity = F(m)/period
    # Explicit pushforward of the uniform event law, with arbitrary mark tests.
    for power in range(4):
        lhs = sum((F(((i+1) % m)+1)**power for i in range(m)), F(0))/m
        rhs = sum((F(i+1)**power for i in range(m)), F(0))/m
        assert lhs == rhs
    assert intensity*sum(gaps)/m == 1
    for t in observation_times:
        direct = direct_correlation(gaps, velocities, t)
        palm = sum((collision_overlap(gaps, velocities, t, i)
                    for i in range(m)), F(0))/m
        assert direct == intensity*palm, (gaps, t, direct, intensity*palm)
        checks += 1
    # Direct time-phase age integration versus length-weighted event sampling.
    for power in (0, 1, 2, 3):
        direct_age = sum((g**(power+1)/(power+1) for g in gaps), F(0))/period
        from_suspension = intensity*sum((g**(power+1)/(power+1)
                                         for g in gaps), F(0))/m
        assert direct_age == from_suspension
    for t in observation_times:
        direct_residual = sum((max(F(0), g-t) for g in gaps), F(0))/period
        from_palm = intensity*sum((max(F(0), g-t) for g in gaps), F(0))/m
        assert direct_residual == from_palm
print('exact time-phase correlation vs collision overlaps: %d cases PASS' % checks)
print('event-shift, roof normalization, age moments, residual waiting law: PASS')

# Nonergodic volume mixtures need intensity-biased component probabilities at events.
mixture_checks = 0
wrong_mixture_gap = F(0)
for weights in ((F(2, 5), F(3, 5)), (F(1, 2), F(1, 2))):
    intensities = tuple(F(len(g))/sum(g) for g, _ in cycles[:2])
    gamma = sum((q*rho for q, rho in zip(weights, intensities)), F(0))
    event_weights = tuple(q*rho/gamma for q, rho in zip(weights, intensities))
    assert sum(event_weights) == 1
    assert gamma*sum((p*sum(g)/len(g) for p, (g, _) in
                      zip(event_weights, cycles[:2])), F(0)) == 1
    for t in observation_times:
        direct = sum((q*direct_correlation(g, v, t)
                      for q, (g, v) in zip(weights, cycles[:2])), F(0))
        suspension = gamma*sum((p*sum((collision_overlap(g, v, t, i)
                                for i in range(len(g))), F(0))/len(g)
                                for p, (g, v) in zip(event_weights, cycles[:2])), F(0))
        assert direct == suspension
        mixture_checks += 1
        wrong = gamma*sum((q*sum((collision_overlap(g, v, t, i)
                           for i in range(len(g))), F(0))/len(g)
                           for q, (g, v) in zip(weights, cycles[:2])), F(0))
        wrong_mixture_gap = max(wrong_mixture_gap, abs(wrong-direct))
    print('mixture volume weights=%s, intensity=%s, event weights=%s' %
          (weights, gamma, event_weights))
assert wrong_mixture_gap > 0
print('exact nonergodic mixture correlations: %d cases PASS' % mixture_checks)
print('negative control, using volume weights at events: discrepancy %s (caught)' %
      wrong_mixture_gap)

# Endpoint cancellation checked independently on finite windows of periodic events.
for gaps, _ in cycles:
    period, m = sum(gaps), len(gaps)
    marks = tuple(F(i*i+1) for i in range(m))
    for phase in (F(1, 11), F(2, 7), F(3, 2)):
        for window in (F(1, 9), F(11, 4), F(23, 3)):
            events = []
            for k in range(-2, 25):
                for i, e in enumerate(epochs(gaps)):
                    if 0 < e+k*period-phase <= window:
                        events.append((e+k*period, i))
            events.sort()
            difference = sum((marks[(i+1) % m]-marks[i]
                              for _, i in events), F(0))
            endpoint = (marks[(events[-1][1]+1) % m]-marks[events[0][1]]
                        if events else F(0))
            assert difference == endpoint
            assert abs(difference) <= 2*max(map(abs, marks))
print('finite-window endpoint cancellation: PASS')


def direct_laplace(gaps, velocities, z):
    """C is piecewise linear and periodic; integrate it over one period."""
    period = sum(gaps)
    points = epochs(gaps)
    cuts = sorted({F(0), period} | {(b-a) % period for a in points for b in points})
    total = 0.0
    for a, b in zip(cuts, cuts[1:]):
        ca = float(direct_correlation(gaps, velocities, a))
        cb = float(direct_correlation(gaps, velocities, b))
        # Independently verify the linear time segment with rational samples.
        exact_a = direct_correlation(gaps, velocities, a)
        exact_b = direct_correlation(gaps, velocities, b)
        for fraction in (F(1, 4), F(1, 2), F(3, 4)):
            actual = direct_correlation(gaps, velocities, a+fraction*(b-a))
            assert actual == exact_a+fraction*(exact_b-exact_a)
        h = float(b-a)
        slope = (cb-ca)/h
        x = z*h
        integral_constant = -math.expm1(-x)/z
        integral_linear = (-math.expm1(-x)-x*math.exp(-x))/(z*z)
        total += math.exp(-z*float(a))*(ca*integral_constant+slope*integral_linear)
    return total/(-math.expm1(-z*float(period)))


def collision_laplace(gaps, velocities, z, constant_velocity=False, nmax=None):
    """Equation (14), with a certified tail for truncation at N."""
    m, period = len(gaps), float(sum(gaps))
    intensity = m/period
    if nmax is None:
        nmax = math.ceil(45/(z*float(min(gaps))))+1
    diagonal_terms, off_terms, tail_terms = [], [], []
    for i, ell in enumerate(gaps):
        ell0 = float(ell)
        b0 = -math.expm1(-z*ell0)
        diagonal_terms.append(ell0/z-b0/(z*z))
        H = 0.0
        local_terms = []
        for n in range(1, nmax+1):
            j = (i+n) % m
            bn = -math.expm1(-z*float(gaps[j]))
            product = 1.0 if constant_velocity else float(dot(velocities[i], velocities[j]))
            local_terms.append(product*b0*math.exp(-z*H)*bn/(z*z))
            H += float(gaps[j])
        off_terms.append(math.fsum(local_terms))
        tail_terms.append(b0*math.exp(-z*H)/(z*z))
    result = intensity*(math.fsum(diagonal_terms)+math.fsum(off_terms))/m
    tail = intensity*math.fsum(tail_terms)/m
    return result, tail


max_laplace_error = max_ballistic_error = max_tail = 0.0
for gaps, velocities in cycles:
    for z in (0.1, 0.7, 2.3):
        direct = direct_laplace(gaps, velocities, z)
        series, tail = collision_laplace(gaps, velocities, z)
        error = abs(direct-series)
        assert error <= tail+2e-11, (gaps, z, direct, series, tail)
        assert abs(series) <= 1/z+2e-11
        ballistic, ballistic_tail = collision_laplace(gaps, velocities, z, True)
        assert abs(ballistic-1/z) <= ballistic_tail+2e-11
        max_laplace_error = max(max_laplace_error, error)
        max_ballistic_error = max(max_ballistic_error, abs(ballistic-1/z))
        max_tail = max(max_tail, tail, ballistic_tail)
        for cutoff in (1, 2, 7):
            partial, partial_tail = collision_laplace(gaps, velocities, z, nmax=cutoff)
            assert abs(direct-partial) <= partial_tail+2e-11
print('finite-index Laplace tail bounds at N=1,2,7: 27 checks PASS')
print('Laplace series vs direct periodic piecewise-linear integral: max error %.3g' %
      max_laplace_error)
print('constant-velocity Laplace 1/z: max error %.3g; largest tail bound %.3g' %
      (max_ballistic_error, max_tail))

# A wrong first off-diagonal exponent, containing ell0, must be detectable.
gaps, _ = cycles[0]
z = 0.7
ell0, ell1 = map(float, gaps)
correct = (-math.expm1(-z*ell0))*(-math.expm1(-z*ell1))/(z*z)
wrong = correct*math.exp(-z*ell0)
assert abs(correct-wrong) > 0.1
print('negative control, including first roof in intervening exponent: caught')

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if sys.platform != 'darwin':
    rss *= 1024
elapsed = time.monotonic()-started
assert rss < 1024**3
assert elapsed < 20*60
print('peak resident bytes', rss)
print('PASS; elapsed %.3f seconds' % elapsed)
