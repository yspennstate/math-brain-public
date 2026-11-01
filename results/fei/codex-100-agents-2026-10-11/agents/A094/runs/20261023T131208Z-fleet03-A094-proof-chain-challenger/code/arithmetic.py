from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,sys,time
RUN=Path(__file__).resolve().parents[1]
START=time.perf_counter(); checks=0
def ck(x):
    global checks
    assert x
    checks+=1
    if time.perf_counter()-START>55: raise TimeoutError('frozen runtime reached')
def fw(v):
    a=list(v); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for i in range(j,j+h):
                x,y=a[i],a[i+h]; a[i],a[i+h]=x+y,x-y
        h*=2
    return [F(x,len(a)) for x in a]
def law(v): return [x*x for x in fw(v)]
def inf(v,i): return F(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v))
def total(v): return sum((inf(v,i) for i in range((len(v)-1).bit_length())),F(0))
def restrict(v,i,b):
    return [v[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(v)//2)]
def drop(t,i): return (t&((1<<i)-1))|((t>>(i+1))<<i)
@lru_cache(maxsize=20000)
def lg(q):
    q=F(q); assert q>0
    e=q.numerator.bit_length()-q.denominator.bit_length()
    x=q/(F(2)**e)
    if x<1: e-=1; x*=2
    z=(x-1)/(x+1)
    s=sum((2*z**(2*j+1)/F(2*j+1) for j in range(24)),F(0))
    rem=2*z**49/(49*(1-z*z))
    z2=F(1,3)
    a=sum((2*z2**(2*j+1)/F(2*j+1) for j in range(24)),F(0))
    b=a+2*z2**49/(49*(1-z2*z2))
    lo,hi=F(e)+s/b,F(e)+(s+rem)/a
    scale=1<<70
    return F((lo*scale).__floor__(),scale),F((hi*scale).__ceil__(),scale)
def ce(p,q):
    l=h=F(0)
    for x,y in zip(p,q):
        if x:
            a,b=lg(y); l-=x*b; h-=x*a
    return l,h
def sub(a,b): return a[0]-b[1],a[1]-b[0]
def add(a,b): return a[0]+b[0],a[1]+b[1]
def scale(a,c): return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def inherit(v,Q,i,info=False):
    p=law(v); vv=[restrict(v,i,b) for b in [0,1]]; pp=[law(x) for x in vv]
    r=[F(0)]*(len(p)//2)
    for t,x in enumerate(Q):r[drop(t,i)]+=x
    m=[(a+b)/2 for a,b in zip(*pp)]
    for t in range(len(m)):
        ck(m[t]==p[(t&((1<<i)-1))|((t>>i)<<(i+1))]+p[(t&((1<<i)-1))|((t>>i)<<(i+1))|(1<<i)])
    raw=[[2*r[t]*pp[b][t]/(2*m[t]) if m[t] else r[t] for t in range(len(m))] for b in [0,1]]
    zz=[sum(x) for x in raw]; ck(sum(zz)==2); ck(min(zz)>0)
    qq=[[x/zz[b] for x in raw[b]] for b in [0,1]]
    for b in [0,1]:
        ck(sum(qq[b])==1)
        for t,x in enumerate(pp[b]):
            if x: ck(x/qq[b][t]==m[t]*zz[b]/r[t])
    if info:
        # CE release decomposes as Delta + conditional spectral KL - mean log Z.
        cond=F(0),F(0)
        for t,x in enumerate(p):
            if x:
                u=drop(t,i); rat=x*r[u]/(Q[t]*m[u]); cond=add(cond,scale(lg(rat),x))
        az=scale(add(lg(zz[0]),lg(zz[1])),F(1,2))
        dp=ce(p,p); dc=scale(add(ce(pp[0],pp[0]),ce(pp[1],pp[1])),F(1,2))
        delta=sub(dp,dc)
        release=sub(ce(p,Q),scale(add(ce(pp[0],qq[0]),ce(pp[1],qq[1])),F(1,2)))
        residual=sub(release,add(delta,sub(cond,az)))
        ck(residual[0]<=0<=residual[1]); ck(release[1]>=0)
    return vv,qq
def root(g,k,m,a,variant):
    n=k+m; delta=F(1,1<<n)
    gg=[g[x&((1<<k)-1)] for x in range(1<<n)]
    v=gg+gg;v[(1<<n)+a]*=-1
    aa=fw(g); p=[x*x for x in aa]; support=[i for i,x in enumerate(p) if x]
    raw=p if variant==0 else [F(2**t.bit_count(),3**k) for t in range(1<<k)]
    s=sum(raw[t] for t in support); r=[raw[t]/s if t in support else F(0) for t in range(1<<k)]
    w=2*delta-len(support)*delta*delta
    Q=[(1-w)*r[t] if t in support else delta*delta for t in range(len(v))]
    ck(sum(Q)==1);P=law(v);ck(min(P)>0);ck(min(Q)>0)
    j=sum(g[a&((1<<k)-1)]!=g[(a&((1<<k)-1))^(1<<i)] for i in range(k))
    ck(total(v)==total(g)+delta*(n+1-2*j))
    for t in range(len(P)):
        if t not in support:ck(P[t]==delta*delta)
    return v,Q,delta,j,p,r
def history(g,k,m,a,variant,policy,info=False):
    v,Q,d,j,p,r=root(g,k,m,a,variant)
    leaves=[]; spendg=spendM=F(0); pathcount=pathpiv=0; nodes=0
    def walk(gv,mv,q,labels,reach,onpath,depth):
        nonlocal spendg,spendM,pathcount,pathpiv,nodes
        stop=not labels or (policy=='first' and depth==1) or (policy=='zero' and (depth==2 or (depth==1 and not onpath)))
        if stop:
            leaves.append((reach,total(mv),ce(law(mv),q) if info else None));return
        i=0; orig=labels[0]
        spendg+=reach*inf(gv,i);spendM+=reach*inf(mv,i);nodes+=1
        if onpath:
            pathcount+=1;pathpiv+=g[a&((1<<k)-1)]!=g[(a&((1<<k)-1))^(1<<orig)]
        vv,qq=inherit(mv,q,i,info)
        for b in [0,1]:walk(restrict(gv,i,b),vv[b],qq[b],labels[1:],reach/2,onpath and b==((a>>orig)&1),depth+1)
    walk(g,v,Q,list(range(k)),F(1),True,0)
    remI=sum(w*ii for w,ii,_ in leaves)
    ck(spendM==spendg+d*(pathcount-2*pathpiv))
    ck(remI==total(g)-spendg+d*(k+m+1-pathcount-2*(j-pathpiv)))
    ck(total(v)==spendM+remI)
    row={'k':k,'m':m,'vertex':a,'reference':variant,'policy':policy,'Pi_g':str(spendg),'Pi_M':str(spendM),'remaining_I':str(remI),'nodes':nodes}
    if info:
        c=ce(p,r); cost=ce(law(v),Q)
        rootbound=c[1]+d*(F(5,4)*(1<<k)*c[1]+4*(k+m)+3)
        ck(cost[1]<=rootbound)
        terminal=F(0),F(0)
        for w,_,cL in leaves:terminal=add(terminal,scale(cL,w))
        ck(terminal[1]<=cost[1]+F(1,1<<50))
        row['terminal_CE_interval']=[str(x) for x in terminal]
        row['rate6_terminal_margin_interval']=[str(6*remI-terminal[1]),str(6*remI-terminal[0])]
        row['root_rate6_margin_interval']=[str(6*total(v)-cost[1]),str(6*total(v)-cost[0])]
        if total(g):
            admission=F(67,2)/(1<<m) if k==5 else (F(5)+6*k-F(3,2))/(1<<m)
            row['coarse_admission']=(c[1]<=4*total(g) and admission<=2-6*spendg/total(g))
            if row['coarse_admission']:ck(terminal[1]<=6*remI)
    return row
