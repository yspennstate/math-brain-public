"""Exact bounds and independent full-matrix audits for PROOF.md.

Standard library only. No imports from the previous worker or recheck script.
The proof uses rational inequalities; floating-point audits target errors.
"""
import itertools
import json
import math
import os
import random
import resource
import time
from fractions import Fraction as Q

resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
started = time.monotonic()
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15

def exp_bracket(x):
    term = total = Q(1)
    for k in range(1, 65):
        term *= x/k
        total += term
    assert 0 < x < 66
    return total, total+term*x/65/(1-x/66)

def tanh_bracket(x):
    lo, hi = exp_bracket(2*x)
    return (lo-1)/(lo+1), (hi-1)/(hi+1)

assert exp_bracket(Q('3.998'))[0] > 54
assert exp_bracket(Q('4.002'))[1] < 55
assert exp_bracket(2*Q('.499')*Q('.963'))[0] > Q('2.611')
assert exp_bracket(2*Q('.501')*Q('.966'))[1] < Q('2.634')
assert tanh_bracket(Q('1.999'))[0] > Q('.963')
assert tanh_bracket(Q('2.001'))[1] < Q('.966')
assert tanh_bracket(Q('.499')*Q('.963'))[0] > Q('.446')
assert tanh_bracket(Q('.501')*Q('.966'))[1] < Q('.450')
assert tanh_bracket(Q(1))[0] > Q(3, 4)
assert sum(Q(3)**k/math.factorial(k) for k in range(9)) > 20
assert Q(4, 20**9) < Q('1e-10')

amin, amax = Q('7.99'), Q('8.01')
bmin, bmax = Q('.499'), Q('.501')
umin, umax, vmin, vmax = map(Q, ('.963', '.966', '.446', '.450'))
fmin, fmax = amin*vmin, amax*vmax
dmin = amin*(1-vmax**2)*umin
dmax = amax*(1-vmin**2)*umax
cmax = amax*(1-vmin**2)*bmax*(1-umin**2)
eps, delta = Q('1e-10'), Q('1e-8')
rho = Q(1, 8)
S = Q('1.1')*Q('6.6')/(1-rho)
assert S == Q(1452, 175)

cert = dict(
    a1_lower=amin-Q('1.1')*fmax*vmax,
    a1_upper=amax-Q('.9')*fmin*vmin,
    W1_lower=bmin-Q('1.1')*fmax*dmax,
    W1_upper=bmax-Q('.9')*fmin*dmin,
    c1_lower=Q('1.999')-Q('1.1')*fmax*cmax,
    m_kernel0_lower=dmin**2,
    m_kernel0_upper=vmax**2+dmax**2+cmax**2,
    loss0_upper=fmax**2/2,
    loss1_lower=Q('6.2')**2*(1-eps)/2,
    tail_cross_error=eps+(16*eps)**2+(416*eps)**2,
    contraction_upper=max(1-Q('.9')*(1-delta), Q('1.1')*(1+delta)-1),
    tail_a_upper=Q('6.6')+S,
    tail_W_lower=-25-S*16*eps,
    tail_W_upper=-19+S*16*eps,
    tail_c_lower=Q('1.07')-S*416*eps,
)
assert cert['a1_lower'] > Q('6.2') and cert['a1_upper'] < Q('6.6')
assert cert['W1_lower'] > -25 and cert['W1_upper'] < -19
assert cert['c1_lower'] > Q('1.07')
assert cert['m_kernel0_lower'] > 37 and cert['m_kernel0_upper'] < 39
assert cert['loss0_upper'] < Q('6.5') and cert['loss1_lower'] > 19
assert cert['tail_cross_error'] < delta and cert['contraction_upper'] < rho
assert cert['tail_a_upper'] < 16
assert cert['tail_W_lower'] > -26 and cert['tail_W_upper'] < -18
assert cert['tail_c_lower'] > 1
assert Q(36,39) > Q('.9') and Q(40,37) < Q('1.1')

# Re-count every term in the metric at several widths, independently of
# the width-free formulas. These are exact rational sums.
for m in (1, 2, 3, 7, 64):
    counted_initial = (sum([vmax*vmax]*m, Q(0))/m
        +sum([dmax*dmax]*(m*m), Q(0))/(m*m)
        +sum([cmax*cmax]*m, Q(0))/m)
    counted_tail_error = (sum([(16*eps)**2]*(m*m), Q(0))/(m*m)
        +sum([(416*eps)**2]*m, Q(0))/m)
    assert counted_initial == cert['m_kernel0_upper']
    assert counted_tail_error+eps == cert['tail_cross_error']

