"""Rational constants and literal-coordinate audits of the centered bootstrap.

Only the analytic estimates prove the theorem at large widths. Small
networks test formulas conditional on the deterministic row event.
"""
import json
import math
import os
import random
import resource
import time
from fractions import Fraction as Q

resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
started = time.monotonic()
assert os.environ['OMP_NUM_THREADS'] == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15

def exp_bounds(x, n=100):
    assert 0 <= x < n+2
    term = total = Q(1)
    for k in range(1, n+1):
        term *= x/k
        total += term
    return total, total+term*x/(n+1)/(1-x/(n+2))

def tanh_bounds(x):
    lo, hi = exp_bounds(2*x)
    return (lo-1)/(lo+1), (hi-1)/(hi+1)

amin, amax = Q('7.9'), Q('8.1')
umin, umax = Q('.96'), Q('.97')
vmax = Q('.225')
assert tanh_bounds(Q('1.97'))[0] > umin
assert tanh_bounds(Q('2.03'))[1] < umax
z_initial_bound = Q('.965')*Q('.021')+Q('.005')*Q('1.001')
z_tube_bound = z_initial_bound+Q('.2')*umax
assert z_tube_bound < vmax
dmin = amin*(1-vmax*vmax)*umin
dmax = amax*umax
cmax = (1-umin*umin)*amax*Q('1.201')
kmin = dmin*dmin-vmax*vmax-cmax*cmax
kmax = dmax*dmax+vmax*vmax+cmax*cmax
assert kmin > 50 and kmax < 63
assert Q('.9')*50-1 > 40 and Q('1.1')*63-1 < 69
r, g = Q('.02'), Q(40)
S = Q('1.1')*r/(1-1/g)
da, dw, dc = vmax*S, dmax*S, cmax*S
assert Q('7.99')-da > amin and Q('8.01')+da < amax
assert dw < Q('.2')
assert Q('1.999')-dc > Q('1.97') and Q('2.001')+dc < Q('2.03')
assert dmin > Q('7.2') and dmax < Q('7.86')
coherence_error = Q('.33')*S
assert coherence_error < Q('.0075')
coord_derivative_lower = Q('7.99')*umin*(1-z_initial_bound**2)
assert coord_derivative_lower > 7
assert Q(1000, 7) < 143
bd_constant = 2*Q('1.001')*Q('8.01')
assert 2*r*r/(bd_constant*bd_constant) > Q(1, 400000)
# At m0, the three failure terms are below 4e-9 in total. They all
# decrease for m>=m0. e^100000 >= e^40, an intentionally crude bound.
m0 = 200000
exp40lower = exp_bounds(Q(40))[0]
prob_at_m0_upper = Q(2*m0+2)/exp40lower+Q(143, m0*m0)
assert prob_at_m0_upper < Q('4e-9')
N = 0
while 40**N < Q(m0**4, 50): N += 1
assert N == 13
cert = dict(z_initial_abs_upper=z_initial_bound, z_tube_abs_upper=z_tube_bound,
            D_lower=dmin, D_upper=dmax, C_abs_upper=cmax,
            cross_lower=kmin, cross_upper=kmax,
            total_h_abs_F=S, a_movement=da, W_movement=dw, c_movement=dc,
            common_shift_error=coherence_error,
            coordinate_derivative_lower=coord_derivative_lower,
            bounded_difference_constant=bd_constant,
            failure_bound_at_200000_upper=prob_at_m0_upper,
            exit_residual_upper=69*r, exit_loss_upper=(69*r)**2/2)

def state(x, m):
    a, B, c = x[:m], x[m:m+m*m], x[m+m*m:]
    u = [math.tanh(cj) for cj in c]
    z = [math.fsum(B[i*m+j]*u[j] for j in range(m))/math.sqrt(m) for i in range(m)]
    v = [math.tanh(zi) for zi in z]
    q = [1/math.cosh(zi)**2 for zi in z]
    F = math.fsum(ai*vi for ai, vi in zip(a, v))/m
    ga = [vi/m for vi in v]
    gB = [a[i]*q[i]*u[j]/(m*math.sqrt(m)) for i in range(m) for j in range(m)]
    gc = [(1-u[j]**2)*math.fsum(a[i]*q[i]*B[i*m+j] for i in range(m))/(m*math.sqrt(m)) for j in range(m)]
    return F, ga+gB+gc

def in_tube(x, x0, m):
    assert min(x[:m]) > 7.9 and max(x[:m]) < 8.1
    assert min(x[m+m*m:]) > 1.97 and max(x[m+m*m:]) < 2.03
    assert max(abs(b-b0)*math.sqrt(m) for b, b0 in zip(x[m:m+m*m], x0[m:m+m*m])) < .2

