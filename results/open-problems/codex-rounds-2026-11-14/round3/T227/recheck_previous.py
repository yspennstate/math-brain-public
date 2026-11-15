"""Independent arithmetic and asymmetric-network audit of the earlier theorem."""
import itertools
import json
import math
import os
import resource
import time
from fractions import Fraction as Q

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
started = time.monotonic()
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15

def exp_interval(x):
    # Reduce to [0,1/8], sum there, then square repeatedly. Independent
    # implementation, not an import or execution of the earlier certificate.
    k = 0
    while x > Q(1, 8):
        x /= 2
        k += 1
    term = total = Q(1)
    for j in range(1, 13):
        term = term * x / j
        total += term
    remainder = term*x/13/(1-x/14)
    return total**(2**k), (total+remainder)**(2**k)

def tanh_interval(x):
    lo, hi = exp_interval(2*x)
    return (lo-1)/(lo+1), (hi-1)/(hi+1)

assert tanh_interval(Q('1.999'))[0] > Q('.963')
assert tanh_interval(Q('2.001'))[1] < Q('.966')
assert tanh_interval(Q('.499')*Q('.963'))[0] > Q('.446')
assert tanh_interval(Q('.501')*Q('.966'))[1] < Q('.450')
assert tanh_interval(Q(1))[0] > Q(3, 4)

A, Z, U, V = Q('8.01'), Q('.501'), Q('.966'), Q('.450')
a, u, v = Q('7.99'), Q('.963'), Q('.446')
f, F = a*v, A*V
jlo, jhi = a*(1-V*V)*u, A*(1-v*v)*U
khi = A*(1-v*v)*Z*(1-u*u)
values = dict(
    a1_lower=a-Q('1.1')*F*V,
    a1_upper=A-Q('.9')*f*v,
    b1_upper=Z-Q('.9')*f*jlo,
    c1_lower=Q('1.999')-Q('1.1')*F*khi,
    kernel0_lower=jlo*jlo,
    kernel0_upper=V*V+jhi*jhi+khi*khi,
    loss0_upper=F*F/2,
    loss1_lower=Q('6.2')**2*(1-Q('1e-10'))/2,
)
assert values['a1_lower'] > Q('6.2')
assert values['a1_upper'] < Q('6.6')
assert values['b1_upper'] < -19
assert values['c1_lower'] > Q('1.07')
assert values['kernel0_lower'] > 37
assert values['kernel0_upper'] < 39
assert values['loss0_upper'] < Q('6.5')
assert values['loss1_lower'] > 19
elo, _ = exp_interval(Q(27))
assert 4/elo < Q('1e-10') and 72/elo < Q('1e-8')
S = Q('1.1')*Q('6.6')/(1-Q(1, 8))
assert Q('6.6')+S < 16
assert -19+S*16*Q('1e-10') < -18
assert Q('1.07')-S*16*Q('1e-8') > 1
assert 2*Q('1e-10')+256*(Q('1e-20')+Q('1e-16')) < Q('1e-8')
assert max(1-Q('.9')*(1-Q('1e-8')), Q('1.1')*(1+Q('1e-8'))-1) < Q(1, 8)
assert Q(36, 39) > Q('.9') and Q(40, 37) < Q('1.1')

def evaluate(ps):
    out, grads = [], []
    for a, b, c in ps:
        u = math.tanh(c)
        z = b*u
        v = math.tanh(z)
        d = 1/math.cosh(z)**2
        out.append(a*v)
        grads.append((v, a*u*d, a*b*d/math.cosh(c)**2))
    return math.fsum(out)/len(ps), grads

corners = list(itertools.product((7.99, 8.01), (.499, .501), (1.999, 2.001)))
networks = [[p] for p in corners]+[corners, corners+[(8., .5, 2.)]*9]
worst_ratio, audits = 0., 0
for ps0 in networks:
    for h in (.9, .95, 1., 1.05, 1.1):
        ps = list(ps0)
        last = None
        for t in range(14):
            F, gs = evaluate(ps)
            mk = math.fsum(x*x for g in gs for x in g)/len(ps)
            if t == 0:
                assert F*F/2 < 6.5 and 37 < mk < 39
            if t == 1:
                assert F*F/2 > 19
            if t >= 1:
                assert abs(mk-1) < 1e-8
                assert all(abs(a)<16 and b < -18 and c > 1 for a, b, c in ps)
            if t >= 2 and abs(last) > 1e-12:
                worst_ratio = max(worst_ratio, abs(F/last))
                assert abs(F) <= abs(last)/8+1e-14
            last = F
            ps = [tuple(x-h*F*g for x, g in zip(p, grad)) for p, grad in zip(ps, gs)]
        audits += 1

data = dict(status='PASS', exact_bounds={k:float(v) for k,v in values.items()},
            sparse_network_audits=audits, max_residual_ratio=worst_ratio,
            process_nice=os.getpriority(os.PRIO_PROCESS,0),
            max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            seconds=time.monotonic()-started)
with open('previous_recheck.json', 'w') as f:
    json.dump(data, f, indent=2)
print(json.dumps(data, indent=2))
