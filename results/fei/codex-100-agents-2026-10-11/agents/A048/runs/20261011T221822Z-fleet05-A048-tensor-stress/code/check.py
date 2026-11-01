"""A048 tensor-scope verifier v1; exact rational laws and prime-log identities."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json, time, hashlib
ROOT=Path(__file__).resolve().parents[1]
checks=0
def eq(a,b):
    global checks
    assert a==b,(a,b)
    checks+=1
def add(*vs):
    out={}
    for v in vs:
        for k,a in v.items(): out[k]=out.get(k,F(0))+a
    return {k:a for k,a in out.items() if a}
def scale(v,a): return {k:a*b for k,b in v.items() if a*b}
@lru_cache(None)
def factors(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1; n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out
def logvec(x):
    assert x>0
    return add(factors(x.numerator),scale(factors(x.denominator),-1))
@lru_cache(None)
def entatom(x): return scale(logvec(x),-x) if x else {}
def entropy(xs): return add(*(entatom(F(x)) for x in xs))
def hb(x): return entropy([x,1-x])
def walsh(tab):
    a=list(tab); step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for k in range(j,j+step):
                u,v=a[k],a[k+step]; a[k],a[k+step]=u+v,u-v
        step*=2
    return [F(x,len(a)) for x in a]
def law(tab): return [a*a for a in walsh(tab)]
def influence(tab):
    n=(len(tab)-1).bit_length()
    return sum((F(sum(tab[x]!=tab[x^(1<<j)] for x in range(len(tab))),len(tab)) for j in range(n)),F(0))
def spectral_i(w): return sum((s.bit_count()*p for s,p in enumerate(w)),F(0))
def marginal(w,A):
    out={}
    for s,p in enumerate(w): out[s&~A]=out.get(s&~A,F(0))+p
    return out
def ledger_uniform(tab,A):
    n=(len(tab)-1).bit_length(); ai=[j for j in range(n) if A>>j&1]; bi=[j for j in range(n) if not A>>j&1]
    child=[]
    for z in range(1<<len(ai)):
        t=[]
        for y in range(1<<len(bi)):
            x=sum(((z>>j)&1)<<i for j,i in enumerate(ai))+sum(((y>>j)&1)<<i for j,i in enumerate(bi))
            t.append(tab[x])
        child.append(entropy(law(t)))
    w=law(tab); h=entropy(w); hm=entropy(marginal(w,A).values()); avg=scale(add(*child),F(1,len(child)))
    return add(h,scale(hm,-1)),add(hm,scale(avg,-1)),h,avg
def bias_law(tab,ps):
    n=len(ps); out=[]
    for s in range(1<<n):
        raw=F(0); norm=F(1)
        for j,p in enumerate(ps):
            if s>>j&1: norm*=p*(1-p)
        for x,f in enumerate(tab):
            v=F(f)
            for j,p in enumerate(ps):
                bit=(x>>j)&1; v*=p if bit else 1-p
                if s>>j&1: v*=bit-p
            raw+=v
        out.append(raw*raw/norm)
    eq(sum(out),1)
    return out
def activation(tab,k):
    # Controls occupy the low k bits; active only at their zero point.
    return [tab[x>>k] if x&((1<<k)-1)==0 else 1 for x in range(len(tab)*(1<<k))]
def product(a,b): return [a[x%len(a)]*b[x//len(a)] for x in range(len(a)*len(b))]
def tensor(a,t):
    out=[1]
    for _ in range(t): out=product(out,a)
    return out
def formula_single(m,p):
    v=1-m*m; q0=1-p*v; a0=(1-p+p*m)**2; b0=p*(1-p)*(1-m)**2
    M=add(entropy([a0,b0]),scale(entatom(q0),-1),scale(hb(p),p*v))
    J=add(hb(p*v),scale(hb(v),-p))
    return M,J
def formula_controls(m,k):
    p=F(1,1<<k); v=1-m*m; q0=1-p*v; r=(p-p*p)*(1-m)**2
    M=scale(hb(r/q0),q0) if q0 else {}
    if r: M=add(M,scale(logvec(F((1<<k)-1)),r))
    M=add(M,{2:p*v*k})
    J=add(hb(p*v),scale(hb(v),-p))
    return M,J
def serial(v): return {str(k):str(a) for k,a in sorted(v.items())}
def ln_interval(x,N=24):
    z=(x-1)/(x+1); total=F(0)
    for j in range(N): total+=2*z**(2*j+1)/F(2*j+1)
    return total,total+2*z**(2*N+1)/F((2*N+1)*(1-z*z))
def log_interval(x):
    k=0
    while x<1: x*=2; k-=1
    while x>=2: x/=2; k+=1
    lo,hi=ln_interval(x); l2,h2=ln_interval(F(2))
    return k+lo/h2,k+hi/l2
def interval(v):
    lo=hi=F(0)
    for prime,a in v.items():
        l,h=log_interval(F(prime)); lo+=a*(l if a>=0 else h); hi+=a*(h if a>=0 else l)
    return lo,hi
def main():
    start=time.perf_counter(); counts={}; certs=[]
    controls=biased=padding=0
    for n in range(4):
        for mask in range(1<<(1<<n)):
            tab=[-1 if mask>>x&1 else 1 for x in range(1<<n)]
            G=walsh(tab); m=G[0]; w=[a*a for a in G]
            eq(sum(w),1); eq(spectral_i(w),influence(tab))
            for k in (1,2,3):
                p=F(1,1<<k); full=activation(tab,k); fw=walsh(full)
                for s,a in enumerate(fw):
                    u=s&((1<<k)-1); t=s>>k
                    expected=(1-p+p*m) if s==0 else p*(m-1) if t==0 else p*G[t]
                    eq(a,expected)
                M,J,H,avg=ledger_uniform(full,(1<<k)-1)
                MF,JF=formula_controls(m,k); eq(M,MF); eq(J,JF)
                d=1-m; v=1-m*m
                LF=add(entatom((1-p*d)**2),{2:2*k*p*v},scale(entatom(m*m),-p))
                if d: LF=add(LF,scale(add({2:F(2*k)},scale(logvec(d*d),-1)),(p-p*p)*d*d))
                eq(add(M,J),LF)
                eq(avg,scale(entropy(w),p)); eq(influence(full),p*(influence(tab)+k*(1-m)))
                eq(spectral_i(law(full)),influence(full)); controls+=1
            zero_active=activation(tab,1)
            full=[zero_active[x^1] for x in range(len(zero_active))]
            for p in (F(1,8),F(1,2),F(7,8)):
                pw=bias_law(full,[p]+[F(1,2)]*n); hm=entropy(marginal(pw,1).values())
                M=add(entropy(pw),scale(hm,-1)); J=add(hm,scale(entropy(w),-p))
                MF,JF=formula_single(m,p); eq(M,MF); eq(J,JF); biased+=1
            base=[1,1,1,-1]; joint=product(base,tab)
            M,J,H,avg=ledger_uniform(joint,1); bM,bJ,bH,bavg=ledger_uniform(base,1)
            eq(M,bM); eq(J,bJ); eq(H,add(bH,entropy(w))); eq(avg,add(bavg,entropy(w)))
            eq(influence(joint),influence(base)+influence(tab)); padding+=1
    counts.update(uniform_control_cases=controls,biased_selector_cases=biased,common_factor_cases=padding)
    # Moving unbalanced tensor family: AND sign has mean 1/2.
    seed=[1,1,1,-1]; moving=0
    for t in (1,2,3):
        core=tensor(seed,t); eq(F(sum(core),len(core)),F(1,2)**t)
        for p in (F(1,8),F(1,2),F(7,8)):
            zero_active=activation(core,1); full=[zero_active[x^1] for x in range(len(zero_active))]
            w=bias_law(full,[p]+[F(1,2)]*(2*t)); hm=entropy(marginal(w,1).values())
            MF,JF=formula_single(F(1,2)**t,p)
            eq(add(entropy(w),scale(hm,-1)),MF); eq(add(hm,scale(entropy(law(core)),-p)),JF); moving+=1
    counts['moving_tensor_selector_cases']=moving
    # Aligned biased products are tested by full actual truth tables.
    ps=[F(1,8),F(1,4)]; w0=bias_law(seed,ps); h0=entropy(w0); hm0=entropy(marginal(w0,1).values())
    child0=scale(hb(F(3,4)),F(1,8)); M0=add(h0,scale(hm0,-1)); J0=add(hm0,scale(child0,-1))
    for t in (1,2,3):
        w=bias_law(tensor(seed,t),ps*t); A=sum(1<<(2*j) for j in range(t)); hm=entropy(marginal(w,A).values())
        eq(entropy(w),scale(h0,t)); eq(hm,scale(hm0,t)); eq(add(entropy(w),scale(hm,-1)),scale(M0,t))
        eq(add(hm,scale(child0,-t)),scale(J0,t))
    counts['aligned_biased_tensor_cases']=3
    debt=add(J0,scale(M0,-1)); lo,hi=interval(debt); assert lo>F(1195,10000); eq(lo>0,True)
    certs.append({'name':'existing_AND_debt','lower':str(lo),'upper':str(hi),'strict_lower':'1195/10000'})
    delta=add(hb(F(1,8)),logvec(F(7,8))); eq(delta,scale(logvec(F(7)),F(1,8)))
    l,h=interval(delta); eq(l>0,True)
    certs.append({'name':'irrelevant_revealed_tax','M':{},'J':{},'I_A':'0','delta_lower':str(l),'delta_upper':str(h)})
    # Collision identity on fixed rational nonnegative arrays; no new raw-L discovery.
    v=[F(1),F(1,4),F(1,16)]; Z=sum(v); L=entropy(v)
    for t in (1,2,3,4):
        vt=[F(1)]
        for _ in range(t): vt=[a*b for a in vt for b in v]
        eq(sum(vt),Z**t); eq(entropy(vt),scale(L,t*Z**(t-1)))
        eq(scale(entropy(vt),1/(Z**t)),scale(L,F(t)/Z))
        eq(entropy([a/(Z**t) for a in vt]),add(scale(L,F(t)/Z),scale(logvec(Z),t)))
    counts['collision_normalization_cases']=4
    out={'status':'PASS','helper_version':'A048-tensor-scope-v1','counts':counts,'assertions':checks,'arithmetic':'Fraction; exact equality of rational prime-log vectors; rational atanh sign enclosures','runtime_seconds':time.perf_counter()-start,'certificates':certs}
    (ROOT/'out'/'CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:out[k] for k in ('status','counts','assertions','runtime_seconds')}))
if __name__=='__main__': main()
