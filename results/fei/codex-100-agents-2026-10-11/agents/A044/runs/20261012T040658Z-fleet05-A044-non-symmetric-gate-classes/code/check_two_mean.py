"""Frozen A044-two-mean-v2. Fractions, formal logs and proved log intervals."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from functools import lru_cache
from math import isqrt
import time,json
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0
def check(x):
    global checks
    checks+=1
    assert x
def prod(xs):
    z=Q(1)
    for x in xs:z*=x
    return z
@lru_cache(None)
def factors(n):
    if n==1:return {}
    sq=isqrt(n)
    if sq*sq==n:return {p:2*k for p,k in factors(sq).items()}
    d={};p=2
    while p*p<=n:
        while n%p==0:d[p]=d.get(p,0)+1;n//=p
        sq=isqrt(n)
        if n>1 and sq*sq==n:
            for k,v in factors(sq).items():d[k]=d.get(k,0)+2*v
            return d
        p+=1
    if n>1:d[n]=d.get(n,0)+1
    return d
def addlog(d,c,x):
    check(x>0)
    for n,s in [(x.numerator,1),(x.denominator,-1)]:
        for p,k in factors(n).items():d[p]=d.get(p,Q(0))+c*s*k
def combine(*parts):
    d={}
    for c,x in parts:
        for p,k in x.items():d[p]=d.get(p,Q(0))+c*k
    return {p:c for p,c in d.items() if c}
def lnat(x):
    z=(x-1)/(x+1);N=32
    lo=2*sum((z**(2*k+1)/Q(2*k+1) for k in range(N)),Q(0))
    return lo,lo+2*z**(2*N+1)/(Q(2*N+1)*(1-z*z))
LN2=lnat(Q(2))
@lru_cache(None)
def lnprime(p):
    k=p.bit_length()-1; l,u=lnat(Q(p,2**k))
    return l+k*LN2[0],u+k*LN2[1]
def interval(d,c=Q(0)):
    lo=hi=c
    for p,a in d.items():
        l,u=lnprime(p);lo+=a*(l if a>=0 else u);hi+=a*(u if a>=0 else l)
    return lo,hi
def ent(P,biases):
    d={}
    for mask,p in enumerate(P):
        if mask and p:
            sigma=prod(4*q*(1-q) for i,q in enumerate(biases) if mask>>i&1)
            addlog(d,p,sigma/p)
    return combine((Q(1),d))
def spectrum(values,biases):
    n=len(biases);rows=[]
    for x,f in values.items():rows.append((x,f,prod(q if b else 1-q for q,b in zip(biases,x))))
    P=[]
    for mask in range(2**n):
        S=[i for i in range(n) if mask>>i&1]
        numerator=sum((w*f*prod(Q(x[i])-biases[i] for i in S) for x,f,w in rows),Q(0))
        P.append(numerator**2/prod(biases[i]*(1-biases[i]) for i in S))
    check(sum(P)==sum((w*f*f for x,f,w in rows),Q(0)))
    return P
def delta(P):return sum(((mask.bit_count()-1)*p for mask,p in enumerate(P) if mask),Q(0))
def pivotal_check(P,values,biases):
    for i,q in enumerate(biases):
        pivotal=sum((prod(b if xj else 1-b for xj,b in zip(x,biases)) for x,f in values.items() if f!=values[x[:i]+(1-x[i],)+x[i+1:]]),Q(0))
        check(sum((p for mask,p in enumerate(P) if mask>>i&1),Q(0))==4*q*(1-q)*pivotal)
def ell(d,c,r):
    addlog(d,2*c*(1-r),Q(2));addlog(d,-2*c*r,r)
grid=[Q(1,16),Q(1,4),Q(1,2),Q(3,4),Q(15,16)]
cases=[];rows=[]
for q,r,s in product(grid,repeat=3):cases.append((q,2*r-1,2*s-1,'grid'))
for q,e in product(grid,[Q(1,4),Q(1,16),Q(1,256),Q(1,65536)]):
    m0,m1=(-1+e,1-e*e) if q<=Q(1,2) else (-1+e*e,1-e)
    cases.append((q,m0,m1,'fixed-q-boundary'))
for e in [Q(1,4),Q(1,16),Q(1,256),Q(1,65536)]:cases.append((e,-1+e,1-e*e,'co-degenerating-boundary'))
for q,m0,m1,kind in cases:
    bs=[q,(1+m0)/2,(1+m1)/2];v0=1-m0*m0;v1=1-m1*m1;d=abs(m1-m0);w=v0+v1
    vals={x:Q(2*x[1+x[0]]-1) for x in product([0,1],repeat=3)}
    P=spectrum(vals,bs)
    expected=[((1-q)*m0+q*m1)**2,q*(1-q)*d*d,(1-q)**2*v0,q*(1-q)*v0,q*q*v1,q*(1-q)*v1,Q(0),Q(0)]
    check(P==expected);pivotal_check(P,vals,bs)
    D=q*(1-q)*w;check(delta(P)==D)
    check(w>=d*(2-d))
    E=ent(P,bs);formula={}
    if d:addlog(formula,q*(1-q)*d*d,Q(4)/(d*d))
    ell(formula,(1-q)*v0,1-q);ell(formula,q*v1,q)
    check(E==combine((Q(1),formula)))
    # K(q)*D*ln2-E = 2D + formal logarithms.
    t=max(q,1-q);margin={}
    addlog(margin,2*D,Q(2));addlog(margin,-2*D*t/(1-t),t)
    margin=combine((Q(1),margin),(-Q(1),E))
    lo,hi=interval(margin,2*D);check(lo>0)
    if kind!='grid':
        l,u=interval(E);ratio=(l/(D*LN2[1]),u/(D*LN2[0]))
        if kind=='co-degenerating-boundary' and q==Q(1,65536):check(ratio[0]>Q(777,100))
        rows.append({'kind':kind,'q':str(q),'m0':str(m0),'m1':str(m1),'deficit':str(D),'ratio_lower':str(ratio[0]),'ratio_upper':str(ratio[1]),'ratio_decimal_for_display':float((ratio[0]+ratio[1])/2)})
profile_cases=0
for mask in range(16):
  for qs in [(Q(1,4),Q(1,2)),(Q(1,4),Q(3,4)),(Q(1,2),Q(1,2))]:
    for m0,m1 in [(Q(-1,2),Q(1,2)),(Q(-3,4),Q(7,8))]:
      ms=[m1 if mask>>c&1 else m0 for c in range(4)];vs=[1-m*m for m in ms]
      u=(m0+m1)/2;t=(m1-m0)/2;w=2-m0*m0-m1*m1
      bs=list(qs)+[(1+m)/2 for m in ms]
      vals={x:Q(2*x[2+x[0]+2*x[1]]-1) for x in product([0,1],repeat=6)}
      P=spectrum(vals,bs);EF=ent(P,bs)
      bvals={x:Q(1 if mask>>(x[0]+2*x[1])&1 else -1) for x in product([0,1],repeat=2)}
      hvals={x:u+t*b for x,b in bvals.items()}
      PB=spectrum(bvals,list(qs));PH=spectrum(hvals,list(qs));EB=ent(PB,qs);EH=ent(PH,qs)
      varB=sum(PB[1:]);Ib=sum((s.bit_count()*p for s,p in enumerate(PB)),Q(0))
      D=Q(0);EC={}
      for c in range(4):
        rs=[q if c>>i&1 else 1-q for i,q in enumerate(qs)];p=prod(rs)
        D+=p*vs[c]*sum((1-r for r in rs),Q(0))
        for r in rs:ell(EC,p*vs[c],r)
      check(EF==combine((Q(1),EH),(Q(1),EC)))
      check(delta(P)==t*t*delta(PB)+D)
      expected=combine((t*t,EB));addlog(expected,t*t*varB,1/(t*t))
      check(EH==combine((Q(1),expected)))
      check(D>=w*Ib/4)
      residual=combine((Q(1),EF),(-t*t,EB));margin={}
      addlog(margin,2*D,Q(2));margin=combine((Q(1),margin),(-Q(1),residual))
      check(interval(margin,4*D)[0]>0)
      profile_cases+=1
check(len(cases)==149);check(profile_cases==96)
result={'helper_version':'A044-two-mean-v2','result':'PASS','mux_cases':len(cases),'profile_cases':profile_cases,'total_cases':len(cases)+profile_cases,'exact_assertions':checks,'runtime_seconds':time.perf_counter()-start,'float_use':'only decimal display of independently certified rational intervals','boundary_records':rows}
(ROOT/'out/CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='boundary_records'}))
