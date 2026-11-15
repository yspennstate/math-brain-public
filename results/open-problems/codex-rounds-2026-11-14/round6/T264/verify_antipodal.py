"""Independent scalar audits of the antipodal four-point theorem.

No numerical optimization or external libraries. Uses continuous dual pricing,
two independent circle integrals, and the explicit analytic risk formula.
"""
import itertools
import json
import math
import os
from pathlib import Path
import random
import resource
import signal
import sys
import time

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(90)
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
started = time.monotonic()
ROOT = Path(__file__).resolve().parent
assert Path.cwd().resolve() == ROOT
pi = math.pi
TAU = 2*pi
rng = random.Random(264061)


def dot(x, y):
    return math.fsum(a*b for a, b in zip(x, y))


def relu(t):
    return max(t, 0.)


def sin_difference(t):
    """t-sin(t), retaining relative precision on small activation arcs."""
    if abs(t) >= .1:
        return t-math.sin(t)
    return math.fsum((-1.)**k*t**(2*k+3)/math.factorial(2*k+3)
                     for k in range(9))


def s_minus_theta_c(theta):
    if theta >= .1:
        return math.sin(theta)-theta*math.cos(theta)
    # Independently integrate t*sin(t)'s Taylor series term by term.
    return math.fsum((-1.)**k*theta**(2*k+3)
                     /(math.factorial(2*k+1)*(2*k+3)) for k in range(9))


def construct(theta, A, B):
    a, b = math.cos(theta/2), math.sin(theta/2)
    s = 2*a*b
    X = ((a, b), (a, -b), (0., 1.), (0., -1.))
    u, v = (b, a), (-b, a)
    atoms = ((1/s, u), (A/a-1/s, v),
             (-1/s, (b, -a)), (B/a+1/s, (-b, -a)))
    lam = (1/(a*b), -1/(a*b), -1/a, 1/a)
    return X, atoms, lam


def actual_value(atoms, x):
    return math.fsum(c*relu(dot(u, x)) for c, u in atoms)


def clipped_value(theta, A, B, x):
    a, b = math.cos(theta/2), math.sin(theta/2)
    t, z = x
    if t*z == 0:
        base = 0.
    else:
        base = math.copysign(min(abs(t)/a, abs(z)/b), t*z)
    return base+A/a*relu(-b*t+a*z)+B/a*relu(-b*t-a*z)


def cuts_for(directions):
    cuts = {0., TAU}
    for u in directions:
        phi = math.atan2(u[1], u[0])
        cuts.update(((phi-pi/2) % TAU, (phi+pi/2) % TAU))
    return sorted(cuts)


def continuous_price(X, lam):
    """All boundaries and all stationary directions on each activation arc."""
    cuts = cuts_for(X)
    candidates = list(cuts)
    for lo, hi in zip(cuts, cuts[1:]):
        mid = (lo+hi)/2
        direction = (math.cos(mid), math.sin(mid))
        active = [i for i, x in enumerate(X) if dot(x, direction) > 0]
        slope = tuple(math.fsum(lam[i]*X[i][k] for i in active)
                      for k in range(2))
        phi = math.atan2(slope[1], slope[0]) % TAU
        for stationary in (phi, (phi+pi) % TAU):
            if lo <= stationary <= hi:
                candidates.append(stationary)
    return max(abs(math.fsum(t*relu(dot(x, (math.cos(phi), math.sin(phi))))
                              for x, t in zip(X, lam))) for phi in candidates)


def solve(matrix, rhs):
    n = len(rhs)
    aug = [list(row)+[r] for row, r in zip(matrix, rhs)]
    for k in range(n):
        pivot = max(range(k, n), key=lambda j: abs(aug[j][k]))
        aug[k], aug[pivot] = aug[pivot], aug[k]
        denom = aug[k][k]
        assert abs(denom) > 1e-15
        aug[k] = [x/denom for x in aug[k]]
        for i in range(n):
            if i != k:
                factor = aug[i][k]
                aug[i] = [x-factor*y for x, y in zip(aug[i], aug[k])]
    return tuple(row[-1] for row in aug)


def arc_risk(atoms):
    """Integrate actual network's linear piece on every activation arc.

    Rotating into each arc's midpoint makes the integral a sum of positive
    terms, so no cancellation of O(theta^-2) risk terms is needed.
    """
    cuts = cuts_for([u for _, u in atoms])
    pieces = []
    for lo, hi in zip(cuts, cuts[1:]):
        mid, half = (lo+hi)/2, (hi-lo)/2
        direction = (math.cos(mid), math.sin(mid))
        active = [(c, u) for c, u in atoms if dot(u, direction) > 0]
        slope = tuple(math.fsum(c*u[k] for c, u in active) for k in range(2))
        C = slope[0]*math.cos(mid)+slope[1]*math.sin(mid)
        D = -slope[0]*math.sin(mid)+slope[1]*math.cos(mid)
        ss = sin_difference(2*half)/2
        cc = 2*half-ss
        pieces.append(cc*C*C+ss*D*D)
    return math.fsum(pieces)/TAU


