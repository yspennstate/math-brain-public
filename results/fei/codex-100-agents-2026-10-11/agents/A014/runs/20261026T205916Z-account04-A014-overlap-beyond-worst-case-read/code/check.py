from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, factorial
import sys, json, time, hashlib

RUN=Path(__file__).resolve().parents[1]
START=time.monotonic(); CHECKS=0
PILOT='--pilot' in sys.argv
def ck(x):
    global CHECKS
    CHECKS+=1
    assert x, CHECKS
    if time.monotonic()-START>55: raise TimeoutError('frozen 55 second cap')

def clique_mass(r,k,lam):
    t=k//2
    even=F(factorial(2*t),2**t*factorial(t))*(lam/48)**t
    return even if k%2==0 else even*(2*t+1)*lam*F(3*r-2*t-3,96)

def matchings(vertices, edges):
    if not vertices:
        yield ();return
    u=min(vertices); rest=vertices-{u}
    yield from matchings(rest,edges)
    for w in rest:
        e=tuple(sorted((u,w)))
        if e in edges:
            for tail in matchings(rest-{w},edges): yield (e,)+tail

def raw(A,n,weights):
    if not A:return F(1)
    edges=set(weights);total=F(0)
    for roots in matchings(set(A),edges):
        covered={x for e in roots for x in e};U=set(A)-covered
        if any(set(e)<=U for e in edges):continue
        options=[]
        for u in sorted(U):
            opts=[];external=F(0)
            for w in range(n):
                e=tuple(sorted((u,w)))
                if e not in weights:continue
                if w not in A: external+=weights[e]/32
                elif w in covered: opts.append((w,weights[e]/8))
            if external:opts.append((-1,external))
            options.append(opts)
        for choices in product(*options):
            val=F(1);counts={x:0 for x in covered}
            for e in roots:val*=weights[e]/24
            for endpoint,w in choices:
                val*=w
                if endpoint!=-1:counts[endpoint]+=1
            for a,b in roots:
                x,y=counts[a],counts[b]
                val*=F(factorial(x)*factorial(y),(x+y+1)**2*(x+y+2))
            total+=val
    return total

def fwht(vals):
    out=list(vals);step=1
    while step<len(out):
        for start in range(0,len(out),2*step):
            for i in range(start,start+step):
                a,b=out[i],out[i+step];out[i],out[i+step]=a+b,a-b
        step*=2
    return out

# Rational enclosures for every logarithmic comparison. Normalize to [1,2),
# use ln x=2 sum t^(2j+1)/(2j+1), t=(x-1)/(x+1)<=1/3,
# with omitted tail <=2*t^(2N+1)/[(2N+1)(1-t^2)].
def ln_unit(x,N=20):
    t=(x-1)/(x+1);term=t;ans=F(0)
    for j in range(N): ans+=2*term/F(2*j+1);term*=t*t
    return ans,ans+2*term/F((2*N+1)*(1-t*t))
LN2=ln_unit(F(2)); LOGCACHE={}
def lg(x):
    x=F(x)
    if x in LOGCACHE:return LOGCACHE[x]
    orig=x;e=0
    while x<1:x*=2;e-=1
    while x>=2:x/=2;e+=1
    a,b=ln_unit(x)
    # Near-one logarithms must retain relative precision: an absolute 2^-40
    # upper error on log(1/(1-v)) would drown a rare event's whole influence.
    diff=abs(orig-1)
    bump=max(0,diff.denominator.bit_length()-diff.numerator.bit_length()+2) if diff else 0
    scale=1<<(40+bump)
    low=F(e)+a/LN2[1];high=F(e)+b/LN2[0]
    out=F((low*scale).__floor__(),scale),F((high*scale).__ceil__(),scale)
    LOGCACHE[orig]=out;return out
def logcost(x,mass=F(1)):
    a,b=lg(x);return mass*a,mass*b
def add(*intervals):return tuple(sum(z[i] for z in intervals) for i in (0,1))
def entropy_binary(v):
    return add(*(logcost(1/x,x) for x in (v,1-v) if x))

