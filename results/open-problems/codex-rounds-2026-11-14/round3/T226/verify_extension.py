"""Independent exact identities and finite probes for the spectral basin theorem."""
import json
import math
import os
import random
import resource
import signal
import sys
from fractions import Fraction as F
from pathlib import Path

assert os.environ.get('OMP_NUM_THREADS') == '1'
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 15, priority
signal.alarm(90)
soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
resource.setrlimit(resource.RLIMIT_CPU, (min(60, hard), hard))
# Fixed-size scalar/list arithmetic only; no numerical libraries or worker threads.

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def tr(a):
    return list(map(list, zip(*a)))

def mm(a, b):
    bt = tr(b)
    return [[dot(row, col) for col in bt] for row in a]

def gram(a):
    return mm(tr(a), a)

def det(a):
    b = [row[:] for row in a]
    ans = 1
    for k in range(len(b)):
        j = next((j for j in range(k, len(b)) if b[j][k] != 0), None)
        if j is None:
            return 0
        if j != k:
            b[j], b[k] = b[k], b[j]
            ans = -ans
        pivot = b[k][k]
        ans *= pivot
        for i in range(k+1, len(b)):
            factor = b[i][k]/pivot
            for j in range(k+1, len(b)):
                b[i][j] -= factor*b[k][j]
            b[i][k] = 0
    return ans

def eigs(a):
    # Symmetric Jacobi diagonalization, independent of the update formulas.
    b = [row[:] for row in a]
    n = len(b)
    if n == 1:
        return [b[0][0]]
    for _ in range(100*n*n):
        i, j = max(((i, j) for i in range(n) for j in range(i+1, n)),
                   key=lambda ij: abs(b[ij[0]][ij[1]]))
        if abs(b[i][j]) < 1e-14:
            return sorted(b[k][k] for k in range(n))
        angle = .5*math.atan2(2*b[i][j], b[j][j]-b[i][i])
        c, s = math.cos(angle), math.sin(angle)
        ai, aj, x = b[i][i], b[j][j], b[i][j]
        for k in range(n):
            if k != i and k != j:
                bi, bj = b[k][i], b[k][j]
                b[k][i] = b[i][k] = c*bi-s*bj
                b[k][j] = b[j][k] = s*bi+c*bj
        b[i][i] = c*c*ai-2*c*s*x+s*s*aj
        b[j][j] = s*s*ai+2*c*s*x+c*c*aj
        b[i][j] = b[j][i] = 0.
    raise AssertionError('Jacobi iteration limit')

def quantities(a, u, y):
    c = gram(u)
    v = [dot(col, a) for col in tr(u)]
    r = [x-z for x, z in zip(v, y)]
    return dot(a, a), c, v, r

def step(a, u, y):
    # Direct simultaneous gradients, never use the claimed recurrences here.
    v = [dot(col, a) for col in tr(u)]
    r = [x-z for x, z in zip(v, y)]
    an = [x-dot(row, r) for x, row in zip(a, u)]
    un = [[x-ai*rj for x, rj in zip(row, r)] for row, ai in zip(u, a)]
    return an, un

rng = random.Random(22620261115)
exact_cases = 0
for _ in range(40):
    m, d = 5, 3
    a = [F(rng.randrange(-5, 6), 7) for _ in range(m)]
    u = [[F(rng.randrange(-5, 6), 11) for _ in range(d)] for _ in range(m)]
    y = [F(rng.randrange(-3, 4), 17) for _ in range(d)]
    q, c, v, r = quantities(a, u, y)
    an, un = step(a, u, y)
    qn, cn, vn, rn = quantities(an, un, y)
    predicted = [r[j]-dot(c[j], r)-q*r[j]+dot(v, r)*r[j] for j in range(d)]
    assert rn == predicted
    a0, u0 = step(a, u, [F(0)]*d)
    q0, c0, v0, _ = quantities(a0, u0, [F(0)]*d)
    h = dot(v, v)
    assert q0 == q-2*h+dot(v, [dot(row, v) for row in c])
    assert c0 == [[c[i][j]+(q-2)*v[i]*v[j] for j in range(d)] for i in range(d)]
    assert v0 == [v[j]-dot(c[j], v)-q*v[j]+h*v[j] for j in range(d)]
    z = [[ai]+row for ai, row in zip(a, u)]
    zn = [[ai]+row for ai, row in zip(a0, u0)]
    assert det(gram(zn)) == det(gram(z))*(1-h)**2
    # Independent audit of the earlier small-step imbalance and total norm laws.
    b = [F(2), F(-1), F(1, 2)]
    eta = F(1, 997)
    rr = [v[j]-b[j] for j in range(d)]
    ga = [dot(row, rr) for row in u]
    gw = [[ai*rj for rj in rr] for ai in a]
    ap = [ai-eta*gi for ai, gi in zip(a, ga)]
    up = [[x-eta*g for x, g in zip(row, gr)] for row, gr in zip(u, gw)]
    old_b = [[dot(u[i], u[j])-a[i]*a[j] for j in range(m)] for i in range(m)]
    new_b = [[dot(up[i], up[j])-ap[i]*ap[j] for j in range(m)] for i in range(m)]
    assert new_b == [[old_b[i][j]+eta**2*(dot(gw[i], gw[j])-ga[i]*ga[j])
                      for j in range(m)] for i in range(m)]
    old_s = dot(a, a)+sum(dot(row, row) for row in u)
    new_s = dot(ap, ap)+sum(dot(row, row) for row in up)
    g2 = dot(ga, ga)+sum(dot(row, row) for row in gw)
    assert new_s-old_s == -4*eta*dot(v, rr)+eta**2*g2
    exact_cases += 1

