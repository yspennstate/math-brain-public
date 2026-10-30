"""A030-plateau-reserve-v1: exact prime-log Bellman reconstruction."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
from functools import lru_cache
import json,time,hashlib
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); checks=0; signs=0; zeros=0
COUNTS=dict(core_trees=0,spectator_parents=0,pair_parents=0,addressing_cases=0)
ZERO=()
def ck(condition):
    global checks
    checks+=1
    assert condition,checks
    assert time.perf_counter()-START<59,'Frozen pilot guard'
def expr(d): return tuple(sorted((p,F(c)) for p,c in d.items() if c))
def add(*xs):
    d={}
    for mult,x in xs:
        for p,c in x: d[p]=d.get(p,F(0))+mult*c
    return expr(d)
def const(c): return expr({2:F(c)})
@lru_cache(None)
def factors(n):
    d={}; p=2
    while p*p<=n:
        while n%p==0: d[p]=d.get(p,0)+1; n//=p
        p+=1
    if n>1:d[n]=d.get(n,0)+1
    return d
@lru_cache(None)
def ln_interval(x):
    x=F(x); k=0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    t=(x-1)/(x+1)
    s=2*sum((t**(2*j+1)/F(2*j+1) for j in range(40)),F(0))
    tail=2*t**81/(81*(1-t*t))
    if k:
        z=F(1,3); a=2*sum((z**(2*j+1)/F(2*j+1) for j in range(40)),F(0))
        b=a+2*z**81/(81*(1-z*z))
        return (s+k*a,s+tail+k*b) if k>0 else (s+k*b,s+tail+k*a)
    return s,s+tail
@lru_cache(None)
def log2_interval(p):
    if p==2:return F(1),F(1)
    a,b=ln_interval(p); u,v=ln_interval(2)
    q=[a/u,a/v,b/u,b/v]
    return min(q),max(q)
@lru_cache(None)
def bounds(x):
    lo=hi=F(0)
    for p,c in x:
        a,b=log2_interval(p)
        if c>=0:lo+=c*a;hi+=c*b
        else:lo+=c*b;hi+=c*a
    return lo,hi
def positive(x):
    global signs,zeros
    if not x:zeros+=1;return ZERO
    lo,hi=bounds(x);signs+=1
    if lo>0:return x
    if hi<0:return ZERO
    raise ArithmeticError('Nonzero prime-log sign not certified within frozen precision')
def walsh(t):
    a=list(t);step=1
    while step<len(a):
        for b in range(0,len(a),2*step):
            for j in range(b,b+step):
                u,v=a[j],a[j+step];a[j],a[j+step]=u+v,u-v
        step*=2
    return a
@lru_cache(None)
def stats(t):
    n=len(t).bit_length()-1;den=len(t)**2;h={};di=[F(0)]*n
    for mask,v in enumerate(walsh(t)):
        if not v:continue
        p=F(v*v,den);h[2]=h.get(2,F(0))+2*n*p
        for prime,e in factors(abs(v)).items():h[prime]=h.get(prime,F(0))-2*p*e
        for j in range(n):
            if mask>>j&1:di[j]+=p
    return expr(h),tuple(di)
def child(t,i,v):
    low=(1<<i)-1
    return tuple(t[(x&low)|((x>>i)<<(i+1))|(v<<i)] for x in range(len(t)//2))
@lru_cache(None)
def reserve(t,order,C):
    if len(set(t))==1:return ZERO
    h,di=stats(t);i=order[0]
    t0,t1=child(t,i,0),child(t,i,1)
    rest=tuple(j-(j>i) for j in order[1:])
    h0,h1=stats(t0)[0],stats(t1)[0]
    q0,q1=reserve(t0,rest,C),reserve(t1,rest,C)
    return positive(add((1,h),(-F(1,2),h0),(-F(1,2),h1),(-1,const(C*di[i])),(F(1,2),q0),(F(1,2),q1)))
def spectators(t,n,m):
    return tuple(t[x&((1<<n)-1)]*(-1 if (x>>n).bit_count()%2 else 1) for x in range(1<<(n+m)))
def pairs(t,n):
    return tuple(t[sum(((x>>(2*i)&3).bit_count()%2)<<i for i in range(n))] for x in range(1<<(2*n)))
for n in (1,2,3):
    for mask in range(1<<(1<<n)):
        t=tuple(-1 if mask>>x&1 else 1 for x in range(1<<n))
        H,di=stats(t);I=sum(di,F(0))
        for order in permutations(range(n)):
            COUNTS['core_trees']+=1
            for C in (0,1,4):
                q=reserve(t,order,C)
                ck(positive(add((1,q),(-1,H)))==ZERO)
                for m in (1,2):
                    parent=spectators(t,n,m)
                    got=reserve(parent,tuple(range(n,n+m))+order,C)
                    expected=positive(add((1,q),(-1,const(C*m))))
                    ck(got==expected)
                    # Every physical plateau leaf, not an average-spectrum substitute.
                    for z in range(1<<m):
                        leaf=tuple(v*(-1 if z.bit_count()%2 else 1) for v in t)
                        ck(reserve(leaf,order,C)==q)
                    COUNTS['spectator_parents']+=1
                if n<=2 or mask in (1,22,105,128,232):
                    parent=pairs(t,n); compression=tuple(2*i+1 for i in range(n))
                    physical_core=tuple(2*i for i in order)
                    got=reserve(parent,compression+physical_core,C)
                    ck(got==positive(add((1,q),(-1,const(C*I)))))
                    ck(stats(parent)[0]==H)
                    ck(sum(stats(parent)[1],F(0))==2*I)
                    COUNTS['pair_parents']+=1
# Independent Boolean address tables, with actual data-first and address-first orders.
address=[]
for a in (1,2,3):
    n=a+(1<<a)
    t=tuple(-1 if x>>(a+(x&((1<<a)-1)))&1 else 1 for x in range(1<<n))
    data_order=tuple(range(a,n))+tuple(range(a))
    addr_order=tuple(range(a))+tuple(range(a,n))
    H,di=stats(t);ck(H==const(2*a));ck(sum(di)==1+F(a,2))
    for C in (1,2,4):
        q=reserve(t,data_order,C);qaddr=reserve(t,addr_order,C)
        ck(positive(add((1,const(a-C)),(-1,q)))==ZERO)
        if C==4:ck(qaddr==ZERO)
        m=(2*a+C-1)//C
        ck(positive(add((1,q),(-1,const(C*m))))==ZERO)
        lo,hi=bounds(q)
        address.append(dict(a=a,C=C,m=m,q_expression=[(p,str(v)) for p,v in q],q_bounds=[str(lo),str(hi)],address_first_q=[(p,str(v)) for p,v in qaddr]))
        COUNTS['addressing_cases']+=1
    # Avoid retaining large addressing tables through future cases.
    stats.cache_clear();reserve.cache_clear()
ck(COUNTS==dict(core_trees=1572,spectator_parents=9432,pair_parents=198,addressing_cases=9))
out=dict(status='PASS',helper_version='A030-plateau-reserve-v1',checks=checks,counts=COUNTS,
 certified_nonzero_signs=signs,exact_zero_signs=zeros,elapsed_seconds=time.perf_counter()-START,
 arithmetic='Fraction prime-log expressions; exact symbolic equalities; 40-term rational atanh sign intervals',
 address_records=address,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(ROOT/'out/VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='address_records'},indent=2))
