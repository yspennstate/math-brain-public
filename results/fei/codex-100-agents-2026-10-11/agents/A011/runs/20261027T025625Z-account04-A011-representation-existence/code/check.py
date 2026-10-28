from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,sys,time,hashlib

RUN=Path(__file__).resolve().parents[1]
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
START=time.monotonic(); LIMIT=55 if MODE!='main' else 300
COUNT=0
def ck(v):
    global COUNT
    COUNT+=1
    assert v,COUNT
    if COUNT%1000==0: assert time.monotonic()-START<LIMIT,'RUNTIME_INCOMPLETE'

def lnseries(z):
    term=z;val=F(0)
    for k in range(24):val+=2*term/(2*k+1);term*=z*z
    return val,val+2*term/(49*(1-z*z))
L2=lnseries(F(1,3));GRID=1<<96
@lru_cache(None)
def lg(q):
    q=F(q);assert q>0
    k=q.numerator.bit_length()-q.denominator.bit_length()
    x=q/(F(2)**k)
    if x<1:k-=1;x*=2
    assert 1<=x<2
    lo,hi=lnseries((x-1)/(x+1))
    lo=lo/L2[1]+k;hi=hi/L2[0]+k
    return F((lo*GRID).__floor__(),GRID),F((hi*GRID).__ceil__(),GRID)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def mul(c,a):return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
ZERO=(F(0),F(0))
def div(p,q):
    ans=ZERO
    for x,y in zip(p,q):
        if x:assert y>0;ans=add(ans,mul(x,lg(x/y)))
    return ans
def ent(p):return div(p,[F(1)]*len(p))
def entropy(p):return mul(-1,ent(p))
def overlap(a,b):return max(a[0],b[0])<=min(a[1],b[1])
def nonneg(a):ck(a[1]>=0)

def spectrum(tab):
    w=list(tab);step=1
    while step<len(w):
        for j in range(0,len(w),2*step):
            for k in range(step):
                x,y=w[j+k],w[j+k+step];w[j+k]=x+y;w[j+k+step]=x-y
        step*=2
    return [F(x*x,len(tab)**2) for x in w]
def child(tab,i,b):return [x for j,x in enumerate(tab) if ((j>>i)&1)==b]
def pair_indices(n,i):
    return [(t,t|(1<<i)) for t in range(1<<n) if not(t&(1<<i))]

def inherit(tab,q,i):
    n=(len(tab)-1).bit_length();p=spectrum(tab);pairs=pair_indices(n,i)
    m=[p[a]+p[b] for a,b in pairs];r=[q[a]+q[b] for a,b in pairs];s=sum(q)
    tabs=[child(tab,i,b) for b in range(2)];ps=[spectrum(t) for t in tabs]
    ck(all((ps[0][j]+ps[1][j])/2==m[j] for j in range(len(m))))
    raws=[[rj*x/mj if mj else rj for x,mj,rj in zip(pb,m,r)] for pb in ps]
    zs=list(map(sum,raws));ck(all(z>0 for z in zs));ck(sum(zs)==2*s)
    qs=[[s*x/z for x in raw] for raw,z in zip(raws,zs)]
    for pb,qb,z in zip(ps,qs,zs):
        ck(sum(qb)==s)
        for x,y,mj,rj in zip(pb,qb,m,r):
            if x:ck(y>0);ck(x/y==(mj/rj)*(z/s))
    # Exact conditional-pair chain-rule ratios, not floating entropy identities.
    for (a,b),mj,rj in zip(pairs,m,r):
        if mj:
            for t in (a,b):
                if p[t]:ck(p[t]/q[t]==(mj/rj)*((p[t]/mj)/(q[t]/rj)))
    dp=div(p,q);dm=div(m,r)
    jensen=mul(F(-1,2),lg(zs[0]*zs[1]/s**2))
    delta=add(sub(dp,dm),jensen)
    # Numerical interval overlap is only a diagnostic for the exact ratios above.
    dchild=mul(F(1,2),add(div(ps[0],qs[0]),div(ps[1],qs[1])))
    ck(overlap(delta,sub(dp,dchild)));nonneg(delta)
    ck(zs[0]*zs[1]<=s*s)
    return tabs,ps,qs,delta,zs

