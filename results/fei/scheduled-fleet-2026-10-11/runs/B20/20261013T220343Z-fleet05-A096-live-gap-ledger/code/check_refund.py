from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
RUN=Path(__file__).resolve().parent.parent
t0=time.perf_counter();checks=0
def ck(v):
    global checks
    checks+=1
    assert v, checks
    assert time.perf_counter()-t0<60
@lru_cache(None)
def factors(n):
    d={};p=2
    while p*p<=n:
        while n%p==0:d[p]=d.get(p,0)+1;n//=p
        p+=1
    if n>1:d[n]=d.get(n,0)+1
    return d
def add(a,b,scale=F(1)):
    a=dict(a)
    for p,c in b.items():
        a[p]=a.get(p,F(0))+scale*c
        if not a[p]:del a[p]
    return a
def lg(x,coef=F(1)):
    assert x>0
    return add({p:coef*c for p,c in factors(x.numerator).items()},
               {p:coef*c for p,c in factors(x.denominator).items()},F(-1))
def times(a,c):return {p:v*c for p,v in a.items() if v*c}
def spectrum(table):
    a=table[:];N=len(a);step=1
    while step<N:
        for j in range(0,N,2*step):
            for z in range(j,j+step):a[z],a[z+step]=a[z]+a[z+step],a[z]-a[z+step]
        step*=2
    return [F(x*x,N*N) for x in a]
def audit(table):
    n=len(table).bit_length()-1;p=spectrum(table);I=F(0);Ms=[];Ds=[];es=[];tail={}
    ck(sum(p)==1)
    for i in range(n):
        bit=1<<i;e=F(sum(table[x]!=table[x^bit] for x in range(len(table))),len(table))
        ck(e==sum(p[s] for s in range(len(p)) if s&bit));I+=e;es.append(e)
        M={};D={};mu=F(0);Q=F(0)
        for s in range(len(p)):
            if s&bit:continue
            lower,upper=p[s],p[s|bit];r=lower+upper;Q+=r
            if not upper:continue
            mu+=upper/e
            term=lg(r/upper,upper);M=add(M,term)
            D=add(D,lg((upper/e)/r,upper/e))
            if s.bit_count()>=2:tail=add(tail,term)
        ck(Q==1)
        if e:
            ck(mu==1);ck(M==add(lg(1/e,e),D,-e))
        else:ck(M=={} and D=={})
        Ms.append(M);Ds.append(D)
    jointP=sum(es)/I if I else F(0)
    jointQ=sum(es)/I if I else F(0)
    if I:ck(jointP==1 and jointQ==1)
    M={};D={}
    for e,mi,di in zip(es,Ms,Ds):M=add(M,mi);D=add(D,di,e)
    return dict(p=p,I=I,M=M,D=D,es=es,Ds=Ds,tail=tail)
seeds=[]
for n,masks in [(1,range(4)),(2,range(16)),(3,[1,7,105,150])]:
    for mask in masks:
        table=[1 if (mask>>x)&1 else -1 for x in range(1<<n)]
        if abs(sum(table))!=len(table):seeds.append((n,mask,table))
ck(len(seeds)==20)
rows=[]
for n,mask,seed in seeds:
    sf=audit(seed)
    for m in [1,2]:
        for ell in [2,3]:
            d=n*m+ell;h=[]
            for x in range(1<<d):
                val=(-1)**((x>>(n*m)).bit_count())
                for b in range(m):val*=seed[(x>>(b*n))&((1<<n)-1)]
                h.append(val)
            ah=audit(h);ck(ah['M']==times(sf['M'],F(m)));ck(ah['D']==times(sf['D'],F(m)))
            ck(ah['I']==m*sf['I']+ell);ck(ah['p'][0]==0)
            for k in [1,2,3]:
                q=F(1,1<<k);d0=(1-q)**2+q*q
                table=[h[x&((1<<d)-1)] if (x>>d)==0 else 1 for x in range(1<<(d+k))]
                af=audit(table);ck(af['I']==q*(ah['I']+k))
                controlD=add(lg(F(1)/(2*q),1-q),lg(q/d0,q))
                controlM=add(lg(F(2),q*(1-q)),lg(d0/(q*q),q*q))
                for i in range(d):
                    ck(af['es'][i]==q*ah['es'][i])
                    if ah['es'][i]:ck(af['Ds'][i]==add(ah['Ds'][i],lg(1/q)))
                for i in range(d,d+k):ck(af['es'][i]==q);ck(af['Ds'][i]==controlD)
                expectedD=add(times(ah['D'],q),lg(1/q,q*ah['I']))
                expectedD=add(expectedD,controlD,k*q);ck(af['D']==expectedD)
                ck(af['M']==add(times(ah['M'],q),controlM,F(k)))
                ck(af['tail']==add(times(ah['M'],q),lg(F(2),k*q*(1-k*q))))
                rows.append(dict(n=n,mask=mask,m=m,ell=ell,k=k,N=d+k))
out=dict(status='PASS',cases=len(rows),assertions=checks,runtime_seconds=time.perf_counter()-t0,
         arithmetic='Integer FWHT; exact Fraction normalizers and physical influences; exact prime-log coefficient cancellation',cases_checked=rows)
(RUN/'out').mkdir(exist_ok=True)
(RUN/'out/CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='cases_checked'},indent=2))
