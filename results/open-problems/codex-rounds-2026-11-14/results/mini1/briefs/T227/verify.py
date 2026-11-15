"""Exact rational certificates and an independent numerical audit of PROOF.md.

No third-party libraries. The theorem uses the rational assertions, not the
floating-point trajectories. Run with the command in LOG.md.
"""
import json
import itertools
import math
import random
import resource
from fractions import Fraction as Q

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))

certificates = {}

def record(name, value):
    certificates[name] = {"exact": str(value), "decimal": float(value)}
    return value

def exp_bounds(x, n=64):
    """Positive Taylor series, with geometric upper bound for its remainder."""
    assert x >= 0 and x < n+2
    term = Q(1)
    total = term
    for k in range(1, n+1):
        term *= x/k
        total += term
    next_term = term*x/(n+1)
    return total, total + next_term/(1-x/(n+2))

def tanh_bounds(x):
    lo, hi = exp_bounds(2*x)
    return (lo-1)/(lo+1), (hi-1)/(hi+1)

amin, amax = Q('7.99'), Q('8.01')
bmin, bmax = Q('.499'), Q('.501')
cmin, cmax = Q('1.999'), Q('2.001')
umin, umax = Q('.963'), Q('.966')
vmin, vmax = Q('.446'), Q('.450')
hmin, hmax = Q('.9'), Q('1.1')
assert tanh_bounds(cmin)[0] > umin
assert tanh_bounds(cmax)[1] < umax
assert tanh_bounds(bmin*umin)[0] > vmin
assert tanh_bounds(bmax*umax)[1] < vmax
assert tanh_bounds(Q(1))[0] > Q(3,4)
# Coarser rational exponential bounds quoted in the written proof.
assert exp_bounds(2*cmin)[0] > 54
assert exp_bounds(2*cmax)[1] < 55
assert exp_bounds(2*bmin*umin)[0] > Q('2.611')
assert exp_bounds(2*bmax*umax)[1] < Q('2.634')
exp27_lower, _ = exp_bounds(Q(27))
assert exp27_lower > 10**11
assert 4/exp27_lower < Q('1e-10')
assert 72/exp27_lower < Q('1e-8')

fmin, fmax = amin*vmin, amax*vmax
jbmin = amin*(1-vmax**2)*umin
jbmax = amax*(1-vmin**2)*umax
jcmax = amax*(1-vmin**2)*bmax*(1-umin**2)
a1min = record('a1_lower', amin-hmax*fmax*vmax)
a1max = record('a1_upper', amax-hmin*fmin*vmin)
b1max = record('b1_upper', bmax-hmin*fmin*jbmin)
c1min = record('c1_lower', cmin-hmax*fmax*jcmax)
assert a1min > Q('6.2') and a1max < Q('6.6')
assert b1max < -19 and c1min > Q('1.07')
k0lower = record('m_kernel0_lower', jbmin**2)
assert k0lower > 37
k0upper = record('m_kernel0_upper', vmax**2+jbmax**2+jcmax**2)
assert k0upper < 39
# A fixed interval in units of the realized initialization kernel is safe.
assert Q(36,39) > hmin and Q(40,37) < hmax
L0upper = record('loss0_upper', fmax**2/2)
L1lower = record('loss1_lower', Q('6.2')**2*(1-Q('1e-10'))/2)
assert L0upper < Q('6.5') and L1lower > 19

small = Q('1e-10')
cross_error = record('cross_gradient_error', 2*small+16**2*(small**2+Q('1e-8')**2))
assert cross_error < Q('1e-8')
klow, khigh = 1-Q('1e-8'), 1+Q('1e-8')
rho = record('contraction_upper', max(abs(1-hmin*klow), abs(1-hmax*khigh)))
assert rho < Q(1,8)
S = record('total_step_residual_bound', hmax*Q('6.6')/(1-Q(1,8)))
record('tail_a_bound', Q('6.6')+S)
record('tail_b_upper', -19+S*16*small)
record('tail_c_lower', Q('1.07')-S*16*Q('1e-8'))
assert Q('6.6')+S < 16
assert -19+S*16*small < -18
assert Q('1.07')-S*16*Q('1e-8') > 1
record('eta_kernel0_lower', hmin*k0lower)
record('eta_kernel_tail_upper', hmax*khigh)