# Audit the earlier rational constants via a separate, direct chain.
assert F(3)*(1+F(1,128))+2 == F(643,128) < 6
assert 6*(1+F(1,64))**2 == F(12675,2048) < 8
assert F(3,2)*8+F(1,2) == F(25,2) < 13
assert 13*F(1,32) < 1
assert F(3,2)*6+F(1,2) < 10
assert F(1,32)-F(2,128) == F(1,64)
assert F(1,64)*F(1,4) == F(1,256)

# Rational full-rank case inside the basin but with initial sharpness >2.
m, d = 16, 8
a = [F(1)] + [F(0)]*(m-1)
u = [[F(0)]*d for _ in range(m)]
u[0][0], u[1][0] = F(4,5), F(1,10)
for j in range(1, d):
    u[j+1][j] = F(1,10)
q, c, v, _ = quantities(a, u, [F(0)]*d)
assert all(c[i][j] == 0 for i in range(d) for j in range(d) if i != j)
s0 = q+max(c[i][i] for i in range(d))
assert s0 == F(33,20) < 2
assert det(gram([[ai]+row for ai, row in zip(a, u)])) > 0
# h=(e1, e1 e1^T), ||h||^2=2; J h=(9/5,0,...), residual=(4/5,0,...).
rayleigh = (F(9,5)**2+2*F(4,5))/2
assert rayleigh == F(121,50) > 2
# Independently recover this second derivative from exact loss evaluations.
# The loss along a line is quartic, so two symmetric differences eliminate
# the quartic coefficient without a numerical differentiation approximation.
def line_loss(t):
    ap = a[:]
    up = [row[:] for row in u]
    ap[0] += t
    up[0][0] += t
    vp = [dot(col, ap) for col in tr(up)]
    return dot(vp, vp)/2
d_one = line_loss(F(1))+line_loss(F(-1))-2*line_loss(F(0))
d_half = line_loss(F(1,2))+line_loss(F(-1,2))-2*line_loss(F(0))
independent_rayleigh = (16*d_half-d_one)/6
assert independent_rayleigh == rayleigh
example_a = [float(x) for x in a]
example_u = [[float(x) for x in row] for row in u]

# At the excluded boundary s0=2 a full-rank stationary global minimizer
# has sharpness exactly 2. Strictness of the basin inequality matters.
boundary_u = [[F(0)]*d for _ in range(m)]
for j in range(d):
    boundary_u[j+1][j] = F(1)
assert step(a, boundary_u, [F(0)]*d) == (a, boundary_u)
assert det(gram([[ai]+row for ai, row in zip(a, boundary_u)])) == 1
assert dot(a,a)+max(gram(boundary_u)[j][j] for j in range(d)) == 2

# Jacobi's numbers checked against trace, determinant, and a known 2x2 spectrum.
test = [[2., 1.], [1., 3.]]
ee = eigs(test)
assert abs(ee[0]-(5-math.sqrt(5))/2) < 1e-12
assert abs(sum(ee)-5) < 1e-12
assert abs(math.prod(ee)-5) < 1e-12

records = []
initials = []
for case in range(12):
    m, d = (16, 8) if case < 8 else (5, 3)
    a = [rng.gauss(0, 1) for _ in range(m)]
    u = [[rng.gauss(0, 1) for _ in range(d)] for _ in range(m)]
    q = dot(a, a)
    c = max(eigs(gram(u)))
    target_s = (.5, 1.0, 1.9, 1.999)[case % 4]
    scale = math.sqrt(target_s/(q+c))
    initials.append(([x*scale for x in a], [[x*scale for x in row] for row in u]))
