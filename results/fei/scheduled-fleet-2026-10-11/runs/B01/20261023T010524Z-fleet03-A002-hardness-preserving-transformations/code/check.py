from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from collections import Counter
import json,time,sys

START=time.monotonic(); C=Counter(); OUT=Path(__file__).resolve().parents[1]/'out'
def ck(b):
    C['assertions']+=1
    assert b
    if time.monotonic()-START>55:raise RuntimeError('frozen55s cap')
def parity(v):return v.bit_count()%2
def rank(vs):
    rows={}
    for v in vs:
        while v:
            j=v.bit_length()-1
            if j in rows:v^=rows[j]
            else:rows[j]=v;break
    return len(rows)
def cheapest(w):
    rows={}; cost=0
    for v in sorted(range(1,len(w)),key=lambda v:(w[v],v)):
        x=v
        while x:
            j=x.bit_length()-1
            if j in rows:x^=rows[j]
            else:rows[j]=x;cost+=w[v];break
    return cost
@lru_cache(None)
def factors(n):
    out=[];p=2
    while p*p<=n:
        e=0
        while n%p==0:e+=1;n//=p
        if e:out.append((p,e))
        p+=1
    if n>1:out.append((n,1))
    return tuple(out)
def add(*terms):
    ans=Counter()
    for scale,d in terms:
        for p,v in d.items():ans[p]+=scale*v
    return {p:q for p,q in ans.items() if q}
def atom(x):
    if not x:return {}
    ans=Counter()
    for p,e in factors(x.numerator):ans[p]-=e*x
    for p,e in factors(x.denominator):ans[p]+=e*x
    return {p:q for p,q in ans.items() if q}
def scalar(x):return {2:Q(x)} if x else {}
def profile(mu,k):
    p=Q(1,1<<k);delta=1-mu
    return add((1,atom((1-p*delta)**2)),(-p,atom(mu*mu)),(p-p*p,atom(delta*delta)),(1,scalar(2*k*p*(1-mu*mu)+2*k*(p-p*p)*delta*delta)))
def activate(f,k):return tuple(f)+(1,)*(len(f)*((1<<k)-1))
@lru_cache(None)
def stats(f):
    n=(len(f)-1).bit_length();a=list(f);step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for i in range(j,j+step):a[i],a[i+step]=a[i]+a[i+step],a[i]-a[i+step]
        step*=2
    d=len(f)**2; sq=[v*v for v in a]
    w=[sum(z for s,z in enumerate(sq) if parity(s&v)) for v in range(len(f))]
    m=[min(v,d-v) for v in w]
    coord=[Q(w[1<<i],d) for i in range(n)]
    H=add(*[(1,atom(Q(v,d))) for v in sq])
    ell=Q(cheapest(w),d); aff=Q(cheapest(m),d)
    if n<=3:
        bases=[b for b in combinations(range(1,1<<n),n) if rank(b)==n]
        ck(ell==Q(min(sum(w[v] for v in b) for b in bases),d))
        ck(aff==Q(min(sum(m[v] for v in b) for b in bases),d))
    return dict(n=n,mu=Q(a[0],len(f)),I=sum(coord,Q(0)),coord=coord,H=H,ell=ell,a=aff,w=w,den=d,walsh=a)
def restrict(f,A,b):
    n=(len(f)-1).bit_length();remain=[i for i in range(n) if i not in A];out=[]
    for x in range(1<<len(remain)):
        j=sum(((x>>t)&1)<<i for t,i in enumerate(remain))+sum(((b>>t)&1)<<i for t,i in enumerate(A));out.append(f[j])
    return tuple(out)
