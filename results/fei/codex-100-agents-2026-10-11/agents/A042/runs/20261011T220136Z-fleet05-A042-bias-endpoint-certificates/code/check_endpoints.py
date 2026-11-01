"""Exact endpoint identities, v1. Run with python -X utf8; no dependencies."""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json, time

ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic()
assertions=0
def check(x):
    global assertions
    assert x
    assertions+=1

def spectrum(table,p):
    n=len(p); cs={}; ps={}; ws={}
    for s in range(1<<n):
        raw=F(0)
        for x in product((0,1), repeat=n):
            mass=F(1); char=F(1)
            for i in range(n):
                mass*=p[i] if x[i] else 1-p[i]
                if s>>i&1: char*=x[i]-p[i]
            raw+=mass*table[x]*char
        den=F(1); w=F(1)
        for i in range(n):
            if s>>i&1: den*=2*p[i]*(1-p[i]); w*=4*p[i]*(1-p[i])
        cs[s]=raw/den; ws[s]=w; ps[s]=w*cs[s]**2
    return cs,ps,ws

fixtures=0; zero_deficit=0; unit_atoms=0
for n in (1,2,3):
    xs=list(product((0,1),repeat=n))
    for bits in range(1<<(1<<n)):
        table={x: F(1 if bits>>k&1 else -1) for k,x in enumerate(xs)}
        for j in range(n):
            others=[i for i in range(n) if i!=j]
            pbase=[F(1,3) if k%2==0 else F(2,5) for k in range(n-1)]
            children=[]
            for value in (0,1):
                child={}
                for y in product((0,1),repeat=n-1):
                    x=list(y); x.insert(j,value); child[y]=table[tuple(x)]
                children.append(spectrum(child,pbase))
            c0,P0,w=children[0]; c1,P1,_=children[1]
            D0=sum((s.bit_count()-1)*P0[s] for s in P0 if s)
            L=sum(2*(s.bit_count()-1)*w[s]*c0[s]*(c1[s]-c0[s]) for s in c0 if s)
            L+=sum(s.bit_count()*w[s]*(c1[s]-c0[s])**2 for s in c0)
            Q=sum(w[s]*(c1[s]-c0[s])**2 for s in c0 if s)
            for e in (F(1,7),F(6,7)):
                p=pbase[:]; p.insert(j,e)
                c,P,W=spectrum(table,p)
                check(sum(P.values())==1)
                for s in c0:
                    full=sum((1<<i) for k,i in enumerate(others) if s>>k&1)
                    b=c1[s]-c0[s]
                    check(c[full]==c0[s]+e*b)
                    check(c[full|(1<<j)]==b/2)
                    check(P[full|(1<<j)]==e*(1-e)*w[s]*b*b)
                D=sum((s.bit_count()-1)*P[s] for s in P if s)
                check(D==D0+e*L-e*e*Q)
                check(all(abs(c[s])<=1 for s in c))
                if D==0:
                    zero_deficit+=1
                    # independent truth-table classification
                    literal=all(v==next(iter(table.values())) for v in table.values())
                    literal|=any(all(table[x]==sgn*(2*x[i]-1) for x in xs) for i in range(n) for sgn in (-1,1))
                    check(literal)
                    check(all(P[s]==0 or c[s]**2==1 for s in c if s))
                if D0==0 and L==0: check(Q==0 and D==0)
                fixtures+=1
    # fair-input unit atoms independently checked on every table
    for bits in range(1<<(1<<n)):
        table={x:F(1 if bits>>k&1 else -1) for k,x in enumerate(xs)}
        c,P,W=spectrum(table,[F(1,2)]*n)
        for s in P:
            if P[s]==1:
                unit_atoms+=1
                check(sum(P[t] for t in P if t!=s)==0)
                check(all(table[x]==table[(0,)*n]*(-1)**sum(x[i] for i in range(n) if s>>i&1) for x in xs))

