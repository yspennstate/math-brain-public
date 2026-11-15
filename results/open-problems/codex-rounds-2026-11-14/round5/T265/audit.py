#!/usr/bin/env python3
"""Exact activation-cell checks, geometry audit, and KKT exception certificates."""
import itertools
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


def scale(s, x):
    return tuple(s*z for z in x)


def rho(z):
    return max(Q(0), z)


def q(t, d=2):
    return (-t, Q(1))+tuple(Q(0) for _ in range(d-2))


def D(u, xs, cs):
    return sum(c*rho(dot(u, x)) for c, x in zip(cs, xs))


def active_sum(u, xs, cs):
    return tuple(sum(c*x[k] for c, x in zip(cs, xs) if dot(u, x)>0)
                 for k in range(len(u)))


# Exhaust all nonempty orientation supports at the three forced lines.
# The relation used here is weaker than KKT: an edge and center may not
# share an orientation. Thus rejection cannot assume the desired sign rule.
supports = [{-1}, {1}, {-1, 1}]
survivors = []
rejected_supports = 0
for left, center, right in itertools.product(supports, repeat=3):
    if left & center or right & center:
        rejected_supports += 1
    else:
        survivors.append([sorted(left), sorted(center), sorted(right)])
assert rejected_supports == 25
assert survivors == [[[-1], [1], [-1]], [[1], [-1], [1]]]

# Check the cell-closure identity for a spanning set of signed multipliers,
# both input signs, either orientation, and dimensions beyond the plane.
closure_checks = zero_center_checks = 0
for d, t, h in itertools.product([2, 3, 5], [Q(-2), Q(0), Q(1, 3)],
                                  [Q(1, 8), Q(2)]):
    slopes = [t-4*h, t-2*h, t, t+2*h, t+5*h]
    xs = []
    for k, r in enumerate(slopes):
        U = Q((-1)**k*(k+1), k+2)
        xs.append((U, U*r)+tuple(Q(k-j, j+2) for j in range(d-2)))
    cs_list = [tuple(Q(int(i==j)) for i in range(5)) for j in range(5)]
    cs_list += [tuple(Q((-1)**i*(i+1), 7) for i in range(5))]
    for eps, off, cs in itertools.product([-1, 1], [-1, 1], cs_list):
        edge, center = scale(eps, q(t+off*h, d)), scale(eps, q(t, d))
        assert all(dot(edge, x) != 0 for x in xs)
        assert dot(center, xs[2]) == 0
        p = active_sum(edge, xs, cs)
        assert D(center, xs, cs) == dot(p, center)
        for xi in [Q(0), Q(1, 3), Q(1)]:
            # At the center only the central sample can change its derivative.
            p0 = tuple(sum(c*x[k]*(xi if dot(center, x)==0 else int(dot(center, x)>0))
                           for c, x in zip(cs, xs)) for k in range(d))
            assert dot(p0, center) == D(center, xs, cs)
            zero_center_checks += 1
        closure_checks += 1

# Independently compare dot products and angular distances. Decimal avoids
# loss of the tiny third-order defect at very small widths.
geometry_checks = angular_checks = symmetric_cases = 0
max_angular_discrepancy = 0.
with localcontext() as ctx:
    ctx.prec = 90
    for t, h in itertools.product([Q(-5), Q(-2), Q(-1, 3), Q(0), Q(1, 7), Q(1), Q(3)],
                                  [Q(1, 8), Q(1, 3), Q(2), Q(10), Q(1, 10**8)]):
        td = Decimal(t.numerator)/Decimal(t.denominator)
        hd = Decimal(h.numerator)/Decimal(h.denominator)
        lc = (1+td*td).sqrt()
        lm, lp = [(1+(td+off*hd)**2).sqrt() for off in [-1, 1]]
        left = (1+td*(td-hd))/(lc*lm)
        right = (1+td*(td+hd))/(lc*lp)
        defect = left-right
        determinant = hd*(1/lp-1/lm)
        # Exact independent difference of squared edge lengths.
        squared_gap = (t+h)**2-(t-h)**2
        assert squared_gap == 4*t*h
        assert (defect == 0) == (t == 0)
        assert (determinant == 0) == (t == 0)
        assert abs(left) < 1 and abs(right) < 1
        if t:
            assert defect*td < 0 and determinant*td < 0
        else:
            symmetric_cases += 1
        if h != Q(1, 10**8):
            tf, hf = float(t), float(h)
            independent = (math.cos(math.atan(tf)-math.atan(tf-hf))
                           -math.cos(math.atan(tf+hf)-math.atan(tf)))
            error = abs(independent-float(defect))
            assert error < 1e-14
            max_angular_discrepancy = max(max_angular_discrepancy, error)
            angular_checks += 1
        geometry_checks += 1

