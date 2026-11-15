#!/usr/bin/env python3
"""Exact primal/dual and polygon audits for the norm formula and comparison."""
import itertools
import json
import math
import os
import resource
import signal
from fractions import Fraction as Q
from pathlib import Path

assert os.environ.get('OMP_NUM_THREADS') == '1'
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 15, priority
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
signal.alarm(60)


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def add(x, y):
    return tuple(a+b for a, b in zip(x, y))


def scale(t, x):
    return tuple(t*a for a in x)


def sub(x, y):
    return add(x, scale(-1, y))


def vector_sum(vectors, d):
    return tuple(sum(v[j] for v in vectors) for j in range(d))


def evaluate(neurons, x):
    return sum(a*max(Q(0), dot(w, x)) for a, w in neurons)


def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower, upper = [], []
    for chain, order in [(lower, points), (upper, list(reversed(points)))]:
        for p in order:
            while len(chain) >= 2 and cross(chain[-2], chain[-1], p) <= 0:
                chain.pop()
            chain.append(p)
    return lower[:-1]+upper[:-1]


def distance_squared_polygon(v, vertices):
    poly = hull(vertices)
    if len(poly) == 1:
        return dot(sub(v, poly[0]), sub(v, poly[0]))
    edges = list(zip(poly, poly[1:]+poly[:1]))
    if len(poly) >= 3 and all(cross(a, b, v) >= 0 for a, b in edges):
        return Q(0)
    distances = []
    for a, b in edges:
        e = sub(b, a)
        t = min(Q(1), max(Q(0), dot(sub(v, a), e)/dot(e, e)))
        residual = sub(v, add(a, scale(t, e)))
        distances.append(dot(residual, residual))
    return min(distances)


def validate_normals(us):
    assert all(dot(u, u) == 1 for u in us)
    for i, u in enumerate(us):
        if any(abs(dot(u, w)) == 1 for w in us[:i]):
            raise ValueError('merge coincident unoriented normals first')


normals2 = [(Q(1), Q(0)), (Q(0), Q(1)), (Q(3, 5), Q(4, 5)),
            (Q(5, 13), Q(-12, 13))]
