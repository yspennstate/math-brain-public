from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,sys,time

RUN=Path(__file__).resolve().parents[1]
START=time.monotonic();ASSERTIONS=0
def check(x):
    global ASSERTIONS
    ASSERTIONS+=1
    if not x:raise AssertionError(ASSERTIONS)

@lru_cache(None)
def ln(x):
    if x==1:return F(0),F(0)
    if x<1:
        a,b=ln(1/x);return -b,-a
    shifts=0
    while x>2:x/=2;shifts+=1
    y=(x-1)/(x+1)
    v=sum((2*y**(2*j+1)/F(2*j+1) for j in range(24)),F(0))
    err=2*y**49/(49*(1-y*y))
    if shifts:
        a,b=ln(F(2));return v+shifts*a,v+err+shifts*b
    return v,v+err
LN2=ln(F(2))
@lru_cache(None)
def log(x):
    if x==1:return F(0),F(0)
    if x<1:
        a,b=log(1/x);return -b,-a
    a,b=ln(x);return a/LN2[1],b/LN2[0]
def cost(p,q):
    lo=hi=F(0)
    for w,r in zip(p,q):
        if w:
            a,b=log(r);lo-=w*b;hi-=w*a
    return lo,hi
def histentropy(hist):
    lo=hi=F(0)
    for p,count in hist:
        if p:
            a,b=log(p);lo-=count*p*b;hi-=count*p*a
    return lo,hi
def fwht(truth):
    v=truth[:];step=1
    while step<len(v):
        for a in range(0,len(v),2*step):
            for j in range(a,a+step):
                x,y=v[j],v[j+step];v[j]=x+y;v[j+step]=x-y
        step*=2
    return [F(x,len(v)) for x in v]
def influence(v):
    n=(len(v)-1).bit_length()
    return F(sum(v[j]!=v[j^(1<<i)] for i in range(n) for j in range(len(v))),len(v))

@lru_cache(None)
def factors(n):
    result={};p=2
    while p*p<=n:
        while n%p==0:result[p]=result.get(p,0)+1;n//=p
        p+=1
    if n>1:result[n]=result.get(n,0)+1
    return result
def addlog(vec,x,mult):
    for p,z in factors(x.numerator).items():vec[p]=vec.get(p,F(0))+z*mult
    for p,z in factors(x.denominator).items():vec[p]=vec.get(p,F(0))-z*mult
def clean(vec):return {p:v for p,v in vec.items() if v}
def cevec(p,q):
    d={}
    for w,r in zip(p,q):
        if w:addlog(d,r,-w)
    return clean(d)
def ratios(p,q):
    d={}
    for w,r in zip(p,q):
        if w:
            a=w/r;d[a]=d.get(a,F(0))+w
    return d

CORE_CASES=REF_CASES=THRESHOLD_CASES=0
ENTROPY_CHANGED=DESTROYED_EDGE_CASES=0
def corecase(g,k,m,a):
    global CORE_CASES,REF_CASES,THRESHOLD_CASES,ENTROPY_CHANGED,DESTROYED_EDGE_CASES
    CORE_CASES+=1;n=k+m;N=1<<n;delta=F(1,N)
    base=g*(1<<m);h=base[:];h[a]*=-1
    v=base+h;av=fwht(g);pv=[x*x for x in fwht(v)]
    pg=[x*x for x in av];support=[j for j,p in enumerate(pg) if p]
    s=len(support);w=2*delta-s*delta*delta
    ig=influence(g);j=sum(g[a]!=g[a^(1<<i)] for i in range(k))
    im=influence(v)
    check(influence(h)==ig+2*delta*(n-2*j))
    check(im==ig+delta*(n+1-2*j))
    check(sum(pv)==1 and all(pv))
    check(sum(pv[T] for T in support)==1-w)
    check(all(pv[T]==delta*delta for T in range(2*N) if T not in support))
    for T in support:
        phase=g[a]*((-1)**((T&a).bit_count()))
        check(pv[T]==(av[T]-delta*phase)**2)
        check(abs(av[T])>=F(1,1<<(k-1)))
    if j:DESTROYED_EDGE_CASES+=1
    eh=cost([x*x for x in fwht(h)],[x*x for x in fwht(h)])
    eg=cost(pg,pg)
    if eh[1]<eg[0] or eh[0]>eg[1]:ENTROPY_CHANGED+=1
    for variant in (0,1):
        REF_CASES+=1
        raw=[F(1 if variant==0 else T+1) for T in range(1<<k)]
        total=sum(raw);raw=[r/total for r in raw]
        rs_mass=sum(raw[T] for T in support)
        rs={T:raw[T]/rs_mass for T in support}
        qm=[(1-w)*rs[T] if T in rs else delta*delta for T in range(2*N)]
        check(sum(qm)==1 and all(qm))
        cg=cost(pg,raw);cs=cost([pg[T] for T in support],[rs[T] for T in support]);cm=cost(pv,qm)
        calvec=cevec(pg,raw);addlog(calvec,rs_mass,F(1))
        check(clean(calvec)==cevec([pg[T] for T in support],[rs[T] for T in support]))
        expression=cevec([pv[T] for T in support],[rs[T] for T in support])
        addlog(expression,1-w,-(1-w));addlog(expression,F(2),2*n*w)
        check(clean(expression)==cevec(pv,qm))
        debt=ratios(pv,qm)
        expected=ratios([pv[T] for T in support],[qm[T] for T in support])
        expected[F(1)]=expected.get(F(1),F(0))+w
        check(debt==expected)
        factor=1+(1<<k)*delta+F(1<<(2*k-2))*delta*delta
        check(all(pv[T]<=factor*pg[T] for T in support))
        check(cm[1]<=cs[0]+delta*(F(5,4)*(1<<k)*cs[0]+4*n+3))
        K=F(6);K0=F(4)
        if ig and cg[1]<=K0*ig:
            threshold=F(1,1<<m)*(F(5,4)*K0+k*K+(3-K)/2)
            if threshold<=K-K0:
                THRESHOLD_CASES+=1;check(cm[1]<=K*im)
        banklower=K*ig-cg[1]-delta*(F(5,4)*(1<<k)*cg[1]+(4-K)*n+K*(2*j-1)+3)
        if banklower>=0:check(cm[1]<=K*im)

