from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
import json,time

RUN=Path(__file__).resolve().parents[1]
START=time.perf_counter()
COUNTS={'product_cases':0,'proper_block_checks':0,'parity_dimensions':0,'parity_block_orbits':0,'direct_parity_children':0,'assertions':0,'strict_slack_certificates':0}
RECORDS=[]

def ck(x):
    COUNTS['assertions']+=1
    assert x

def deadline():
    if time.perf_counter()-START>55:
        (RUN/'out'/'TIMEOUT.json').write_text(json.dumps(COUNTS,indent=2),encoding='utf-8')
        raise TimeoutError('55 second internal pilot stop')

def fwht(f):
    w=list(f); h=1
    while h<len(w):
        for b in range(0,len(w),2*h):
            for j in range(b,b+h):
                u,v=w[j],w[j+h]; w[j],w[j+h]=u+v,u-v
        h*=2
    return w

def spectrum(f):
    return tuple(Q(w*w,len(f)**2) for w in fwht(f))

def influences(f):
    n=len(f).bit_length()-1
    return tuple(Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f)) for i in range(n))

@lru_cache(maxsize=4096)
def log2(x):
    if x==1: return Q(0),Q(0)
    assert x>0
    k=0
    while x>=2: x/=2; k+=1
    while x<1: x*=2; k-=1
    def ln(y):
        z=(y-1)/(y+1)
        z2=z*z; power=z; s=Q(0); m=48
        for i in range(m):
            s+=2*power/Q(2*i+1); power*=z2
        return s,s+2*power/Q(2*m+1)/(1-z2)
    a,b=ln(x); c,d=ln(Q(2))
    return k+a/d,k+b/c

@lru_cache(maxsize=4096)
def entropy(P):
    lo=hi=Q(0)
    for p in P:
        if p:
            a,b=log2(1/p);lo+=p*a;hi+=p*b
    return lo,hi

def plus(x,y): return x[0]+y[0],x[1]+y[1]
def sub(x,y): return x[0]-y[1],x[1]-y[0]
def scale(x,q):
    assert q>=0
    return x[0]*q,x[1]*q