# A family of exact KKT certificates at the exceptional center. k=5 is
# the certificate printed in PROOF.md; the others independently stress it.
certificates = []
stationarity_vectors = margins = score_checks = 0
for k in range(5, 17):
    h = Q(2*k, k*k-1)
    L = Q(k*k+1, k*k-1)
    assert L*L == 1+h*h and 3*h*h < 1
    xs = [(Q(1), Q(0)), (-h*h/2, h/2), (h*h/4, -h/2)]
    ys = [1, 1, -1]
    multipliers = [2*h/L, 2/(h*L), 2/h]
    cs = [l*y for l, y in zip(multipliers, ys)]
    units = [(h/L, 1/L), (-h/L, 1/L), (Q(0), Q(-1))]
    coeffs = [L/h, L/h, -2/h]
    xi_zero = L/4
    assert 0 < xi_zero < 1
    assert all(l > 0 for l in multipliers)
    assert all(dot(u, u) == 1 for u in units)
    for j, (b, u) in enumerate(zip(coeffs, units)):
        s = 1 if b>0 else -1
        p = tuple(sum(c*x[a]*(xi_zero if dot(u, x)==0 else int(dot(u, x)>0))
                      for c, x in zip(cs, xs)) for a in range(2))
        assert p == scale(s, u)
        assert D(u, xs, cs) == s
        stationarity_vectors += 1
    for x, y in zip(xs, ys):
        assert sum(b*rho(dot(u, x)) for b, u in zip(coeffs, units)) == y
        margins += 1
    for U, V in itertools.product([Q(-2), Q(0), Q(1), Q(3, 2)],
                                   [Q(-1), Q(0), Q(1, 7), Q(2)]):
        x = (U, V)
        absolute_form = (abs(V+h*U)-2*abs(V)+abs(V-h*U))/(2*h)
        assert sum(b*rho(dot(u, x)) for b, u in zip(coeffs, units)) == 2*V/h+absolute_form
        score_checks += 1
    J = sum(abs(b) for b in coeffs)
    assert J == sum(multipliers) == 2*k
    if k == 5:
        assert h == Q(5, 12) and xi_zero == Q(13, 48)
        assert xs == [(1, 0), (Q(-25, 288), Q(5, 24)), (Q(25, 576), Q(-5, 24))]
        assert multipliers == [Q(10, 13), Q(288, 65), Q(24, 5)]
    certificates.append(dict(k=k, h=str(h), xi_zero=str(xi_zero),
                              J=str(J), multiplier_sum=str(sum(multipliers))))

result = dict(orientation_supports_enumerated=27, rejected_supports=rejected_supports,
              surviving_supports=survivors, exact_cell_closure_checks=closure_checks,
              exact_zero_derivative_checks=zero_center_checks,
              high_precision_geometry_checks=geometry_checks,
              independent_angle_checks=angular_checks, zero_center_exceptions=symmetric_cases,
              max_angle_discrepancy=max_angular_discrepancy,
              exact_KKT_certificates=certificates,
              exact_stationarity_vectors=stationarity_vectors, exact_margins=margins,
              exact_exception_score_checks=score_checks, niceness=priority,
              max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path(__file__).with_name('audit_results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
