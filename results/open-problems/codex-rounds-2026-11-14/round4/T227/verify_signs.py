"""Exact certificate and asymmetric full-network audits for signed initialization.

Standard library only; all exact claims use fractions. Numerical audits use
small widths conditional on the deterministic event, not a claimed Monte
Carlo estimate of the theorem's large-width probability.
"""
import itertools
import json
import math
import os
import random
import resource
import time
from fractions import Fraction as Q

resource.setrlimit(resource.RLIMIT_CPU, (120,120))
started=time.monotonic()
assert os.environ['OMP_NUM_THREADS']=='1'
assert os.getpriority(os.PRIO_PROCESS,0)>=15

def exp_bounds(x,n=80):
    assert 0<=x<n+2
    term=total=Q(1)
    for k in range(1,n+1):
        term=term*x/k
        total+=term
    return total,total+term*x/(n+1)/(1-x/(n+2))

def tanh_bounds(x):
    lo,hi=exp_bounds(2*x)
    return (lo-1)/(lo+1),(hi-1)/(hi+1)

al,ah=Q('7.99'),Q('8.01')
ul,uh=Q('.96395'),Q('.96410')
vl,vh=Q('.407'),Q('.487')
wl,wh,absw=Q('.449'),Q('.551'),Q('1.001')
u_mid,u_rad=(ul+uh)/2,(uh-ul)/2
zl,zh=u_mid*wl-u_rad*absw,u_mid*wh+u_rad*absw
assert tanh_bounds(Q('1.999'))[0]>ul
assert tanh_bounds(Q('2.001'))[1]<uh
assert tanh_bounds(zl)[0]>vl and tanh_bounds(zh)[1]<vh
kl,kh=al*(1-vh*vh),ah*(1-vl*vl)
k_mid,k_rad=(kl+kh)/2,(kh-kl)/2
dl,dh=kl*ul,kh*uh
ch=(1-ul*ul)*(k_mid*wh+k_rad*absw)
fl,fh=al*vl,ah*vh
hl,hh=Q('.9'),Q('1.1')
eps,delta,rho=Q('2e-8'),Q('1e-6'),Q(1,8)
S=hh*Q('6.9')/(1-rho)
cert=dict(
    u_mid=u_mid,u_rad=u_rad,z_lower=zl,z_upper=zh,
    k_lower=kl,k_upper=kh,C0_abs_upper=ch,
    F0_lower=fl,F0_upper=fh,D0_lower=dl,D0_upper=dh,
    a1_lower=al-hh*fh*vh,a1_upper=ah-hl*fl*vl,
    W1_lower=-absw-hh*fh*dh,W1_upper=absw-hl*fl*dl,
    c1_lower=Q('1.999')-hh*fh*ch,
    m_kernel0_lower=dl*dl,m_kernel0_upper=vh*vh+dh*dh+ch*ch,
    loss0_upper=fh*fh/2,loss1_lower=Q('5.8')**2*(1-eps)/2,
    cross_error=eps+(18*eps)**2+(540*eps)**2,
    contraction_upper=max(1-hl*(1-delta),hh*(1+delta)-1),
    total_step_residual=S,tail_a_upper=Q('6.9')+S,
    tail_W_lower=-29-18*eps*S,tail_W_upper=-16+18*eps*S,
    tail_c_lower=Q('.84')-540*eps*S)
assert cert['a1_lower']>Q('5.8') and cert['a1_upper']<Q('6.9')
assert cert['W1_lower']>-29 and cert['W1_upper']<-16
assert cert['c1_lower']>Q('.84')
assert cert['m_kernel0_lower']>34 and cert['m_kernel0_upper']<43
assert cert['loss0_upper']<8 and cert['loss1_lower']>16
assert tanh_bounds(Q('.8'))[0]>Q('.66')
assert 4/exp_bounds(Q('19.8'))[0]<eps
assert cert['cross_error']<delta and cert['contraction_upper']<rho
assert cert['tail_a_upper']<18
assert cert['tail_W_lower']>-30 and cert['tail_W_upper']<-15
assert cert['tail_c_lower']>Q('.8')
# At m=20,000: failure <=80,000/e^25 <2e-6. The function
# m exp(-m/800) decreases for all m>800.
assert exp_bounds(Q(25))[0]>40_000_000_000

def sech2(x):
    e=math.exp(-2*abs(x))
    return 4*e/(1+e)**2

def state(a,W,c):
    m=len(a)
    u=[math.tanh(x) for x in c]
    z=[math.fsum(w*uj for w,uj in zip(row,u))/m for row in W]
    v=[math.tanh(x) for x in z]
    k=[ai*sech2(zi) for ai,zi in zip(a,z)]
    D=[[ki*uj for uj in u] for ki in k]
    C=[sech2(c[j])*math.fsum(k[i]*W[i][j] for i in range(m))/m for j in range(m)]
    F=math.fsum(ai*vi for ai,vi in zip(a,v))/m
    mk=math.fsum(vi*vi for vi in v)/m+math.fsum(x*x for row in D for x in row)/(m*m)+math.fsum(x*x for x in C)/m
    return F,v,D,C,mk