ys2 = [(Q(a), Q(b)) for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
ys2 += [(Q(3, 5), Q(4, 5)), (Q(-4, 5), Q(3, 5)),
        (Q(5, 13), Q(-12, 13)), (Q(12, 13), Q(5, 13))]
normals3 = [(Q(1), Q(0), Q(0)), (Q(0), Q(1), Q(0)),
            (Q(3, 5), Q(0), Q(4, 5)), (Q(0), Q(3, 5), Q(4, 5))]
ys3 = [(Q(1), Q(0), Q(0)), (Q(0), Q(1), Q(0)), (Q(0), Q(0), Q(1)),
       (Q(0), Q(0), Q(-1)), (Q(3, 5), Q(0), Q(4, 5)),
       (Q(4, 5), Q(0), Q(-3, 5))]
beta_sets = [[Q(1), Q(-2), Q(3, 2), Q(-1, 3)],
             [Q(-1, 3), Q(1, 5), Q(-7, 4), Q(2)],
             [Q(1, 10**8), Q(-1), Q(3), Q(-2)]]

formula_cases = polygon_cases = identities = split_representations = 0
for us, ys in [(normals2, ys2), (normals3, ys3),
               ([(Q(1), Q(0), Q(0)), (Q(0), Q(1), Q(0))], ys3)]:
    validate_normals(us)
    d, k = len(us[0]), len(us)
    for raw_betas in beta_sets:
        betas = raw_betas[:k]
        for y, lam in itertools.product(ys, [Q(0), Q(1, 7), Q(3)]):
            assert dot(y, y) == 1
            ts = []
            for u, beta in zip(us, betas):
                product = dot(u, y)
                ts.append(abs(beta)*(1 if product > 0 else -1 if product < 0 else Q(1, 3)))
            z = vector_sum([scale(t, u) for t, u in zip(ts, us)], d)
            v = add(z, scale(lam, y))
            neurons = []
            for u, beta, t in zip(us, betas, ts):
                neurons.extend([(beta+t, u), (beta-t, scale(-1, u))])
            neurons.extend([(lam, y), (-lam, scale(-1, y))])
            expected = 2*sum(abs(b) for b in betas)+2*lam
            # Every first-layer weight here is unit, so the cost is rational.
            cost = sum(abs(a) for a, _ in neurons)
            dual = 2*sum(abs(b) for b in betas)+2*(
                dot(v, y)-sum(abs(b)*abs(dot(u, y)) for b, u in zip(betas, us)))
            assert cost == dual == expected
            points = list(itertools.product([Q(-1), Q(0), Q(2, 3)], repeat=d))
            for x in points:
                target = dot(v, x)+sum(b*abs(dot(u, x)) for b, u in zip(betas, us))
                assert evaluate(neurons, x) == target
                identities += 1
            # Reparameterize each neuron and split it into three copies.
            transformed = [(a/6, scale(2, w)) for a, w in neurons for _ in range(3)]
            assert sum(2*abs(a) for a, _ in transformed) == cost
            for x in points[:4]:
                assert evaluate(transformed, x) == evaluate(neurons, x)
                split_representations += 1
            if d == 2:
                vertices = [vector_sum([scale(sign*abs(b), u)
                                       for sign, b, u in zip(signs, betas, us)], d)
                            for signs in itertools.product([-1, 1], repeat=k)]
                assert distance_squared_polygon(v, vertices) == lam*lam
                polygon_cases += 1
            formula_cases += 1

# Interior points, including a pure linear score and rank-one zonotopes.
edge_cases = 0
for v in [(Q(0), Q(0)), (Q(1, 4), Q(0)), (Q(3), Q(0)),
          (Q(1, 2), Q(7, 3)), (Q(-3), Q(4))]:
    clipped = (min(Q(1), max(Q(-1), v[0])), Q(0))
    expected2 = dot(sub(v, clipped), sub(v, clipped))
    assert distance_squared_polygon(v, [(Q(-1), Q(0)), (Q(1), Q(0))]) == expected2
    edge_cases += 1
assert distance_squared_polygon((Q(3), Q(4)), [(Q(0), Q(0))]) == 25
edge_cases += 1

# Coincident hyperplanes must be merged; an unmerged formula would be false.
rejected_duplicates = 0
for us in [[(Q(1), Q(0)), (Q(1), Q(0))],
           [(Q(1), Q(0)), (Q(-1), Q(0))]]:
    try:
        validate_normals(us)
    except ValueError:
        rejected_duplicates += 1
    else:
        raise AssertionError('duplicate normal accepted')

# x_1+|x_1| has norm two, not the naive additive value four.
for x in itertools.product([Q(-2), Q(0), Q(3)], repeat=2):
    assert 2*max(Q(0), x[0]) == x[0]+abs(x[0])

# Explicit interpolation comparison, audited with exact neuron gradients.
xs = [(Q(1), Q(0)), (Q(1), Q(3))]
labels = [Q(1), Q(-1)]
v = tuple(sum(y*x[j] for x, y in zip(xs, labels))/2 for j in range(2))
assert v == (0, Q(-3, 2))
slopes = [x[1]/x[0] for x in xs]
amplitudes = [(y-dot(v, x))/abs(x[0]) for x, y in zip(xs, labels)]
assert slopes == [0, 3] and amplitudes == [1, Q(7, 2)]
gradient_jumps = interpolation_points = 0
comparison = {}
for name, h in [('narrow', Q(1, 8)), ('wide', Q(1))]:
    ridges, three = [], [(Q(1), v), (Q(-1), scale(-1, v))]
    for t, a in zip(slopes, amplitudes):
        for r, coeff in [(t-h, 1), (t, -2), (t+h, 1)]:
            q = (-r, Q(1))
            gamma = a*coeff/(2*h)
            ridges.append((r, q, gamma))
            three.append((a*coeff/h, q))
    for x, y in zip(xs, labels):
        assert evaluate(three, x) == y
        interpolation_points += 1
    # A second minimal representation absorbs the baseline into existing pairs.
    linear_coeffs = {Q(0): Q(-3, 2)} if name == 'narrow' else {
        Q(-1): Q(-1, 4), Q(0): Q(-1), Q(1): Q(-1, 4)}
    absorbed = []
    odd_parts = []
    for r, q, gamma in ridges:
        t = linear_coeffs.get(r, Q(0))
        assert abs(t) <= abs(gamma)
        odd_parts.append(scale(t, q))
        absorbed.extend([(gamma+t, q), (gamma-t, scale(-1, q))])
    assert vector_sum(odd_parts, 2) == v
    for x in itertools.product([Q(-2), Q(0), Q(1), Q(7, 3)], repeat=2):
        assert evaluate(absorbed, x) == evaluate(three, x)
    # Gradient jumps of the three-hinge representation, not the cost formula.
    jump_norms = []
    for r, q, gamma in ridges:
        delta = min(abs(r-r0) for r0, _, _ in ridges if r0 != r)/4
        gradients = []
        for location in [r-delta, r+delta]:
            point = (Q(1), location)
            gradients.append(vector_sum([scale(a, w) for a, w in three
                                         if dot(w, point) > 0], 2))
        jump = sub(gradients[1], gradients[0])
        assert jump == scale(2*gamma, q)
        jump_norms.append(math.sqrt(float(dot(jump, jump))))
        gradient_jumps += 1
    c_formula = math.fsum(float(abs(a)/h)*(
        math.hypot(1, float(t-h))+2*math.hypot(1, float(t))
        +math.hypot(1, float(t+h))) for t, a in zip(slopes, amplitudes))
    c_jumps = math.fsum(jump_norms)
    c_absorbed = math.fsum(float(abs(a))*math.sqrt(float(dot(w, w))) for a, w in absorbed)
    assert math.isclose(c_formula, c_jumps, rel_tol=2e-15)
    assert math.isclose(c_formula, c_absorbed, rel_tol=2e-15)
    comparison[name] = dict(intrinsic_norm=c_formula, norm_from_gradient_jumps=c_jumps,
                            norm_of_absorbed_representation=c_absorbed,
                            interpolates=True)

lower = 4*sum(abs(a) for a in amplitudes)/Q(1, 8)
upper = sum(4*abs(a)*(1+abs(t)+1) for a, t in zip(amplitudes, slopes))+3
assert lower == 144 and upper == 81 and lower > upper
assert comparison['narrow']['intrinsic_norm'] >= float(lower)
assert comparison['wide']['intrinsic_norm'] <= float(upper)
comparison['exact_lower_narrow'] = str(lower)
comparison['exact_upper_wide'] = str(upper)
comparison['strict_threshold_from_upper'] = str(4*sum(abs(a) for a in amplitudes)/upper)

monotonic_checks = 0
for t in [-100., -3., -.5, 0., 2., 100.]:
    hs = [1e-6, 1e-3, .1, 1., 10., 1000.]
    costs = [(math.hypot(1, t-h)+2*math.hypot(1, t)+math.hypot(1, t+h))/h for h in hs]
    for left, right in zip(costs, costs[1:]):
        assert left > right
        monotonic_checks += 1

# Tangent of the balanced six-neuron realization, with all zero derivatives.
# Although balancing uses square roots, the score derivative can be written
# exactly using k=(d/dh)log(balance_factor), which is rational here.
local_descent_cases = exact_zero_subgradient_checks = widened_interpolations = 0
local_samples = [
    ([(Q(1), Q(0)), (Q(1), Q(3))], [Q(1), Q(-1)]),
    ([(Q(-2), Q(1)), (Q(1), Q(3))], [Q(-1), Q(1)]),
    ([(Q(1), Q(0)), (Q(-1), Q(1, 1000)), (Q(1), Q(1, 1000))],
     [Q(1), Q(1), Q(1)]),
    ([(Q(1), Q(-2), Q(3)), (Q(-2), Q(1), Q(4)), (Q(3), Q(2), Q(-1))],
     [Q(1), Q(-1), Q(-1)]),
]
for points, ys in local_samples:
    n, d = len(points), len(points[0])
    baseline = tuple(sum(y*x[j] for x, y in zip(points, ys))/n for j in range(d))
    ts = [x[1]/x[0] for x in points]
    hs = [min(Q(1, n**3), min(abs(t-s) for j, s in enumerate(ts) if i != j)/3)
          for i, t in enumerate(ts)]
    amps = [(y-dot(baseline, x))/abs(x[0]) for x, y in zip(points, ys)]
    for i, (t, h, amplitude) in enumerate(zip(ts, hs, amps)):
        if amplitude == 0:
            continue
        records = []
        objective_derivative = 0.
        for offset, coeff in [(-1, 1), (0, -2), (1, 1)]:
            r = t+offset*h
            for orientation in [-1, 1]:
                a0 = amplitude*coeff/(2*h)
                w = (orientation*(-r), Q(orientation))+tuple(Q(0) for _ in range(d-2))
                wp = (Q(-orientation*offset), Q(0))+tuple(Q(0) for _ in range(d-2))
                logarithmic_a = -1/h
                logarithmic_length = dot(w, wp)/dot(w, w)
                k = (logarithmic_a-logarithmic_length)/2
                records.append((a0, w, wp, logarithmic_a, k))
                objective_derivative += float(abs(a0))*math.sqrt(float(dot(w, w)))*float(
                    logarithmic_a+logarithmic_length)
        # Test all zero-preactivation slopes at 0, 1/3 and 1, exactly.
        for x, xi_zero in itertools.product(points, [Q(0), Q(1, 3), Q(1)]):
            derivative = Q(0)
            for a0, w, wp, logarithmic_a, k in records:
                preactivation = dot(w, x)
                xi = 1 if preactivation > 0 else 0 if preactivation < 0 else xi_zero
                corrected_wp = add(wp, scale(k, w))
                if preactivation == 0:
                    assert dot(corrected_wp, x) == 0
                derivative += a0*(logarithmic_a-k)*max(Q(0), preactivation)
                derivative += a0*xi*dot(corrected_wp, x)
            assert derivative == 0
            exact_zero_subgradient_checks += 1
        tf, hf, af = float(t), float(h), float(abs(amplitude))
        r_minus, r_plus = math.hypot(1, tf-hf), math.hypot(1, tf+hf)
        derivative_formula = af*((-(tf-hf)/r_minus+(tf+hf)/r_plus)/hf
            -(r_minus+2*math.hypot(1, tf)+r_plus)/hf**2)
        bound = -2*af*math.hypot(1, tf)/hf**2
        assert objective_derivative <= bound+1e-10*abs(bound) < 0
        assert math.isclose(objective_derivative, derivative_formula, rel_tol=2e-14)
        # Widen by a positive rational amount, preserving disjoint intervals.
        slack = min(abs(t-ts[j])-h-hs[j] for j in range(n) if j != i)
        increment = min(h/10, slack/4)
        assert increment > 0
        new_hs = hs.copy()
        new_hs[i] += increment
        for x, y in zip(points, ys):
            score = dot(baseline, x)
            for t0, h0, a0 in zip(ts, new_hs, amps):
                score += a0*sum(c*abs(x[1]-r*x[0])
                    for r, c in [(t0-h0, 1), (t0, -2), (t0+h0, 1)])/(2*h0)
            assert score == y
            widened_interpolations += 1
        local_descent_cases += 1

result = dict(exact_primal_dual_cases=formula_cases,
              independent_exact_polygon_distances=polygon_cases,
              exact_score_identities=identities,
              rescaled_split_score_checks=split_representations,
              degenerate_zonotope_cases=edge_cases,
              rejected_duplicate_normal_cases=rejected_duplicates,
              exact_gradient_jumps=gradient_jumps,
              exact_sample_interpolations=interpolation_points,
              monotonicity_checks=monotonic_checks,
              balanced_feasible_descent_cases=local_descent_cases,
              exact_tangent_subgradient_checks=exact_zero_subgradient_checks,
              exact_widened_interpolations=widened_interpolations,
              comparison=comparison, niceness=priority,
              max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path(__file__).with_name('audit_results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