direct=0;generic_atoms=0
for r,m in [(3,1),(3,2),(4,1),(4,2)]:
    if PILOT and (r,m)!=(3,1):continue
    n=r+2*m;lam=F(1,r-1)
    edges=list(combinations(range(r),2))+[(r+2*j,r+2*j+1) for j in range(m)]
    weights={e:lam for e in edges}
    C=[int(not any((x>>a&1) and (x>>b&1) for a,b in edges)) for x in range(1<<n)]
    f=[1-2*z for z in C];w=fwht(f);s=F(sum(C),1<<n);v=4*s*(1-s)
    influence=F(sum(f[x]!=f[x^(1<<j)] for x in range(1<<n) for j in range(n)),1<<n)
    ck(s==F(r+1,2**r)*F(3,4)**m)
    ck(influence==s*(F(4*m,3)+F(2*r*(r-1),r+1)))
    masses=[];active=F(0);single=F(0);double=F(0);spectralI=F(0)
    for mask in range(1<<n):
        A={j for j in range(n) if mask>>j&1};k=sum(j<r for j in A)
        one=sum(len(A&{r+2*j,r+2*j+1})==1 for j in range(m))
        two=sum({r+2*j,r+2*j+1}<=A for j in range(m))
        formula=clique_mass(r,k,lam)*(lam/32)**one*(lam/48)**two
        exact=raw(A,n,weights);ck(exact==formula);masses.append(exact);generic_atoms+=1
        if mask:
            p=F(w[mask]**2,4**n)
            active+=p*(one+two);single+=p*one;double+=p*two;spectralI+=p*len(A)
    Z=sum(masses)-1;ZK=sum(comb(r,k)*clique_mass(r,k,lam) for k in range(r+1))-1
    ck(Z==(1+ZK)*(1+lam/12)**m-1);ck(active==m*s)
    ck(single==F(2*m,3)*s);ck(double==F(m,3)*s);ck(spectralI==influence)
    direct+=1

rows=[]
for r in (range(3,7) if PILOT else range(3,17)):
    for m in (range(1,4) if PILOT else range(1,13)):
        lam=F(1,r-1);sK=F(r+1,2**r);s=sK*F(3,4)**m;v=4*s*(1-s)
        I=s*(F(4*m,3)+F(2*r*(r-1),r+1));ZK=sum(comb(r,k)*clique_mass(r,k,lam) for k in range(r+1))-1
        Z=(1+ZK)*(1+lam/12)**m-1
        ck(Z>0);ck(all(clique_mass(r,k,lam)>0 for k in range(r+1)))
        pc=[F(comb(r,k)*(r+1-2*k)**2,2**r*(r+1)) for k in range(r+1)]
        ck(sum(pc)==1);ck(sum(k*x for k,x in enumerate(pc))==F(r*(r-1),2*(r+1)))
        actualI=F(0);actualV=F(0);act=F(0)
        for k in range(r+1):
            for t in range(m+1):
                if not (k or t):continue
                mass=4*s*pc[k]*comb(m,t)*F(1,4)**t*F(3,4)**(m-t)
                actualV+=mass;actualI+=mass*(k+F(4*t,3));act+=mass*t
        ck(actualV==v);ck(actualI==I);ck(act==m*s)
        # Complete cost, including signed log Z and wrapper.
        core=add(*(logcost(1/clique_mass(r,k,lam),4*s*pc[k]) for k in range(r+1) if pc[k]))
        cost=add(entropy_binary(v),core,logcost(1/lam,m*s),logcost(32,F(2*m,3)*s),logcost(48,F(m,3)*s),logcost(Z,v))
        ck(cost[0]>=0)
        rows.append({'r':r,'m':m,'s':str(s),'I':str(I),'Z':str(Z),'CE_over_I_interval':[str(x/I) for x in cost]})

scalars=0
for r in range(12,257):
    m=r*r;hr=F(2*r*(r-1),r+1)
    ck(F(m,12*(r-1))>=1);ck(F(4*m,3)+hr<=F(3*m,2));ck(F(m)/(F(4*m,3)+hr)>=F(2,3))
    ck(F(9*r,2)+6<=5*r);ck(F(63,4*r)+F(153,32)+2<=F(259,32));scalars+=1
ck(13**8<2*12**8);ck(9>8);ck(F(104,3)<64);ck(52<64)
# m=1: normalized one-edge q is EXACTLY independent of lambda.
for lam in [F(1),F(1,3),F(1,101),F(1,2**20)]:
    ck((lam/32)/(lam/12)==F(3,8));ck((lam/48)/(lam/12)==F(1,4))

out={'mode':'pilot' if PILOT else 'main','helper_version':'A014-global-scale-v1','parameter_pairs':len(rows),'direct_truth_tables':direct,'generic_occupation_atoms':generic_atoms,'scalar_r_values':scalars,'assertions':CHECKS,'elapsed_seconds':time.monotonic()-START,'arithmetic':'exact integers/Fractions, rigorous directed logarithm intervals','rows':rows}
dest=RUN/'out'/('pilot.json' if PILOT else 'check.json')
dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
