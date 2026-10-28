from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import sys,time,json,hashlib
START=time.monotonic(); LIMIT=55
RUN=Path(__file__).resolve().parents[1]
COUNT=0
def check(b):
    global COUNT
    COUNT+=1
    assert b,COUNT
    if COUNT%500==0 and time.monotonic()-START>LIMIT:raise TimeoutError('frozen runtime cap')
@lru_cache(None)
def factors(n):
    ans={};p=2
    while p*p<=n:
        while n%p==0:ans[p]=ans.get(p,0)+1;n//=p
        p+=1
    if n>1:ans[n]=ans.get(n,0)+1
    return ans
def add(*terms):
    d={}
    for a in terms:
        for p,c in a.items():d[p]=d.get(p,F(0))+c
    return {p:c for p,c in d.items() if c}
def scale(a,t):return {p:c*t for p,c in a.items() if c*t}
def logform(x,w=F(1)):
    assert x>0
    return add({p:w*k for p,k in factors(x.numerator).items()}, {p:-w*k for p,k in factors(x.denominator).items()})
def entropy(p):return add(*(logform(v,-v) for v in p.values() if v))
def divergence(p,q):return add(*(logform(v/q[k],v) for k,v in p.items() if v))
@lru_cache(None)
def ln_interval(p):
    k=p.bit_length()-1;x=F(p,2**k);z=(x-1)/(x+1)
    def series(z):
        v=sum((2*z**(2*j+1)/F(2*j+1) for j in range(32)),F(0))
        return v,v+2*z**65/(65*(1-z*z))
    lo,hi=series(z);l2,u2=series(F(1,3));lo+=k*l2;hi+=k*u2
    grid=2**48
    return F((lo*grid).__floor__(),grid),F((hi*grid).__ceil__(),grid)
def interval(a):
    lo=hi=F(0)
    for p,c in a.items():
        l,u=ln_interval(p)
        lo+=c*(l if c>0 else u);hi+=c*(u if c>0 else l)
    return lo,hi
def nonnegative(a):return not a or interval(a)[0]>=0
def proj(p,i):
    q={}
    for m,v in p.items():q[m&~(1<<i)]=q.get(m&~(1<<i),F(0))+v
    return {m:v for m,v in q.items() if v}
def reference(p,n,kind):
    if kind==0:return p.copy()
    if kind==1:return {m:F(1,2**n) for m in range(2**n)}
    if kind==2:return {m:(p.get(m,F(0))+F(1,2**n))/2 for m in range(2**n)}
    return {m:F(2**(n-m.bit_count()),3**n) for m in range(2**n)}
def spectrum(tt,n,state):
    rem=[i for i,x in enumerate(state) if x==2]
    a=[]
    for y in range(2**len(rem)):
        x=sum(v<<i for i,v in enumerate(state) if v!=2)
        for j,i in enumerate(rem):x|=((y>>j)&1)<<i
        a.append(F(1 if (tt>>x)&1 else -1))
    for j in range(len(rem)):
        for b in range(0,len(a),2**(j+1)):
            for k in range(2**j):
                u,v=a[b+k],a[b+k+2**j];a[b+k],a[b+k+2**j]=u+v,u-v
    return {sum(((m>>j)&1)<<i for j,i in enumerate(rem)):(v/len(a))**2 for m,v in enumerate(a) if v}
def infl(p):return sum((m.bit_count()*v for m,v in p.items()),F(0))
def process(n,tt):
    states=list(product(range(3),repeat=n))
    ps={s:spectrum(tt,n,s) for s in states}
    for p in ps.values():check(sum(p.values())==1)
    for kind in range(4):
        qroot=reference(ps[(2,)*n],n,kind)
        qs={}
        for s in states:
            q=qroot
            for i,v in enumerate(s):
                if v!=2:q=proj(q,i)
            qs[s]=q
            check(sum(q.values())==1)
            check(nonnegative(divergence(ps[s],q)))
        for s in states:
            p,q=ps[s],qs[s];dp=divergence(p,q)
            for i,v in enumerate(s):
                if v!=2:continue
                daughters=[]
                for b in (0,1):
                    t=list(s);t[i]=b;daughters.append(tuple(t))
                p0,p1=[ps[t] for t in daughters];qm=proj(q,i);pm=proj(p,i)
                check(pm=={m:(p0.get(m,F(0))+p1.get(m,F(0)))/2 for m in set(p0)|set(p1)})
                check(all(qs[t]==qm for t in daughters))
                js=add(entropy(pm),scale(add(entropy(p0),entropy(p1)),F(-1,2)))
                loss=add(dp,scale(divergence(pm,qm),-1))
                avgd=scale(add(*(divergence(ps[t],qs[t]) for t in daughters)),F(1,2))
                check(add(loss,avgd,scale(dp,-1),scale(js,-1))=={})
                check(nonnegative(loss));check(nonnegative(js))
                di=sum((w for m,w in p.items() if m>>i&1),F(0))
                check(infl(p)==di+(infl(p0)+infl(p1))/2)
                check(interval(js)[1]<=2*di)
                # Exact identity plus the preceding inequality is the Bellman
                # supersolution for all policies, with both stop children kept.
                check(add(entropy(p),dp,scale(add(entropy(p0),entropy(p1),divergence(p0,qm),divergence(p1,qm)),F(-1,2)),scale(loss,-1))==add(entropy(p),scale(add(entropy(p0),entropy(p1)),F(-1,2)),scale(js,-1)))
def main():
    mode=sys.argv[1] if len(sys.argv)>1 else 'pilot';maxn=2 if mode=='pilot' else 3
    roots=0
    for n in range(maxn+1):
        for tt in range(2**(2**n)):process(n,tt);roots+=1
    # AND2 convention: truth table +1 only at (1,1).
    p=spectrum(8,2,(2,2));pm=proj(p,0);child=spectrum(8,2,(0,2))
    check(p=={m:F(1,4) for m in range(4)})
    check(child=={0:F(1)})
    check(pm=={0:F(1,2),2:F(1,2)})
    check(child.get(2,0)==0 and pm[2]>0)
    result={'helper':'projection22-v1','mode':mode,'roots':roots,'assertions':COUNT,'elapsed_seconds':time.monotonic()-START,'arithmetic':'Fraction and exact prime-log identities; 32-term rational atanh outward intervals','maximum_dimension':maxn,'negative_control':'AND2 true-kernel child has zero nonempty mass; marginal has mass1/2 there, hence reverse conversion KL infinite','status':'PASS','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (RUN/'out'/f'{mode.upper()}.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