# Independent numerical implementation: full width-m network, with F shared
# across paths. Do not substitute the equal-path scalar recurrence.
def path_value(p):
    a,b,c = p
    return a*math.tanh(b*math.tanh(c))

def path_gradient(p):
    # Backpropagation using the cosh derivative, separately from scout.py.
    a,b,c = p
    z1 = c
    z2 = b*math.tanh(z1)
    d2 = 1/math.cosh(z2)**2
    return (math.tanh(z2), a*d2*math.tanh(z1),
            a*d2*b/math.cosh(z1)**2)

def network_value(ps):
    return sum(path_value(p) for p in ps)/len(ps)

gradient_error = 0.
for p in ((8.,.5,2.), (6.4,-21.,1.2), (-.5,-19.,1.1)):
    g = path_gradient(p)
    for k in range(3):
        plus,minus = list(p),list(p)
        plus[k] += 1e-6
        minus[k] -= 1e-6
        fd = (path_value(plus)-path_value(minus))/2e-6
        gradient_error = max(gradient_error,abs(fd-g[k]))
assert gradient_error < 1e-7

rng = random.Random(227)
audits = []
for m in (1,7,8,64):
    # Include corners, independent random paths, and learning-rate endpoints.
    initializations = [
        [(7.99,.499,1.999)]*m,
        [(8.01,.501,2.001)]*m,
        [(rng.uniform(7.99,8.01),rng.uniform(.499,.501),rng.uniform(1.999,2.001)) for _ in range(m)]
    ]
    labels = ['lower_corner','upper_corner','independent_uniform']
    corners = list(itertools.product((7.99,8.01),(.499,.501),(1.999,2.001)))
    if m == 1:
        initializations.extend([[p] for p in corners])
        labels.extend(['corner_'+str(i) for i in range(8)])
    if m == 8:
        initializations.append(corners)
        labels.append('all_eight_mixed_corners')
    for label, init in zip(labels, initializations):
        for h in (.9,1.,1.1):
            ps = init
            rows = []
            previous_abs_F = None
            for t in range(16):
                F = network_value(ps)
                gs = [path_gradient(p) for p in ps]
                K = sum(sum(gj*gj for gj in g) for g in gs)/m**2
                rows.append(dict(t=t,F=F,loss=F*F/2,m_kernel=m*K))
                if t >= 2 and previous_abs_F > 1e-100:
                    assert abs(F) <= previous_abs_F/8 + 1e-14
                if t >= 1:
                    assert all(abs(a)<16 and b<-18 and c>1 for a,b,c in ps)
                previous_abs_F = abs(F)
                ps = [tuple(pj-h*F*gj for pj,gj in zip(p,g)) for p,g in zip(ps,gs)]
            assert rows[1]['loss']>rows[0]['loss']
            assert rows[0]['m_kernel']>37 and rows[1]['m_kernel']<1.00000001
            audits.append(dict(width=m,initialization=label,h=h,rows=rows))

# Check the Euclidean network NTK normalization independently by finite
# differences of the actual width-7 network function.
ps = initializations[0][:7]
fd_kernel = 0.
eps = 1e-6
for i in range(7):
    for j in range(3):
        pp, pm = [list(p) for p in ps], [list(p) for p in ps]
        pp[i][j] += eps
        pm[i][j] -= eps
        d = (network_value(pp)-network_value(pm))/(2*eps)
        fd_kernel += d*d
analytic_kernel = sum(sum(x*x for x in path_gradient(p)) for p in ps)/49
normalization_error = abs(fd_kernel-analytic_kernel)
assert normalization_error < 1e-7

data = dict(exact_certificates=certificates,gradient_max_abs_error=gradient_error,
            kernel_normalization_abs_error=normalization_error,
            audits=audits, max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
with open('verification_data.json','w') as out:
    json.dump(data,out,indent=2)
print('Exact rational certificates: PASS')
for name in ('a1_lower','a1_upper','b1_upper','c1_lower','m_kernel0_lower',
             'loss0_upper','loss1_lower','contraction_upper','tail_a_bound','tail_c_lower'):
    print(name+':',certificates[name]['decimal'])
print('Full-network numerical audits:',len(audits),'PASS')
print('Finite-difference gradient max error:',gradient_error)
print('Finite-difference NTK normalization error:',normalization_error)
print('max_rss_bytes:',data['max_rss_bytes'])