def step(a,W,c,h):
    F,v,D,C,_=state(a,W,c)
    return ([x-h*F*g for x,g in zip(a,v)],
            [[x-h*F*g for x,g in zip(row,dr)] for row,dr in zip(W,D)],
            [x-h*F*g for x,g in zip(c,C)])

def sign_patterns(m):
    for fraction in (.225,.25,.275):
        k=round(m*fraction)
        yield 'circulant_'+str(fraction),[[(-1 if (j-i)%m<k else 1) for j in range(m)] for i in range(m)]
    # Each block is circulant; top rows and left columns have 22.5%
    # negatives, bottom rows and right columns 27.5% negatives.
    n=m//2
    b=m//40
    yield 'four_blocks',[[(-1 if (j%n-i%n)%n<((4 if i<n and j<n else 6 if i>=n and j>=n else 5)*b) else 1) for j in range(m)] for i in range(m)]

audits=[]
worst=0.
for m in (40,80,160):
    for pattern,signs in sign_patterns(m):
        assert all(.45-1e-12<=sum(row)/m<=.55+1e-12 for row in signs)
        assert all(.45-1e-12<=sum(signs[i][j] for i in range(m))/m<=.55+1e-12 for j in range(m))
        for kind in ('random','aligned_corners','reversed_corners'):
            rng=random.Random(227+m)
            if kind=='random':
                a=[rng.uniform(7.99,8.01) for _ in range(m)]
                c=[rng.uniform(1.999,2.001) for _ in range(m)]
                W=[[s*rng.uniform(.999,1.001) for s in row] for row in signs]
            else:
                reverse=kind=='reversed_corners'
                a=[8.01 if ((i<m//2)^reverse) else 7.99 for i in range(m)]
                c=[2.001 if ((j<m//2)^reverse) else 1.999 for j in range(m)]
                W=[[s*(1.001 if ((i+j)%2)^reverse else .999) for j,s in enumerate(row)] for i,row in enumerate(signs)]
            for h in (.9,1.,1.1):
                aa,ww,cc=a,W,c
                rows=[]
                prev=None
                for t in range(13):
                    F,A,D,C,mk=state(aa,ww,cc)
                    rows.append(dict(t=t,F=F,loss=F*F/2,m_kernel=mk))
                    if t==0:
                        assert F*F/2<8 and 34<mk<43
                    if t==1:
                        assert F*F/2>16
                    if t>=1:
                        assert max(map(abs,aa))<18
                        assert all(-30<x<-15 for row in ww for x in row)
                        assert min(cc)>.8 and abs(mk-1)<1e-6
                    if t>=2 and abs(prev)>1e-9:
                        worst=max(worst,abs(F/prev))
                        assert abs(F/prev)<.125
                    prev=F
                    aa,ww,cc=step(aa,ww,cc,h)
                audits.append(dict(width=m,pattern=pattern,kind=kind,h=h,rows=rows))

# Literal forward expression and finite differences in the actual B metric.
def forward(x,m):
    a=x[:m]
    B=x[m:m+m*m]
    c=x[m+m*m:]
    return math.fsum(a[i]*math.tanh(math.fsum(B[i*m+j]*math.tanh(c[j]) for j in range(m))/math.sqrt(m)) for i in range(m))/m

fd_error=update_error=0.
for m in (2,3,7):
    rng=random.Random(m+227)
    a=[rng.uniform(7.99,8.01) for _ in range(m)]
    c=[rng.uniform(1.999,2.001) for _ in range(m)]
    W=[[rng.choice((-1,1))*rng.uniform(.999,1.001) for _ in range(m)] for _ in range(m)]
    for phase in range(2):
        if phase:
            a=[rng.choice((-18.,18.)) for _ in range(m)]
            c=[.8]*m
            W=[[-15.]*m for _ in range(m)]
        F,A,D,C,_=state(a,W,c)
        x=a+[w/math.sqrt(m) for row in W for w in row]+c
        grad=[v/m for v in A]+[d/(m*math.sqrt(m)) for row in D for d in row]+[g/m for g in C]
        for k,g in enumerate(grad):
            xp,xm=x[:],x[:]
            xp[k]+=1e-6
            xm[k]-=1e-6
            fd_error=max(fd_error,abs((forward(xp,m)-forward(xm,m))/2e-6-g))
        an,wn,cn=step(a,W,c,.9)
        actual=[xi-.9*m*F*g for xi,g in zip(x,grad)]
        aux=an+[w/math.sqrt(m) for row in wn for w in row]+cn
        update_error=max(update_error,max(abs(x-y) for x,y in zip(actual,aux)))
assert fd_error<1e-7 and update_error<1e-12

summary=dict(status='PASS',certificates={k:dict(exact=str(v),decimal=float(v)) for k,v in cert.items()},
             network_audits=len(audits),max_residual_ratio=worst,
             finite_difference_gradient_error=fd_error,Euclidean_update_error=update_error,
             probability_failure_bound_at_20000=80000*math.exp(-25),
             nice=os.getpriority(os.PRIO_PROCESS,0),
             max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
             seconds=time.monotonic()-started)
assert summary['max_rss_bytes']<1_000_000_000
with open('signed_verification.json','w') as f:
    json.dump(dict(summary=summary,audits=audits),f,indent=2)
print(json.dumps(summary,indent=2))
