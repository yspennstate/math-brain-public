from pathlib import Path
from fractions import Fraction as F
import itertools,json,time,sys,hashlib
R=Path(__file__).resolve().parents[1]
start=time.perf_counter(); count=0
def ck(b):
    global count
    assert b
    count+=1
    if time.perf_counter()-start>55: raise RuntimeError('frozen 55s cap')
def walsh(a):
    a=list(a); k=1
    while k<len(a):
        for j in range(0,len(a),2*k):
            for i in range(j,j+k):
                x,y=a[i],a[i+k];a[i],a[i+k]=x+y,x-y
        k*=2
    return a
def dot(a,b):return (a&b).bit_count()%2
def rankbasis(vs):
    piv={}
    for v in vs:
        while v:
            j=v.bit_length()-1
            if j in piv:v^=piv[j]
            else:piv[j]=v;break
    return len(piv)
def primes(n):
    ans={};d=2
    while d*d<=n:
        while n%d==0:ans[d]=ans.get(d,0)+1;n//=d
        d+=1
    if n>1:ans[n]=ans.get(n,0)+1
    return ans
def add(*terms):
    out={}
    for term in terms:
        for k,v in term.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}
def scale(q,a):return {k:q*v for k,v in a.items() if q*v}
def logq(q):
    q=F(q);out=primes(q.numerator)
    for k,v in primes(q.denominator).items():out[k]=out.get(k,0)-v
    return {k:F(v) for k,v in out.items() if v}
def hh(q):
    q=F(q)
    return {} if not q else scale(-q*q,logq(q*q))
def ent(a):
    n=len(a);w=walsh(a)
    return add(*(hh(F(v,n)) for v in w if v))
def inf(a):
    n=len(a);d=n.bit_length()-1
    return [F(sum(a[x]!=a[x^(1<<j)] for x in range(n)),n) for j in range(d)]
def mean(a):return F(sum(a),len(a))
def dirs(a):
    n=len(a)
    return [F(sum(a[x]!=a[x^v] for x in range(n)),n) for v in range(n)]
