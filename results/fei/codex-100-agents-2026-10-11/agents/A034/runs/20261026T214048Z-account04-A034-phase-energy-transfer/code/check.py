from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import itertools, json, sys, time, hashlib

RUN=Path(__file__).resolve().parents[1]
START=time.monotonic(); CHECKS=0
def need(v,msg):
    global CHECKS
    CHECKS+=1
    if not v: raise AssertionError(msg)
    if time.monotonic()-START>55: raise TimeoutError('frozen 55-second cap')

@lru_cache(None)
def logint(x):
    # Rational atanh series: normalize x to [1,2), so 0<=z<1/3.
    x=Q(x); k=x.numerator.bit_length()-x.denominator.bit_length()
    if x<Q(2)**k:k-=1
    z=(x/(Q(2)**k)-1)/(x/(Q(2)**k)+1)
    def lnseries(z):
        lo=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(16)),Q(0))
        return lo,lo+2*z**33/(33*(1-z*z))
    a,b=lnseries(z);c,d=lnseries(Q(1,3))
    return Q(k)+a/d,Q(k)+b/c

def walsh(v):
    a=list(v);h=1
    while h<len(a):
        for k in range(0,len(a),2*h):
            for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return a

def influences(v):
    N=len(v); n=N.bit_length()-1
    return [Q(sum((v[y]-v[y^(1<<i)])**2 for y in range(N)),4*N) for i in range(n)]

def bill(v):
    N=len(v);W=walsh(v)
    lo=hi=Q(0)
    for w in W:
        if w:
            p=Q(w*w,N*N);l,h=logint(1/p);lo+=p*l;hi+=p*h
    return lo,hi

def affine(support):
    if not support:return False
    a=next(iter(support));V={x^a for x in support}
    return len(V)&(len(V)-1)==0 and all(x^y in V for x in V for y in V)

def groups(pieces):
    pieces=sorted(pieces,key=lambda p:-sum(x*x for x in p));s=len(pieces);R=64*s*s
    result=[];last=None
    for p in pieces:
        mass=sum(x*x for x in p)
        if last is None or last>R*mass:result.append([])
        result[-1].append(p);last=mass
    return [[sum(a) for a in zip(*g)] for g in result]

def check(pieces, entropy=True):
    N=len(pieces[0]);s=len(pieces)
    v=[sum(a) for a in zip(*pieces)]
    need(all(x in (-1,0,1) for x in v),'physical disjointness')
    vg=groups(pieces);es=[influences(w) for w in vg];eu=influences(v)
    for i,e in enumerate(eu):
        need(2*e>=sum(a[i] for a in es),'group energy dominates')
    if entropy:
        Bs=[bill(w) for w in vg];B=bill(v)
        if len(vg)==1:need(vg[0]==v,'single-group entropy equality')
        else:need(B[1]<=len(vg)*sum(b[0] for b in Bs),'certified coherent entropy upper inequality')
        # Verify stronger per-group analytic upper constants using rigorously rounded logs.
        for w,e,b in zip(vg,es,Bs):
            active=[p for p in pieces if any(x*y for x,y in zip(p,w))]
            alpha=Q(min(sum(x*x for x in p) for p in active),N)
            mu=Q(sum(x*x for x in w),N)
            L=logint(mu/alpha)[0]+Q(22,5) # log2(e)>7/5 analytically
            need(b[1]<=L*sum(e),'certified retained complete group bill')
        L=logint(Q(s))[0]+(s-1)*logint(Q(64*s*s))[0]+Q(22,5)
        need(B[1]<=2*s*L*sum(eu),'certified complete row theorem')
    return v,len(vg)

def rows():
    count=0
    for n in range(4):
        N=1<<n
        for v in itertools.product((-1,0,1),repeat=N):
            ps=[]
            for i,x in enumerate(v):
                if x:
                    p=[0]*N;p[i]=x;ps.append(p)
            if ps:check(ps)
            else:need(not any(v),'zero row')
            count+=1
    need(count==6654,'all frozen ternary rows')
    return {'rows':count}

