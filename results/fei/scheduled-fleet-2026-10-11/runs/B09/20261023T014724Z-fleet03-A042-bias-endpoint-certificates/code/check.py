from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
from math import prod
import json,time

ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();checks=0;fixtures=0;coefficients=0;zero_deficit=0
orders=(0,1,2,3)
def check(x,context=''):
    global checks
    checks+=1
    if not x:raise AssertionError((checks,context))
def cell(t):
    check(0<t<=1,'coefficient cap')
    j=0;u=t
    while u<=F(1,2):u*=2;j+=1
    z=(1-u)/(1+u)
    check(F(1,2)<u<=1 and 0<=z<F(1,3),'dyadic cell')
    return j,u,z
@lru_cache(maxsize=2048)
def tails(z):
    # ln(1/u) - L_N(z), with dyadic ln2 extracted EXACTLY.
    terms=[2*z**(2*k+1)/(2*k+1) for k in range(40)]
    rest=2*z**81/(81*(1-z*z))
    return tuple((sum(terms[N:]),sum(terms[N:])+rest) for N in orders)
def contract(vals,ps):
    n=len(ps);active=[i for i,p in enumerate(ps) if 0<p<1]
    out={}
    for y in product((0,1),repeat=len(active)):
        x=[int(p) if p in (0,1) else None for p in ps]
        for i,b in zip(active,y):x[i]=b
        out[y]=vals[tuple(x)]
    return out,tuple(ps[i] for i in active)
def evaluate(vals,ps,label):
    global fixtures,coefficients,zero_deficit
    fixtures+=1
    vals,ps=contract(vals,ps);n=len(ps);xs=list(vals);vs=[4*p*(1-p) for p in ps]
    w={x:prod(ps[i] if x[i] else 1-ps[i] for i in range(n)) for x in xs}
    c={};P={};vp={}
    for S in range(1<<n):
        numerator=sum(w[x]*vals[x]*prod(x[i]-ps[i] for i in range(n) if S>>i&1) for x in xs)
        denominator=prod(2*ps[i]*(1-ps[i]) for i in range(n) if S>>i&1)
        c[S]=numerator/denominator
        vp[S]=prod(vs[i] for i in range(n) if S>>i&1)
        P[S]=vp[S]*c[S]**2
    check(sum(P.values())==1,(label,'Parseval'))
    D=sum((S.bit_count()-1)*P[S] for S in range(1,1<<n))
    R=sum((S.bit_count()-2)*P[S] for S in range(1,1<<n) if S.bit_count()>=3)
    high=sum(P[S] for S in range(1,1<<n) if S.bit_count()>=2)
    check(high==D-R,'actual high packet bank')
    # Independent physical alternating cofactor means; singletons also supply d_i.
    bank=F(0)
    for S in range(1,1<<n):
        coefficients+=1
        inds=[i for i in range(n) if S>>i&1];other=[i for i in range(n) if not S>>i&1]
        m=F(0);second=F(0)
        for y in product((0,1),repeat=len(other)):
            fixed=dict(zip(other,y));value=F(0)
            for bits in product((0,1),repeat=len(inds)):
                x=fixed|dict(zip(inds,bits))
                value+=F((-1)**(len(inds)-sum(bits)),2**len(inds))*vals[tuple(x[i] for i in range(n))]
            weight=prod(ps[i] if fixed[i] else 1-ps[i] for i in other)
            m+=weight*value;second+=weight*value*value
        check(c[S]==m,(label,S,'independent derivative'))
        check(abs(m)<=1)
        if len(inds)==1:
            t=abs(m);V=second-m*m
            check(second>=t,'Boolean derivative admission')
            check(V>=t*(1-t),'singleton variance bank')
            bank+=vp[S]*V
    check(bank==2*D-R,'same global reserve')
    if D==0:zero_deficit+=1
    totals=[[F(0),F(0)] for _ in orders]
    single=[[F(0),F(0)] for _ in orders]
    for S in range(1,1<<n):
        t=abs(c[S])
        if not t:continue
        j,u,z=cell(t)
        if t==1:check(j==0 and z==0,'unit endpoint')
        tt=tails(z)
        for N in orders:
            lo,hi=(2*P[S]*a for a in tt[N]);totals[N][0]+=lo;totals[N][1]+=hi
            A=(2*N+1)*9**N;epsilon=F(3,2*A);beta=F(2,A)
            check(lo>=0,'monotone logarithm tail')
            check(hi<=epsilon*P[S],(label,S,N,'mass-weighted tail'))
            if S.bit_count()==1:
                if t>F(1,2) and t<1:
                    # The singularity cancellation used in equation(5).
                    check(4*t/(1+t)/(1-z*z)==1+t,'rational cancellation')
                if t<=F(1,2):check(t*t<=t*(1-t),'small-mean branch')
                check(hi<=beta*vp[S]*t*(1-t),(label,S,N,'endpoint bound'))
                single[N][0]+=lo;single[N][1]+=hi
    for N in orders:
        A=(2*N+1)*9**N;cap=F(11*D-7*R,2*A)
        check(single[N][1]<=F(2,A)*bank,'singleton sum retains owner')
        check(totals[N][1]<=cap,(label,N,'full degree-refined error'))
        check(cap<=F(11,2*A)*D)
        if D==0:check(totals[N][1]==0,'zero deficit exact')

