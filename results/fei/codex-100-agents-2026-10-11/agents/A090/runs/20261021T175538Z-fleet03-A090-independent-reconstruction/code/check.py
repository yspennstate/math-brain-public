from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json, time, hashlib

HERE=Path(__file__).resolve().parents[1]
started=time.perf_counter()
checks=0
def require(x):
    global checks
    checks+=1
    if not x: raise AssertionError(checks)

# Logarithmic linear forms, indexed by primes. Exact equality is tested
# before any intervals are consulted.
def add(*terms):
    r={}
    for c,d in terms:
        for p,v in d.items():
            r[p]=r.get(p,F(0))+c*v
    return {p:v for p,v in r.items() if v}
def logq(q):
    q=F(q); require(q>0); r={}
    for n,sgn in [(q.numerator,1),(q.denominator,-1)]:
        p=2
        while p*p<=n:
            while n%p==0:
                r[p]=r.get(p,F(0))+sgn; n//=p
            p+=1
        if n>1:r[n]=r.get(n,F(0))+sgn
    return {p:v for p,v in r.items() if v}
def entropy(p):return add(*[(-q,logq(q)) for q in p if q])
def ce(p,q):
    require(len(p)==len(q))
    require(all(not x or y>0 for x,y in zip(p,q)))
    return add(*[(-x,logq(y)) for x,y in zip(p,q) if x])
def ln_interval(x):
    t=(x-1)/(x+1); require(0<=t<=F(1,3))
    value=sum((2*t**(2*k+1)/F(2*k+1) for k in range(40)),F(0))
    err=2*t**81/(81*(1-t*t))
    return value,value+err
LN2=ln_interval(F(2))
@lru_cache(None)
def log_interval(p):
    k=p.bit_length()-1; lo,hi=ln_interval(F(p,2**k))
    return F(k)+lo/LN2[1],F(k)+hi/LN2[0]
def interval(d):
    lo=hi=F(0)
    for p,c in d.items():
        a,b=log_interval(p)
        lo+=c*(a if c>=0 else b); hi+=c*(b if c>=0 else a)
    return lo,hi
def positive(d):return interval(d)[0]>0
def nonnegative(d):return not d or interval(d)[0]>=0
def approx(d):return [float(x) for x in interval(d)]
def walsh(v):
    a=list(v); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):a[k],a[k+h]=a[k]+a[k+h],a[k]-a[k+h]
        h*=2
    return a
def spectrum(v):return [F(x*x,len(v)**2) for x in walsh(v)]
def restriction(v,j,s):
    return [x for k,x in enumerate(v) if (k>>j)&1==s]
def marginal(p,j):
    return [p[k]+p[k|(1<<j)] for k in range(len(p)) if not k&(1<<j)]
def influence(v,j):
    return F(sum(x!=v[k^(1<<j)] for k,x in enumerate(v)),len(v))
