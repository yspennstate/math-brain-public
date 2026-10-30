from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json, sys, time

ROOT=Path(__file__).resolve().parents[1]
COUNT=0
def ck(b):
    global COUNT
    COUNT+=1
    assert b, COUNT

@lru_cache(None)
def logi(x):
    x=F(x)
    assert x>0
    if x==1: return (F(0),F(0))
    if x<1:
        lo,hi=logi(1/x)
        return -hi,-lo
    k=0
    while x>=2:
        x/=2; k+=1
    z=(x-1)/(x+1)
    def series(z):
        val=sum((2*z**(2*j+1)/F(2*j+1) for j in range(40)),F(0))
        tail=2*z**81/(81*(1-z*z))
        return val,val+tail
    lo,hi=series(z)
    if k:
        l,h=series(F(1,3)); lo+=k*l; hi+=k*h
    return lo,hi

def addlog(acc,c,x):
    lo,hi=logi(F(x))
    return (acc[0]+c*(lo if c>=0 else hi),acc[1]+c*(hi if c>=0 else lo))

def spectrum(vals,n):
    N=1<<n; a=list(vals)
    for j in range(n):
        d=1<<j
        for x in range(N):
            if not x&d:
                u,v=a[x],a[x+d]; a[x]=u+v; a[x+d]=u-v
    P={s:F(a[s]**2,N*N) for s in range(1,N) if a[s]}
    I=sum((p*s.bit_count() for s,p in P.items()),F(0))
    flips=sum(vals[x]!=vals[x^(1<<j)] for x in range(N) for j in range(n))
    ck(I==F(flips,N)); ck(sum(a0*a0 for a0 in a)==N*N)
    return P,I

def masks(E): return [s for s in range(1<<(E.bit_length())) if s&~E==0]

def fixture(r,w):
    n=1+r*w; Es=[1|(((1<<w)-1)<<(1+j*w)) for j in range(r)]
    opts=[masks(E) for E in Es]
    vals=[2*int(bool(x&1) or all(x&(E^1) for E in Es))-1 for x in range(1<<n)]
    P,I=spectrum(vals,n); v=sum(P.values(),F(0)); a=(1-F(1,1<<w))**r
    ck(I==1-a+a*r*w*F(1,1<<w)/(1-F(1,1<<w)))
    ck(P[1]==(1-a)**2)
    aliases={}
    tuples=list(product(*opts))
    for z in tuples:
        A=0
        for s in z: A|=s
        aliases.setdefault(A,[]).append(z)
    M=[F(0)]*r; h=(F(0),F(0))
    for A,p in P.items():
        zs=aliases[A]; h=addlog(h,p,len(zs))
        for j in range(r): M[j]+=p*F(sum(bool(z[j]) for z in zs),len(zs))
    ck(len(set(M))==1)
    alpha=min(M[0]/v,F(1,r))
    price=(M[0]-v*alpha)/(alpha*(1-alpha))
    ck(price>=0); ck(r*alpha<=1); ck(price*(r*alpha-1)==0)
    for j in range(r):
        ck((v*alpha-M[j])/(alpha*(1-alpha))+price==0)
    # Every private constraint is alpha<=1; the shared one is r*alpha<=1.
    for i in range(n): ck(sum(alpha for E in Es if E&(1<<i))<=1)
    N=(1<<(w+1))-1; Z=1-(1-alpha)**r
    Q={}
    for A,zs in aliases.items():
        if not A: continue
        mass=F(0)
        for z in zs:
            k=sum(bool(s) for s in z)
            mass+=(alpha/N)**k*(1-alpha)**(r-k)
        Q[A]=mass/Z
    ck(sum(Q.values(),F(0))==1); ck(Q[1]<=F(1,N))
    for k in range(1,r+1): ck(F(1,N)**k<=F(1,N))
    B=(-h[1],-h[0]); C=(F(0),F(0))
    for m in M:
        B=addlog(B,-m,alpha); B=addlog(B,-(v-m),1-alpha); B=addlog(B,m,N)
    for A,p in P.items(): C=addlog(C,-p,Q[A])
    sharp=addlog(B,v,Z)
    ck(C[1]<sharp[0]); ck(C[1]<B[0])
    ln2=logi(F(2))
    ck(B[1]<32*I*ln2[0])
    # Independent complete actual-anchor enumeration and union/occupation DP.
    t=F(1,1<<(w+1)); rho=r*t
    local=[{s:(1-t if not s else t*t/(1-t)) for s in op} for op in opts]
    direct={}; events=0
    for z in tuples:
        A=0; mu=F(1)
        for j,s in enumerate(z): A|=s; mu*=local[j][s]
        for anchor,s in enumerate(z):
            if s:
                direct[A]=direct.get(A,F(0))+mu/rho; events+=1
    arr={0:(F(1),F(0))}
    for loc in local:
        nxt={}
        for A,(u,k0) in arr.items():
            for s,m in loc.items():
                B0=A|s; u0,k1=nxt.get(B0,(F(0),F(0)))
                nxt[B0]=(u0+u*m,k1+(k0+bool(s)*u)*m)
        arr=nxt
    for A in range(1,1<<n): ck(direct[A]==arr[A][1]/rho)
    ck(sum(direct.values(),F(0))==1)
    return dict(r=r,w=w,truth_inputs=1<<n,allocation_tuples=len(tuples),actual_anchor_events=events,
                I=str(I),v=str(v),M=list(map(str,M)),alpha=str(alpha),shared_price=str(price),
                certified_B_bits_over_I_upper=str(B[1]/(ln2[0]*I)),Q_core=str(Q[1]))

