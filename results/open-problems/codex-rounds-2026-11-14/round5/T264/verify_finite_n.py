"""Small standard-library audits for PROOF.md; no minimizers are computed.

Run with --prior-only to audit the predecessor before the extension.
All file output is in this script's directory. Every network checked below
is an explicit feasible competitor, not an optimizer supplied by a grid.
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
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
signal.alarm(90)
started = time.monotonic()
ROOT = Path(__file__).resolve().parent
assert Path.cwd().resolve() == ROOT
rng = random.Random(26405)
pi = math.pi


def dot(x, y):
    return math.fsum(a*b for a, b in zip(x, y))


def normalized(x):
    r = math.sqrt(dot(x, x))
    return tuple(a/r for a in x)


def unit(d):
    return normalized(tuple(rng.gauss(0, 1) for _ in range(d)))


def relu(x):
    return max(0., x)


def value(atoms, x):
    return math.fsum(c*relu(dot(u, x)) for c, u in atoms)


def risk(atoms, d):
    terms = []
    for c, u in atoms:
        for h, v in atoms:
            co = min(1., max(-1., dot(u, v)))
            beta = math.acos(co)
            terms.append(c*h*(math.sin(beta)+(pi-beta)*co)/(2*pi*d))
    return math.fsum(terms)


def circle(atoms, count=32768):
    return math.fsum(value(atoms, (math.cos(2*pi*(i+.5)/count),
                                   math.sin(2*pi*(i+.5)/count)))**2
                     for i in range(count))/count


def inverse(matrix):
    n = len(matrix)
    a = [list(row)+[float(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for j in range(n):
        p = max(range(j, n), key=lambda i: abs(a[i][j]))
        a[j], a[p] = a[p], a[j]
        assert abs(a[j][j]) > 1e-12
        denom = a[j][j]
        a[j] = [x/denom for x in a[j]]
        for i in range(n):
            if i != j:
                t = a[i][j]
                a[i] = [x-t*y for x, y in zip(a[i], a[j])]
    return [row[n:] for row in a]


def mv(matrix, x):
    return [dot(row, x) for row in matrix]


def triangular_solve(matrix, rhs):
    n = len(rhs)
    out = [0.]*n
    for i in reversed(range(n)):
        out[i] = (rhs[i]-math.fsum(matrix[i][j]*out[j]
                                 for j in range(i+1, n)))/matrix[i][i]
    return out


def audit_prior():
    maximum = 0.
    for theta in (1e-5, .01, .4):
        a, b = math.cos(theta/2), math.sin(theta/2)
        for tau in (-1, 1):
            v = (b, -a)
            if tau == -1:
                C, D = a/b, (1+b)/a
                atoms = [(1., (a, b)), (-C, v), (-D, (-b, a))]
                formula = (1+C*C+D*D)/4-(C+D)/(2*pi)
            else:
                W = ((1-b)/a, 1.)
                L = math.hypot(*W)
                C = (1-b)/(a*b)
                atoms = [(L, normalized(W)), (-C, v)]
                beta = math.acos(-math.sqrt((1-b)/2))
                formula = (L*L+C*C)/4-L*C*(math.sin(beta)
                           +(pi-beta)*math.cos(beta))/(2*pi)
            for x, y in (((a, b), 1), ((a, -b), -1), ((0., 1.), tau)):
                assert abs(value(atoms, x)-y) < 2e-10
            direct = circle([(theta*c, u) for c, u in atoms])
            err = abs(direct/(theta*theta*formula)-1)
            maximum = max(maximum, err)
            assert err < 2e-8
            if theta == 1e-5:
                assert abs(direct-1) < 2e-5
    count = 0
    for d in (2, 3, 7):
        for theta in (1e-5, .05, .4):
            a, b = math.cos(theta/2), math.sin(theta/2)
            for u in [unit(d) for _ in range(500)]:
                g = (relu(a*u[0]+b*u[1])-relu(a*u[0]-b*u[1]))/math.sin(theta)
                for t in (-1, 1):
                    lhs = math.fsum((x-(t if i == 1 else 0))**2
                                    for i, x in enumerate(u))
                    assert lhs <= 4*(1-a*t*g)+2e-10
                    count += 1
    print(f'PASS prior: actual circle quadrature vs exact risk; max relative error {maximum:.3g}')
    print(f'PASS prior: mass inequality in {count} signed ambient directions')
    return {'circle_max_relative_error': maximum, 'signed_directions': count}


def planar_basis(z):
    ratios = [x[0]/x[1] for x in z]
    assert all(ratios[i] < ratios[i+1] for i in range(len(z)-1))
    knots = [(x+y)/2 for x, y in zip(ratios, ratios[1:])]+[ratios[-1]+1]
    d = len(z[0])
    u = [normalized((-1., t)+(0.,)*(d-2)) for t in knots]
    matrix = [[relu(dot(v, x)) for v in u] for x in z]
    for i in range(len(z)):
        assert matrix[i][i] > 0
        for j in range(i):
            assert matrix[i][j] == 0
        for j, t in enumerate(knots):
            formula = z[i][1]*relu(t-ratios[i])/math.sqrt(1+t*t)
            assert abs(matrix[i][j]-formula) < 1e-15
    return u, matrix


def general_basis(z, attempts=2000):
    # Select independent columns without an optimization package.
    directions, echelon = [], []
    for _ in range(attempts):
        u = list(unit(len(z[0])))
        u[0] = -abs(u[0])
        col = [relu(dot(u, x)) for x in z]
        for pivot, basis in echelon:
            t = col[pivot]
            col = [x-t*y for x, y in zip(col, basis)]
        pivot = max(range(len(z)), key=lambda i: abs(col[i]))
        if abs(col[pivot]) <= 1e-9:
            continue
        denom = col[pivot]
        echelon.append((pivot, [x/denom for x in col]))
        directions.append(tuple(u))
        if len(directions) == len(z):
            break
    matrix = [[relu(dot(u, x)) for u in directions] for x in z]
    return directions, matrix


def make_configuration(d, k):
    z = []
    for i in range(k):
        ratio = -1.4+2.8*(i+.5)/k
        if d == 2:
            z.append(normalized((ratio, 1.)))
        else:
            h = .15+.2*rng.random()
            other = unit(d-2)
            q = math.sqrt((1-h*h)/(1+ratio*ratio))
            z.append((ratio*q, q)+tuple(h*v for v in other))
    return z


def audit_configuration(z, directions, matrix, name):
    d, k = len(z[0]), len(z)
    inv = inverse(matrix)
    for i, row in enumerate(matrix):
        for j in range(k):
            assert abs(dot(row, [inv[t][j] for t in range(k)])-(i == j)) < 1e-9
    B = math.fsum(abs(x) for row in inv for x in row)
    H = 2.5
    K = 2+B*(H+2)
    delta = min(x[1] for x in z)
    margin = min(-u[0] for u in directions)
    theta_max = min(.01, delta/2, margin)
    labels = [(-H, 0., H)[i % 3] for i in range(k)]
    rows = []
    for theta in (theta_max, theta_max*1e-3, theta_max*1e-6):
        a, b = math.cos(theta/2), math.sin(theta/2)
        x1, x2 = (a, b)+(0.,)*(d-2), (a, -b)+(0.,)*(d-2)
        e1, v = (1.,)+(0.,)*(d-1), (b, -a)+(0.,)*(d-2)
        rhs = [y-relu(x[0])/a for x, y in zip(z, labels)]
        coeff = mv(inv, rhs)
        if name.startswith('triangular'):
            second = triangular_solve(matrix, rhs)
            assert max(abs(c-h) for c, h in zip(coeff, second)) < 1e-8
        assert math.fsum(abs(c) for c in coeff) <= B*(H+2)
        for u in directions:
            assert dot(u, x1) < 0 and dot(u, x2) < 0
        assert all(dot(v, x) < 0 for x in z)
        atoms = [(1/a, e1), (-1/(a*b), v)]+list(zip(coeff, directions))
        cost = math.fsum(abs(c) for c, u in atoms)
        assert cost <= 2/math.sin(theta)+K+1e-6
        U = 2*theta/math.sin(theta)+K*theta
        gap = K*theta+(theta/b)*2*math.sin(theta/4)**2/a
        E = 2*math.sqrt(U*gap)
        bound = (1+1/delta)*E+theta*H/delta+U-2
        for sign in (1, -1):
            def reflect(x):
                return tuple(sign*v if j == 1 else v for j, v in enumerate(x))
            aa = [(sign*c, reflect(u)) for c, u in atoms]
            zz = [reflect(x) for x in z]
            interpolation = max(abs(value(aa, x)-y) for x, y in
                                [(x1, 1.), (x2, -1.)]
                                +list(zip(zz, [sign*y for y in labels])))
            assert interpolation < 1e-8
            tests = [unit(d) for _ in range(60)]+[x1, x2]+zz
            actual = max(abs(theta*value(aa, x)+2*sign*relu(-sign*x[1])) for x in tests)
            assert actual <= bound+1e-10
            scaled = [(theta*c, u) for c, u in aa]
            R = risk(scaled, d)
            assert max(0, math.sqrt(2/d)-bound)**2-1e-10 <= R
            assert R <= (math.sqrt(2/d)+bound)**2+1e-10
            if theta == theta_max*1e-6:
                assert abs(R-2/d) < 2e-4
            rows.append({'configuration': name, 'd': d, 'n': k+2,
                         'theta': theta, 'hemisphere': sign,
                         'inverse_entry_sum': B, 'K': K,
                         'interpolation_error': interpolation,
                         'sampled_uniform_error': actual, 'proved_error_bound': bound,
                         'theta_squared_risk': R})
        if theta == theta_max and name == 'triangular_d2_n6':
            direct = circle([(theta*c, u) for c, u in atoms], 65536)
            exact = risk([(theta*c, u) for c, u in atoms], 2)
            assert abs(direct/exact-1) < 2e-7
            print(f'PASS independent circle integral: {direct:.12g}, kernel {exact:.12g}')
        if theta == theta_max and name == 'tied_ratios_d3_n5':
            nz, np = 128, 512
            scaled = [(theta*c, u) for c, u in atoms]
            def surface():
                for j in range(nz):
                    alt = -1+2*(j+.5)/nz
                    rad = math.sqrt(1-alt*alt)
                    for h in range(np):
                        phi = 2*pi*(h+.5)/np
                        x = (rad*math.cos(phi), rad*math.sin(phi), alt)
                        yield value(scaled, x)**2
            direct = math.fsum(surface())/(nz*np)
            exact = risk(scaled, 3)
            assert abs(direct/exact-1) < 2e-4
            print(f'PASS independent off-plane surface integral: {direct:.12g}, kernel {exact:.12g}')
    last = rows[-1]
    print(f"PASS {name}: smallest theta={last['theta']:.3g}, theta^2 R={last['theta_squared_risk']:.12g}, limit={2/d:.12g}")
    return rows


def simpson(f, left, right, steps=512):
    h = (right-left)/steps
    return h/3*(f(left)+f(right)+math.fsum((4 if i % 2 else 2)*f(left+i*h)
                                        for i in range(1, steps)))


def audit_probability():
    records = []
    integrals = {0: pi, 1: 2.}
    for m in range(2, 6):
        integrals[m] = (m-1)/m*integrals[m-2]
    for n in range(3, 11):
        k = n-2
        signs = list(itertools.product((-1, 1), repeat=k))
        same = sum(len(set(s)) == 1 for s in signs)/len(signs)
        opposite_labels = sum(x != y for x, y in itertools.product((-1, 1), repeat=2))/4
        joint = same*opposite_labels
        assert joint == 2.**(2-n)
        for d in range(2, 8):
            alpha = (d-1)/2
            C = math.gamma(d/2)/(math.sqrt(pi)*math.gamma((d-1)/2))
            assert abs(C*integrals[d-2]-1) < 2e-15
            constant = 2.**(2-n)*C/(d-1)*(2/d)**alpha
            # Separate event enumeration and cap integration.
            t = 1e8
            cutoff = math.sqrt((2/d)/t)
            cap = simpson(lambda th: math.sin(th)**(d-2)/integrals[d-2], 0, cutoff)
            numerical = joint*cap*t**alpha
            assert abs(numerical/constant-1) < 2e-7
            if d == 2:
                assert abs(constant/(2.**(2-n)/pi)-1) < 1e-15
            if d == 3:
                assert abs(constant/(2.**(2-n)/6)-1) < 1e-15
            if n == 3:
                assert abs(constant/(C/(2*(d-1))*(2/d)**alpha)-1) < 1e-15
            # An endpoint angular shell has scale-invariant mass.
            endpoint = (d-1)/2
            exponent = d-2-2*endpoint
            assert exponent == -1
            shell = simpson(lambda u: math.exp((exponent+1)*u), -8., -7.)
            assert abs(shell-1) < 1e-15
            records.append({'n': n, 'd': d, 'joint_sign_probability': joint,
                            'tail_lower_constant': constant,
                            'independent_cap_constant': numerical})
    print('PASS probability: sign enumeration, sine recurrence, cap integrals, endpoint shells; n=3..10, d=2..7')
    return records


data = {'prior': audit_prior()}
if '--prior-only' not in sys.argv:
    rows = []
    for d in (2, 3, 7):
        for n in (3, 4, 6, 10):
            z = make_configuration(d, n-2)
            u, matrix = planar_basis(z)
            rows.extend(audit_configuration(z, u, matrix, f'triangular_d{d}_n{n}'))
    tied = [(0., .8, .6), (0., .8, -.6), (.4, .8, math.sqrt(.2))]
    u, matrix = general_basis(tied)
    assert len(u) == len(tied)
    assert all(math.isclose(dot(z, z), 1., abs_tol=1e-14) for z in tied)
    rows.extend(audit_configuration(tied, u, matrix, 'tied_ratios_d3_n5'))
    # Duplicated observations cannot have independent response rows.
    u, matrix = general_basis([tied[0], tied[0]], attempts=100)
    assert len(u) == 1
    print('PASS negative check: duplicated points produce rank one, not two')
    data['feasible_networks'] = rows
    data['probability'] = audit_probability()
    print(f"PASS extension: {len(rows)} feasible networks; maximum interpolation error {max(r['interpolation_error'] for r in rows):.3g}")

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss if sys.platform == 'darwin' else 1024*rss
assert rss_bytes < 1_000_000_000
data['resources'] = {'seconds': time.monotonic()-started, 'peak_rss_bytes': rss_bytes,
                     'nice': os.getpriority(os.PRIO_PROCESS, 0), 'threads': 1}
destination = 'prior_data.json' if '--prior-only' in sys.argv else 'verification_data.json'
(ROOT/destination).write_text(json.dumps(data, indent=2)+'\n')
print('All assertions passed.')
print('Resources:', data['resources'])
