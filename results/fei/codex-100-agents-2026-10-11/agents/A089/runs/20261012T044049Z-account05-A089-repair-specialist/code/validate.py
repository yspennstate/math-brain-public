"""Independent exact Walsh/edge and biased-outer reconstruction, v1."""
from profiles import *
from collections import Counter
checks=0
def eq(a,b):
    global checks
    assert a==b,(a,b);checks+=1
@lru_cache(maxsize=4096)
def factor(n):
    d=2;v={}
    while d*d<=n:
        while n%d==0:v[d]=v.get(d,0)+1;n//=d
        d+=1
    if n>1:v[n]=v.get(n,0)+1
    return v
def add(a,b,t=F(1)):
    c=a.copy()
    for p,v in b.items():
        c[p]=c.get(p,F(0))+t*v
        if not c[p]:del c[p]
    return c
@lru_cache(maxsize=10000)
def entropy(x):
    if not x:return {}
    a,b=factor(x.numerator),factor(x.denominator)
    return {p:x*(b.get(p,0)-a.get(p,0)) for p in set(a)|set(b) if a.get(p,0)!=b.get(p,0)}
@lru_cache(maxsize=10000)
def phi(a,b):return add(add(entropy(a),entropy(b)),entropy(a+b),-1)
def lex_symbolic(n,t,i):
    u=1-2*F(t%(1<<(i+1)),1<<(i+1));d=1-abs(u)
    if not d:return F(0),{}
    J={2:2-2*d} if d!=1 else {}
    for j in range(i+1,n):
        c=1-2*((t>>j)&1)
        J=add(J,phi((u-c)**2,d*d),1/(2*d));u=(u+c)/2;d/=2
    return d,add({},add(J,phi(u*u,d*d),1/d),d)
def B(w,i):
    pairs=Counter((w[t],w[t|(1<<i)]) for t in range(len(w)) if not t&(1<<i))
    result={};inf=F(0)
    for (a,b),count in pairs.items():result=add(result,phi(a*a,b*b),F(count));inf+=count*b*b
    return inf,result
def outer(v):return -1 if v<3 else 1
start=time.perf_counter();lexcount=0
for n in range(1,7):
    for t in range(1,1<<n):
        vals=[-1 if x<t else 1 for x in range(1<<n)];w=fwht(vals)
        eq(sum(a*a for a in w),F(1));lexcount+=1
        for i in range(n):
            inf,bi=B(w,i);di,formula=lex_symbolic(n,t,i)
            eq(inf,di);eq(bi,formula)
            eq(inf,F(sum(vals[x]!=vals[x^(1<<i)] for x in range(1<<n)),1<<n))
        assert time.perf_counter()-start<55
for mask in range(16):
    gv=[-1 if (mask>>x)&1 else 1 for x in range(4)];gw=fwht(gv);mu=gw[0]
    vals=[]
    for x in range(1<<10):
        index=sum((gv[(x>>(2*j))&3]==-1)<<j for j in range(5));vals.append(outer(index))
    w=fwht(vals)
    for j in range(5):
        q,rows=section(mu,j)
        for i in range(2):
            di,bi=B(gw,i);singleton=gw[1<<i]
            formula=add({},add(bi,phi(mu*mu,singleton*singleton),-1),q)
            for T,a,b,weight in rows:formula=add(formula,phi((a+mu*b)**2,b*b*singleton*singleton),weight)
            actualinf,actualB=B(w,2*j+i)
            eq(actualinf,q*di);eq(actualB,formula)
            eq(actualinf,F(sum(vals[x]!=vals[x^(1<<(2*j+i))] for x in range(1<<10)),1<<10))
    assert time.perf_counter()-start<55
data=json.loads((ROOT/'out'/'PROFILES.json').read_text())
mus=[F(0)]+[F(c['mean']) for c in data['composition'][:3]]+[F(-3,4),F(-1,2),F(1,2),F(3,4)]
for mu in mus:
    var=1-mu*mu
    for j in (0,2):
        others=[i for i in range(5) if i!=j];q,rows=section(mu,j)
        events=[]
        for mask in range(16):
            index=sum(((mask>>k)&1)<<i for k,i in enumerate(others))
            signs={i:1-2*((index>>i)&1) for i in others}
            weight=F(1)
            for i in others:weight*=(1+mu*signs[i])/2
            fp,fm=outer(index),outer(index|(1<<j))
            events.append((signs,weight,F(fp-fm,2),((1+mu)*fp+(1-mu)*fm)/2))
        eq(q,sum(weight*b*b for signs,weight,b,center in events))
        for T,a,b,weight in rows:
            bdirect=adirect=F(0)
            for signs,prob,bv,center in events:
                test=F(1)
                for i in others:
                    if T&(1<<i):test*=signs[i]-mu
                bdirect+=prob*bv*test;adirect+=prob*center*test
            eq(b,bdirect/var**T.bit_count());eq(a+mu*b,adirect/var**T.bit_count())
        assert time.perf_counter()-start<55
result={'version':'validate.py/v1','arithmetic':'integer Walsh, exact boundary counts, Fraction and formal prime-log equality; independently reconstructed biased-product moments','lex_truth_tables':lexcount,'lex_domain':'all thresholds on n=1..6','composition_inner_truth_tables':16,'composition_dimension':10,'biased_outer_parameters':len(mus),'assertions_passed':checks,'failed':0,'runtime_seconds':time.perf_counter()-start}
(ROOT/'out'/'VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
