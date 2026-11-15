"""Independent round-4 certificate audit; no prior code imported."""
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
scale = 10**30

def lower(x): return Q(math.floor(x*scale), scale)
def upper(x): return Q(math.ceil(x*scale), scale)

def exp_bounds(x):
    squarings = 0
    while x > Q(1, 16):
        x /= 2
        squarings += 1
    term = total = Q(1)
    for k in range(1, 19):
        term *= x/k
        total += term
    lo = lower(total)
    hi = upper(total + term*x/19/(1-x/20))
    for _ in range(squarings):
        lo, hi = lower(lo*lo), upper(hi*hi)
    return lo, hi

def tanh_bounds(x):
    lo, hi = exp_bounds(2*x)
    return lower((lo-1)/(lo+1)), upper((hi-1)/(hi+1))

ul = tanh_bounds(Q('1.999'))[0]
uh = tanh_bounds(Q('2.001'))[1]
# Extremize positive and negative contributions separately. This does not
# use the proof's midpoint decomposition of either signed sum.
zl = Q('.725')*Q('.999')*ul-Q('.275')*Q('1.001')*uh
zh = Q('.775')*Q('1.001')*uh-Q('.225')*Q('.999')*ul
vl, vh = tanh_bounds(zl)[0], tanh_bounds(zh)[1]
al, ah = Q('7.99'), Q('8.01')
kl, kh = al*(1-vh*vh), ah*(1-vl*vl)
ch = (1-ul*ul)*(Q('.775')*Q('1.001')*kh-Q('.225')*Q('.999')*kl)
fl, fh, dl, dh = al*vl, ah*vh, kl*ul, kh*uh
cert = dict(a1_lower=al-Q('1.1')*fh*vh, a1_upper=ah-Q('.9')*fl*vl,
            W1_lower=-Q('1.001')-Q('1.1')*fh*dh,
            W1_upper=Q('1.001')-Q('.9')*fl*dl,
            c1_lower=Q('1.999')-Q('1.1')*fh*ch,
            kernel0_lower=dl*dl, kernel0_upper=vh*vh+dh*dh+ch*ch,
            L0_upper=fh*fh/2)
assert cert['a1_lower'] > Q('5.8') and cert['a1_upper'] < Q('6.9')
assert cert['W1_lower'] > -29 and cert['W1_upper'] < -16
assert cert['c1_lower'] > Q('.84')
assert cert['kernel0_lower'] > 34 and cert['kernel0_upper'] < 43
assert cert['L0_upper'] < 8
e, d = Q('2e-8'), Q('1e-6')
assert tanh_bounds(Q('.8'))[0] > Q('.66')
assert 4/exp_bounds(Q('19.8'))[0] < e
assert e+(18*e)**2+(540*e)**2 < d
S = Q('1.1')*Q('6.9')/(1-Q(1, 8))
assert Q('6.9')+S < 18 and -29-18*e*S > -30 and -16+18*e*S < -15
assert Q('.84')-540*e*S > Q('.8')
assert max(1-Q('.9')*(1-d), Q('1.1')*(1+d)-1) < Q(1, 8)
assert Q('5.8')**2*(1-e)/2 > 16
assert 80000/exp_bounds(Q(25))[0] < Q('2e-6')

def forward_grad(x, m):
    a, B, c = x[:m], x[m:m+m*m], x[m+m*m:]
    u = [math.tanh(cj) for cj in c]
    z = [math.fsum(B[i*m+j]*u[j] for j in range(m))/math.sqrt(m) for i in range(m)]
    v = [math.tanh(zi) for zi in z]
    q = [1/math.cosh(zi)**2 for zi in z]
    F = math.fsum(ai*vi for ai, vi in zip(a, v))/m
    g = ([vi/m for vi in v]
         +[a[i]*q[i]*u[j]/(m*math.sqrt(m)) for i in range(m) for j in range(m)]
         +[(1-u[j]**2)*math.fsum(a[i]*q[i]*B[i*m+j] for i in range(m))/(m*math.sqrt(m)) for j in range(m)])
    return F, g

audits, fd, ratio = [], 0., 0.
for m in (4, 40, 80):
    for count in sorted({math.ceil(.225*m), m//4, math.floor(.275*m)}):
        rng = random.Random(227500+m+count)
        x0 = ([rng.uniform(7.99, 8.01) for _ in range(m)]
              +[(-1 if (j-i)%m < count else 1)*rng.uniform(.999, 1.001)/math.sqrt(m) for i in range(m) for j in range(m)]
              +[rng.uniform(1.999, 2.001) for _ in range(m)])
        if m == 4:
            _, g = forward_grad(x0, m)
            for k, gi in enumerate(g):
                xp, xm = x0[:], x0[:]
                xp[k] += 1e-6
                xm[k] -= 1e-6
                fd = max(fd, abs((forward_grad(xp, m)[0]-forward_grad(xm, m)[0])/2e-6-gi))
        for h in (.9, 1., 1.1):
            x, prev, losses = x0[:], None, []
            for t in range(12):
                f, g = forward_grad(x, m)
                losses.append(f*f/2)
                mk = m*math.fsum(gi*gi for gi in g)
                if t == 0: assert 34 < mk < 43 and losses[-1] < 8
                if t == 1: assert losses[-1] > 16
                if t >= 1:
                    assert abs(mk-1) < 1e-6 and max(map(abs, x[:m])) < 18
                    assert all(-30 < b*math.sqrt(m) < -15 for b in x[m:m+m*m])
                    assert min(x[m+m*m:]) > .8
                if t >= 2 and abs(prev) > 1e-9:
                    ratio = max(ratio, abs(f/prev))
                    assert abs(f/prev) < .125
                prev = f
                x = [xi-m*h*f*gi for xi, gi in zip(x, g)]
            audits.append(dict(width=m, negative_count=count, h=h, losses=losses))
assert fd < 1e-7
result = dict(status='PASS', bounds={k:float(v) for k,v in cert.items()},
              trajectories=len(audits), finite_difference_error=fd,
              max_tail_ratio=ratio, nice=os.getpriority(os.PRIO_PROCESS, 0),
              max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              seconds=time.monotonic()-started)
assert result['max_rss_bytes'] < 1_000_000_000
with open('previous_recheck.json', 'w') as f:
    json.dump(dict(summary=result, audits=audits), f, indent=2)
print(json.dumps(result, indent=2))
