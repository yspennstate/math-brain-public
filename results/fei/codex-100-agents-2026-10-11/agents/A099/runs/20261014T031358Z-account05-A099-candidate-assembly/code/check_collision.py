from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,sys,time
RUN=Path(__file__).resolve().parents[1]; start=time.perf_counter(); checks=0
def verify(ok):
    global checks
    checks+=1
    assert ok
@lru_cache(None)
def primes(n):
    p=2;v={}
    while p*p<=n:
        while n%p==0:v[p]=v.get(p,0)+1;n//=p
        p+=1
    if n>1:v[n]=v.get(n,0)+1
    return v
def term(v,w,q):
    if not w:return
    assert q>0
    for n,sign in ((q.numerator,1),(q.denominator,-1)):
        for p,e in primes(n).items():v[p]=v.get(p,F(0))+sign*w*e
    for p in list(v):
        if not v[p]:del v[p]
def combine(*vs):
    o={}
    for v in vs:
        for p,w in v.items():o[p]=o.get(p,F(0))+w
    return {p:w for p,w in o.items() if w}
def scale(v,c):return {p:w*c for p,w in v.items() if w*c}
def CE(p,r):
    o={}
    for x,y in zip(p,r):
        if x:term(o,x,1/y)
    return o
# Bound the power-of-two contribution using the explicit ln2 series.
@lru_cache(None)
def lnat(q):
    power=0
    while q>=2:q/=2;power+=1
    while q<1:q*=2;power-=1
    def series(x):
        z=(x-1)/(x+1);lo=sum((2*z**(2*j+1)/F(2*j+1) for j in range(20)),F(0))
        return lo,lo+2*z**41/(41*(1-z*z))
    lo,hi=series(q);l2,h2=series(F(2))
    return lo+power*(l2 if power>=0 else h2),hi+power*(h2 if power>=0 else l2)
def interval(v):
    lo=hi=F(0)
    for p,w in v.items():
        a,b=lnat(F(p));lo+=w*(a if w>=0 else b);hi+=w*(b if w>=0 else a)
    return lo,hi
def coeff(t):
    N=len(t)
    return [F(sum(y*(-1 if (s&x).bit_count()%2 else 1) for x,y in enumerate(t)),N) for s in range(N)]
def table(n,mask):return [-1 if mask>>x&1 else 1 for x in range(1<<n)]
def influences(t):return [F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(len(t).bit_length()-1)]
def calibrate(p,r,C):
    v=sum(p[i] for i in range(len(p)) if i not in C);w=sum(r[i] for i in range(len(p)) if i not in C)
    return [p[i] if i in C else r[i]*v/w if v else F(0) for i in range(len(p))]
def run(t,x,y,G,H):
    ag,bh=coeff(G),coeff(H);ig,ih=influences(G),influences(H)
    nd=t+x+y;N=1<<nd
    a=[F(0)]*N;b=[F(0)]*N
    for j,v in enumerate(ag):a[j]=v
    for j,v in enumerate(bh):b[(j&((1<<t)-1))|((j>>t)<<(t+x))]=v
    union=[(G[j&((1<<(t+x))-1)],H[(j&((1<<t)-1))|((j>>(t+x))<<t)]) for j in range(N)]
    d=F(sum(g!=h for g,h in union),N); ds=min(d,1-d)
    parent=[g if z==0 else h for z in (0,1) for g,h in union]
    p=[v*v for v in coeff(parent)];pa=[v*v for v in a];pb=[v*v for v in b]
    verify(sum(p)==1 and sum(pa)==1 and sum(pb)==1)
    ip=influences(parent);verify(ip[-1]==d)
    for j in range(nd):
        e=(ig[j] if j<t+x else F(0))+(ih[j] if j<t else ih[t+j-(t+x)] if j>=t+x else F(0))
        verify(ip[j]==e/2)
    bf=[-v if d>F(1,2) else v for v in b];C=set(range(1<<t))
    delta=sum((a[j]-bf[j])**2/4 for j in C)
    verify(0<=delta<=min(ds,(1<<t)*ds*ds))
    outside=sum((pa[j]+pb[j])/2 for j in range(N) if j not in C)
    verify(outside<=2*ds)
    ep=CE(p,p);eg=CE(pa,pa);eh=CE(pb,pb);de=combine(ep,scale(eg,F(-1,2)),scale(eh,F(-1,2)))
    if not ds:verify(not de)
    else:
        lo,hi=interval(de);l2,h2=lnat(F(2))
        verify((t+2)*ds*l2+3*ds-hi>0)
    for refkind in ('uniform','increasing'):
        rg=[F(1,len(ag)) if refkind=='uniform' else F(j+1,len(ag)*(len(ag)+1)//2) for j in range(len(ag))]
        rh=[F(1,len(bh)) if refkind=='uniform' else F(j+1,len(bh)*(len(bh)+1)//2) for j in range(len(bh))]
        pg=[v*v for v in ag];ph=[v*v for v in bh];cg=calibrate(pg,rg,C);ch=calibrate(ph,rh,C)
        verify(sum(cg)==sum(ch)==1)
        Rg=[F(0)]*N;Rh=[F(0)]*N
        for j,v in enumerate(cg):Rg[j]=v
        for j,v in enumerate(ch):Rh[(j&((1<<t)-1))|((j>>t)<<(t+x))]=v
        Q=[F(0)]*(2*N)
        for j in range(N):
            r=(Rg[j]+Rh[j])/2;q=(pa[j]+pb[j])/2
            if q:Q[j]=r*p[j]/q;Q[j+N]=r*p[j+N]/q
            else:Q[j]=r
        verify(sum(Q)==1 and all(Q[j]>0 for j,v in enumerate(p) if v))
        cp=CE(p,Q);cchild=scale(combine(CE(pg,cg),CE(ph,ch)),F(1,2))
        verify(not combine(cp,scale(cchild,-1),scale(de,-1)))
        for old,new,true in ((rg,cg,pg),(rh,ch,ph)):
            diff=combine(CE(true,old),scale(CE(true,new),-1))
            verify(not diff or interval(diff)[0]>0)
    verify(time.perf_counter()-start<60)
cases=[]
for g in range(16):
    for h in range(16):cases.append((2,0,0,table(2,g),table(2,h)))
masks=[1<<j for j in range(8)]+[0,255,150,232]
for g in masks:
    for h in masks:cases.append((3,0,0,table(3,g),table(3,h)))
private=[0,255,1,7,105,150,232,254]
for g in private:
    for h in private:cases.append((2,1,1,table(3,g),table(3,h)))
bent=[(-1)**(((j&1)*((j>>1)&1)+((j>>2)&1)*((j>>3)&1))%2) for j in range(16)]
flip=bent.copy();flip[0]*=-1
cases.extend([(4,0,0,bent,flip),(4,0,0,bent,[-v for v in flip])])
if '--pilot' in sys.argv:cases=cases[:4]
for case in cases:run(*case)
out={'status':'PASS','cases':len(cases),'reference_cases':2*len(cases),'assertions':checks,'runtime_seconds':time.perf_counter()-start,'arithmetic':'Direct signed characters and physical edges; Fraction complete references; prime-log cancellation; fixed 20-term rational ln bounds','max_root_dimension':5,'helper_version':'A099-linear-collision-review-v1'}
(RUN/'out'/('PILOT.json' if '--pilot' in sys.argv else 'EXACT_REVIEW.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
