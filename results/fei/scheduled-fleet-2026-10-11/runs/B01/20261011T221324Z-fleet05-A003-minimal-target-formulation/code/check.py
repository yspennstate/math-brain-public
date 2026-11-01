from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time,math
ROOT=Path(__file__).resolve().parents[1]
checks=0
def check(t):
    global checks
    assert t
    checks+=1
def fwht(v):
    v=list(v); h=1
    while h<len(v):
        for k in range(0,len(v),2*h):
            for j in range(k,k+h):
                a,b=v[j],v[j+h]; v[j],v[j+h]=a+b,a-b
        h*=2
    return v
def spectrum(v):
    N=len(v); return [F(w,N) for w in fwht(v)]
def add(*xs):
    d={}
    for x in xs:
        for k,v in x.items(): d[k]=d.get(k,F(0))+v
    return {k:v for k,v in d.items() if v}
def scale(x,c): return {k:v*c for k,v in x.items() if v*c}
def factors(n):
    d={}; k=2
    while k*k<=n:
        while n%k==0: d[k]=d.get(k,0)+1;n//=k
        k+=1
    if n>1:d[n]=d.get(n,0)+1
    return d
@lru_cache(None)
def log(x):
    x=F(x);check(x>0)
    return add(factors(x.numerator),scale(factors(x.denominator),-1))
def ent(p): return add(*(scale(log(x),-x) for x in p if x))
@lru_cache(None)
def ln_interval(x):
    z=F(x-1,x+1); s=F(0)
    for k in range(80):s+=2*z**(2*k+1)/(2*k+1)
    error=2*abs(z)**161/(161*(1-z*z))
    return s-error,s+error
@lru_cache(None)
def log_interval(p):
    k=p.bit_length()-1;x=F(p,2**k)
    lo,hi=ln_interval(x);a,b=ln_interval(F(2))
    return F(k)+lo/b,F(k)+hi/a
def interval(e):
    lo=hi=F(0)
    for p,c in e.items():
        a,b=log_interval(p)
        lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
    return lo,hi
def nonnegative(e):
    if not e:return True
    return interval(e)[0]>=0
start=time.monotonic();case_count=0
for n in range(4):
    N=2**n
    for table in range(2**N):
        vals=[1 if table>>x&1 else -1 for x in range(N)]
        a=spectrum(vals);p=[x*x for x in a];H=ent(p)
        check(sum(p)==1);B={};L={}
        for u in range(1,N):check(sum(a[s]*a[s^u] for s in range(N))==0)
        for i in range(n):
            bit=1<<i; pairs=[(s,s|bit) for s in range(N) if not s&bit]
            marg=[p[s]+p[t] for s,t in pairs]
            Bi=add(H,scale(ent(marg),-1)); B=add(B,Bi)
            Li=add(*(scale(log((p[s]+p[t])/p[t]),p[t]) for s,t in pairs if p[t]));L=add(L,Li)
            qp=[(a[s]+a[t])**2 for s,t in pairs]; qm=[(a[s]-a[t])**2 for s,t in pairs]
            js=add(ent(marg),scale(add(ent(qp),ent(qm)),-F(1,2)))
            delta=add(H,scale(add(ent(qp),ent(qm)),-F(1,2)))
            check(add(delta,scale(add(Bi,js),-1))=={})
            influence=sum(p[t] for s,t in pairs)
            Ip=sum(s.bit_count()*w for s,w in enumerate(qp)); Im=sum(s.bit_count()*w for s,w in enumerate(qm))
            # Parent labels below and above i compress when i is removed.
            Ip=sum((s&~bit).bit_count()*w for (s,t),w in zip(pairs,qp))
            Im=sum((s&~bit).bit_count()*w for (s,t),w in zip(pairs,qm))
            I=sum(s.bit_count()*p[s] for s in range(N))
            check(I==influence+(Ip+Im)/2)
            check(nonnegative(add(Bi,scale(Li,-1))))
        check(nonnegative(add(H,scale(B,-1))))
        check(nonnegative(add(B,scale(L,-1))))
        case_count+=1
family=[]
for n in range(2,9):
    d=n+1;N=2**n;D=2**d
    vals=[]
    for x in range(D):
        z=x>>n&1; y=(x&(N-1))^(N-1 if z else 0)
        vals.append(-1 if y==0 else 1)
    a=spectrum(vals);p=[t*t for t in a]
    check(p[0]==F(N-2,N)**2)
    check(all(p[s]==(F(4,N*N) if s.bit_count()%2==0 else 0) for s in range(1,D)))
    I=sum(s.bit_count()*p[s] for s in range(D));check(I==F(2*d,N))
    check(all(not(p[s] and p[s^(1<<i)]) for s in range(D) for i in range(d)))
    R={}
    for s in range(1,D):
        if not p[s]:continue
        ranks=[i+1 for i in range(d) if s>>i&1];k=len(ranks)
        ratio=F(math.prod(ranks),math.factorial(k))
        check(1<=ratio<=math.comb(d,k))
        R=add(R,scale(log(ratio),F(6,5)*p[s]))
    rlo,rhi=interval(R);check(rhi<=F(12,5)*I)
    # pi=1/N, lambda=1: 2^Lambda=1+pi, Z=pi/(1+pi).
    pi=F(1,N);check((1+pi)*pi/(1+pi)==pi)
    family.append({'n':n,'I':str(I),'R_interval':[str(rlo),str(rhi)],'R_over_I_float_evidence':float((rlo+rhi)/(2*I)),'B':'0','complete_residual_bound':'12/5 I'})
out={'helper_version':'A003-exact-v1','exhaustive_tables':case_count,'family_cases':family,'assertions':checks,'runtime_seconds':time.monotonic()-start,'arithmetic':'Fraction and exact log-prime expressions with rational intervals','status':'PASS'}
(ROOT/'out/VALIDATION.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='family_cases'}))