laws2=[(F(1,2),F(1,2)),(F(1,64),F(63,64)),(F(1,2**20),F(1,2**12))]
laws3=[(F(1,2),)*3,(F(1,8),F(1,4),F(3,4)),(F(1,64),F(1,4096),F(1,16)),(F(63,64),F(4095,4096),F(15,16)),(F(0),F(1,3),F(2,5)),(F(0),F(1),F(0))]
laws4=[(F(1,2),)*4,(F(1,3),F(1,4),F(3,5),F(5,6)),(F(1,16),F(1,256),F(1,65536),F(1,16)),(1-F(1,1024),F(1,4096),F(1,256),1-F(1,16384))]
masks4=[0,65535,1,32768,27030,38505,56067,33152,232,59432,42405,43690]
for n,masks,laws in [(2,range(16),laws2),(3,range(256),laws3),(4,masks4,laws4)]:
    xs=list(product((0,1),repeat=n))
    for mask in masks:
        vals={x:F(1 if mask>>i&1 else -1) for i,x in enumerate(xs)}
        for ps in laws:evaluate(vals,ps,(n,mask,tuple(map(str,ps))))

# All-r formulas are proved analytically; these finite checks calibrate empty normalization.
for r in range(1,13):
    q=F(1,4**r);P=q;t=F(1,2**r)
    j,u,z=cell(t);check(j==r and u==1 and z==0)
    check(all(a==b==0 for a,b in tails(z)))
    check(sum(__import__('math').comb(2*r,k)*q for k in range(2*r+1))==1)
    # Coefficients of ln2 in corrected entropy and full entropy.
    corrected=2*r*(1-q);full=2*r;empty=2*r*q
    check(corrected+empty==full)
    D=r-1+q;check(D>0)
    residual=corrected-2*D
    check(residual==2*(1-(r+1)*q))

# Counterexample to dropping Boolean derivative admission: scaled real literal.
t=F(2,3);j,u,z=cell(t);check(z==F(1,5));check(t*t<t)
for N in orders:check(tails(z)[N][0]>0,'real literal has positive error at Delta=0')

result={'status':'PASS','Boolean_fixtures':fixtures,'actual_nonempty_coefficients':coefficients,'zero_deficit_fixtures':zero_deficit,'bent_formula_cases':12,'nonBoolean_controls':4,'orders':list(orders),'exact_assertions':checks,'runtime_seconds':time.perf_counter()-start,'error_constants':{str(N):str(F(11,2*(2*N+1)*9**N)) for N in orders},'arithmetic':'Fraction identities and outward rational positive-tail bounds; dyadic ln2 retained symbolically'}
(ROOT/'out/CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