def sech2(z):
    # Do not use 1-tanh(z)^2: saturation would erase tiny derivatives.
    e = math.exp(-2*abs(z))
    return 4*e/(1+e)**2

def dense_state(a, W, c):
    m = len(a)
    u = [math.tanh(x) for x in c]
    v = [math.tanh(math.fsum(w*uj for w, uj in zip(row, u))/m) for row in W]
    z = [math.fsum(w*uj for w, uj in zip(row, u))/m for row in W]
    aq = [ai*sech2(zi) for ai, zi in zip(a, z)]
    D = [[aqi*uj for uj in u] for aqi in aq]
    C = [sech2(c[j])*math.fsum(aq[i]*W[i][j] for i in range(m))/m for j in range(m)]
    F = math.fsum(ai*vi for ai, vi in zip(a, v))/m
    mk = (math.fsum(x*x for x in v)/m
          +math.fsum(x*x for row in D for x in row)/(m*m)
          +math.fsum(x*x for x in C)/m)
    return F, v, D, C, mk

def update(a, W, c, h):
    F, A, D, C, _ = dense_state(a, W, c)
    return ([x-h*F*y for x,y in zip(a,A)],
            [[x-h*F*y for x,y in zip(row,drow)] for row,drow in zip(W,D)],
            [x-h*F*y for x,y in zip(c,C)])

def patterns(m):
    for ai, bij, cj in itertools.product((7.99,8.01),(.499,.501),(1.999,2.001)):
        yield 'global_corner_'+str((ai,bij,cj)), [ai]*m, [[bij]*m for _ in range(m)], [cj]*m
    av = [7.99 if i%2 else 8.01 for i in range(m)]
    cv = [1.999 if j%2 else 2.001 for j in range(m)]
    yield 'checkerboard', av, [[.499 if (i+j)%2 else .501 for j in range(m)] for i in range(m)], cv
    yield 'row_stripes', av, [[.499 if i%2 else .501 for j in range(m)] for i in range(m)], cv
    yield 'column_stripes', av, [[.499 if j%2 else .501 for j in range(m)] for i in range(m)], cv
    yield 'one_column', av, [[.501 if j==0 else .499 for j in range(m)] for i in range(m)], cv
    for seed in (227, 228, 229):
        rng = random.Random(seed+100*m)
        yield ('independent_'+str(seed),
               [rng.uniform(7.99,8.01) for _ in range(m)],
               [[rng.uniform(.499,.501) for _ in range(m)] for _ in range(m)],
               [rng.uniform(1.999,2.001) for _ in range(m)])

audits = []
worst_ratio = 0.
for m in (1, 2, 3, 7, 16, 64):
    for label, a0, W0, c0 in patterns(m):
        for h in (.9, .95, 1., 1.05, 1.1):
            a,W,c = a0,W0,c0
            rows = []
            last = None
            for t in range(16):
                F,A,D,C,mk = dense_state(a,W,c)
                rows.append(dict(t=t,F=F,loss=F*F/2,m_kernel=mk))
                if t == 0:
                    assert F*F/2 < 6.5 and 37 < mk < 39
                if t == 1:
                    assert F*F/2 > 19
                if t >= 1:
                    assert abs(mk-1) < 1e-8
                    assert all(abs(x)<16 for x in a)
                    assert all(-26<x<-18 for row in W for x in row)
                    assert min(c)>1
                if t >= 2 and abs(last)>1e-11:
                    worst_ratio = max(worst_ratio,abs(F/last))
                    assert abs(F) < abs(last)/8+1e-13
                last = F
                # Exact convergence is proved analytically; floating-point
                # cancellation below this threshold is not used as evidence.
                if t>=2 and abs(F)<1e-13:
                    break
                a,W,c = update(a,W,c,h)
            audits.append(dict(width=m,initialization=label,h=h,rows=rows))

# An independent forward-mode automatic differentiator in the actual
# Euclidean a,B,c coordinates, plus centered finite differences.
class Dual:
    def __init__(self, value, tangent=0.):
        self.v, self.d = value, tangent
    def __add__(self, other):
        if not isinstance(other,Dual): other=Dual(other)
        return Dual(self.v+other.v,self.d+other.d)
    __radd__=__add__
    def __mul__(self, other):
        if not isinstance(other,Dual): other=Dual(other)
        return Dual(self.v*other.v,self.d*other.v+self.v*other.d)
    __rmul__=__mul__
    def tanh(self):
        return Dual(math.tanh(self.v),self.d/math.cosh(self.v)**2)

