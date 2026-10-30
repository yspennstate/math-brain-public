from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]; tests=0
def add(*xs):
    z={}
    for x in xs:
        for p,c in x.items():z[p]=z.get(p,F(0))+c
    return {p:c for p,c in z.items() if c}
def times(x,c):return {p:v*c for p,v in x.items() if v*c}
@lru_cache(None)
def log(x):
    z={}; x=F(x); assert x>0
    for m,sign in ((x.numerator,1),(x.denominator,-1)):
        k=2
        while k*k<=m:
            while m%k==0:z[k]=z.get(k,0)+sign;m//=k
            k+=1
        if m>1:z[m]=z.get(m,0)+sign
    return {p:F(v) for p,v in z.items() if v}
def num(x):return {2:F(x)} if x else {}
def entropy(p):return add(*(times(log(x),-x) for x in p if x))
def KL(p,q):return add(*(times(log(x/y),x) for x,y in zip(p,q) if x))
def CE(p,q):return add(entropy(p),KL(p,q))
def same(x,y):
    global tests
    tests+=1;assert not add(x,times(y,-1)),(x,y)
@lru_cache(None)
def interval(p):
    def ln(q):
        z=(q-1)/(q+1); s=sum((2*z**(2*j+1)/(2*j+1) for j in range(48)),F(0))
        return s,s+2*z**97/(97*(1-z*z))
    k=p.bit_length()-1; a,b=ln(F(p,2**k)); c,d=ln(F(2));return k+a/d,k+b/c
def ge(x):
    global tests
    tests+=1;assert sum((c*interval(p)[0 if c>0 else 1] for p,c in x.items()),F(0))>=0,x
def chars(a):return tuple(F(sum(x*(-1 if (s&z).bit_count()%2 else 1) for z,x in enumerate(a)),len(a)) for s in range(len(a)))
def spectrum(a):return tuple(c*c for c in chars(a))
def mixture(p,e):return tuple((1-e if j==0 else 0)+e*x for j,x in enumerate(p))
def inherited(a,r,i):
    P=spectrum(a); m=len(a)//2; kids=[tuple(x for z,x in enumerate(a) if z>>i&1==b) for b in (0,1)]; pcs=[spectrum(k) for k in kids]
    output=[[],[]]
    for s in range(m):
        j=(s%2**i)+(s//2**i)*2**(i+1); k=j+2**i
        mass=P[j]+P[k]; ref=r[j]+r[k]
        for b in (0,1):output[b].append(ref*pcs[b][s]/(2*mass) if mass else ref/2)
    norms=[sum(q) for q in output];rr=[tuple(x/n for x in q) for q,n in zip(output,norms)]
    contraction=add(KL(P,r),times(add(*(KL(p,q) for p,q in zip(pcs,rr))),-F(1,2)));ge(contraction)
    dh=add(entropy(P),times(add(*(entropy(p) for p in pcs)),-F(1,2)))
    same(CE(P,r),add(dh,contraction,times(add(*(CE(p,q) for p,q in zip(pcs,rr))),F(1,2))))
    return rr
start=time.monotonic(); family=[tuple(1 if mask>>j&1 else -1 for j in range(4)) for mask in range(16)]
family += [tuple(-1 if j==0 else 1 for j in range(8)),tuple(-1 if j&1 else 1 for j in range(8)),tuple((-1)**j.bit_count() for j in range(8)),tuple(1 if j.bit_count()>=2 else -1 for j in range(8))]
mixcases=phasecases=0
for a in family:
    P=spectrum(a); n=len(a); m=n.bit_length()-1
    uniform=tuple(F(1,n) for j in range(n));tilt=tuple(F(j+1,n*(n+1)//2) for j in range(n))
    vac=(P[0],)+tuple((1-P[0])*F(j,n*(n-1)//2) for j in range(1,n))
    for q in (uniform,tilt,vac):
        r=tuple((p+x)/2 for p,x in zip(P,q)); D=KL(P,r);ge(add(num(1),times(D,-1)))
        if q==vac:ge(add(num(1-P[0]),times(D,-1))); ge(num(sum(P[s]*s.bit_count() for s in range(n))-(1-P[0])))
        for eta in (F(1,64),F(1,8),F(1,2)):
            x=mixture(P,eta); y=mixture(r,eta)
            v=add(times(D,eta),times(KL(x,y),-1));ge(v)
            # Posterior KL on the ONLY ambiguous observed atom.
            pp=(eta*P[0]/x[0],(1-eta)/x[0]); qq=(eta*r[0]/y[0],(1-eta)/y[0])
            same(v,times(KL(pp,qq),x[0]));mixcases+=1
        for i in range(m):inherited(a,r,i);phasecases+=1
    assert time.monotonic()-start<180
literal=(-1,1,-1,1);P=spectrum(literal);r=tuple((p+F(1,4))/2 for p in P);eta=F(1,64)
v=add(times(KL(P,r),eta),times(KL(mixture(P,eta),mixture(r,eta)),-1))
same(v,times(log(F(505,504)),F(63,64)));ge(v);assert v
P=spectrum((-1,1,1,1));r=(F(1,4),F(3,16),F(1,4),F(5,16))
same(add(times(KL(P,r),eta),times(KL(mixture(P,eta),mixture(r,eta)),-1)),{})
same(KL(P,r),times(log(F(16,15)),F(1,4)));ge(KL(P,r))
out={'status':'PASS','mixture_cases':mixcases,'source_phase_queries':phasecases,'strict_guards':2,'assertions':tests,'elapsed_seconds':time.monotonic()-start,'implementation':'direct characters; separate rational log/posterior algebra; no production imports','review':'different author implementation, not external acceptance'}
(ROOT/'out/independent.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