def erasure(p,j):return add((1,entropy(p)),(-1,entropy(marginal(p,j))))
def one_query(v,q,j):
    p=spectrum(v); pm=marginal(p,j); qm=marginal(q,j)
    children=[restriction(v,j,s) for s in (0,1)]
    ps=[spectrum(c) for c in children]
    require(all((a+b)/2==c for a,b,c in zip(*ps,pm)))
    require(sum(qm)==1)
    b=erasure(p,j)
    # Independent occupancy-conditional definition, including Q-only support.
    r=add(*[(x,logq(x*qm[k//2 if j==0 else ((k&((1<<j)-1))|((k>>(j+1))<<j))]/(q[k]*pm[k//2 if j==0 else ((k&((1<<j)-1))|((k>>(j+1))<<j))]))) for k,x in enumerate(p) if x])
    require(nonnegative(r))
    terminal=add((F(1,2),ce(ps[0],qm)),(F(1,2),ce(ps[1],qm)))
    require(not add((1,ce(p,q)),(-1,b),(-1,r),(-1,terminal)))
    return children,qm,b,r
def adaptive(v,q,depth=0):
    n=len(v).bit_length()-1
    if not n:return {},ce(spectrum(v),q),{}
    # Outcome-dependent future choices are encoded by truth-table-dependent
    # influence ordering. Every actual leaf/reference is kept, even constants.
    j=min(range(n),key=lambda j:(influence(v,j),j)) if depth%2 else max(range(n),key=lambda j:(influence(v,j),-j))
    cs,qm,b,r=one_query(v,q,j)
    c0,t0,r0=adaptive(cs[0],qm,depth+1); c1,t1,r1=adaptive(cs[1],qm,depth+1)
    costs=add((1,b),(F(1,2),c0),(F(1,2),c1))
    terminal=add((F(1,2),t0),(F(1,2),t1))
    refunds=add((1,r),(F(1,2),r0),(F(1,2),r1))
    require(not add((1,ce(spectrum(v),q)),(-1,costs),(-1,terminal),(-1,refunds)))
    return costs,terminal,refunds

small=0
for n in range(4):
    for mask in range(1<<(1<<n)):
        v=[1 if mask>>k&1 else -1 for k in range(1<<n)]
        p=spectrum(v); u=[F(1,len(v))]*len(v)
        for q in [p,u,[(a+b)/2 for a,b in zip(p,u)]]:
            for j in range(n):one_query(v,q,j)
            adaptive(v,q)
        small+=1
        require(time.perf_counter()-started<60)

# Nine-bit fixture, data bits 0..5, Maj3 bits 6..8.
b=[1 if y&7==0 else -1 for y in range(64)]
c=[-1 if y==0 else b[y] for y in range(64)]
v=[(1 if (z>>6).bit_count()<=1 else -1) if z%64==0 else b[z%64] for z in range(512)]
p=spectrum(v); rootH=entropy(p)
require(positive(add((F(3),{2:F(1)}),(-1,rootH))))
require(interval(rootH)[1]<F(489,200))
require(interval(add((3,{2:F(1)}),(-1,rootH)))[0]>F(111,200))
require(sum(influence(v,j) for j in range(6))==F(3,4))
# Direct character sums are a separate implementation of the root amplitudes.
w=walsh(v)
require(all(w[t]==sum(x*(-1 if (k&t).bit_count()%2 else 1) for k,x in enumerate(v)) for t in range(512)))
t0=add((F(1,2),entropy(spectrum(b))),(F(1,2),entropy(spectrum(c))))
escrow=add((3,{2:F(1)}),(-1,t0))
def fixed_policy(v,q,labels,order):
    if not order:return {},entropy(spectrum(v)),ce(spectrum(v),q),{}
    j=labels.index(order[0]); cs,qm,e,r=one_query(v,q,j)
    labs=labels[:j]+labels[j+1:]
    a=fixed_policy(cs[0],qm,labs,order[1:]); b_=fixed_policy(cs[1],qm,labs,order[1:])
    return tuple(add((1,e if k==0 else r if k==3 else {}),(F(1,2),a[k]),(F(1,2),b_[k])) for k in range(4))
rows=[]
for j in range(6):
    W,T,C,R=fixed_policy(v,p,list(range(9)),[j,6,7,8])
    require(not add((1,rootH),(-1,W),(-1,C),(-1,R)))
    margin=add((3,{2:F(1)}),(-1,W),(-1,T))
    frozen=add((1,escrow),(-1,W))
    require(positive(margin))
    require(positive(frozen) if j>=3 else positive(add((-1,frozen))))
    flo,fhi=interval(frozen)
    if j<3:
        require(-F(28552,10**6)<flo<=fhi<-F(28551,10**6))
        require(interval(margin)[0]>F(1112678,10**6))
    else:
        require(F(546819,10**6)<flo<=fhi<F(546820,10**6))
        require(interval(margin)[0]>F(634309,10**6))
    require(positive(add((3,{2:F(1)}),(-1,W),(-1,C))))
    rows.append(dict(query=j,margin=approx(margin),frozen_margin=approx(frozen),inherited_CE_margin=approx(add((3,{2:F(1)}),(-1,W),(-1,C))),refund=approx(R)))
for j in range(9):one_query(v,p,j)

# Matching initial law, constant actual child, nonzero inherited terminal bill.
point=[1,1,1,1,-1,1,1,1]; pp=spectrum(point)
cs,qq,_,_=one_query(point,pp,0)
require(cs[1]==[1]*4)
require(qq==[F(5,8),F(1,8),F(1,8),F(1,8)])
cost=ce(spectrum(cs[1]),qq)
require(not add((1,cost),(-1,logq(F(8,5)))))
require(positive(cost))
result={"status":"PASS", "small_truth_tables":small,"assertions":checks,"arithmetic":"exact Fraction and prime-log identities; rational atanh-40 intervals", "root_entropy_bits":approx(rootH),"root_entropy_exact_prime_log_form":{str(k):str(x) for k,x in rootH.items()},"certified_root_entropy_upper":"489/200","certified_original_bank_surplus_lower":"111/200", "root_same_bank_margin":approx(add((3,{2:F(1)}),(-1,rootH))),"six_queries":rows,"constant_terminal_CE":approx(cost),"elapsed_seconds":time.perf_counter()-started,"checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'out/CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