def review(widths):
    blocks=[]; k=0
    for w in widths*2:
        blocks.append(((1<<w)-1)<<k); k+=w
    cut=sum(widths); n=k; r=len(widths)
    def u(x,offset,neg=False):
        pos=offset
        for w in widths:
            bits=(x>>pos)&((1<<w)-1)
            if neg: bits^=(1<<w)-1
            if not bits: return 0
            pos+=w
        return 1
    vals=[2*u(x,0)*(1-u(x,cut,True))-1 for x in range(1<<n)]
    P,I=spectrum(vals,n); ts=[F(1,1<<w) for w in widths]; q=F(1)
    for t in ts:q*=1-t
    ck(I==2*q*sum((w*t/(1-t) for w,t in zip(widths,ts)),F(0)))
    rho=2*sum(ts,F(0)); Q={}; events=0
    for z in product(*(masks(E) for E in blocks)):
        mu=F(1); A=0
        for j,s in enumerate(z):
            t=ts[j%r]; mu*=1-t if not s else t*t/(1-t); A|=s
        for anchor,s in enumerate(z):
            if s: Q[A]=Q.get(A,F(0))+mu/rho; events+=1
    ck(sum(Q.values(),F(0))==1)
    C=(F(0),F(0))
    for A,p in P.items():C=addlog(C,-p,Q[A])
    ck(C[1]<F(155,24)*I*logi(F(2))[0])
    for j,E in enumerate(blocks):
        mom=sum((p for A,p in P.items() if A&E),F(0))
        expected=4*q*(1-q if j<r else q)*ts[j%r]
        ck(mom==expected)
    return dict(widths=widths,truth_inputs=1<<n,actual_anchor_events=events,I=str(I))

def main():
    start=time.perf_counter(); pilot='--pilot' in sys.argv
    rows=[fixture(*p) for p in ([(2,1)] if pilot else [(2,1),(2,2),(3,1),(3,2)])]
    rr=[review(ws) for ws in ([(1,)] if pilot else [(1,),(2,),(1,2),(2,2),(1,1,1)])]
    for w in range(8,129):
        e=F(1,1<<w); jbound=F(w*w,1<<w)/(1-e)
        ck(jbound<=F(64,255)); ck(jbound<1); ck((1-e)**2>F(1,2))
        ck((1<<(w+1))-1>(1<<w)); ck(F((w+1)**2,1<<(w+1))<F(w*w,1<<w))
    elapsed=time.perf_counter()-start; ck(elapsed<55)
    result=dict(status='PASS',mode='pilot' if pilot else 'main',assertions=COUNT,elapsed_seconds=elapsed,
                fixtures=rows,source_review=rr,obstruction_scalar_parameters=121,
                interval_method='40-term exact rational atanh series and proved geometric remainder; no floating sign tests')
    (ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','mode','assertions','elapsed_seconds')}),flush=True)

if __name__=='__main__':main()
