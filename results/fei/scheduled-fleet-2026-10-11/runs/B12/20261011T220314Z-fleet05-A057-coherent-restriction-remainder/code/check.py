from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import itertools,json,time,hashlib

START=time.monotonic()
COUNTS={}
def check(ok,key):
    assert ok,key
    COUNTS[key]=COUNTS.get(key,0)+1
    if time.monotonic()-START>60: raise RuntimeError('frozen 60 second runtime exceeded')
def walsh(t):
    v=list(t); n=len(v); step=1
    while step<n:
        for k in range(0,n,2*step):
            for j in range(k,k+step):
                x,y=v[j],v[j+step]; v[j],v[j+step]=x+y,x-y
        step*=2
    return [Q(x,n) for x in v]
def restrict(t,i,s):
    return [t[(z&((1<<i)-1)) | (s<<i) | ((z>>i)<<(i+1))] for z in range(len(t)//2)]
def influence(t,i):
    return Q(sum(t[z]!=t[z^(1<<i)] for z in range(len(t))),len(t))
def total_inf(t): return sum(influence(t,i) for i in range(len(t).bit_length()-1))
def add(*exprs):
    d={}
    for e in exprs:
        for p,c in e.items(): d[p]=d.get(p,Q(0))+c
    return {p:c for p,c in d.items() if c}
def scale(e,c): return {p:v*c for p,v in e.items() if v*c}
@lru_cache(None)
def factor(n):
    d={}; p=2
    while p*p<=n:
        while n%p==0: d[p]=d.get(p,0)+1; n//=p
        p+=1
    if n>1:d[n]=d.get(n,0)+1
    return d
@lru_cache(None)
def log_expr(x):
    x=Q(x)
    return add(factor(x.numerator),scale(factor(x.denominator),-1))
def mass_ent(m):
    return add(*(scale(log_expr(Q(1)/x),x) for x in m if x))
def raw(v):return mass_ent([x*x for x in v])
def entropy(t):return raw(walsh(t))
def erasure(t,i):
    w=walsh(t); p=[v*v for v in w]
    marginal=[p[(z&((1<<i)-1)) | ((z>>i)<<(i+1))]+p[(z&((1<<i)-1)) | (1<<i) | ((z>>i)<<(i+1))] for z in range(len(p)//2)]
    return add(mass_ent(p),scale(mass_ent(marginal),-1))
def dec(t,i):return add(entropy(t),scale(add(entropy(restrict(t,i,0)),entropy(restrict(t,i,1))),Q(-1,2)))
@lru_cache(None)
def log_bounds_integer(p):
    k=p.bit_length()-1; x=Q(p,1<<k)
    def series(x):
        z=(x-1)/(x+1); term=z; acc=Q(0)
        for j in range(48):
            acc+=term/Q(2*j+1);term*=z*z
        lo=2*acc;err=2*term/(Q(97)*(1-z*z))
        return lo,lo+err
    a,b=series(x); c,d=series(Q(2))
    return a+k*c,b+k*d
def bounds(e):
    lo=hi=Q(0)
    for p,c in e.items():
        a,b=log_bounds_integer(p)
        lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
    return lo,hi

balanced=[tuple(1 if z in pos else -1 for z in range(8)) for pos in itertools.combinations(range(8),4)]
min_margin=None
for mask in range(16):
    g=tuple(1 if mask>>z&1 else -1 for z in range(4))
    gp,gm=restrict(g,0,0),restrict(g,0,1)
    # bit 0 is physical sign +1 and bit 1 is -1.
    a=walsh([Q(u+v,2) for u,v in zip(gp,gm)])
    b=walsh([Q(u-v,2) for u,v in zip(gp,gm)])
    q=sum(v*v for v in b)
    A=[u*u for u in a];B=[v*v for v in b]
    outer_erasure=add(mass_ent(A),mass_ent(B),scale(mass_ent([u+v for u,v in zip(A,B)]),-1))
    for h in balanced:
        f=tuple(g[(0 if h[z&7]==1 else 1) | ((z>>3)<<1)] for z in range(16))
        for i in range(3):
            alpha=walsh(h)[1<<i]; x=alpha*alpha;t=q*x
            ap=[u+alpha*v for u,v in zip(a,b)]; am=[u-alpha*v for u,v in zip(a,b)]
            rarity=scale(log_expr(Q(1)/x),t) if x else {}
            remainder=add(rarity,raw(a),scale(raw(b),x),scale(add(raw(ap),raw(am)),Q(-1,2)))
            check(dec(f,i)==add(scale(dec(h,i),q),remainder),'exact_coherent_identity')
            check(influence(f,i)==q*influence(h,i),'exact_influence_factorization')
            check(abs(alpha)<=influence(h,i),'singleton_derivative_bound')
            s=[u+x*v for u,v in zip(A,B)]
            allocation=add(raw(a),scale(raw(b),x),rarity,scale(mass_ent(s),-1))
            js=add(mass_ent(s),scale(add(raw(ap),raw(am)),Q(-1,2)))
            check(remainder==add(allocation,js),'exact_allocation_js_split')
            check(erasure(f,i)==add(scale(erasure(h,i),q),allocation),'exact_erasure_composition')
            check(add(dec(f,i),scale(erasure(f,i),-1))==add(scale(add(dec(h,i),scale(erasure(h,i),-1)),q),js),'exact_js_composition')
            concavity_gap=add(scale(outer_erasure,x),rarity,scale(allocation,-1))
            c_lo,c_hi=bounds(concavity_gap)
            check(c_lo>=0 or concavity_gap=={},'certified_allocation_bound')
            js_lo,js_hi=bounds(js)
            check(js_hi<=2*t or js=={},'certified_js_bound')
            margin=2*t+bounds(add(scale(outer_erasure,x),rarity,scale(remainder,-1)))[0]
            check(margin>=0,'certified_full_remainder_bound')
            if min_margin is None or margin<min_margin:min_margin=margin
            rlo,rhi=bounds(rarity)
            check(rhi<=q*influence(h,i),'certified_log_payment_coarse_constant_1_nat')

parity_rows=[]
for n in range(3,9):
    u=[(-1)**z.bit_count() for z in range(1<<(n-1))];u[0]*=-1
    h=tuple((1 if z&1==0 else -1)*u[z>>1] for z in range(1<<n))
    alpha=walsh(h)[1]
    check(abs(alpha)==Q(1,1<<(n-2)),'parity_alpha')
    check(influence(h,0)==1,'parity_influence')
    check(dec(h,0)=={},'parity_zero_decrement')
    x=alpha*alpha
    # S''=3+ln(1-alpha^2)>=0 for |alpha|<=1/2; exact lower bound R/(q*x)>=ln(1/x).
    lower=log_expr(Q(1)/x)
    check(lower=={2:Q(2*(n-2))},'exact_log_divergence_scale')
    parity_rows.append({'n':n,'alpha':str(alpha),'lower_R_over_q_alpha2_in_nats':f'{2*(n-2)} ln(2)'})

def tree_ledger(t,weight=Q(1)):
    if len(t)==1:return Q(0),{},Q(0)
    a=walsh(t)[1];d=influence(t,0);x=a*a
    log=scale(log_expr(Q(1)/x),weight*x) if x else {}
    l=tree_ledger(restrict(t,0,0),weight/2);r=tree_ledger(restrict(t,0,1),weight/2)
    return weight*d+l[0]+r[0],add(log,l[1],r[1]),weight*abs(a)+l[2]+r[2]
for mask in range(256):
    t=tuple(1 if mask>>z&1 else -1 for z in range(8))
    consumed,logcharge,l1=tree_ledger(t)
    check(consumed==total_inf(t),'exact_tree_influence_telescope')
    check(l1<=consumed,'exact_tree_singleton_budget')
    check(bounds(logcharge)[1]<=consumed or not logcharge,'certified_tree_log_budget_1_nat')

result={'status':'PASS','counts':COUNTS,'composition_splits':3360,'parity_controls':parity_rows,'physical_trees':256,'minimum_certified_remainder_margin':str(min_margin),'arithmetic':'integer Walsh, Fraction, exact prime-log identities and rational logarithm enclosures','log_interval_terms':48,'elapsed_seconds':time.monotonic()-START}
out=Path(__file__).resolve().parents[1]/'out'/'validation.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
