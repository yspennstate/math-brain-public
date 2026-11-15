"""Independent check of the round-3 entrance, metric, and tail constants."""
import itertools
import json
import math
import os
import random
import resource
import time
from fractions import Fraction as Q

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
started = time.monotonic()
assert os.environ['OMP_NUM_THREADS'] == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15

def exp_bounds(x):
    term = total = Q(1)
    for k in range(1, 91):
        term *= x / k
        total += term
    assert 0 <= x < 92
    return total, total + term*x/91/(1-x/92)

def tanh_bounds(x):
    lo, hi = exp_bounds(2*x)
    return (lo-1)/(lo+1), (hi-1)/(hi+1)

assert tanh_bounds(Q('1.999'))[0] > Q('.963')
assert tanh_bounds(Q('2.001'))[1] < Q('.966')
assert tanh_bounds(Q('.499')*Q('.963'))[0] > Q('.446')
assert tanh_bounds(Q('.501')*Q('.966'))[1] < Q('.450')
assert tanh_bounds(Q(1))[0] > Q(3, 4)
assert 4/exp_bounds(Q(27))[0] < Q('1e-10')

al, ah, ul, uh, vl, vh = map(Q, ('7.99','8.01','.963','.966','.446','.450'))
fl, fh = al*vl, ah*vh
dl, dh = al*(1-vh*vh)*ul, ah*(1-vl*vl)*uh
ch = ah*(1-vl*vl)*Q('.501')*(1-ul*ul)
eps = Q('1e-10')
S = Q('1.1')*Q('6.6')/(1-Q(1,8))
cert = dict(a1_lo=al-Q('1.1')*fh*vh, a1_hi=ah-Q('.9')*fl*vl,
            W1_lo=Q('.499')-Q('1.1')*fh*dh,
            W1_hi=Q('.501')-Q('.9')*fl*dl,
            c1_lo=Q('1.999')-Q('1.1')*fh*ch,
            kernel_lo=dl*dl, kernel_hi=vh*vh+dh*dh+ch*ch,
            loss0_hi=fh*fh/2, loss1_lo=Q('6.2')**2*(1-eps)/2,
            cross_error=eps+(16*eps)**2+(416*eps)**2,
            tail_a=Q('6.6')+S, tail_W_lo=-25-16*eps*S,
            tail_W_hi=-19+16*eps*S, tail_c_lo=Q('1.07')-416*eps*S)
assert Q('6.2') < cert['a1_lo'] < cert['a1_hi'] < Q('6.6')
assert -25 < cert['W1_lo'] < cert['W1_hi'] < -19
assert cert['c1_lo'] > Q('1.07')
assert 37 < cert['kernel_lo'] < cert['kernel_hi'] < 39
assert cert['loss0_hi'] < Q('6.5') and cert['loss1_lo'] > 19
assert cert['cross_error'] < Q('1e-8')
assert cert['tail_a'] < 16 and cert['tail_W_lo'] > -26
assert cert['tail_W_hi'] < -18 and cert['tail_c_lo'] > 1
assert max(1-Q('.9')*(1-Q('1e-8')),Q('1.1')*(1+Q('1e-8'))-1) < Q(1,8)
assert Q(36,39)>Q('.9') and Q(40,37)<Q('1.1')

def literal(flat, m, gradient=False):
    a, B, c = flat[:m], flat[m:m+m*m], flat[m+m*m:]
    u = list(map(math.tanh,c))
    z = [math.fsum(B[i*m+j]*u[j] for j in range(m))/math.sqrt(m) for i in range(m)]
    v = list(map(math.tanh,z))
    F = math.fsum(ai*vi for ai,vi in zip(a,v))/m
    if not gradient:
        return F
    q = [4*math.exp(-2*abs(x))/(1+math.exp(-2*abs(x)))**2 for x in z]
    ga = [vi/m for vi in v]
    gB = [a[i]*q[i]*u[j]/(m*math.sqrt(m)) for i in range(m) for j in range(m)]
    gc = [(1-u[j]**2)*math.fsum(a[i]*q[i]*B[i*m+j] for i in range(m))/(m*math.sqrt(m)) for j in range(m)]
    return F,ga+gB+gc

rng = random.Random(22704)
fd_error = ratio = 0.
audits = 0
for m in (1,2,5,16):
    for case in range(5):
        x = ([rng.uniform(7.99,8.01) for _ in range(m)]
             +[rng.uniform(.499,.501)/math.sqrt(m) for _ in range(m*m)]
             +[rng.uniform(1.999,2.001) for _ in range(m)])
        F,g = literal(x,m,True)
        if m <= 5:
            for k,gi in enumerate(g):
                xp,xm=x[:],x[:]
                xp[k]+=1e-6
                xm[k]-=1e-6
                fd_error=max(fd_error,abs((literal(xp,m)-literal(xm,m))/2e-6-gi))
        for h in (.9,1.,1.1):
            y=x[:]
            prev=None
            for t in range(14):
                f,g=literal(y,m,True)
                mk=m*math.fsum(gi*gi for gi in g)
                if t == 0:
                    assert f*f/2<6.5 and 37<mk<39
                if t == 1:
                    assert f*f/2>19
                if t>=1:
                    assert abs(mk-1)<1e-8
                    assert max(map(abs,y[:m]))<16
                    assert all(-26<math.sqrt(m)*b<-18 for b in y[m:m+m*m])
                    assert min(y[m+m*m:])>1
                if t>=2 and abs(prev)>1e-9:
                    ratio=max(ratio,abs(f/prev))
                    assert abs(f/prev)<.125
                prev=f
                y=[yi-m*h*f*gi for yi,gi in zip(y,g)]
            audits+=1
assert fd_error<1e-7
result=dict(status='PASS', exact={k:str(v) for k,v in cert.items()},
            decimals={k:float(v) for k,v in cert.items()},
            literal_Euclidean_trajectories=audits,finite_difference_error=fd_error,
            max_residual_ratio=ratio,nice=os.getpriority(os.PRIO_PROCESS,0),
            max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            seconds=time.monotonic()-started)
assert result['max_rss_bytes']<1_000_000_000
with open('recheck_dense.json','w') as f:
    json.dump(result,f,indent=2)
print(json.dumps({k:v for k,v in result.items() if k!='exact'},indent=2))