def euclidean_forward(flat, m):
    a = flat[:m]
    B = [flat[m+i*m:m+(i+1)*m] for i in range(m)]
    c = flat[m+m*m:]
    if isinstance(flat[0],Dual):
        u = [x.tanh() for x in c]
        v = [(sum(b*uj for b,uj in zip(row,u))*(1/math.sqrt(m))).tanh() for row in B]
    else:
        u = [math.tanh(x) for x in c]
        v = [math.tanh(math.fsum(b*uj for b,uj in zip(row,u))/math.sqrt(m)) for row in B]
    return sum(x*y for x,y in zip(a,v))*(1/m)

ad_error = fd_error = output_error = step_error = 0.
for m in (1,3,7):
    for label,a,W,c in list(patterns(m))[-2:]:
        for saturated in (False,True):
            if saturated:
                a,W,c=update(a,W,c,1.1)
            F,A,D,C,mk=dense_state(a,W,c)
            flat = a+[x/math.sqrt(m) for row in W for x in row]+c
            analytic = [x/m for x in A]+[x/(m*math.sqrt(m)) for row in D for x in row]+[x/m for x in C]
            output_error=max(output_error,abs(euclidean_forward(flat,m)-F))
            for k,g in enumerate(analytic):
                dual=[Dual(x,float(j==k)) for j,x in enumerate(flat)]
                ad=euclidean_forward(dual,m).d
                ad_error=max(ad_error,abs(ad-g))
                plus,minus=flat[:],flat[:]
                step=2e-6
                plus[k]+=step
                minus[k]-=step
                fd=(euclidean_forward(plus,m)-euclidean_forward(minus,m))/(2*step)
                fd_error=max(fd_error,abs(fd-g))
            assert abs(m*sum(x*x for x in analytic)-mk)<1e-12
            h=.95
            next_a,next_W,next_c=update(a,W,c,h)
            explicit=[x-m*h*F*g for x,g in zip(flat,analytic)]
            implemented=next_a+[x/math.sqrt(m) for row in next_W for x in row]+next_c
            step_error=max(step_error,max(abs(x-y) for x,y in zip(explicit,implemented)))
assert ad_error<1e-12 and fd_error<1e-7
assert output_error<1e-12 and step_error<1e-12

# Test the cross-gradient bound on unequal points in the entire tail
# region, including mixed signs in a and c at the lower boundary.
cross_values=[]
rng=random.Random(8227)
for m in (1,2,7,16):
    tail=[]
    for kind in range(8):
        a=[rng.choice((-16.,16.)) for _ in range(m)]
        W=[[rng.choice((-26.,-18.)) for _ in range(m)] for _ in range(m)]
        c=[rng.choice((1.,1.00001,3.,10.)) for _ in range(m)]
        if kind==0:
            W=[[-18.]*m for _ in range(m)]
            c=[1.]*m
        tail.append(dense_state(a,W,c))
    for s in tail:
        for t in tail:
            cross=(math.fsum(x*y for x,y in zip(s[1],t[1]))/m
              +math.fsum(x*y for row1,row2 in zip(s[2],t[2]) for x,y in zip(row1,row2))/(m*m)
              +math.fsum(x*y for x,y in zip(s[3],t[3]))/m)
            assert 1-1e-8<cross<1+1e-8
            cross_values.append(cross)

summary=dict(status='PASS',exact_certificates={k:dict(exact=str(v),decimal=float(v)) for k,v in cert.items()},
             dense_network_audits=len(audits),max_residual_ratio=worst_ratio,
             autodiff_gradient_max_error=ad_error,finite_difference_gradient_max_error=fd_error,
             actual_coordinate_update_max_error=step_error,independent_forward_max_error=output_error,
             tail_cross_checks=len(cross_values),tail_cross_min=min(cross_values),tail_cross_max=max(cross_values),
             process_nice=os.getpriority(os.PRIO_PROCESS,0),
             max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
             seconds=time.monotonic()-started)
assert summary['max_rss_bytes'] < 1_000_000_000
with open('dense_verification.json','w') as out:
    json.dump(dict(summary=summary,audits=audits),out,indent=2)
print(json.dumps(summary,indent=2))