initials.append((example_a, example_u))
max_gram_determinant_error = 0.
for case, (a_start, u_start) in enumerate(initials):
    m, d = len(a_start), len(u_start[0])
    q0, c0, v0, _ = quantities(a_start, u_start, [0.]*d)
    cmax0 = max(eigs(c0))
    initial_s = q0+cmax0
    initial_det = det(gram([[ai]+row for ai, row in zip(a_start, u_start)]))
    assert initial_s < 2 and initial_det > 0
    b = [1/math.sqrt(d)]*d
    for eta in (0., .01, .0001, .000001):
        a, u = a_start[:], [row[:] for row in u_start]
        y = [eta*x for x in b]
        cumulative_h = 0.
        for t in range(2500):
            q, c, v, r = quantities(a, u, y)
            rnorm = math.sqrt(dot(r, r))
            if rnorm < 1e-12:
                break
            an, un = step(a, u, y)
            if eta == 0:
                qn = dot(an, an)
                assert qn <= q+2e-13
                assert q <= q0+2e-13
                cumulative_h += dot(v, v)
                assert cumulative_h <= q0/(2-cmax0)+1e-10
                if t % 25 == 0:
                    go = gram([[ai]+row for ai, row in zip(a, u)])
                    gn = gram([[ai]+row for ai, row in zip(an, un)])
                    expected = det(go)*(1-dot(v,v))**2
                    error = abs(det(gn)-expected)/max(abs(expected), 1e-100)
                    max_gram_determinant_error = max(max_gram_determinant_error, error)
                    assert error < 1e-9
            a, u = an, un
        q, c, v, r = quantities(a, u, y)
        residual = math.sqrt(dot(r, r))
        endpoint_s = q+max(eigs(c))
        assert residual < 1e-10, (case, eta, residual)
        assert endpoint_s <= (2+initial_s)/2+1e-10, (case, eta, endpoint_s)
        if eta == 0:
            assert endpoint_s <= initial_s+1e-10
            assert min(eigs(c)) > 0 and q > 0
        records.append({'case': case, 'm': m, 'd': d, 'scaled_target_norm': eta,
                        'initial_s': initial_s, 'steps': t,
                        'final_residual_norm': residual, 'endpoint_s': endpoint_s,
                        'zero_target_sum_h': cumulative_h if eta == 0 else None})

# At the final nonzero-target endpoint, differentiate the gradient in every
# parameter coordinate and compare to a separately constructed J^T J. The
# residual is nonzero only at roundoff tolerance, which is included below.
theta = a+[x for row in u for x in row]
def grad_flat(theta):
    aa = theta[:m]
    uu = [theta[m+i*d:m+(i+1)*d] for i in range(m)]
    vv = [dot(col, aa) for col in tr(uu)]
    rr = [x-z for x,z in zip(vv, y)]
    return [dot(row, rr) for row in uu]+[ai*rj for ai in aa for rj in rr]
jacobian = [[u[i][j] for i in range(m)]+
            [a[i] if ell == j else 0. for i in range(m) for ell in range(d)]
            for j in range(d)]
expected_hessian = mm(tr(jacobian), jacobian)
delta = 1e-5
fd_error = 0.
for j in range(len(theta)):
    plus, minus = theta[:], theta[:]
    plus[j] += delta
    minus[j] -= delta
    gp, gm = grad_flat(plus), grad_flat(minus)
    for i in range(len(theta)):
        fd_error = max(fd_error, abs((gp[i]-gm[i])/(2*delta)-expected_hessian[i][j]))
assert fd_error < 1e-8
output_gram = mm(jacobian, tr(jacobian))
endpoint_c = gram(u)
assert max(abs(output_gram[i][j]-endpoint_c[i][j]-(dot(a,a) if i==j else 0.))
           for i in range(d) for j in range(d)) < 1e-12
assert abs(max(eigs(output_gram))-(dot(a,a)+max(eigs(endpoint_c)))) < 1e-12

# Two independent evaluations of the Chernoff exponent and its optimizer.
p = 144
u_ratio = F(4)
tau2 = F(1, 2*p)
t_opt = (1-1/float(u_ratio))/2
log_bound = -p*(float(u_ratio)-1-math.log(float(u_ratio)))/2
log_mgf_bound = -t_opt*2/float(tau2)-p/2*math.log1p(-2*t_opt)
assert abs(log_bound-log_mgf_bound) < 1e-12
bound = math.exp(log_bound)
# Integer power times exponential, independently avoiding logarithm evaluation.
independent_bound = (4**72)*math.exp(-216)
assert abs(bound/independent_bound-1) < 2e-14
assert bound < 3.5e-51

peak_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if sys.platform != 'darwin':
    peak_rss *= 1024
assert peak_rss < 1024**3
summary = {'status': 'PASS', 'effective_nice': priority, 'peak_rss_bytes': peak_rss,
           'exact_cases': exact_cases, 'trajectory_cases': len(records),
           'largest_steps': max(r['steps'] for r in records),
           'maximum_final_residual_norm': max(r['final_residual_norm'] for r in records),
           'maximum_gram_determinant_relative_error': max_gram_determinant_error,
           'initial_supercritical_example_s': str(s0),
           'initial_hessian_rayleigh_quotient': str(rayleigh),
           'independent_loss_rayleigh_quotient': str(independent_rayleigh),
           'endpoint_hessian_finite_difference_max_error': fd_error,
           'chernoff_log_bound': log_bound, 'chernoff_bound': bound,
           'independent_chernoff_bound': independent_bound}
Path('verification.json').write_text(json.dumps({'summary': summary, 'trajectories': records}, indent=2)+'\n')
print(json.dumps(summary, indent=2))
