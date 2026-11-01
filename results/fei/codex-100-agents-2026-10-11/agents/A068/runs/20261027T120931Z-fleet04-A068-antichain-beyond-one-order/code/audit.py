from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,math
R=Path(__file__).resolve().parents[1];t=time.perf_counter();checks=0
def ck(x):
    global checks
    checks+=1;assert x,checks
    if time.perf_counter()-t>55:raise RuntimeError('frozen cap55s')
def par(x):return x.bit_count()&1
def direct(a):return [F(sum(v*(-1 if par(x&s) else 1) for x,v in enumerate(a)),len(a)) for s in range(len(a))]
def lnseries(y):
    z=(y-1)/(y+1);z2=z*z;term=z;s=F(0);steps=20
    for j in range(steps):s+=term/F(2*j+1);term*=z2
    lo=2*s;return lo,lo+2*term/F(2*steps+1)/(1-z2)
L2=lnseries(F(2))
@lru_cache(None)
def log2bounds(x):
    ck(x>=1)
    k=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/F(2)**k
    if y<1:k-=1;y*=2
    if y>=2:k+=1;y/=2
    lo,hi=lnseries(y)
    return F(k)+lo/L2[1],F(k)+hi/L2[0]
def cebounds(p,q):
    lo=hi=F(0)
    for a,b in zip(p,q):
        if a:
            ck(b>0);l,h=log2bounds(1/b);lo+=a*l;hi+=a*h
    return lo,hi
source_rows=[]
for d,m,mask in ((0,6,1),(1,6,2),(2,8,1),(3,12,1)):
    cn=1<<d;N=d+m;size=1<<N
    g=[1 if mask>>i&1 else -1 for i in range(cn)];gh=direct(g);pg=[v*v for v in gh]
    ig=sum((F(g[x]!=g[x^(1<<i)],cn) for x in range(cn) for i in range(d)),F(0))
    q=pg if not ig else [(a+F(1,cn))/2 for a in pg]
    Cg=cebounds(pg,q)
    maxk=1<<(m//4)
    for k in (1,2,maxk):
        E={((j*9)^(j<<d))%size for j in range(k)};ck(len(E)==k)
        theta=F(k,size);eta=4*theta
        e=[-F(2,size)*sum(g[x&(cn-1)]*(-1 if par(u&x) else 1) for x in E) for u in range(cn)]
        inside=[(a+b)**2 for a,b in zip(gh,e)]
        outside=4*theta-sum((v*v for v in e),F(0));ck(outside>=0);ck(sum(inside)+outside==1)
        floor=eta/size;qr=[(1-eta)*v+floor for v in q]
        C=cebounds(inside+[outside],qr+[floor])
        signed=0
        for x in E:
            for i in range(N):
                y=x^(1<<i)
                if y in E:continue
                was=(g[x&(cn-1)]!=g[y&(cn-1)])
                signed+=-1 if was else 1
        If=ig+F(signed,size//2)
        ck(If-ig>=m*theta);ck(C[1]<=2*Cg[0]+24*(If-ig))
        source_rows.append(dict(d=d,m=m,k=k,If=str(If),actual_CE_upper=str(C[1]),bound='2Cg+24(actual influence increase)'))

@lru_cache(None)
def factor(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def add(*terms):
    out={}
    for v,c in terms:
        for p,a in v.items():out[p]=out.get(p,F(0))+c*a
    return {p:a for p,a in out.items() if a}
def logexpr(x):return add((factor(x.numerator),F(1)),(factor(x.denominator),F(-1)))
def ce(p,q):
    ans={}
    for a,b in zip(p,q):
        if a:ans=add((ans,F(1)),(logexpr(b),-a))
    return ans
def entropy(p):return ce(p,p)
def kl(p,q):return add((ce(p,q),F(1)),(entropy(p),F(-1)))
def project(p,i):
    out=[F(0)]*(len(p)//2)
    for s,a in enumerate(p):
        j=(s&((1<<i)-1))|((s>>(i+1))<<i);out[j]+=a
    return out
queries=0;roots=0
for n in range(4):
    size=1<<n
    for mask in range(1<<size):
        roots+=1;a=[1 if mask>>x&1 else -1 for x in range(size)];p=[v*v for v in direct(a)]
        for i in range(n):
            children=[]
            for b in (0,1):
                child=[a[(x&((1<<i)-1))|(b<<i)|((x>>i)<<(i+1))] for x in range(size//2)]
                children.append([v*v for v in direct(child)])
            pp=project(p,i);ck(pp==[(u+v)/2 for u,v in zip(*children)])
            for q in ([(v+F(1,size))/2 for v in p],[F(s+1,size*(size+1)//2) for s in range(size)]):
                qp=project(q,i)
                D=kl(p,q);L=add((D,F(1)),(kl(pp,qp),F(-1)))
                J=add((kl(children[0],pp),F(1,2)),(kl(children[1],pp),F(1,2)))
                diff=add((kl(children[0],qp),F(1,2)),(kl(children[1],qp),F(1,2)),(D,F(-1)),(J,F(-1)),(L,F(1)))
                ck(not diff)
                # The COMPLETE one-query bill is CEroot+J, never just minus a KL.
                bill=add((entropy(p),F(1)),(entropy(children[0]),F(-1,2)),(entropy(children[1]),F(-1,2)),(L,F(1)),(ce(children[0],qp),F(1,2)),(ce(children[1],qp),F(1,2)),(ce(p,q),F(-1)),(J,F(-1)))
                ck(not bill)
                queries+=1
# AND2 projection != prescribed true-kernel inheritance on its constant child.
p=[F(1,4)]*4;qp=project(p,0);ck(qp==[F(1,2),F(1,2)]);ck(qp!=[F(1),F(0)])
result=dict(status='PASS',assertions=checks,seconds=time.perf_counter()-t,source_roots=len(source_rows),local_roots=roots,query_reference_cases=queries,arithmetic='direct characters/sparse edge toggles;20-term rational atanh intervals; exact prime-log identities',source_rows=source_rows)
(R/'out/AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k!='source_rows'}))