# Exact logarithm bounds: range reduction then atanh series, rational tail.
def ln_bounds(x,N=28):
    assert x>0
    k=0
    while x>=2: x/=2; k+=1
    while x<1: x*=2; k-=1
    def atanh(v):
        z=(v-1)/(v+1)
        lo=2*sum((z**(2*h+1)/F(2*h+1) for h in range(N)),F(0))
        err=2*z**(2*N+1)/(F(2*N+1)*(1-z*z))
        return lo,lo+err
    a,b=atanh(x); l,u=atanh(F(2))
    return (a+k*l,b+k*u) if k>=0 else (a+k*u,b+k*l)
def add(A,B): return A[0]+B[0],A[1]+B[1]
def scale(c,A): return (c*A[0],c*A[1]) if c>=0 else (c*A[1],c*A[0])
def logterm(c,x): return scale(c,ln_bounds(x))
def div(A,B):
    assert B[0]>0
    corners=[a/b for a in A for b in B]
    return min(corners),max(corners)
def outward(A,digits=10):
    k=10**digits
    return [str(F((A[0]*k).__floor__(),k)),str(F((A[1]*k).__ceil__(),k))]

weighted=[]
for m in (2,3,4,8,16,32):
    q=F(1,m*m); r=q**m; a=(m-1)*r/(1+(m-1)*r); z=1-a
    alpha=a+z*r
    I0=4*a*z*(1-r); Il=4*m*z*r*(1-q); I=I0+Il
    V=4*alpha*(1-alpha)
    D=I-V
    Dg=4*r*(m*(1-q)-1+r)
    Do=4*a*r*z*(1-r)
    check(D==z*Dg+Do)
    Eg=add((2*Dg,2*Dg),div(logterm(8*m*r*(q-r),1/q),ln_bounds(F(2))))
    Eo=add(add(logterm(8*a*z*(1-r)**2,1/(1-r)),logterm(8*r*(1-r)*z*z,1/z)),logterm(8*a*r*z*(1-r),F(2)))
    Enat=add(scale(z,scale(1,Eg)),div(Eo,ln_bounds(F(2)))) # Eg and final value in bits
    ratio=div(Enat,(D,D))
    def h(x): return add(logterm(-x,x),logterm(-(1-x),1-x))
    eta=F(1,m); marginal=eta+(1-eta)*q
    TC=add(scale(m,h(marginal)),scale(-(m-1),h(q)))
    eventratio=scale(alpha/I,TC)
    credit=add(logterm(V,1/V),add(logterm(-I0,(1-r)/(alpha*(1-alpha))),logterm(-Il,F(m)/(1-alpha))))
    creditratio=scale(1/I,credit)
    weighted.append({'m':m,'Hplus_over_deficit_bits':outward(ratio),'event_TC_over_I_nats':outward(eventratio),'unit_pivotal_residual_over_I_nats':outward(creditratio)})

for m in range(1,6):
    q=F(1,m*m+2); r=q**m; a=r/(1+r); z=1-a
    table={x:F(1 if x[0] or all(x[1:]) else -1) for x in product((0,1),repeat=m+1)}
    c,P,W=spectrum(table,[a]+[q]*m)
    for s in P:
        k=(s>>1).bit_count()
        if s==0: expected=(2*(a+z*r)-1)**2
        elif s==1: expected=4*a*z*(1-r)**2
        elif s&1: expected=4*a*z*r*r*((1-q)/q)**k
        else: expected=4*z*z*r*r*((1-q)/q)**k
        check(P[s]==expected)
    D=sum((s.bit_count()-1)*P[s] for s in P if s)
    check(D==4*a*r*z*(1-r)+z*4*r*(m*(1-q)-1+r))

result={'helper_version':'A042-endpoint-v1','slice_fixtures':fixtures,'zero_deficit_fixtures':zero_deficit,'fair_unit_atoms':unit_atoms,'assertions_passed':assertions,'weighted_rational_log_certificates':weighted,'runtime_seconds':time.monotonic()-start,'asymptotic_proof':'REPORT.md and BIASED_ENDPOINT_SERIES.tex; finite logs do not certify asymptotic statements'}
(ROOT/'out'/'CHECK_OUTPUT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