def patterns(m):
    yield 'balanced_circulant', [[(-1 if (j-i)%m < m//2 else 1) for j in range(m)] for i in range(m)]
    # Columns can be completely imbalanced. No column event is used.
    yield 'identical_balanced_rows', [[(-1 if j < m//2 else 1) for j in range(m)] for i in range(m)]
    if m == 100:
        yield 'row_event_boundaries', [[(-1 if (j-i)%m < 49+(i%3) else 1) for j in range(m)] for i in range(m)]
        yield 'one_unbalanced_row', [[(-1 if (j-i)%m < (49 if i == 0 else 50) else 1) for j in range(m)] for i in range(m)]

audits, fd = [], 0.
for m in (4, 20, 100):
    for label, signs in patterns(m):
        assert all(abs(sum(row)/m) <= .02+1e-15 for row in signs)
        for mode in ('independent', 'opposing_corners'):
            rng = random.Random(2275000+m)
            if mode == 'independent':
                a = [rng.uniform(7.99, 8.01) for _ in range(m)]
                c = [rng.uniform(1.999, 2.001) for _ in range(m)]
                W = [signs[i][j]*rng.uniform(.999, 1.001) for i in range(m) for j in range(m)]
            else:
                a = [7.99 if i%2 else 8.01 for i in range(m)]
                c = [1.999 if j < m//2 else 2.001 for j in range(m)]
                W = [signs[i][j]*(.999 if j < m//2 else 1.001) for i in range(m) for j in range(m)]
            x0 = a+[w/math.sqrt(m) for w in W]+c
            F0, grad0 = state(x0, m)
            assert abs(F0) < .02
            if abs(F0) < 1e-12:
                # Floating point cannot test amplification of an exactly
                # or nearly balanced residual. The analytic lemma covers it.
                continue
            if m == 4:
                for k, gi in enumerate(grad0):
                    xp, xm = x0[:], x0[:]
                    xp[k] += 1e-6
                    xm[k] -= 1e-6
                    fd = max(fd, abs((state(xp, m)[0]-state(xm, m)[0])/2e-6-gi))
            for h in (.9, 1., 1.1):
                x, rows, signed_sum = x0[:], [], 0.
                for t in range(30):
                    F, grad = state(x, m)
                    in_tube(x, x0, m)
                    mk = m*math.fsum(gi*gi for gi in grad)
                    assert 50 < mk < 63
                    common_shift = -7.53*signed_sum
                    coh = max(abs((b-b0)*math.sqrt(m)-common_shift) for b, b0 in zip(x[m:m+m*m], x0[m:m+m*m]))
                    assert coh < .0075
                    rows.append(dict(t=t, F=F, m_kernel=mk, common_shift_error=coh))
                    if abs(F) >= .02:
                        assert t >= 1 and abs(F) < 1.38
                        break
                    y = [xi-m*h*F*gi for xi, gi in zip(x, grad)]
                    Fy = state(y, m)[0]
                    assert 40 < abs(Fy/F) < 69 and F*Fy < 0
                    # Evaluate the whole update segment at several points;
                    # the proof covers all points by convexity.
                    for alpha in (0., .25, .5, .75, 1.):
                        mid = [(1-alpha)*xi+alpha*yi for xi, yi in zip(x, y)]
                        in_tube(mid, x0, m)
                        _, gm = state(mid, m)
                        cross = m*math.fsum(gi*gj for gi, gj in zip(grad, gm))
                        assert 50 < cross < 63
                    signed_sum += h*F
                    x = y
                else:
                    raise AssertionError('No exit in numerical audit')
                audits.append(dict(width=m, pattern=label, mode=mode, h=h, rows=rows))
assert fd < 1e-7
# Exact balanced support point: demonstrates why F0=0 must be excluded.
balanced = [8.]*4+[(-1 if j < 2 else 1)/2 for i in range(4) for j in range(4)]+[2.]*4
assert state(balanced, 4)[0] == 0
summary = dict(status='PASS', certificates={k:dict(exact=str(v), decimal=float(v)) for k,v in cert.items()},
               literal_Euclidean_trajectories=len(audits),
               finite_difference_error=fd,
               residual_ratio_min=min(abs(row['F']/prev['F']) for a in audits for prev,row in zip(a['rows'], a['rows'][1:])),
               residual_ratio_max=max(abs(row['F']/prev['F']) for a in audits for prev,row in zip(a['rows'], a['rows'][1:])),
               max_exit_time=max(a['rows'][-1]['t'] for a in audits),
               time_bound_at_200000=N,
               nice=os.getpriority(os.PRIO_PROCESS, 0),
               max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
               seconds=time.monotonic()-started)
assert summary['max_rss_bytes'] < 1_000_000_000
with open('bootstrap_verification.json', 'w') as f:
    json.dump(dict(summary=summary, audits=audits), f, indent=2)
print(json.dumps(summary, indent=2))
