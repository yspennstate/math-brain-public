"""Exact, bounded checks of the distinct shared-controller family. UTF-8 outputs."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json, sys, time, math
ROOT=Path(__file__).resolve().parents[1]
COUNT=0
DIRECT=False

def ck(v,tag):
    global COUNT
    COUNT+=1
    if not v: raise AssertionError(tag)

def add(*es):
    d={}
    for e in es:
        for p,c in e.items(): d[p]=d.get(p,Q(0))+c
    return {p:c for p,c in d.items() if c}

def mul(e,c): return {p:v*c for p,v in e.items() if v*c}
def const(c): return {2:Q(c)} if c else {}
def eq(a,b,tag): ck(not add(a,mul(b,-1)),tag)

@lru_cache(None)
def factors(n):
    out={}; p=2
    while p*p<=n:
        while n%p==0: out[p]=out.get(p,0)+1; n//=p
        p+=1 if p==2 else 2
    if n>1: out[n]=out.get(n,0)+1
    return out

def log(q):
    q=Q(q)
    ck(q>0,'positive logarithm')
    return add(factors(q.numerator),mul(factors(q.denominator),-1))

def phi(q): return mul(log(q),-q) if q else {}
def avg(es): return mul(add(*es),Q(1,len(es)))

def fwht(f):
    a=list(f); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return a

def direct(f):
    return [sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(f)) for s in range(len(f))]

def tails(p):
    t=list(p); n=len(p).bit_length()-1
    for i in range(n):
        for s in range(len(p)):
            if not s&(1<<i): t[s]+=t[s|(1<<i)]
    return t

def cut(f,i,b): return tuple(v for x,v in enumerate(f) if (x>>i)&1==b)

def marked_singleton(f):
    aa=(direct if DIRECT else fwht)(f); pp=[Q(v*v,len(f)**2) for v in aa]
    if not pp[1]: return {}
    return mul(log(sum(p for s,p in enumerate(pp) if s&1)/pp[1]),pp[1])

def stats(f):
    n=len(f).bit_length()-1; N=len(f)
    aa=(direct if DIRECT else fwht)(f); pp=[x*x for x in aa]; tt=tails(pp)
    vv={}
    for s in range(1,N):
        if pp[s]: vv=add(vv,mul(add(log(tt[s]),mul(log(pp[s]),-1)),Q(pp[s],N*N)))
    physical=[Q(sum(f[x]!=f[x^(1<<i)] for x in range(N)),N) for i in range(n)]
    spectral=[sum(Q(pp[s],N*N) for s in range(N) if s&(1<<i)) for i in range(n)]
    ck(physical==spectral,'actual Boolean physical/spectral influences')
    ck(sum(pp)==N*N,'Boolean Parseval')
    return {'V':vv,'I':sum(physical),'piv':physical,'mean':Q(sum(f),N)}

def ledger(f):
    r=stats(f); children=[]; drifts=[]
    for i in range(len(f).bit_length()-1):
        cs=[stats(cut(f,i,b)) for b in (0,1)]
        children.append(cs); drifts.append(add(r['V'],mul(avg([c['V'] for c in cs]),-1)))
    r.update(children=children,drifts=drifts,GV=add(*drifts))
    return r

def majority(n,z): return 1 if z.bit_count()<=n//2 else -1
def seed(x): return (-1 if x&7==0 else 1)*(-1 if x>>3==0 else 1)
def fam(n):
    f=[]
    for r in range(1<<(n+7)):
        x=r&63; w=1-2*((r>>6)&1); a=majority(n,r>>7)
        f.append(seed(x)*(a if x==0 else a*w if x==1 else 1))
    return tuple(f)

def mux(n):
    return tuple(majority(n,r>>2)*(1 if r&1==0 else -(1-2*((r>>1)&1))) for r in range(1<<(n+2)))

def T(s):
    delta=Q(1,64)
    B=tuple(seed(x)-int(x==0)+int(x==1) for w in range(2) for x in range(64))
    C=tuple(int(x==0)-(1-2*w)*int(x==1) for w in range(2) for x in range(64))
    bb=[Q(x,128) for x in fwht(B)]; cc=[Q(x,128) for x in fwht(C)]
    ck(all(x*x==delta*delta for x in cc),'uniform full carrier spectrum')
    ck(sum(x*x for x in cc)==2*delta,'actual carrier norm')
    M=[b*b+2*s*b*c+c*c for b,c in zip(bb,cc)]; Z=tails(M)
    e={}
    for S in range(1,64):
        p=(bb[S]+s*cc[S])**2
        ck(p>=delta*delta and Z[S]>=p and Z[S]<=1,'smooth denominator domain')
        e=add(e,mul(log(Z[S]/p),p))
    return add(e,const(7*delta-4*delta*s*s))

@lru_cache(None)
def lnbounds(q):
    q=Q(q); z=(q-1)/(q+1); term=z; lo=Q(0)
    for j in range(40): lo+=2*term/(2*j+1); term*=z*z
    return lo,lo+2*term/(81*(1-z*z))

def bounds(e):
    out=[Q(0),Q(0)]; ll,lh=lnbounds(Q(2))
    for p,c in e.items():
        k=p.bit_length()-1; a,b=lnbounds(Q(p,2**k)); a,b=k+a/lh,k+b/ll
        if c<0: a,b=b,a
        out[0]+=c*a; out[1]+=c*b
    return out

def run(mode):
    global DIRECT
    start=time.perf_counter(); DIRECT=mode=='replay'
    ns=[1] if DIRECT else [1,3] if mode=='pilot' else [1,3,5]
    delta=Q(1,64); rows=[]; Dstar=None
    for n in ns:
        f=fam(n); a=tuple(majority(n,z) for z in range(1<<n)); h=mux(n)
        F=ledger(f); A=ledger(a); H=ledger(h)
        d=Q(math.comb(n-1,(n-1)//2),1<<(n-1)); q=d*d
        eq(F['V'],add(mul(A['V'],2*delta),T(Q(0))),'root carrier decomposition')
        for b in (0,1):
            child=F['children'][7][b]; ac=A['children'][0][b]; s=ac['mean']
            eq(child['V'],add(mul(ac['V'],2*delta),mul(phi(s*s),delta),T(s)),'both biased child decompositions')
        S=mul(add(T(Q(0)),mul(avg([T(d),T(-d)]),-1)),n)
        D=add(*F['drifts'][:7])
        if Dstar is None: Dstar=D
        else: eq(D,Dstar,'DATA residual independent of majority width')
        eq(add(*F['drifts'][7:]),add(mul(A['GV'],2*delta),mul(phi(q),-delta*n),S),'complete z drift')
        # U=V+phi(mean^2); at root majority U=V and each child adds phi(q).
        GUa=add(A['GV'],mul(phi(q),-n))
        eq(H['GV'],add(GUa,const(2),mul(phi(q/4),n)),'all physical mux coordinates')
        residual=add(F['GV'],mul(H['GV'],-2*delta))
        rhs=add(mul(phi(q),delta*n/2),const(-delta*n*q-4*delta),S,D)
        eq(residual,rhs,'exact logarithmic residual equation2')
        marked=add(H['GV'],mul(phi(q),Q(n,4)),const(Q(n,4)*q))
        actual_marked=dict(H['GV'])
        for i in range(1,n+2):
            actual_marked=add(actual_marked,avg([marked_singleton(cut(h,i,b)) for b in (0,1)]))
        eq(marked,actual_marked,'actual marked functional, both children of EVERY physical control')
        ck(not marked_singleton(h),'actual root singleton exactly zero')
        mr=add(F['GV'],mul(marked,-2*delta))
        eq(mr,add(const(-Q(3,2)*delta*n*q-4*delta),S,D),'marked owner exact cancellation equation4')
        ck(bounds(add(const(256*sum(F['piv'][:6])),mul(mr,-1)))[0]>0,'SAME256 marked owner paid from ORIGINAL SIX DATA owners, both terminals')
        eq(phi(q/4),add(mul(phi(q),Q(1,4)),const(q/2)),'logarithm scaling exact')
        ck(sum(F['piv'][:6])<=6,'six original physical DATA coordinates')
        ck(H['mean']==0,'zero root marked singleton')
        ck(F['I']==sum(F['piv'][:7])+2*delta*A['I'],'original actual influence decomposition')
        ck(F['piv'][6]==delta,'w actual controller influence is charged ONCE')
        ck(F['I']==sum(F['piv'][:6])+delta*(2*A['I']+1),'six-DATA plus full two-controller influence identity')
        ck(sum(F['piv'][:6])>=Q(21,16),'same original DATA lower bound')
        lo,hi=bounds(S); ck(lo>=-7 and hi<=7,'Taylor envelope finite boundary')
        rows.append({'n':n,'data_influence':str(sum(F['piv'][:6])), 'controller_w_influence':str(F['piv'][6]), 'residual':{str(p):str(v) for p,v in residual.items()},'residual_interval':list(map(str,bounds(residual))), 'S_interval':list(map(str,(lo,hi)))})
        if time.perf_counter()-start>(60 if mode in ('pilot','replay') else 180): raise TimeoutError('frozen cap')
    # Exact endpoint checks for the all-m induction, not inference from samples.
    for m in range(1,257):
        d=Q(math.comb(2*m,m),4**m)
        ck(Q(1,4*m)<=d*d<=Q(1,2*m+1),'majority squared bounds')
        ck(Q((2*m+1)**2,4*(m+1)**2)>=Q(m,m+1),'lower induction ratio')
        ck((2*m+1)*(2*m+3)<4*(m+1)**2,'upper induction ratio')
    ck(32**32<=2**7*31**31,'binary entropy constant exact integer certificate')
    result={'status':'PASS','mode':mode,'assertions':COUNT,'seconds':time.perf_counter()-start,'roots':rows,'direct_character':DIRECT,'independent_person_review':False}
    (ROOT/'out').mkdir(exist_ok=True)
    (ROOT/'out'/f'{mode}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='roots'}))

if __name__=='__main__': run(sys.argv[1])