def split_simpson(theta, A, B, steps=192):
    # Independent integrand: the stable clipping identity, not summed slopes.
    _, atoms, _ = construct(theta, A, B)
    cuts = cuts_for([u for _, u in atoms])
    def fun(phi):
        return clipped_value(theta, A, B, (math.cos(phi), math.sin(phi)))**2
    total = []
    for lo, hi in zip(cuts, cuts[1:]):
        step = (hi-lo)/steps
        interior = math.fsum((4 if j % 2 else 2)*fun(lo+j*step)
                             for j in range(1, steps))
        total.append(step/3*(fun(lo)+fun(hi)+interior))
    return math.fsum(total)/TAU


def risk_formula(theta, A, B, d):
    a, b = math.cos(theta/2), math.sin(theta/2)
    s = math.sin(theta)
    remainder = s_minus_theta_c(theta)
    r0 = 1/(d*a*a)-4*remainder/(pi*d*s*s)
    return ((1+b*(B-A))*r0+(A*A+B*B)/(2*d*a*a)
            +A*B*remainder/(pi*d*a*a))


def base_quadrant_formula(theta, d):
    h = theta/2
    a, b = math.cos(h), math.sin(h)
    # h-ab = (theta-sin(theta))/2, with its own small-angle series.
    first = sin_difference(theta)/(2*b*b)
    second = (pi/2-h-a*b)/(a*a)
    return 2/(pi*d)*(first+second)


rows = []
max_price_error = max_risk_error = max_interp = max_atom_error = 0.
for theta in (1e-4, .02, .2, .9, 1.3, 2.8):
    a, b = math.cos(theta/2), math.sin(theta/2)
    X, atoms, lam = construct(theta, 0., 0.)
    price = continuous_price(X, lam)
    max_price_error = max(max_price_error, abs(price-1))
    assert abs(price-1) < 3e-10
    # Recover dual multipliers from exposed-atom equations, not the formula.
    matrix = [[relu(dot(u, x)) for x in X] for _, u in atoms]
    recovered = solve(matrix, (1., -1., -1., 1.))
    assert max(abs(x-y)/max(1., abs(y)) for x, y in zip(recovered, lam)) < 1e-11
    for A, B in itertools.product((-2.5, -1., 0., 1., 2.5), repeat=2):
        if A > 1/(2*b) or B < -1/(2*b):
            continue
        X, atoms, lam = construct(theta, A, B)
        labels = (1., -1., A, B)
        interpolation = max(abs(actual_value(atoms, x)-y) for x, y in zip(X, labels))
        max_interp = max(max_interp, interpolation)
        assert interpolation < 1e-10
        cost = math.fsum(abs(c) for c, _ in atoms)
        formula_cost = 4/math.sin(theta)+(B-A)/a
        dual = dot(lam, labels)
        assert abs(cost-formula_cost) < 1e-10*max(1., cost)
        assert abs(cost-dual) < 1e-10*max(1., cost)
        odd_vector = tuple(math.fsum(c*u[k] for c, u in atoms) for k in range(2))
        expected_vector = (-b*(A+B)/a, A-B)
        assert max(abs(x-y) for x, y in zip(odd_vector, expected_vector)) < 1e-10
        # Directly compare four separate ReLUs against the clipping identity.
        for j in range(96):
            phi = TAU*(j+.3)/96
            x = (math.cos(phi), math.sin(phi))
            err = abs(actual_value(atoms, x)-clipped_value(theta, A, B, x))
            max_atom_error = max(max_atom_error, err)
            assert err < 1e-10
        direct = arc_risk(atoms)
        separate = split_simpson(theta, A, B)
        formula = risk_formula(theta, A, B, 2)
        odd_risk = dot(odd_vector, odd_vector)/8
        assert odd_risk <= formula+1e-10
        error = max(abs(direct-formula), abs(separate-formula))
        relative = error/max(1., abs(formula))
        max_risk_error = max(max_risk_error, relative)
        assert relative < 2e-9, (theta, A, B, direct, separate, formula)
        assert abs(base_quadrant_formula(theta, 2)-risk_formula(theta, 0, 0, 2)) < 2e-12
        rows.append({'theta': theta, 'A': A, 'B': B, 'cost': cost,
                     'dual': dual, 'interpolation_error': interpolation,
                     'risk_arc_d2': direct, 'risk_simpson_d2': separate,
                     'risk_formula_d2': formula, 'relative_error': relative})
print(f'PASS {len(rows)} exact cases: interpolation, signs, primal=dual, two circle integrals')
print(f'Maximum continuous-price error: {max_price_error:.3g}')
print(f'Maximum interpolation error: {max_interp:.3g}; atom/clipping error: {max_atom_error:.3g}')
print(f'Maximum normalized risk discrepancy: {max_risk_error:.3g}')