def fixture(f,k=2):
    s=stats(f);F=activate(f,k);t=stats(F);p=Q(1,1<<k);delta=1-s['mu'];n=s['n']
    ck(t['a']==t['ell']==p*(s['ell']+k*delta))
    ck(t['I']==p*(s['I']+k*delta))
    ck(t['H']==add((p,s['H']),(1,profile(s['mu'],k))))
    for v in range(1<<t['n']):ck(Q(t['w'][v],t['den'])==(p*delta if v>>n else p*Q(s['w'][v],s['den'])))
    for mask in range(1<<n):
        A=tuple(i for i in range(n) if mask>>i&1);N=1<<len(A);children=[restrict(f,A,b) for b in range(N)]
        cs=[stats(c) for c in children]; FC=[restrict(F,A,b) for b in range(N)];cts=[stats(c) for c in FC]
        for h,c in zip(children,FC):ck(c==activate(h,k))
        IA=sum((s['coord'][i] for i in A),Q(0)); IAF=sum((t['coord'][i] for i in A),Q(0))
        avgA=sum((c['a'] for c in cs),Q(0))/N;avgell=sum((c['ell'] for c in cs),Q(0))/N
        rho=s['I']-IA-avgA;r=s['I']-IA-avgell
        rhoF=t['I']-IAF-sum((c['a'] for c in cts),Q(0))/N;gap=avgell-avgA
        ck(r>=0 and rho>=r and gap>=0)
        ck(rhoF==p*r==p*(rho-gap));ck(IAF==p*IA)
        L=add((1,s['H']),*[(Q(-1,N),c['H']) for c in cs])
        LF=add((1,t['H']),*[(Q(-1,N),c['H']) for c in cts])
        correction=add((1,profile(s['mu'],k)),*[(Q(-1,N),profile(c['mu'],k)) for c in cs])
        ck(LF==add((p,L),(1,correction)))
        # Resolve the SAME controls after linear-only child resets. The
        # unavailable translation release is redeemed here, exactly once.
        ck(p*(IA+r)+p*k*delta+p*gap+p*avgA==t['I'])
        late_entropy=add(*[(Q(1,N),c['H']) for c in cts],*[(Q(-p,N),c['H']) for c in cs])
        for K in [0,2,8]:
            bankF=add((1,LF),(1,scalar(-K*(IAF+rhoF))))
            source=add((1,L),(1,scalar(-K*(IA+rho))))
            ck(bankF==add((p,source),(1,correction),(1,scalar(K*p*gap))))
            late_bank=add((1,late_entropy),(1,scalar(-K*(p*k*delta+p*gap))))
            final_bank=add((1,t['H']),*[(Q(-p,N),c['H']) for c in cs],(1,scalar(-K*(t['I']-p*avgA))))
            ck(add((1,bankF),(1,late_bank))==final_bank)
        C['blocks']+=1;C['actual_children']+=N
    C['fixtures']+=1
    return s,t

pilot='--pilot' in sys.argv
for n in range(3 if pilot else 4):
    for mask in range(1<<(1<<n)):
        f=tuple(1-2*((mask>>x)&1) for x in range(1<<n));fixture(f);C['labelled_seeds']+=1
examples={}
if not pilot:
    bent=(1,1,1,-1)
    for k in [2,3,4,5]:
        h,F=fixture(bent,k);p=Q(1,1<<k)
        ch=[stats(restrict(bent,(0,),b)) for b in range(2)]
        chF=[stats(restrict(activate(bent,k),(0,),b)) for b in range(2)]
        rho=h['I']-h['coord'][0]-sum(c['a'] for c in ch)/2
        rhoF=F['I']-F['coord'][0]-sum(c['a'] for c in chF)/2
        ck(rho==Q(1,2));ck(rhoF==0);ck(F['a']==F['I']);ck(F['mu']==1-p/2)
        C['zero_credit_guards']+=1
    for tnum in [2,3]:
        h=(1,)
        for _ in range(tnum):h=tuple(a*b for b in bent for a in h)
        # Frozen t2,t3 source-bound quadratic fixtures, not a new exhaustive dimension.
        s=stats(h);F=stats(activate(h,2));p=Q(1,4)
        ch=[stats(restrict(h,(0,),b)) for b in range(2)]
        chF=[stats(activate(restrict(h,(0,),b),2)) for b in range(2)]
        ck(s['I']==s['ell']==s['a']==tnum)
        ck(sorted(c['ell'] for c in ch)==[Q(tnum-1),Q(2*tnum-1,2)])
        rhoF=F['I']-F['coord'][0]-sum(c['a'] for c in chF)/2
        ck(rhoF==p/4);ck(F['a']==F['I']);C['tensor_guards']+=1
    # Essential boundary: one control and negative constant.
    s=stats((-1,));F=stats(activate((-1,),1));ck(F['a']==0);ck(Q(1,2)*(s['ell']+1*(1-s['mu']))==1)
    examples={'bent2_query':'source rho=1/2; activated rho=0 for k2..5','bent_tensors':'source rho=1/2; activated rho=p/4 for frozen t2,t3','k1_negative_constant':'affine optimum0, invalid formula1'}
result={'status':'PASS','pilot':pilot,'counts':dict(C),'seconds':time.monotonic()-START,'arithmetic':'integer Walsh; Fraction; exact prime-log vectors; n<=3 exhaustive basis replay','examples':examples,'cache_entries':stats.cache_info().currsize}
(OUT/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
