from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
import json,time,argparse
RUN=Path(__file__).resolve().parent.parent
SCALE=1<<50
def ln1(y):
    z=(y-1)/(y+1); total=F(0); power=z
    for j in range(18):
        total+=2*power/F(2*j+1); power*=z*z
    rem=2*power/(37*(1-z*z))
    return total,total+rem
L2=ln1(F(2))
@lru_cache(None)
def ln(x):
    x=F(x); k=0
    while x<1: x*=2; k-=1
    while x>=2: x/=2; k+=1
    lo,hi=ln1(x)
    if k>=0: return lo+k*L2[0],hi+k*L2[1]
    return lo+k*L2[1],hi+k*L2[0]
@lru_cache(None)
def lg(x):
    a,b=ln(F(x)); vals=[a/L2[0],a/L2[1],b/L2[0],b/L2[1]]
    return min(vals),max(vals)
def floor(x): return x.numerator//x.denominator
def ceil(x): return -((-x.numerator)//x.denominator)
@lru_cache(None)
def entropy2(u,N):
    if not u:return 0,0
    a,b=lg(F(N*N,u))
    return floor(u*a*SCALE),ceil(u*b*SCALE)
@lru_cache(None)
def psi(u,v):
    if not u or not v: return 0,0
    a,b=lg(F(u+v,u));c,d=lg(F(u+v,v))
    return floor((u*a+v*c)*SCALE),ceil((u*b+v*d)*SCALE)
def fwht(a):
    a=list(a); step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for k in range(j,j+step):
                u,v=a[k],a[k+step];a[k],a[k+step]=u+v,u-v
        step*=2
    return a
def run(ns,label,cap):
    start=time.perf_counter();counts=0;checks=0;best=(0,1);witness=None
    # Constant comparison is itself a rational certificate.
    e0=F(27,10);l0=F(69,100);s0=F(71,50)
    K2=8/(e0*e0*l0)+2/e0+s0/(e0*l0)
    K12=2*K2+1/l0
    assert K12<8 and F(163,60)>e0 and F(56,81)>l0 and s0*s0>2
    checks+=4
    # Regression checks for the signed logarithm interval kernel.
    for k in range(-8,9):
        a,b=lg(F(2)**k);assert a<=k<=b;checks+=1
    for n in ns:
        N=1<<n
        pairs=[(i,j,(1<<i)|(1<<j)) for i in range(n) for j in range(i+1,n)]
        for mask in range(1<<N):
            table=[1 if (mask>>x)&1 else -1 for x in range(N)]
            w=fwht(table);u=[v*v for v in w]
            assert sum(u)==N*N;checks+=1
            epsnum=[sum(table[x]!=table[x^(1<<i)] for x in range(N)) for i in range(n)]
            for i in range(n):
                infnum=sum(u[s] for s in range(N) if (s>>i)&1)
                assert infnum==epsnum[i]*N;checks+=1
                # Support of Boolean derivative equals the physical flip event.
                support=sum(table[x]!=table[x|(1<<i)] for x in range(N) if not ((x>>i)&1))
                assert 2*support==epsnum[i];checks+=1
                di=sum(u[(1<<i)|(1<<j)] for j in range(n) if j!=i)
                if not epsnum[i]:assert di==0
                else:
                    low,_=ln(F(2*N,epsnum[i]))
                    assert F(di)<=2*epsnum[i]*epsnum[i]*low
                checks+=1
            I=sum(epsnum)*N
            hlo=hhi=tlo=thi=0
            for i,j,s in pairs:
                l,h=entropy2(u[s],N);hlo+=l;hhi+=h
                for b in [1<<i,1<<j]:
                    l,h=psi(u[b],u[s]);tlo+=l;thi+=h
            if I:
                assert hhi*K2.denominator<=K2.numerator*I*SCALE;checks+=1
                assert thi<8*I*SCALE;checks+=1
                assert thi*K12.denominator<=K12.numerator*I*SCALE;checks+=1
                if thi*best[1]>best[0]*I:
                    best=(thi,I);witness={'n':n,'mask':mask,'walsh':w,'I':str(F(I,N*N)),'T12_lower':str(F(tlo,N*N*SCALE)),'T12_upper':str(F(thi,N*N*SCALE))}
            else:assert hhi==thi==0;checks+=1
            counts+=1
            if counts%1024==0 and time.perf_counter()-start>cap:raise RuntimeError('Frozen runtime cap exceeded')
    result={'status':'PASS','label':label,'n':ns,'cases':counts,'assertions_passed':checks,'runtime_seconds':time.perf_counter()-start,'K2_rational_upper':str(K2),'K12_rational_upper':str(K12),'max_T12_over_I_upper':str(F(best[0],best[1]*SCALE)),'extremal_observed_witness':witness,'arithmetic':'Exact integers and outward rational logarithm certificates','proof_scope':'Finite validation; universal theorem is analytic in DERIVATION.md'}
    (RUN/'out').mkdir(exist_ok=True)
    (RUN/'out'/f'{label}.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['pilot','full'],required=True);args=ap.parse_args()
    run([0,1,2,3] if args.mode=='pilot' else [4],args.mode.upper(),60 if args.mode=='pilot' else 180)
