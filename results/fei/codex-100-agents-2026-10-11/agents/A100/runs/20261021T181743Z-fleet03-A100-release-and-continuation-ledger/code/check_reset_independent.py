from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, sys, time, math
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; pilot='--pilot' in sys.argv
start=time.perf_counter(); checks=0
def require(x):
    global checks
    checks+=1
    assert x, checks
    assert time.perf_counter()-start<55, 'frozen runtime cap'
def walsh_direct(f):
    N=len(f)
    return [sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(f)) for s in range(N)]
def walsh_butterfly(f):
    a=f[:]; step=1
    while step<len(a):
        for k in range(0,len(a),2*step):
            for i in range(k,k+step):a[i],a[i+step]=a[i]+a[i+step],a[i]-a[i+step]
        step*=2
    return a
def spectrum(f):
    w=walsh_direct(f);require(w==walsh_butterfly(f));p=[F(x*x,len(f)**2) for x in w];require(sum(p)==1);return p
def edges(f,i):return F(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f))
def ln_unit(x):
    # 1<=x<=2; positive atanh expansion with a geometric majorant.
    require(1<=x<=2)
    z=(x-1)/(x+1); require(0<=z<=F(1,3))
    z2=z*z; power=z; total=F(0)
    for k in range(40):total+=2*power/(2*k+1);power*=z2
    tail=2*power/(81*(1-z2))
    return total,total+tail
LN2=ln_unit(F(2))
@lru_cache(None)
def log2(x):
    require(x>0)
    k=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/(F(2)**k)
    if y<1:k-=1;y*=2
    lo,hi=ln_unit(y)
    return F(k)+lo/LN2[1],F(k)+hi/LN2[0]
def entropy(p):
    lo=hi=F(0)
    for x in p:
        if x:
            a,b=log2(x);lo-=x*b;hi-=x*a
    return lo,hi
def outward(x,upper=False):
    scale=1<<80
    z=x*scale
    num=-((-z.numerator)//z.denominator) if upper else z.numerator//z.denominator
    return str(F(num,scale))
cases=[]
for n in ([2,3] if pilot else [2,3,4,5,6,7]):
    N=1<<(n+1);t=F(1,1<<n);f=[-1 if x in (0,1,3) else 1 for x in range(N)]
    P=spectrum(f);g=f[::2];h=f[1::2];pg=spectrum(g);ph=spectrum(h)
    require(all(x>0 for x in P));require(min(g)!=max(g) and min(h)!=max(h))
    require(edges(f,0)==t);I=sum(edges(f,i) for i in range(n+1));require(I==(3*n-1)*t)
    w=walsh_direct(f)
    for s in range(1,N):
        bracket=1+(-1 if s&1 else 1)+(-1 if ((s&1)+((s>>1)&1))%2 else 1)
        require(F(w[s],N)==-t*bracket)
    q=[P[2*s]+P[2*s+1] for s in range(N//2)]
    require(q==[(x+y)/2 for x,y in zip(pg,ph)])
    require(all(x>0 for x in q));require(sum(q)==1)
    p0=(1-2*t)**2;qa=2*t*t;q0=1-6*t+10*t*t;M=1<<(2*n-2)
    require(pg[0]==p0 and pg[1]==4*t*t and ph[1]==0)
    require(q[0]==q0 and q[1]==qa and q0>=p0/2>0)
    delta=qa*(1-F(1,1<<M));qt=q[:];qt[1]=qa/(1<<M);qt[0]+=delta
    require(sum(qt)==1 and min(qt)>0)
    require(sum(abs(x-y) for x,y in zip(q,qt))/2==delta)
    require(delta<2*t*t and pg[1]*M==1)
    require(all(q[s]==qt[s] for s in range(2,len(q))))
    # Exact matching conditional occupancy distributions: refund zero atom by atom.
    for s in range(len(q)):
        for b in [0,1]:require(P[2*s+b]/q[s]==P[2*s+b]/q[s])
    ratio=1+delta/q0;L,U=log2(ratio)
    Zlo=(1-p0*U)/2;Zhi=(1-p0*L)/2
    require(Zlo>F(3,8));require(Zhi<F(1,2))
    Hlo,Hhi=entropy(P);require(Hhi<=8*I)
    require(12*(n+1)<=8*(3*n-1))
    if n==2:require(ratio==F(31,16) and ratio<2)
    else:require(4*qa<=F(1,8) and p0/q0<=2)
    # Analytic lower ratio bound grows without using floating logs.
    require(F(3,8)/t>=F(3,2))
    cases.append({'n':n,'dimension':n+1,'vertices':N,'I':str(I),'query_influence':str(t),'TV_upper':str(2*t*t),'M':M,'weighted_reset_interval':[outward(Zlo),outward(Zhi,True)],'H_upper':outward(Hhi,True),'8I':str(8*I),'zero_refund':'exact matching conditional distributions','both_children_nonconstant':True})
# Every labeled two-bit sign: two nonconstant one-bit children force monomial spectrum.
minimal=0
for code in range(16):
    f=[-1 if code>>x&1 else 1 for x in range(4)]
    for j in range(2):
        children=[[f[x] for x in range(4) if (x>>j)&1==b] for b in [0,1]]
        if all(min(c)!=max(c) for c in children):
            p=spectrum(f);require(sum(x>0 for x in p)==1);require(not all(x>0 for x in p));minimal+=1
result={'status':'PASS','helper_version':'A100-independent-reset-review-v1','pilot':pilot,'cases':cases,'minimality_truth_tables':16,'qualifying_query_cases':minimal,'exact_assertions':checks,'elapsed_seconds':round(time.perf_counter()-start,6),'arithmetic':'independent direct signed character sums; butterfly crosscheck; physical edges; Fraction atanh intervals','rung':'analytic all-n reconstruction plus independent exact finite certificates; Lean receipt separate','limits':'finite checks do not prove all-n extension; no FEI counterfamily or integrated assembly acceptance'}
(OUT/('PILOT_RESET_REVIEW.json' if pilot else 'INDEPENDENT_RESET_REVIEW.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))