def bent(k):return [(-1)**sum(((j>>(2*i))&1)*((j>>(2*i+1))&1) for i in range(k//2)) for j in range(1<<k)]
def compressed(k,m):
    n=k+m;delta=F(1,1<<n);e=F(1,1<<(k//2));N=1<<n;A=1<<k
    plus=(A+(1<<(k//2)))//2;minus=A-plus
    pm=[((e-delta)**2,plus),((-e-delta)**2,minus),(delta*delta,2*N-A)]
    ph=[((e-2*delta)**2,plus),((-e-2*delta)**2,minus),(4*delta*delta,N-A)]
    check(sum(p*c for p,c in pm)==sum(p*c for p,c in ph)==1)
    return histentropy(pm),histentropy(ph),pm,ph

H4=compressed(4,0)[0];CPT=(H4[0]*F(16,29),H4[1]*F(16,29))
check(F(2297,1000)<CPT[0] and CPT[1]<F(2299,1000))
check(F(34,15)<CPT[0]<CPT[1]<F(37,16))
DIRECT=COMPRESSED=0
def audit_direct(k,m):
    global DIRECT
    g=bent(k);n=k+m;base=g*(1<<m);model=compressed(k,m)
    modelpm=sorted(p for p,c in model[2] for _ in range(c))
    modelph=sorted(p for p,c in model[3] for _ in range(c))
    for a in range(1<<n):
        h=base[:];h[a]*=-1;root=base+h
        degree=(a&((1<<k)-1)).bit_count();delta=F(1,1<<n)
        check(influence(base)==F(k,2))
        check(influence(h)==F(k,2)+2*delta*(n-2*degree))
        check(influence(root)==F(k,2)+delta*(n+1-2*degree))
        check(sorted(x*x for x in fwht(root))==modelpm)
        check(sorted(x*x for x in fwht(h))==modelph)
        DIRECT+=1
def audit_compressed(k,m):
    global COMPRESSED
    n=k+m;delta=F(1,1<<n);hm,hh,_,_=compressed(k,m)
    i0=F(k,2)+(n+1)*delta
    check(hm[1]<F(17,8)*i0)
    bankmargin=F(17,8)*i0-hm[1];check(bankmargin>F(1,64))
    for weight in range(k+1):
        COMPRESSED+=1;i=F(k,2)+(n+1-2*weight)*delta
        if k==4 and m==0 and weight==4:
            check(i==F(29,16));check(hm==H4)
            check(hm[0]>F(17,8)*i)
        else:check(hm[1]<CPT[0]*i)
        if n>=6:check(hm[1]<F(34,15)*i)

mode=sys.argv[1] if len(sys.argv)>1 else 'pilot';limit=32 if mode=='pilot' else 6360
for k in (1,2,3):
    for mask in range(1<<(1<<k)):
        g=[1 if mask>>j&1 else -1 for j in range(1<<k)]
        for a in range(1<<k):
            for m in (0,2,4):
                if CORE_CASES==limit:break
                corecase(g,k,m,a)
            if CORE_CASES==limit:break
        if CORE_CASES==limit:break
    if CORE_CASES==limit:break
audit_direct(4,0)
if mode!='pilot':
    audit_direct(4,1);audit_direct(6,0)
    for k in range(4,21,2):
        for m in range(9):audit_compressed(k,m)
    # Inherited-reference failure is certified with exact rationals, not an entropy guess.
    b=8;eps=F(1,1<<b);r=[eps,1-eps]
    g=[1,-1];h=[-1,-1];pg=[x*x for x in fwht(g)];ph=[x*x for x in fwht(h)]
    check(pg==[0,1] and ph==[1,0]);check(1-eps>=F(1,2))
    c=cost(pg,r);ch=cost(ph,r)
    check(c[1]<=1 and ch[0]<=8<=ch[1])
    inherited=[r[T]/2 for T in range(2)]*2
    rootp=[x*x for x in fwht(g+h)]
    check(rootp==[F(1,4)]*4);check(cost(rootp,inherited)[0]>5)
    check(influence(g+h)==1)
elapsed=time.monotonic()-START
check(elapsed<(60 if mode=='pilot' else 240))
result={'status':'PASS','helper_version':'A095-support-completion-and-vertex-audit-v1.1','mode':mode,'exact_assertions':ASSERTIONS,'core_edit_pairs':CORE_CASES,'reference_cases':REF_CASES,'certified_threshold_cases':THRESHOLD_CASES,'entropy_changed_cases':ENTROPY_CHANGED,'destroyed_edge_cases':DESTROYED_EDGE_CASES,'a094_direct_vertices':DIRECT,'a094_compressed_cases':COMPRESSED,'sharp_C_pt_interval':[str(x) for x in CPT],'elapsed_seconds':elapsed,'log_arithmetic':'24-term rational atanh with range reduction and proved tail'}
(RUN/'out'/('PILOT.json' if mode=='pilot' else 'EXACT_RESULTS.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
