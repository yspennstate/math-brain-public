"""Independent A045 exact product-spectrum and prime-boundary audit, version 1."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from math import comb
import json, time, sys

ROOT = Path(__file__).resolve().parents[1]
PILOT = '--pilot' in sys.argv
START = time.perf_counter()
checks = 0
def ck(x):
    global checks
    checks += 1
    assert x, checks
    if checks % 200 == 0:
        assert time.perf_counter()-START < 55, 'frozen runtime exceeded'

def spec(vals, ps):
    c = list(map(Q, vals)); n = len(ps)
    for i,p in enumerate(ps):
        for s in range(1<<n):
            if s >> i & 1: continue
            lo,hi = c[s],c[s|1<<i]
            c[s] = (1-p)*lo+p*hi
            c[s|1<<i] = (hi-lo)/2
    v = [Q(1)]*(1<<n)
    for s in range(1,1<<n):
        bit=s & -s; i=bit.bit_length()-1
        v[s]=v[s^bit]*4*ps[i]*(1-ps[i])
    mass=[v[s]*c[s]**2 for s in range(1<<n)]
    ck(sum(mass)==1)
    return c,v,mass

def edge(vals,ps,i):
    t=Q(0); d=Q(0)
    for s in range(len(vals)):
        if s>>i&1:continue
        w=Q(1)
        for j,p in enumerate(ps):
            if i!=j:w*=p if s>>j&1 else 1-p
        D=Q(vals[s|1<<i]-vals[s],2)
        t+=w*D;d+=w*D*D
    return t,d

def scale(t):
    t=abs(t); j=0
    if t==0:return 0
    while t<=Q(1,2):t*=2;j+=1
    ck(Q(1,2)<t<=1)
    return j

def prime_rows(vals,n):
    for a in range(1,1<<n):
        if not 2<=a.bit_count()<=n-1:continue
        aa=[s for s in range(1<<n) if s & ~a==0]
        bb=[s for s in range(1<<n) if s & a==0]
        rows={tuple(vals[s|t] for t in bb) for s in aa}
        ck(len(rows)==3)

records=[]
arities=[4] if PILOT else [3,4,5,6]
exponents=[6,10] if PILOT else [5,6,8,10,14,20]
for n in arities:
    m=n-2; vals=[1 if s.bit_count()>=2 else -1 for s in range(1<<n)]
    prime_rows(vals,n)
    for k in exponents:
        e=Q(1,2**k); ps=[Q(1,2)]*2+[e]*m
        ck(m*e<=Q(1,8))
        c,v,p=spec(vals,ps)
        I=sum(s.bit_count()*p[s] for s in range(1,1<<n))
        V=1-p[0]; delta=I-V
        R=sum((s.bit_count()-2)*p[s] for s in range(1,1<<n) if s.bit_count()>=3)
        j=[scale(x) for x in c]
        J1=sum(p[1<<i]*j[1<<i] for i in range(n))
        Jhi=sum(p[s]*j[s] for s in range(1,1<<n) if s.bit_count()>=2)
        Is=Q(0)
        for i in range(n):
            t,d=edge(vals,ps,i)
            ck(t==c[1<<i] and d==t and 0<t<=Q(1,2))
            Is+=v[1<<i]*d
        ck(Is==I)
        ck(2*delta-R==sum(v[1<<i]*(c[1<<i]-c[1<<i]**2) for i in range(n)))
        p0=(1-e)**m;p1=m*e*(1-e)**(m-1)
        ck(c[3]==(p0-p1)/2)
        ck(Q(3,8)<=c[3]<=Q(1,2) and j[3]==1)
        ck(Jhi>=p[3]>=Q(9,64))
        A=comb(m,2)*e**2
        ck(c[1]>=Q(1,2)*(1-A) and c[2]==c[1] and j[1]==j[2]==1)
        ck(-Q(1,2)<=c[0]<=0)
        ck(V>=Q(3,4) and I<=1+2*m*e and delta<=Q(1,4)+2*m*e)
        U=2*delta-J1 # upper bound for Bstar/ln4 + R
        ck(0<=U<=4*m*e+A<=5*m*e)
        ck(Jhi>=Q(9,320*m)/e*U)
        # Endpoint is a physical contraction; no zero variance is divided out.
        cc,vv,pp=spec(vals,[Q(1,2)]*2+[Q(0)]*m)
        ck(pp[0]==pp[1]==pp[2]==pp[3]==Q(1,4))
        ck(all(pp[s]==0 for s in range(4,1<<n)))
        records.append(dict(n=n,e=str(e),Delta=str(delta),R=str(R),
                            Jhi_over_ln4=str(Jhi),reserve_upper_over_ln4=str(U),
                            rigorous_ratio_lower=str(Q(9,320*m)/e)))

# Independent uniform equality census: integer Walsh versus physical edge counts.
census=[]
for n in (range(4) if PILOT else range(5)):
    N=1<<n; hits=0
    for mask in range(1<<N):
        f=[1 if mask>>s&1 else -1 for s in range(N)]
        w=f.copy()
        step=1
        while step<N:
            for a in range(0,N,2*step):
                for k in range(step):
                    x,y=w[a+k],w[a+k+step]
                    w[a+k],w[a+k+step]=x+y,y-x
            step*=2
        ck(sum(x*x for x in w)==N*N)
        zero=True
        for i in range(n):
            ds=[(f[s|1<<i]-f[s])//2 for s in range(N) if not(s>>i&1)]
            t=abs(sum(ds)); d=sum(x*x for x in ds)
            ck(abs(w[1<<i])==2*t)
            if d!=t or t not in {0,N//4,N//2}:zero=False
        # n=1: N//4 is zero, so the same integer test still applies.
        if zero:hits+=1
    expected=2+2*n+8*comb(n,2)+8*comb(n,3)
    ck(hits==expected)
    census.append(dict(n=n,tables=1<<N,zero_reserve=hits))

result=dict(status='PASS',helper_version=1,pilot=PILOT,checks=checks,
            seconds=round(time.perf_counter()-START,6),census=census,
            prime_boundary_records=records,
            scope='Exact rational upper bounds; Bstar nonnegativity is analytic; no logarithmic numerical inference.')
dest=ROOT/'out'/('PILOT.json' if PILOT else 'CHECKS.json')
dest.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['prime_boundary_records']}))