# Test full-dimensional directions without relying on planar equality arguments.
signed_directions = 0
for d in (2, 3, 7):
    for theta in (.002, .4, 1.7):
        X, atoms, lam = construct(theta, 0., 0.)
        a, b = math.cos(theta/2), math.sin(theta/2)
        for _ in range(500):
            raw = [rng.gauss(0, 1) for _ in range(d)]
            norm = math.sqrt(dot(raw, raw))
            r = tuple(x/norm for x in raw)
            planar = r[:2]
            actual = math.fsum(t*relu(dot(x, planar)) for x, t in zip(X, lam))
            independent = min(a*abs(r[0]), b*abs(r[1]))/(a*b)
            assert abs(abs(actual)-independent) < 1e-11
            assert abs(actual) <= 1+1e-11
            signed_directions += 2
print(f'PASS ambient dual and absolute-price identity: {signed_directions} signed directions')

# Label-boundary case: both correction totals vanish, recovering the old two-point minimum.
boundaries = []
for theta in (.01, .3, 1.1):
    b = math.sin(theta/2)
    A, B = 1/(2*b), -1/(2*b)
    X, atoms, lam = construct(theta, A, B)
    assert abs(atoms[1][0]) < 1e-12 and abs(atoms[3][0]) < 1e-12
    assert abs(math.fsum(abs(c) for c, _ in atoms)-2/math.sin(theta)) < 1e-11
    prior_risk = (pi-math.sin(theta)+theta*math.cos(theta))/(2*pi*math.sin(theta)**2)
    measured = risk_formula(theta, A, B, 2)
    assert abs(measured/prior_risk-1) < 1e-12
    boundaries.append({'theta': theta, 'A': A, 'B': B, 'risk': measured})
print('PASS sign boundaries: exact reduction to the earlier two-point cost and risk')

theta = .3
b, a = math.sin(theta/2), math.cos(theta/2)
A, B = 1/(2*b)+1, 0.
_, atoms, lam = construct(theta, A, B)
outside_gap = math.fsum(abs(c) for c, _ in atoms)-dot(lam, (1., -1., A, B))
assert abs(outside_gap-2/a) < 1e-12
assert atoms[1][0] > 0
print(f'PASS out-of-domain check: forbidden coefficient sign; cost exceeds displayed dual by {outside_gap:.12g}')

# Small-angle risk and its first correction, including every Rademacher label choice.
limits = []
for d in (2, 3, 7):
    for A, B in ((0., 0.), (-1., -1.), (-1., 1.), (1., -1.), (1., 1.), (2.5, -.7)):
        limit = (1+(A*A+B*B)/2)/d
        slope = ((B-A)/2-4/(3*pi))/d
        theta = 1e-6
        measured = risk_formula(theta, A, B, d)
        _, actual_atoms, _ = construct(theta, A, B)
        independent = arc_risk(actual_atoms)*2/d
        assert abs(independent-limit) < 4*theta
        assert abs(independent-measured) < 2e-8
        actual_cost = math.fsum(abs(c) for c, _ in actual_atoms)
        assert abs(theta*actual_cost-4) < 10*theta
        assert abs(measured-limit) < 4*theta
        assert abs((measured-limit)/theta-slope) < 4e-6
        limits.append({'d': d, 'A': A, 'B': B, 'theta': theta,
                       'risk': measured, 'independent_arc_risk': independent,
                       'limit': limit,
                       'measured_linear_correction': (measured-limit)/theta,
                       'predicted_linear_correction': slope})
print('PASS finite positive limits and first-order coefficient: 18 dimension/label cases')
for d in (2, 3, 7):
    row = next(r for r in limits if r['d'] == d and r['A'] == -1 and r['B'] == 1)
    print(f"d={d} theta={row['theta']:g} A=-1 B=1: R={row['risk']:.12g}, limit={row['limit']:.12g}")

# An actual S^2 surface integral checks the ambient 2/d planar-radius multiplier.
theta, A, B = .2, 1., -1.
nz, nphi = 128, 2048
def sphere_values():
    for j in range(nz):
        z = -1+2*(j+.5)/nz
        radius = math.sqrt(1-z*z)
        for k in range(nphi):
            phi = TAU*(k+.5)/nphi
            x = (radius*math.cos(phi), radius*math.sin(phi))
            yield clipped_value(theta, A, B, x)**2
surface = math.fsum(sphere_values())/(nz*nphi)
formula = risk_formula(theta, A, B, 3)
assert abs(surface/formula-1) < 6e-5, (surface, formula)
print(f'PASS independent S^2 surface risk: {surface:.12g}, formula {formula:.12g}')

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss if sys.platform == 'darwin' else 1024*rss
assert rss_bytes < 1_000_000_000
stats = {'seconds': time.monotonic()-started, 'peak_rss_bytes': rss_bytes,
         'nice': os.getpriority(os.PRIO_PROCESS, 0), 'threads': 1}
data = {'exact_cases': rows, 'limits': limits, 'boundary_checks': boundaries,
        'outside_domain_gap': outside_gap, 'signed_directions': signed_directions,
        'surface': {'actual': surface, 'formula': formula},
        'max_price_error': max_price_error, 'max_risk_error': max_risk_error,
        'max_interpolation_error': max_interp, 'max_atom_error': max_atom_error,
        'resources': stats}
(ROOT/'verification_data.json').write_text(json.dumps(data, indent=2)+'\n')
print('All assertions passed.')
print('Resources:', stats)
