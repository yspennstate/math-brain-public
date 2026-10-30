"""Frozen v1 exact Boolean and symbolic-log audit. No external imports."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter()
checks=0
def check(v):
    global checks
    assert v
    checks+=1

@lru_cache(None)
def factor(n):
    ans={}; p=2
    while p*p<=n:
        while n%p==0: ans[p]=ans.get(p,0)+1; n//=p
        p+=1
    if n>1: ans[n]=ans.get(n,0)+1
    return ans

def add(*xs):
    z={}
    for x in xs:
        for p,c in x.items(): z[p]=z.get(p,Q(0))+c
    return {p:c for p,c in z.items() if c}
def scale(x,c): return {p:v*c for p,v in x.items() if v*c}
def log(x):
    x=Q(x); assert x>0
    return {} if x==1 else {x:Q(1)}
def phi(x):
    x=Q(x)
    return scale(log(x),-x) if x else {}
def h(x): return add(phi(x),phi(1-x))
def entropy(p): return add(*(phi(x) for x in p))

@lru_cache(None)
def ln_bounds(q):
    q=Q(q); assert q>0
    e=0
    while q>=2: q/=2; e+=1
    while q<1: q*=2; e-=1
    def series(x):
        z=(x-1)/(x+1); z2=z*z; power=z; val=Q(0)
        for j in range(40): val+=2*power/(2*j+1); power*=z2
        return val,val+2*power/(81*(1-z2))
    a,b=series(q); c,d=series(Q(2))
    return (a+e*c,b+e*d) if e>=0 else (a+e*d,b+e*c)
@lru_cache(None)
def log_bounds(p):
    a,b=ln_bounds(Q(p)); c,d=ln_bounds(Q(2)); vals=[a/c,a/d,b/c,b/d]; return min(vals),max(vals)
def bounds(x):
    lo=hi=Q(0)
    for p,c in x.items():
        a,b=log_bounds(p)
        if c>=0: lo+=c*a; hi+=c*b
        else: lo+=c*b; hi+=c*a
    return lo,hi
def nonneg(x): return not x or bounds(x)[0]>=0

def walsh(vals):
    w=list(vals); step=1
    while step<len(w):
        for b in range(0,len(w),2*step):
            for j in range(b,b+step): a,c=w[j],w[j+step]; w[j],w[j+step]=a+c,a-c
        step*=2
    return w
def point(r): return [-1]+[1]*((1<<r)-1)
def data(vals):
    n=(len(vals)-1).bit_length(); den=len(vals)
    w=walsh(vals); p=[Q(a*a,den*den) for a in w]
    check(sum(p)==1)
    inf=[sum(p[s] for s in range(len(p)) if s>>i&1) for i in range(n)]
    for i in range(n):
        edge=Q(sum(vals[x]!=vals[x^(1<<i)] for x in range(len(vals))),den)
        check(inf[i]==edge)
    return p,inf

# Independent raw point spectra, exact marginal entropy, and GU source guard.
point_rows=[]
for m in range(1,9):
    p,inf=data(point(m)); d=Q(2,1<<m)
    check(p[0]==(1-d)**2); check(all(x==d*d for x in p[1:])); check(inf==[d]*m)
    hp=entropy(p); mp=scale(h(d),m)
    check(hp==add(phi((1-d)**2),scale(phi(d*d),(1<<m)-1)))
    check(nonneg(add(scale(log(2),4*m*d),scale(hp,-1))))
    U=add(phi((1-d)**2),scale(log(2),m*d-m*d*d))
    if m==1: child={}
    else:
        e=2*d; child=add(phi((1-e)**2),scale(log(2),(m-1)*e-(m-1)*e*e))
    check(nonneg(add(scale(log(2),Q(19,8)*d),scale(U,-1),scale(child,Q(1,2)))))
    point_rows.append({'m':m,'I':str(m*d),'H_interval':list(map(str,bounds(hp)))})

# All parameter triples: exact point/activation laws and lower-bound signs.
param_rows=[]
for m in range(2,8):
    d=Q(2,1<<m); N=1/d; mu=(1-d)**int(N); a=1-mu
    Hpoint=add(phi((1-d)**2),scale(phi(d*d),(1<<m)-1)); Hg=scale(Hpoint,N)
    for t in range(1,7):
        delta=Q(1,1<<t); I=delta*(m+t*a)
        # Empty atom; nonempty core spectrum repeated across control subsets;
        # then control-only atoms. This is a normalized actual squared law.
        mass=(1-delta*a)**2+delta*(1-mu*mu)+delta*(1-delta)*a*a
        check(mass==1)
        HF=add(phi((1-delta*a)**2),scale(Hg,delta),scale(phi(mu*mu),-delta),
               scale(log(2),2*t*delta*(1-mu*mu)),
               scale(phi(delta*delta*a*a),(1<<t)-1))
        # Rational sufficient bound H/I < 4+6/m <= 7, via ln2>2/3.
        check(nonneg(add(scale(log(2),4*I+6*delta*a),scale(HF,-1))))
        check((4*I+6*delta*a)/I<=4+Q(6,m))
        for k in range(m):
            r=m-k; sharp=scale(h(Q(2,1<<r)),delta*r*Q(1,1<<k)*N)
            lower=delta*r*(r-1)
            check(nonneg(add(sharp,scale(log(2),-lower))))
            check(lower/I>=Q(r*(r-1),m+t))
            param_rows.append((m,t,k))

# Raw activated Boolean sources: compare EVERY Fourier coefficient with formula;
# exact control/core influences, full support, and all physical product cuts.
raw_rows=[]
for m,t in [(2,1),(2,2),(2,3),(3,1)]:
    N=1<<(m-1); b=m*N; D=1<<b; d=Q(2,1<<m); delta=Q(1,1<<t)
    g=[]
    for x in range(D):
        sign=1
        for j in range(N):
            if (x>>(j*m))&((1<<m)-1)==0: sign=-sign
        g.append(sign)
    w=walsh(g); mu=Q(sum(g),D); a=1-mu
    vals=[(g[x& (D-1)] if (x>>b)==0 else 1) for x in range(D*(1<<t))]
    p,inf=data(vals); wf=walsh(vals); den=len(vals)
    for s,num in enumerate(wf):
        core=s&(D-1); ctrl=s>>b
        expected=delta*Q(w[core],D) if core else (1-delta*a if ctrl==0 else -delta*a)
        check(Q(num,den)==expected); check(p[s]>0)
    check(inf[:b]==[delta*d]*b); check(inf[b:]==[delta*a]*t)
    check(sum(inf)==delta*(m+t*a))
    # All nontrivial bipartitions for n<=7; rank-one sign matrix criterion.
    n=b+t; cuts=0
    if n<=7:
        for mask in range(1,(1<<n)-1):
            if not mask&1: continue
            # A sign truth table tensors over a cut iff every 2x2 minor is zero.
            nonzero_minor=False
            for x in range(len(vals)):
                if vals[x]*vals[0]!=vals[x&mask]*vals[x&(((1<<n)-1)^mask)]:
                    nonzero_minor=True; break
            check(nonzero_minor); cuts+=1
    raw_rows.append({'m':m,'t':t,'variables':n,'checked_physical_cuts':cuts})

# EVERY adaptive finite policy on two point3 blocks, exposure cap k. Dynamic
# min includes STOP and every legal physical query, using only exact intervals
# to choose a minimum; it verifies the claimed sharp value, not sampled policies.
from itertools import product
states=0; actions=0
for k in range(3):
    r0=3-k
    @lru_cache(None)
    def solve(state):
        global states,actions
        states+=1
        M=add(*(scale(h(Q(2,1<<r)),r) for r in state if r))
        target=scale(h(Q(2,1<<r0)),sum(Q(r0,1<<(r-r0)) for r in state if r))
        candidates=[M]
        check(nonneg(add(M,scale(target,-1))))
        for j,r in enumerate(state):
            if r<=r0: continue
            actions+=1
            c=list(state); c[j]=0; z=list(state); z[j]=r-1
            cand=scale(add(solve(tuple(c)),solve(tuple(z))),Q(1,2))
            check(cand==target); candidates.append(cand)
        best=candidates[0]
        for cand in candidates[1:]:
            diff=add(cand,scale(best,-1))
            if not diff or bounds(diff)[1]<0: best=cand
            else: check(bounds(diff)[0]>=0)
        check(best==target)
        return best
    root=solve((3,3))
    check(root==scale(h(Q(2,1<<r0)),Q(2*r0,1<<k)))

elapsed=time.perf_counter()-start
check(elapsed<55)
out={'status':'PASS','assertions':checks,'parameter_triples':len(param_rows),'raw_activated_sources':raw_rows,
     'raw_points':point_rows,'adaptive_states':states,'adaptive_query_actions':actions,
     'seconds':elapsed,'arithmetic':'exact Fraction rational-log forms plus rigorous outward 40-term atanh intervals',
     'scope':'finite certificates plus written all-dimensional proof; external review pending'}
(ROOT/'out/EXACT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['raw_points']}))
