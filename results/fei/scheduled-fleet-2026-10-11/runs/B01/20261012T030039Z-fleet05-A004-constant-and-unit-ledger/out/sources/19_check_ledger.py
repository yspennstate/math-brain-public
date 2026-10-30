"""Frozen v1: integer Walsh/Fraction/log-linear exact normalization audit."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, time, hashlib, math
ROOT=Path(__file__).resolve().parents[1]
checks=0
CONSTANTS={}
def ck(x):
    global checks
    assert x
    checks+=1
def walsh(t):
    a=list(t); step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for k in range(j,j+step):
                u,v=a[k],a[k+step]; a[k],a[k+step]=u+v,u-v
        step*=2
    return [F(x,len(a)) for x in a]
def factors(n):
    d=2; z={}
    while d*d<=n:
        while n%d==0: z[d]=z.get(d,0)+1; n//=d
        d+=1
    if n>1: z[n]=z.get(n,0)+1
    return z
def add(*terms):
    z={}
    for t in terms:
        for p,c in t.items(): z[p]=z.get(p,F(0))+c
    return {p:c for p,c in z.items() if c}
def mul(c,t): return {p:c*v for p,v in t.items() if c*v}
def log(q):
    q=F(q); assert q>0
    return add({p:F(e) for p,e in factors(q.numerator).items()},
               {p:F(-e) for p,e in factors(q.denominator).items()})
def entropy(q): return add(*(mul(-p,log(p)) for p in q if p))
def h2(q): return entropy([q,1-q])
@lru_cache(None)
def ln_interval(q):
    q=F(q); assert q>0
    k=0
    while q>=2: q/=2; k+=1
    while q<1: q*=2; k-=1
    def unit(r):
        z=(r-1)/(r+1); m=32
        low=2*sum((z**(2*j+1)/F(2*j+1) for j in range(m)),F(0))
        err=2*z**(2*m+1)/F(2*m+1)/(1-z*z)
        return low,low+err
    lo,hi=unit(q); a,b=unit(F(2))
    return (lo+k*a,hi+k*b) if k>=0 else (lo+k*b,hi+k*a)
def log_interval(q):
    a,b=ln_interval(F(q)); c,d=ln_interval(F(2))
    corners=[a/c,a/d,b/c,b/d]
    return min(corners),max(corners)
def bounds(t):
    lo=hi=F(0)
    for p,c in t.items():
        a,b=log_interval(F(p)); lo+=c*(a if c>0 else b); hi+=c*(b if c>0 else a)
    return lo,hi
def upper(t,r):
    ck(not t or bounds(t)[1]<=r)
def direct_spectrum(t):
    return [F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)),len(t)) for s in range(len(t))]
def audit(t,n,label):
    a=walsh(t); p=[x*x for x in a]; ck(a==direct_spectrum(t)); ck(sum(p)==1)
    infl=[sum((p[s] for s in range(len(t)) if s>>i&1),F(0)) for i in range(n)]
    edge=[F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(n)]
    ck(infl==edge)
    it=sum(infl,F(0)); v=1-p[0]; D=sum((min(q,1-q) for q in infl),F(0))
    ck(it>=v); ck(D<=4*(it-v))
    U=sum(1<<i for i in range(n) if infl[i]>F(1,2))
    shifted=walsh([t[x]*(-1 if (x&U).bit_count()%2 else 1) for x in range(len(t))])
    ck(all(shifted[s]==a[s^U] for s in range(len(t))))
    ck(sum((s.bit_count()*shifted[s]**2 for s in range(len(t))),F(0))==D)
    H=entropy(p); Hp=entropy(p[1:]); E0=entropy(p[:1])
    ck(H==add(Hp,E0)); upper(E0,2*it)
    upper(E0,v/ln_interval(F(2))[1])
    upper(E0,F(2553,1000)*(it-v))
    levels=[sum((p[s] for s in range(len(t)) if s.bit_count()==k),F(0)) for k in range(n+1)]
    upper(entropy(levels),F(CONSTANTS['Clev_bits']['lower'])*it)
    upper(H,F(CONSTANTS['Creg_bits']['lower'])*D)
    upper(Hp,F(CONSTANTS['CT_bits']['lower'])*(it-v))
    upper(h2(v),2*it)
    g=[F(x+1,2) for x in t]; b=walsh(g); q=[x*x for x in b]; r=sum(g,F(0))/len(g)
    ck(sum(q)==r); ck(b[0]==r); ck(all(a[s]==2*b[s] for s in range(1,len(t))))
    Ig=sum((s.bit_count()*q[s] for s in range(len(t))),F(0)); ck(Ig==it/4)
    ck(Hp==add(mul(4,entropy(q[1:])),{2:-2*v} if v else {}))
    if v:
        R=[x/v for x in p[1:]]; ck(H==add(h2(v),mul(v,entropy(R))))
        ck(Hp==add(mul(v,entropy(R)),mul(-v,log(v))))
    else: ck(not H)
    if r:
        Hg=entropy([x/r for x in q]); ck(Hg==add(mul(1/r,entropy(q)),log(r)))
        ck(H==add(h2(v),mul(4*r,add(Hg,mul(-1,h2(r))))))
    for i in range(n):
        plus=[t[x] for x in range(len(t)) if x>>i&1]; minus=[t[x] for x in range(len(t)) if not x>>i&1]
        ap=walsh(plus); am=walsh(minus); pp=[x*x for x in ap]; pm=[x*x for x in am]
        masses=[p[s]+p[s|(1<<i)] for s in range(len(t)) if not s>>i&1]
        Bi=add(H,mul(-1,entropy(masses)))
        JS=add(entropy(masses),mul(-F(1,2),add(entropy(pp),entropy(pm))))
        delta=add(H,mul(-F(1,2),add(entropy(pp),entropy(pm))))
        ck(delta==add(Bi,JS))
        if JS: ck(bounds(JS)[0]>=0)
        c=2/ln_interval(F(2))[1]
        upper(JS,c*min(infl[i],1-infl[i]))
        childI=sum((s.bit_count()*(pp[s]+pm[s])/2 for s in range(len(pp))),F(0))
        ck(it==childI+infl[i])
        oriented=F(sum(t[x]==-1 and t[x^(1<<i)]==1 for x in range(len(t))),len(t))
        ck(oriented==infl[i]/2)
    return {'label':label,'n':n,'I':str(it),'variance':str(v),'D':str(D),'H_log2_prime_coefficients':{str(k):str(c) for k,c in H.items()}}
def arctan_interval(q,m=48):
    z=F(1,q); s=sum(((-1)**j*z**(2*j+1)/F(2*j+1) for j in range(m)),F(0))
    other=s+(-1)**m*z**(2*m+1)/F(2*m+1)
    return min(s,other),max(s,other)
def constants():
    e=sum((F(1,math.factorial(j)) for j in range(48)),F(0)); eu=e+F(49,48*math.factorial(48))
    a,b=arctan_interval(5); c,d=arctan_interval(239); piL,piU=16*a-4*d,16*b-4*c
    cl=(log_interval(4+e)[0],log_interval(4+eu)[1])
    cr=(cl[0]+2*log_interval(e*piL)[0],cl[1]+2*log_interval(eu*piU)[1])
    l2,u2=ln_interval(F(2)); ct=(F(460)/u2+80,F(460)/l2+80)
    kr=(3+2*log_interval(F(3))[0]+log_interval(6*e)[0],3+2*log_interval(F(3))[1]+log_interval(6*eu)[1])
    ck(cr[1]<F(8937,1000)); ck(ct[1]<744)
    ck(F(2)/(1-u2)<F(2553,1000)**2)
    def serialize(x):
        scale=1<<100
        low=F((x[0]*scale).__floor__(),scale)
        high=F((x[1]*scale).__ceil__(),scale)
        ck(low<=x[0] and x[1]<=high)
        return {'lower':str(low),'upper':str(high),'display_only':float((low+high)/2)}
    return {name:serialize(x) for name,x in [('Clev_bits',cl),('Creg_bits',cr),('CT_bits',ct),('Kref_bits',kr),('erasure_additive_bits',(2/u2,2/l2))]}
def main():
    global CONSTANTS
    start=time.perf_counter(); records=[]; counts={}
    CONSTANTS=constants()
    for n in range(4):
        N=1<<n; counts[str(n)]=1<<N
        for mask in range(1<<N): audit([1 if mask>>x&1 else -1 for x in range(N)],n,'exhaustive')
    for n in range(1,9):
        N=1<<n
        families={'constant':[1]*N,'dictator':[1 if x&1 else -1 for x in range(N)],'parity':[(-1)**x.bit_count() for x in range(N)],'point_defect':[-1]+[1]*(N-1)}
        for name,t in families.items():
            records.append(audit(t,n,name))
            if name=='point_defect':
                a=walsh(t); rare=F(1,N); ck(a[0]==1-2*rare); ck(all(abs(c)==2*rare for c in a[1:])); ck(F(records[-1]['I'])==2*n*rare)
    out={'helper_version':'A004-ledger-check-v1','exhaustive_counts':counts,'exhaustive_total':sum(counts.values()),'endpoint_cases':len(records),'assertions':checks,'status':'PASS','runtime_seconds':time.perf_counter()-start,'constants':CONSTANTS,'endpoints':records,'arithmetic':'integer Walsh; Fraction; exact log-linear identities; rational atanh/Taylor/Machin interval certificates'}
    out['assertions']=checks
    (ROOT/'out'/'validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ['status','exhaustive_total','endpoint_cases','assertions','runtime_seconds']}))
if __name__=='__main__': main()
