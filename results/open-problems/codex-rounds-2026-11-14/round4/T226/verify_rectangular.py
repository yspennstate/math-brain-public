"""Exact audits and bounded finite probes for the enlarged zero-target basin.

Run with the command in LOG.md. Standard-library lists, one process, no workers.
Vectors are stored as columns, independently of the earlier row-based scripts.
"""
import json
import math
import os
import random
import resource
import signal
import sys
import time
from fractions import Fraction as Q
from pathlib import Path

started = time.monotonic()
assert os.environ.get('OMP_NUM_THREADS') == '1'
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 15, priority
signal.alarm(90)
soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
resource.setrlimit(resource.RLIMIT_CPU, (min(60, hard), hard))


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def transpose(a):
    return [list(row) for row in zip(*a)]


def product(a, b):
    return [[dot(row, col) for col in transpose(b)] for row in a]


def add(a, b, sign=1):
    return [[x+sign*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def identity(n, exact=False):
    return [[Q(i == j) if exact else float(i == j) for j in range(n)] for i in range(n)]


def det(a):
    a = [row[:] for row in a]
    result = 1
    for i in range(len(a)):
        piv = next((j for j in range(i, len(a)) if a[j][i] != 0), None)
        if piv is None:
            return 0
        if piv != i:
            a[i], a[piv] = a[piv], a[i]
            result = -result
        d = a[i][i]
        result *= d
        for j in range(i+1, len(a)):
            factor = a[j][i]/d
            for k in range(i+1, len(a)):
                a[j][k] -= factor*a[i][k]
            a[j][i] = 0
    return result


def inverse(a):
    n = len(a)
    b = [row[:] + ident for row, ident in zip(a, identity(n, True))]
    for i in range(n):
        piv = next(j for j in range(i, n) if b[j][i] != 0)
        b[i], b[piv] = b[piv], b[i]
        d = b[i][i]
        b[i] = [x/d for x in b[i]]
        for j in range(n):
            if i != j:
                factor = b[j][i]
                b[j] = [x-factor*y for x, y in zip(b[j], b[i])]
    return [row[n:] for row in b]


def mv(a, x):
    return [dot(row, x) for row in a]


def data(columns):
    a, *u = columns
    q = dot(a, a)
    c = [[dot(x, y) for y in u] for x in u]
    v = [dot(x, a) for x in u]
    hmat = [[x+(q if i == j else 0) for j, x in enumerate(row)] for i, row in enumerate(c)]
    return q, c, v, dot(v, v), hmat


def step(columns):
    # Evaluate the two layer gradients directly, using only column dot products.
    a, *u = columns
    residual = [dot(a, col) for col in u]
    ga = [sum(col[i]*r for col, r in zip(u, residual)) for i in range(len(a))]
    anew = [x-g for x, g in zip(a, ga)]
    unew = [[x-ai*r for x, ai in zip(col, a)] for col, r in zip(u, residual)]
    return [anew]+unew


def kblock(v):
    n = len(v)+1
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for j, x in enumerate(v, 1):
        ans[0][j] = ans[j][0] = x
    return ans


def gram(columns):
    return [[dot(x, y) for y in columns] for x in columns]


def corrected(columns):
    *_, v, h, hmat = data(columns)
    w = mv(inverse(hmat), v)
    z = transpose(columns)
    return product(z, add(identity(len(columns), True), kblock(w), -1)), w


def eigenvalues(a):
    # Cyclic-free Jacobi diagonalization for small symmetric matrices.
    a = [row[:] for row in a]
    n = len(a)
    if n == 1:
        return [a[0][0]]
    for _ in range(120*n*n):
        i, j = max(((i, j) for i in range(n) for j in range(i+1, n)), key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[i][j]) < 1e-14:
            return sorted(a[i][i] for i in range(n))
        theta = .5*math.atan2(2*a[i][j], a[j][j]-a[i][i])
        c, s = math.cos(theta), math.sin(theta)
        di, dj, off = a[i][i], a[j][j], a[i][j]
        for k in range(n):
            if k not in (i, j):
                x, y = a[k][i], a[k][j]
                a[k][i] = a[i][k] = c*x-s*y
                a[k][j] = a[j][k] = s*x+c*y
        a[i][i] = c*c*di-2*c*s*off+s*s*dj
        a[j][j] = s*s*di+2*c*s*off+c*c*dj
        a[i][j] = a[j][i] = 0.
    raise AssertionError('Jacobi iteration cap')


rng = random.Random(226202611150509)
exact_count = 0
for case in range(32):
    columns = [[Q(rng.randint(-5, 5), 7) for _ in range(4)] for _ in range(3)]
    if det(gram(columns)) == 0:
        continue
    nxt = step(columns)
    q, c, v, h, hh = data(columns)
    qn, cn, vn, hn, hhn = data(nxt)
    assert qn == q-2*h+dot(v, mv(c, v))
    assert cn == [[c[i][j]+(q-2)*v[i]*v[j] for j in range(2)] for i in range(2)]
    assert vn == [v[i]-dot(hh[i], v)+h*v[i] for i in range(2)]
    assert det(gram(nxt)) == det(gram(columns))*(1-h)**2
    # Independent first-round imbalance cancellation, via row outer products.
    a, *u = columns
    an, *un = nxt
    ga = [x-y for x, y in zip(a, an)]
    gw = [[x-y for x, y in zip(col, coln)] for col, coln in zip(u, un)]
    old_imb = [[sum(col[i]*col[j] for col in u)-a[i]*a[j] for j in range(4)] for i in range(4)]
    new_imb = [[sum(col[i]*col[j] for col in un)-an[i]*an[j] for j in range(4)] for i in range(4)]
    assert add(new_imb, old_imb, -1) == [[sum(col[i]*col[j] for col in gw)-ga[i]*ga[j] for j in range(4)] for i in range(4)]
    assert sum(dot(col, col) for col in nxt)-sum(dot(col, col) for col in columns) == -4*h+dot(ga, ga)+sum(dot(col, col) for col in gw)
    # Audit both new cancellation identities over exact rational arithmetic.
    ff, w = corrected(columns)
    ffn, wn = corrected(nxt)
    hinv, hninv = inverse(hh), inverse(hhn)
    left = [wn[i]-w[i]+v[i] for i in range(2)]
    right1 = mv(add(hninv, hinv, -1), v)
    right2 = mv(product(hninv, add(hhn, hh, -1)), v)
    right3 = mv(hninv, v)
    assert left == [x+y+h*z for x, y, z in zip(right1, right2, right3)]
    zz = transpose(columns)
    first = product(zz, kblock(left))
    second = product(product(zz, kblock(v)), kblock(wn))
    assert add(ffn, ff, -1) == add(second, first, -1)
    exact_count += 1
assert exact_count >= 30

# Scalar constants in the previous proofs, recomputed from their ingredients.
assert Q(3)*(1+Q(1, 128))+2 == Q(643, 128) < 6
assert 6*(1+Q(1, 64))**2 == Q(12675, 2048) < 8
assert Q(3, 2)*8+Q(1, 2) == Q(25, 2) < 13
assert 13*Q(1, 32) < 1
assert Q(1, 32)-2*Q(1, 128) == Q(1, 64)
assert Q(1, 64)/4 == Q(1, 256)
old_probability = math.exp(-72*(3-math.log(4)))
assert abs(old_probability/((4**72)*math.exp(-216))-1) < 2e-14

# Explicit supercritical endpoint: direct parameter update, not Gram recurrence.
m, d = 16, 8
columns = [[Q(0) for _ in range(m)] for _ in range(d+1)]
columns[0][0:2] = [Q(4, 3), Q(1, 3)]
columns[1][0:2] = [Q(52, 51), Q(47, 51)]
for j in range(2, d+1):
    columns[j][j] = Q(1, 2)
q0, c0, v0, h0, _ = data(columns)
assert q0 == c0[0][0] == Q(17, 9)
assert v0 == [Q(5, 3)]+[0]*(d-1)
assert h0 == Q(25, 9)
assert det(gram(columns)) > 0
endpoint = step(columns)
q1, c1, v1, h1, _ = data(endpoint)
assert q1 == c1[0][0] == Q(128, 81)
assert v1 == [0]*d and step(endpoint) == endpoint
sharpness = q1+c1[0][0]
assert sharpness == Q(256, 81) > 2
assert det(gram(endpoint)) > 0
# Independent Hessian action on an output-lifted eigenvector.
a, *u = endpoint
alpha = u[0]
vv = [[ai if j == 0 else Q(0) for ai in a] for j in range(d)]
jh = [dot(col, alpha)+dot(pert, a) for col, pert in zip(u, vv)]
ha = [sum(col[i]*x for col, x in zip(u, jh)) for i in range(m)]
hu = [[ai*x for ai in a] for x in jh]
assert ha == [sharpness*x for x in alpha]
assert hu == [[sharpness*x for x in col] for col in vv]
assert dot(alpha, alpha)+sum(dot(col, col) for col in vv) > 0
# Gram-form prediction independently checked against the full lifted Hessian.
assert jh == [sharpness]+[0]*(d-1)

# Rank-collapse exception really occurs inside the rectangle.
collapse = [[Q(1), Q(1, 2), Q(1, 2)], [Q(1), Q(-1, 2), Q(1, 2)]]
assert data(collapse)[0] == data(collapse)[1][0][0] == Q(3, 2)
assert data(collapse)[3] == 1 and det(gram(collapse)) > 0
collapse1 = step(collapse)
assert det(gram(collapse1)) == 0
assert step(collapse1) == [[0, 0, 0], [0, 0, 0]]

# Independent Jacobi diagnostic.
test_eigs = eigenvalues([[2., 1.], [1., 3.]])
assert abs(test_eigs[0]-(5-math.sqrt(5))/2) < 1e-12
assert abs(sum(test_eigs)-5) < 1e-12
assert abs(math.prod(test_eigs)-5) < 1e-12

starts = []
for case in range(24):
    m, d = (16, 8) if case < 16 else (5, 3)
    a = [rng.gauss(0, 1) for _ in range(m)]
    u = [[rng.gauss(0, 1) for _ in range(m)] for _ in range(d)]
    qwant = (1.1, 1.5, 1.9, 1.999)[case % 4]
    cwant = (1.8, 1.9, 1.5, 1.999)[case % 4]
    sa = math.sqrt(qwant/dot(a, a))
    sc = math.sqrt(cwant/max(eigenvalues(gram(u))))
    starts.append([[x*sa for x in a]]+[[x*sc for x in col] for col in u])
# Include h>1 with no exact residual kill, in the 144-parameter network.
m, d = 16, 8
special = [[0.]*m for _ in range(d+1)]
special[0][:2] = [1.2, .4]
special[1][:2] = [1.2, .2]
for j in range(2, d+1):
    special[j][j] = .5
assert data(special)[3] > 1
starts.append(special)
starts.append([[float(x) for x in col] for col in columns])

records = []
new_region = 0
max_residual = 0.
for case, start in enumerate(starts):
    z = [col[:] for col in start]
    qinit, cinit, vinit, hinit, _ = data(z)
    cmax = max(eigenvalues(cinit))
    assert qinit < 2 and cmax < 2 and det(gram(z)) > 0
    new_region += qinit+cmax >= 2
    sumh = 0.
    peak_h = 0.
    largest_corrected_increment_ratio = 0.
    loss_increases = 0
    updates = 0
    for iteration in range(5000):
        q, c, v, h, hh = data(z)
        sumh += h
        peak_h = max(peak_h, h)
        assert sumh <= qinit/(2-cmax)+1e-8
        if h < 1e-26:
            break
        zn = step(z)
        qn, cn, vn, hn, hhn = data(zn)
        assert qn <= q+1e-12 and q <= qinit+1e-12
        delta_c = add(cn, c, -1)
        assert max(eigenvalues(delta_c)) < 1e-12
        if hn > h*(1+1e-10):
            loss_increases += 1
        # Audit the exact corrected-frame difference in floating arithmetic.
        if iteration < 20:
            ft, w = corrected(z)
            fn, wn = corrected(zn)
            errvec = [v[i]+wn[i]-w[i] for i in range(len(v))]
            direct = add(fn, ft, -1)
            formula = add(product(product(transpose(z), kblock(v)), kblock(wn)), product(transpose(z), kblock(errvec)), -1)
            err = max(abs(x-y) for ar, br in zip(direct, formula) for x, y in zip(ar, br))
            assert err < 1e-10
            incnorm = math.sqrt(sum(dot(row, row) for row in direct))
            largest_corrected_increment_ratio = max(largest_corrected_increment_ratio, incnorm/h)
        z = zn
        updates += 1
    qf, cf, vf, hf, hhf = data(z)
    assert min(eigenvalues(gram(z))) > 0
    max_residual = max(max_residual, math.sqrt(hf))
    records.append({'case': case, 'm': len(z[0]), 'd': len(z)-1,
                    'initial_q': qinit, 'initial_cmax': cmax,
                    'initial_h': hinit, 'peak_h': peak_h,
                    'steps': updates, 'sum_h': sumh,
                    'reached_residual_tolerance': math.sqrt(hf) < 1e-13,
                    'loss_increasing_steps': loss_increases,
                    'final_residual_norm': math.sqrt(hf),
                    'final_sharpness': qf+max(eigenvalues(cf)),
                    'largest_tested_corrected_increment_over_h': largest_corrected_increment_ratio})

assert new_region == len(starts)
peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if sys.platform != 'darwin':
    peak *= 1024
assert peak < 1024**3
summary = {'status': 'PASS', 'effective_nice': priority,
           'peak_rss_bytes': peak, 'elapsed_seconds': time.monotonic()-started,
           'exact_rational_cases': exact_count,
           'trajectory_cases_outside_old_basin': new_region,
           'largest_steps': max(r['steps'] for r in records),
           'budget_limited_trajectories': sum(not r['reached_residual_tolerance'] for r in records),
           'maximum_final_residual_norm': max_residual,
           'cases_with_h_above_one': sum(r['peak_h'] > 1 for r in records),
           'cases_with_loss_increase': sum(r['loss_increasing_steps'] > 0 for r in records),
           'exact_example_initial_q_and_cmax': str(q0),
           'exact_example_initial_h': str(h0),
           'exact_example_endpoint_q': str(q1),
           'exact_example_endpoint_sharpness': str(sharpness),
           'rank_collapse_exception_checked': True,
           'earlier_chernoff_bound': old_probability}
Path('verification.json').write_text(json.dumps({'summary': summary, 'trajectories': records}, indent=2)+'\n')
print(json.dumps(summary, indent=2))