def walk(tab,q,depth,reset):
    p=spectrum(tab);n=(len(tab)-1).bit_length()
    if n==0:return ZERO,ZERO,div(p,q),1
    i=(depth+sum(v<0 for v in tab))%n
    tabs,ps,qs,delta,zs=inherit(tab,q,i)
    es=ZERO;ds=ZERO;ql=delta;nodes=1
    for b in range(2):
        new=qs[b]
        if reset and (depth+b)%2==0:
            # Actual finite-cost reset, with ghost mass and signed price retained.
            mass=sum(new);u=F(1,len(new));new=[(x+mass*u)/2 for x in new]
        charge=sub(div(ps[b],new),div(ps[b],qs[b]))
        e,l,d,num=walk(tabs[b],new,depth+1,reset)
        es=add(es,mul(F(1,2),add(charge,e)))
        ql=add(ql,mul(F(1,2),l));ds=add(ds,mul(F(1,2),d));nodes+=num
    ck(overlap(div(p,q),add(sub(ds,es),ql)))
    if not reset:ck(overlap(div(p,q),add(ds,ql)));ck(overlap(es,ZERO))
    nonneg(ds);nonneg(ql)
    return es,ql,ds,nodes

def finite():
    maxn=2 if MODE=='pilot' else 3
    sources=edges=trees=nodes=0
    for n in range(maxn+1):
        for label in range(1<<(1<<n)):
            tab=[-1 if label>>i&1 else 1 for i in range(1<<n)];p=spectrum(tab);u=F(1,len(p));sources+=1
            models=[p,[x/2 for x in p],[(x+u)/6 for x in p]]
            for q in models:
                for i in range(n):inherit(tab,q,i);edges+=1
                for reset in ([False] if MODE=='pilot' else [False,True]):
                    e,l,d,num=walk(tab,q,0,reset);trees+=1;nodes+=num
                    rootce=add(entropy(p),div(p,q))
                    ck(overlap(add(rootce,e),add(add(entropy(p),d),l)))
    return dict(sources=sources,first_queries=edges,complete_trees=trees,tree_nodes=nodes)

def scalar():
    witnesses=[]
    for b in range(12,33):
        ep=F(1,1<<(b+1));den=(1+3*ep)*(1-2*ep+2*ep*ep);num=1+3*ep*ep
        ck(den-num==ep*(1-ep)*(1-6*ep));ck(den>num>0)
        z=num/den;ze=2-z;ck(z*ze<1);ck(1-z*ze==(1-z)**2)
        delta=mul(F(-1,2),lg(z*ze));ck(delta[0]>0)
        witnesses.append({'b':b,'epsilon':str(ep),'Zclean':str(z),'Zedit':str(ze),'loss_lower':str(delta[0]),'loss_upper':str(delta[1])})
    cs=4*F(4081,4096)-F(135,92)-1;cc=15*F(4081,4096)-320*F(151,8192)-F(37,8)
    ck(cs==F(35751,23552));ck(cc==F(18111,4096));ck(cs>0 and cc>0)
    ck(F(6144,23)<320)
    rows=0
    for a in range(1,17):
        for b in range(12,33):
            L=a+b
            for M in range(129):
                finite=sum((1+j*(j+1))*F(L+j,1<<j) for j in range(1,M+1))
                tail=F(M**3+(L+7)*M*M+(5*L+23)*M+9*L+34,1<<M)
                ck(finite+tail==9*L+34)
                ck(F(9*L+34,a*(1<<(b+1)))<=F(151,8192))
                ck(F(a+b+2,a*(1<<b))<=F(15,4096));rows+=1
    for j in range(3,129):
        A=1+j*(j+1);B=1+4*j*(j+1)
        ck(5+16*j*(j+1)<=2**(j+5));ck(B<=4*A);ck(F(1536*B,23)<=320*A)
    (RUN/'out/WITNESSES.json').write_text(json.dumps(witnesses,indent=2),encoding='utf-8')
    return dict(witnesses=len(witnesses),scalar_tuples=rows,residual_C0=str(cs),residual_constant=str(cc))

ans=scalar() if MODE=='scalar' else finite()
ans.update(mode=MODE,status='PASS',assertions=COUNT,seconds=time.monotonic()-START,helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),log_cache=lg.cache_info()._asdict())
(RUN/f'out/{MODE.upper()}.json').write_text(json.dumps(ans,indent=2),encoding='utf-8')
print(json.dumps(ans))