def abs_upper(x): return max(abs(x[0]),abs(x[1]))
def h2(p): return entropy((p,1-p))
def E(n):
    if n<2: return Q(0),Q(0)
    if n<4: return Q(n),Q(n)
    u=Q(2)**(1-n//2)
    return plus(h2(u),(n*u,n*u))

def child(f,mask,value):
    n=len(f).bit_length()-1
    free=[i for i in range(n) if not mask>>i&1]
    def expand(v): return value|sum(((v>>j)&1)<<i for j,i in enumerate(free))
    return tuple(f[expand(v)] for v in range(1<<len(free)))

def children(f,mask):
    fixed=[i for i in range(len(f).bit_length()-1) if mask>>i&1]
    return [child(f,mask,sum(((a>>j)&1)<<i for j,i in enumerate(fixed))) for a in range(1<<len(fixed))]

def block(f,mask):
    P=spectrum(f)
    c=children(f,mask)
    childP=[spectrum(v) for v in c]
    av=scale(tuple(sum(entropy(q)[i] for q in childP) for i in (0,1)),Q(1,len(c)))
    L=sub(entropy(P),av)
    inf=influences(f)
    I=sum(inf[i] for i in range(len(inf)) if mask>>i&1)
    # Independent spectral marginal vs physical-child averaging identity.
    kept=[i for i in range(len(inf)) if not mask>>i&1]
    marginal=[Q(0) for _ in range(1<<len(kept))]
    for s,p in enumerate(P):
        t=sum(((s>>i)&1)<<j for j,i in enumerate(kept)); marginal[t]+=p
    avP=tuple(sum(q[t] for q in childP)/len(c) for t in range(len(marginal)))
    ck(tuple(marginal)==avP)
    return L,I,childP

for c in range(16):
    h=[1-2*(c>>x&1) for x in range(4)]
    for d in range(16):
        deadline()
        k=[1-2*(d>>x&1) for x in range(4)]
        f=tuple(h[x&3]*k[x>>2] for x in range(16))
        g=(-f[0],)+f[1:]
        P,Qp=spectrum(f),spectrum(g); p=Q(1,16)
        tv=sum(abs(x-y) for x,y in zip(P,Qp))/2
        ck(tv*tv<=4*p*(1-p))
        ratios0=[];ratios1=[]; errs=[]
        for mask in range(1,15):
            a=mask.bit_count();m=4-a
            L0,I0,C0=block(f,mask);L1,I1,C1=block(g,mask)
            ck(abs(I1-I0)<=2*a*p)
            actual_dt=sum(abs(x-y) for x,y in zip(C0[0],C1[0]))/(2*(1<<a))
            ck(all(C0[j]==C1[j] for j in range(1,len(C0))))
            # TV of the actual uniform-query/retained-spectrum channel.
            b=plus(scale(plus((tv,tv),(actual_dt,actual_dt)),a),plus(h2(tv),h2(actual_dt)))
            ck(abs_upper(sub(L1,L0))<=b[0])
            eta=plus(E(4),scale(E(m),Q(1,1<<a)))
            ck(abs_upper(sub(L1,L0))<=eta[0])
            ck(L0[0]>=0 and L1[0]>=0)
            if I0:
                ratios0.append(scale(L0,1/I0))
            if I1:
                ratios1.append(scale(L1,1/I1))
            if I0>2*a*p:
                r0=scale(L0,1/I0)
                exacterr=scale(plus(eta,scale(r0,2*a*p)),1/(I0-2*a*p))
                ck(abs_upper(sub(scale(L1,1/I1),r0))<=exacterr[0])
            COUNTS['proper_block_checks']+=1
        inf=influences(f)
        if all(inf):
            kap=min(inf)
            ck(kap>2*p)
            phi0=(min(x[0] for x in ratios0),min(x[1] for x in ratios0))
            phi1=(min(x[0] for x in ratios1),min(x[1] for x in ratios1))
            errors=[]
            for a in range(1,4):
                eta=plus(E(4),scale(E(4-a),Q(1,1<<a)))
                errors.append(plus(scale(eta,1/(a*(kap-2*p))), (4*p/(kap*(kap-2*p)),)*2))
            uniform=(max(e[0] for e in errors),max(e[1] for e in errors))
            ck(abs_upper(sub(phi1,phi0))<=uniform[0])
        COUNTS['product_cases']+=1

def pd_spectrum(n):
    if n==0: return (Q(1),)
    p=Q(1,1<<n)
    return ((1-2*p)**2,)+ (4*p*p,)*((1<<n)-1)

def decimals(interval):
    # Displays only; all decisions above use rational intervals.
    return [float(interval[0]),float(interval[1])]

previous=None
for n in range(2,13):
    deadline()
    p=Q(1,1<<n); u=1-2*p
    hn=entropy(pd_spectrum(n)); rn=scale(hn,1/(n*2*p))
    if previous: ck(rn[0]>previous[1])
    previous=rn
    rG=scale(hn,1/(n*u)); orbits=[]
    for a in range(1,n):
        hm=entropy(pd_spectrum(n-a))
        L=sub(hn,scale(hm,Q(1,1<<a)))
        ratio=scale(L,1/(a*u))
        residual=sub(L,scale(rG,a*u))
        ck(residual[0]>0)
        if n<=8:
            G=tuple((-1)**x.bit_count()*(1-2*(x==0)) for x in range(1<<n))
            mask=(1<<a)-1
            Lphys,Iphys,childP=block(G,mask)
            ck(Iphys==a*u)
            ck(abs_upper(sub(L,Lphys))<Q(1,10**20))
            ck(all(entropy(q)==(Q(0),Q(0)) for q in childP[1:]))
            ck(sorted(spectrum(G))==sorted(pd_spectrum(n)))
            COUNTS['direct_parity_children']+=1
        orbits.append({'block_size':a,'ratio_display':decimals(ratio),'own_ratio_residual_lower':str(residual[0]),'own_ratio_residual_upper':str(residual[1])})
        COUNTS['parity_block_orbits']+=1
    RECORDS.append({'n':n,'defect_mass':str(p),'point_defect_ratio_display':decimals(rn),'surgery_ratio_display':decimals(rG),'phi_display':[min(v['ratio_display'][0] for v in orbits),min(v['ratio_display'][1] for v in orbits)],'proper_blocks':orbits})
    COUNTS['parity_dimensions']+=1

# Fixed h=pd_2, F_t=z*h^tensor t: strict slack transfers by explicit singleton bill.
ln2=log2(Q(2)) # log2 2=1; use certified log2(e)=1/ln2 via ln2's atanh series.
z=Q(1,3); s=2*sum(z**(2*j+1)/Q(2*j+1) for j in range(48))
tail=2*z**97/Q(97)/(1-z*z)
loge=(1/(s+tail),1/s)
for t in range(3,9):
    n=2*t+1;p=Q(1,1<<n);e=2*p
    Hlow=2*t-E(n)[1]
    Ilow=t+1-2*n*p;Ihigh=t+1+2*n*p
    Rlower=Hlow/Ihigh
    singleton_upper=(h2(e)[1]+2*loge[1]*e)/(1-e)
    ck(Rlower>singleton_upper)
    COUNTS['strict_slack_certificates']+=1

COUNTS['runtime_seconds']=time.perf_counter()-START
COUNTS['status']='PASS'
ck(COUNTS['product_cases']==256 and COUNTS['proper_block_checks']==3584)
ck(COUNTS['parity_block_orbits']==66)
(RUN/'out'/'EXACT_CHECK.json').write_text(json.dumps(COUNTS,indent=2)+'\n',encoding='utf-8')
(RUN/'out'/'PARITY_CERTIFICATES.json').write_text(json.dumps(RECORDS,indent=2)+'\n',encoding='utf-8')
print(json.dumps(COUNTS,indent=2))