def scales():
    result=[]
    for n in range(8,12):
        N=1<<n
        for sign in (-1,1):
            a=[int(not(y&1)) for y in range(N)]
            b=[sign*int(y==N-1) for y in range(N)]
            v,q=check([a,b])
            need(all(e==0 or e>=Q(1,2*N) for e in influences(v)),'ternary derivative minimum')
            result.append({'n':n,'sign':sign,'groups':q,'mass_ratio':N//2})
    # Negative control: comparing original cells rather than mass groups is FALSE.
    a=[1,0];b=[0,1];u=[1,1]
    need(sum(influences(u))==0 and sum(influences(a))+sum(influences(b))>0,'real cancellation negative control')
    return {'fixtures':result,'ungrouped_energy_claim':'REFUTED by constant two-cell cover'}

def assign(state,k):
    y=0;j=0
    for i,v in enumerate(state):
        if v==-1:y|=((k>>j)&1)<<i;j+=1
        else:y|=v<<i
    return y

def carrier():
    states=0;maxrows=0
    for state in itertools.product((-1,0,1),repeat=6):
        xs=state[:2];ys=state[2:];nx=xs.count(-1);ny=ys.count(-1);N=1<<ny
        byrow={};data=[]
        for local in range(N):
            y=assign(ys,local);t=y&1;z=(y>>1)&3;a=(y>>3)&1
            label=z if t else 0
            phase=a*((z>>(1 if t else 0))&1)
            fixed=sum(v*((label>>i)&1) for i,v in enumerate(xs) if v!=-1)&1
            free=[i for i,v in enumerate(xs) if v==-1]
            j=sum(((label>>i)&1)<<k for k,i in enumerate(free))
            byrow.setdefault(j,{}).setdefault(t,[0]*N)[local]=1-2*(phase^fixed)
            data.append((label,phase))
        E=Q(0);B=Q(0);Ws={}
        for j,ps in byrow.items():
            for p in ps.values():need(affine({i for i,x in enumerate(p) if x}),'carrier fiber affine')
            u,q=check(list(ps.values()));E+=sum(influences(u));B+=bill(u)[0];Ws[j]=walsh(u)
        vals=[]
        for label,phase in data:
            for x in range(1<<nx):vals.append(1-2*(phase^((assign(xs,x)&label).bit_count()&1)))
        W=walsh(vals);scale=1<<nx
        for k,w in enumerate(W):need(w==scale*Ws.get(k&(scale-1),[0]*N)[k>>nx],'independent full-F Fourier ledger')
        iy=sum(influences(vals)[nx:]);need(iy==E,'SAME physical IY')
        need(B==bill(vals)[0],'entire joint entropy retained')
        states+=1;maxrows=max(maxrows,len(byrow))
    need(states==729,'all mixed physical restrictions')
    return {'states':states,'max_nonempty_rows':maxrows,'full_joint_ledger':'PASS'}

def audit():
    # Independent rational reconstruction of the two numerical steps, with boundary cases.
    for s in range(1,129):
        R=64*s*s
        need(Q(2*s,R)<=Q(1,32),'group tail relative energy')
        need(Q(9,16)>=Q(1,2)*(1+Q(2*s,R)),'reverse triangle pays factor2')
        need(Q(1,32)<=Q(1,16),'squared tail norm weakens to quarter')
    for r in range(1,33):
        need(Q(1,2)/Q(1,2**(r+1))==2**r,'different carriers have unbounded fiber mass ratio')
    need(logint(Q(2))[0]==1,'log exact dyadic boundary')
    need(logint(Q(1))[0]==0,'log at one')
    return {'s_range':[1,128],'unequal_carrier_parameters':32}

if __name__=='__main__':
    mode=sys.argv[1];result=globals()[mode]()
    result.update(mode=mode,status='PASS',assertions=CHECKS,seconds=time.monotonic()-START,
                  helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (RUN/'out').mkdir(exist_ok=True)
    (RUN/'out'/f'{mode}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
