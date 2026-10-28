"""A089 v1: independent integer characters, exact log vectors, bounded pilot."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json,time
from arithmetic import Q,LN2,log2,scale,plus,fwht
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
def add(*vs):
    d={}
    for v in vs:
        for p,c in v.items():d[p]=d.get(p,F(0))+c
    return {p:c for p,c in d.items() if c}
def mul(v,c):return {p:a*c for p,a in v.items() if a*c}
@lru_cache(None)
def factors(n):
    ans={};p=2
    while p*p<=n:
        while n%p==0:ans[p]=ans.get(p,0)+1;n//=p
        p+=1
    if n>1:ans[n]=ans.get(n,0)+1
    return ans
def lv(x):return add(factors(x.numerator),mul(factors(x.denominator),-1))
def ent(ps):return add(*(mul(lv(p),-p) for p in ps if p))
@lru_cache(None)
def phi(a,b):return add(mul(lv(a+b),a+b),mul(lv(a),-a) if a else {},mul(lv(b),-b) if b else {}) if a+b else {}
def interval(v):
    z=(0,0)
    for p,c in v.items():
        u=scale(log2(F(p)),abs(c))
        if c<0:u=(-u[1],-u[0])
        z=plus(z,u)
    return z
def restrict(t,i,b):return tuple(t[x] for x in range(len(t)) if ((x>>i)&1)==b)
@lru_cache(None)
def data(t):
    n=len(t).bit_length()-1;N=len(t)
    w=tuple(F(sum(t[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)),N) for s in range(N))
    assert w==tuple(fwht(list(t)))
    assert sum(v*v for v in w)==1
    ds=tuple(F(sum(t[x]!=t[x^(1<<i)] for x in range(N)),N) for i in range(n))
    assert sum(ds)==sum(s.bit_count()*v*v for s,v in enumerate(w))
    return w,ent(tuple(v*v for v in w)),sum(ds),ds
@lru_cache(None)
def erase(t,i):
    w,H,I,ds=data(t);N=len(t)
    rows=[s for s in range(N) if not s&(1<<i)]
    B=add(*(phi(w[s]**2,w[s|(1<<i)]**2) for s in rows))
    kids=[restrict(t,i,b) for b in [0,1]]
    # Exact coefficient identities, independent of entropy expression simplification.
    for b in [0,1]:
        wc=data(kids[b])[0]
        assert wc==tuple(w[s]+(1 if b==0 else -1)*w[s|(1<<i)] for s in rows)
    J=add(ent(tuple(w[s]**2+w[s|(1<<i)]**2 for s in rows)),*(mul(data(k)[1],-F(1,2)) for k in kids))
    assert add(H,*(mul(data(k)[1],-F(1,2)) for k in kids))==add(B,J)
    assert I-sum(data(k)[2] for k in kids)/2==ds[i]
    return B,J
def compose(h,gs):
    ns=[len(g).bit_length()-1 for g in gs];n=sum(ns);t=[]
    for x in range(1<<n):
        z=0;shift=0
        for j,(g,m) in enumerate(zip(gs,ns)):
            if g[(x>>shift)&((1<<m)-1)]==1:z|=1<<j
            shift+=m
        t.append(h[z])
    return tuple(t)
def qs(h,gs):
    out=[]
    for j in range(len(gs)):
        val=F(0);others=[k for k in range(len(gs)) if k!=j]
        for signs in product([0,1],repeat=len(others)):
            z=0;p=F(1)
            for k,b in zip(others,signs):
                z|=b<<k;p*=F(sum(v==(1 if b else -1) for v in gs[k]),len(gs[k]))
            if h[z]!=h[z|(1<<j)]:val+=p
        out.append(val)
    return out
def correction(h,gs):
    t=compose(h,gs);q=qs(h,gs)
    return add(data(t)[1],*(mul(data(g)[1],-a) for a,g in zip(q,gs)))
def audit_row(h,gs,j,i):
    t=compose(h,gs);q=qs(h,gs);offset=sum(len(g).bit_length()-1 for g in gs[:j]);physical=offset+i
    w,H,I,ds=data(t);g=gs[j];v=data(g)[0];d=data(g)[3][i]
    assert ds[physical]==q[j]*d
    B,J=erase(t,physical);Bi,Ji=erase(g,i)
    mask=((len(g)-1)<<offset)^(1<<physical)
    special=add(*(phi(w[s]**2,w[s|(1<<physical)]**2) for s in range(len(t)) if not s&(1<<physical) and not s&mask))
    exceptional=phi(v[0]**2,v[1<<i]**2)
    assert B==add(mul(add(Bi,mul(exceptional,-1)),q[j]),special)
    children=[];qchildren=[]
    for b in [0,1]:
        gg=list(gs);gg[j]=restrict(g,i,b)
        assert compose(h,gg)==restrict(t,physical,b)
        children.append(correction(h,gg));qchildren.append(qs(h,gg))
    assert all((qchildren[0][k]+qchildren[1][k])/2==q[k] for k in range(len(gs)))
    drift=add(*(mul(c,F(1,2)) for c in children),mul(correction(h,gs),-1))
    assert drift==add(mul(add(exceptional,Ji),q[j]),mul(special,-1),mul(J,-1))
    mu,tt=abs(v[0]),abs(v[1<<i]);assert mu+tt<=1 and tt<=d
    # Enclosure is rigorous: Phi <= tt*(mu+tt)/ln2 and J <=2*d/ln2.
    if tt:
        rhs=tt*(mu+tt);assert interval(exceptional)[1]*LN2[1] <= rhs*Q*Q
    else:assert not exceptional
    assert interval(drift)[1]<=F(9,2)*ds[physical]*Q or not drift
    return drift,ds[physical]
def main():
    tables=[tuple(1 if mask&(1<<x) else -1 for x in range(4)) for mask in range(16)]
    count=0
    for h,g1,g2 in product(tables,repeat=3):
        for j,i in product(range(2),repeat=2):
            audit_row(h,[g1,g2],j,i);count+=1
        assert time.perf_counter()-START<55
    scalar=0
    for a in range(17):
        for b in range(17-a):
            aa,bb=F(a,16),F(b,16);z=phi(aa*aa,bb*bb)
            if bb:assert interval(z)[1]*LN2[1] <= bb*(aa+bb)*Q*Q
            else:assert not z
            scalar+=1
    h=tuple(1 if x==7 else -1 for x in range(8))
    point=lambda n:tuple(-1 if x==0 else 1 for x in range(1<<n))
    gs=[point(3),point(2),point(2)]
    drift,D=audit_row(h,gs,0,0);assert D==F(9,64)
    assert drift=={2:-F(37,16),3:-F(567,512),5:-F(25,1024),7:F(3087,2048)}
    for j in range(3):
        for i in range(len(gs[j]).bit_length()-1):audit_row(h,gs,j,i)
    assert interval(drift)[0]>F(107184,1000000)*Q and interval(drift)[1]<F(107185,1000000)*Q
    signs=[2**14592>3**2862*7**3087,2**3392>3**1701*5**25,2**48>3**27,7**3087>2**4736*3**2268*5**50,3**9>2**14]
    assert all(signs)
    def serial(v):return {str(p):str(c) for p,c in v.items()}
    result={'status':'PASS','version':'A089-sharp-signed-v1','exhaustive_compositions':4096,'physical_query_rows':count,'scalar_triangle_points':scalar,'seven_bit_all_queries':7,'source_integer_signs':signs,'witness_drift_log_vector':serial(drift),'witness_drift_interval_scaled_2pow192':interval(drift),'queried_physical_influence':str(D),'rational_reserve_release':str(F(9,2)*D),'rational_reserve_surplus_log_vector':serial(add({2:F(9,2)*D},mul(drift,-1))),'runtime_seconds':time.perf_counter()-START,'proof_scope':'finite identities exact; universal extension is analytic in PROOF.md; initial FEI payment unproved'}
    (ROOT/'out/VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(result))
if __name__=='__main__':main()