def canon(a):
    n=len(a);d=n.bit_length()-1;w=walsh(a);ps=dirs(a)
    rows=[]
    for v in sorted(range(1,n),key=lambda v:(min(ps[v],1-ps[v]),v)):
        if rankbasis(rows+[v])>len(rows):rows.append(v)
        if len(rows)==d:break
    ww=[0]*n
    for s,c in enumerate(w):
        z=sum((dot(v,s) ^ int(ps[v]>F(1,2)))<<i for i,v in enumerate(rows))
        ww[z]=c
    aa=walsh(ww);ck(all(v%n==0 for v in aa));aa=[v//n for v in aa]
    ck(all(abs(v)==1 for v in aa));ck(ent(aa)==ent(a));ck(sum(inf(aa))<=sum(inf(a)))
    # Exact exhaustive basis cross-check on the frozen <=3-bit source.
    costs=[min(x,1-x) for x in ps]
    best=min((sum(costs[v] for v in b) for b in itertools.combinations(range(1,n),d) if rankbasis(b)==d),default=F(0))
    ck(sum(inf(aa))==best)
    used=[j for j,p in enumerate(inf(aa)) if p]
    out=[aa[sum(((x>>i)&1)<<j for i,j in enumerate(used))] for x in range(1<<len(used))]
    ck(ent(out)==ent(a));ck(sum(inf(out))==best)
    ss=[s for s,c in enumerate(walsh(out)) if c]
    ck(rankbasis([s^ss[0] for s in ss])==len(used))
    return out
def product(a,b):return [a[x]*b[y] for y in range(len(b)) for x in range(len(a))]
Q=[(-1)**(((x&1)*((x>>1)&1)+(x&1)*((x>>2)&1)+((x>>1)&1)*((x>>2)&1)+(x&1)*((x>>3)&1))%2) for x in range(16)]
def activate(a,k):return list(a)+[1]*(len(a)*((1<<k)-1))
def childpair(a,b):
    # Pair occupies two lowest original data coordinates.
    return [a[(x<<2)|b] for x in range(len(a)//4)]
def shear(a):
    # Child data bits0=c,1=z; other data and controls fixed.
    return [a[x^(((x>>1)&1))] for x in range(len(a))]
def rr(k,u):
    p=F(1,1<<k)
    return add(hh(1-p*(1-u)),scale(-p,hh(u)),scale(p*(1-p),hh(1-u)),scale(2*k*p*((1-u*u)+(1-p)*(1-u)**2),{2:F(1)}))
def entropyprofile(k,H,u):return add(scale(F(1,1<<k),H),rr(k,u))
def fixture(g,t,k):
    p=F(1,1<<k);core=[1]
    for _ in range(t):core=product(core,g)
    G=product(Q,core);root=activate(G,k)
    mu=mean(g)**t;h=ent(g);q=sum(inf(g))
    ck(mean(G)==mu/4);ck(ent(G)==add({2:F(4)},scale(t,h)))
    ck(ent(root)==entropyprofile(k,add({2:F(4)},scale(t,h)),mu/4))
    ck(sum(inf(root))==p*(t*q+2+k*(1-mu/4)))
    ck(sum(inf(root)[:2])==p)
    children=[childpair(root,b) for b in range(4)]
    reset=[shear(a) if b==1 else a for b,a in enumerate(children)]
    for b,(a,ar) in enumerate(zip(children,reset)):
        u=mu if b==0 else F(0);weight=0 if b==0 else 1
        ck(ent(a)==entropyprofile(k,scale(t,h),u))
        ck(ent(a)==ent(ar))
        ck(sorted(x*x for x in walsh(a))==sorted(x*x for x in walsh(ar)))
        ck(sum(inf(ar))==p*(t*q+weight+k*(1-u)))
        ck(all(x<=F(1,2) for x in inf(a)))
    release=sum((sum(inf(a))-sum(inf(ar)) for a,ar in zip(children,reset)),F(0))/4
    ck(release==p/4)
    L=add(ent(root),scale(-F(1,4),add(*(ent(a) for a in children))))
    ck(L==add({2:4*p},rr(k,mu/4),scale(-F(1,4),rr(k,mu)),scale(-F(3,4),rr(k,0))))
    for K in [F(0),F(16,5),F(15,4),F(8)]:
        D=add(ent(root),{2:-K*sum(inf(root))})
        S=scale(F(1,4),add(*(add({2:K*sum(inf(a))},scale(-1,ent(a))) for a in reset)))
        ck(add(D,S)==add(L,{2:-K*F(5,4)*p}))
    # Check actual affine minimum via ALL directional parity costs.
    ds=dirs(root);ps=inf(root)
    ck(all(ps[j]<=min(ds[v],1-ds[v]) for v in range(1,len(root)) for j in range(len(ps)) if (v>>j)&1))
    support=[s for s,c in enumerate(walsh(root)) if c]
    ck(rankbasis([s^support[0] for s in support])==len(ps))
    return {'seed_dimension':len(g).bit_length()-1,'t':t,'k':k,'mean':str(mu),'root_I':str(sum(inf(root))),'release':str(release),'L':{str(a):str(b) for a,b in L.items()}}
pilot='--pilot' in sys.argv
rows=[];seeds=0
for d in range(3 if pilot else 4):
    for mask in range(1<<(1<<d)):
        a=[1-2*((mask>>x)&1) for x in range(1<<d)]
        g=canon(a);rows.append(fixture(g,1,2));seeds+=1
if not pilot:rows.append(fixture(canon([1,1,1,-1]),2,2))
result={'status':'PASS','helper_version':'A005-paid-pair-v1','pilot':pilot,'source_tables':seeds,'fixtures':len(rows),'assertions':count,'runtime_seconds':time.perf_counter()-start,'fixtures_detail':rows}
(R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='fixtures_detail'}))
