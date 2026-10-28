from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import json,time

ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0; endpoint=0
def check(x):
    global checks
    checks+=1
    assert x, checks
def rawlog(x):
    z=(x-1)/(x+1); s=F(0); zz=z
    for k in range(40):
        s+=2*zz/(2*k+1); zz*=z*z
    err=2*abs(z)**81/(81*(1-z*z))
    return s-err,s+err
L2=rawlog(F(2))
@lru_cache(None)
def log(x):
    assert x>0
    k=0
    while x<1: x*=2; k-=1
    while x>2: x/=2; k+=1
    a,b=rawlog(x)
    return (a+k*L2[0],b+k*L2[1]) if k>=0 else (a+k*L2[1],b+k*L2[0])
def h(x):
    if not x:return F(0),F(0)
    a,b=log(1/(x*x));return x*x*a,x*x*b
def endpoint_check(j,a,b,V):
    global endpoint
    if not 0<b<=F(1,4):return
    endpoint+=1
    check(abs(a)<=b);check(V==b-a*a);check(b*(1-b)<=V<=b)
    lo,hi=h(j+a)
    if j==0:
        # compare to an outward lower bound on RHS; exact a=0 included
        check(lo>=0)
        if abs(a)==b:
            # Exact equality: both expressions have the SAME logarithm.
            # Comparing separate outward endpoints cannot certify equality.
            check(V==b*(1-b))
            check(a*a/V==b/(1-b))
        else:
            check(hi/V<=2*b*log(1/b)[0]/(1-b))
    elif abs(j)==1:
        target=-2*j*a/b
        check(lo/V>=target-8*b);check(hi/V<=target+8*b)

laws=[(F(1,2),)*3,(F(1,8),F(1,4),F(3,4)),(F(1,64),F(1,4096),F(1,16)),(F(63,64),F(4095,4096),F(15,16)),(F(1,1024),F(1,2),F(1023,1024))]
xs=list(product((0,1),repeat=3));fixtures=0;profiles=0
for mask in range(256):
    vals={x:F(1 if mask>>i&1 else -1) for i,x in enumerate(xs)}
    for ps in laws:
        fixtures+=1
        vs=[4*p*(1-p) for p in ps]
        weights={x:__import__('math').prod(ps[i] if x[i] else 1-ps[i] for i in range(3)) for x in xs}
        # normalized centered moments c_S; squared basis norm v_S is kept rational
        cs={};P={}
        for S in range(8):
            num=sum(weights[x]*vals[x]*__import__('math').prod(x[i]-ps[i] for i in range(3) if S>>i&1) for x in xs)
            den=__import__('math').prod(2*ps[i]*(1-ps[i]) for i in range(3) if S>>i&1)
            cs[S]=num/den
            P[S]=cs[S]**2*__import__('math').prod(vs[i] for i in range(3) if S>>i&1)
        check(sum(P.values())==1)
        for S in range(1,8):
            profiles+=1; inds=[i for i in range(3) if S>>i&1];other=[i for i in range(3) if not S>>i&1]
            distribution=[]
            for y in product((0,1),repeat=len(other)):
                fixed=dict(zip(other,y));z=F(0)
                for t in product((0,1),repeat=len(inds)):
                    d=fixed|dict(zip(inds,t));x=tuple(d[i] for i in range(3))
                    z+=(-1)**(len(inds)-sum(t))*vals[x]/2
                check(z.denominator==1)
                w=__import__('math').prod(ps[i] if fixed[i] else 1-ps[i] for i in other)
                distribution.append((w,z))
            m=sum(w*z for w,z in distribution);V=sum(w*(z-m)**2 for w,z in distribution)
            scale=F(__import__('math').prod(vs[i] for i in inds),4**(len(inds)-1))
            W=sum(P[T] for T in range(8) if T!=S and T&S==S)
            check(m==2**(len(inds)-1)*cs[S]);check(scale*V==W)
            for j in (-1,0,1):
                b=sum(w*(z-j)**2 for w,z in distribution)
                endpoint_check(j,m-j,b,V)
            if mask==128 and S.bit_count()==2:
                i=other[0];check(m==ps[i]);check(V==ps[i]*(1-ps[i]));check(W==P[7])
                check(V>0)

standalone=0
for j,d,p in product((-1,0,1),(-3,-2,-1,1,2,3),(F(1,16),F(1,64),F(1,1024))):
    standalone+=1;a=p*d;b=p*d*d
    endpoint_check(j,a,b,b-a*a)

bernoulli=0
for k in range(2,22):
    for p in (F(1,2**k),1-F(1,2**k)):
        bernoulli+=1
        phi_lo=2*p*log(1/p)[0]/(1-p);phi_hi=2*p*log(1/p)[1]/(1-p)
        check(phi_lo>0);check(phi_hi<2)
        if p<F(1,2):check(phi_hi<=4*p*log(1/p)[0])
        else:
            e=1-p;target=2-e;err=e*e/(3*(1-e))
            check(phi_lo>=target-err);check(phi_hi<=target)

# Independent phase-free rejection of the fair AND3 deleted spectrum.
check(all(F(j-4,4)**2!=F(3,5) for j in range(9)))
check((F(9,16)/(1-F(1,16)))==F(3,5))
result={'status':'PASS','boolean_fixtures':fixtures,'actual_profiles':profiles,'standalone_evaluated':standalone,'bernoulli_endpoints':bernoulli,'admitted_endpoint_checks':endpoint,'exact_assertions':checks,'seconds':time.perf_counter()-start,'arithmetic':'Fraction and outward rational log intervals; no floats in sign tests'}
(ROOT/'out/checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
