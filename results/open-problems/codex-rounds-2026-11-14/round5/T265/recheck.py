#!/usr/bin/env python3
"""Independent checks of round 4's explicit norm and descent certificates."""
import json
import math
import os
import resource
import signal
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from pathlib import Path

assert os.environ.get('OMP_NUM_THREADS') == '1'
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 15, priority
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
signal.alarm(60)


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def q(t):
    return (-t, Q(1))


def rho(z):
    return max(Q(0), z)


def cone(x, t, h):
    if x[0] == 0:
        return Q(0)
    return abs(x[0])*max(Q(0), 1-abs(x[1]/x[0]-t)/h)


xs = [(Q(1), Q(0)), (Q(1), Q(3))]
ys = [Q(1), Q(-1)]
v = tuple(sum(y*x[k] for x, y in zip(xs, ys))/2 for k in range(2))
ts = [x[1]/x[0] for x in xs]
amps = [(y-dot(v, x))/abs(x[0]) for x, y in zip(xs, ys)]
assert v == (0, Q(-3, 2)) and amps == [1, Q(7, 2)]


def attaining_representation(h):
    # lambda is a linear coefficient on the nonunit vector q(r).
    # The allocation is deliberately different for the two widths.
    allocation = {(0, 0): Q(-3, 2)} if h == Q(1, 8) else {
        (0, -1): Q(-1, 4), (0, 0): Q(-1), (0, 1): Q(-1, 4)}
    neurons = []
    groups = []
    supplied_linear = [Q(0), Q(0)]
    for i, (t, amp) in enumerate(zip(ts, amps)):
        for offset, mult in [(-1, 1), (0, -2), (1, 1)]:
            r = t+offset*h
            even = amp*mult/(2*h)
            odd = allocation.get((i, offset), Q(0))
            assert abs(odd) <= abs(even)
            for k in range(2):
                supplied_linear[k] += odd*q(r)[k]
            neurons.extend([(even+odd, q(r)),
                            (even-odd, tuple(-z for z in q(r)))])
            groups.append((r, even))
    assert tuple(supplied_linear) == v
    return neurons, groups


identities = jumps = 0
norm_rows = []
with localcontext() as ctx:
    ctx.prec = 70
    for h, expected in [(Q(1, 8), 386.3134673380746), (Q(1), 49.22147835683593)]:
        neurons, groups = attaining_representation(h)
        path = math.fsum(abs(float(a))*math.hypot(*map(float, w)) for a, w in neurons)
        # Independent high-precision sum of the forced gradient-jump norms.
        forced = sum(2*abs(Decimal(e.numerator)/Decimal(e.denominator))
                     * (Decimal(1)+(Decimal(r.numerator)/Decimal(r.denominator))**2).sqrt()
                     for r, e in groups)
        assert abs(path-float(forced)) < 1e-12
        assert abs(path-expected) < 1e-12
        points = xs + [(Q(u), Q(z, 7)) for u in [-2, -1, 0, 1, 3]
                       for z in range(-14, 15)]
        for x in points:
            actual = sum(a*rho(dot(w, x)) for a, w in neurons)
            wanted = dot(v, x)+sum(a*cone(x, t, h) for a, t in zip(amps, ts))
            assert actual == wanted
            identities += 1
        for x, y in zip(xs, ys):
            assert sum(a*rho(dot(w, x)) for a, w in neurons) == y
        # Recover jumps by evaluating gradients on opposite sides of each line.
        for r, even in groups:
            gap = min(abs(r-other) for other, _ in groups if other != r)/4
            gradients = []
            for z in [r-gap, r+gap]:
                x = (Q(1), z)
                gradients.append(tuple(sum(a*w[k] for a, w in neurons if dot(w, x)>0)
                                       for k in range(2)))
            jump = tuple(b-a for a, b in zip(*gradients))
            assert jump == tuple(2*even*z for z in q(r))
            jumps += 1
        norm_rows.append(dict(h=str(h), neuron_path_cost=path,
                              forced_jump_norm_sum_decimal=str(forced),
                              exact_baseline_allocation=True))

assert 4*sum(abs(a) for a in amps)/Q(1, 8) == 144
assert 4*amps[0]*2+4*amps[1]*5+3 == 81
assert 144 > 81

# Recheck the balanced displayed-realization descent by two derivatives.
derivative_checks = 0
for t in [-5., -.25, 0., .25, 3.]:
    for h in [1/8, 1/2, 2.]:
        # Differentiate each original neuron's |a| ||w|| contribution.
        direct = 0.
        for off, coeff in [(-1, 1), (0, -2), (1, 1)]:
            r = t+off*h
            ell = math.hypot(1., r)
            # Factor two accounts for the paired orientations.
            direct += abs(coeff)*(-ell/h**2 + r*off/(h*ell))
        # Independently differentiate the three-term closed cost formula.
        lm, lc, lp = [math.hypot(1., z) for z in [t-h, t, t+h]]
        formula = ((-(t-h)/lm+(t+h)/lp)/h
                   -(lm+2*lc+lp)/h**2)
        assert math.isclose(direct, formula, rel_tol=1e-12, abs_tol=1e-12)
        assert direct <= -2*lc/h**2+1e-11
        derivative_checks += 1

result = dict(earlier_result_holds=True, exact_score_checks=identities,
              exact_gradient_jumps=jumps, norms=norm_rows,
              exact_coarse_bounds=[144, 81], descent_derivative_checks=derivative_checks,
              niceness=priority, max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path(__file__).with_name('recheck_results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
