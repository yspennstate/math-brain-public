"""Direct characters and independent three-component reference construction."""
from pathlib import Path
from fractions import Fraction as F
import time,json
import helper as loglib
R=Path(__file__).resolve().parents[1];start=time.perf_counter();count=0
spec={'helper_version':'A026-independent-dummy-v1','domain':'same48 frozen roots plus24 r=1 boundary roots; direct character spectra, independent mixture construction; local dummy reset only','case_count':72,'symmetry':'no quotient; first dummy label','arithmetic':'integer characters, Fraction, shared rational log interval routine only','memory_estimate_mb':70,'max_runtime_seconds':55}
(R/'INDEPENDENT_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
def ck(x):
 global count
 assert x,count;count+=1
 assert time.perf_counter()-start<55
def fourier(v):return tuple(F(sum(z*(-1 if (x&T).bit_count()%2 else 1) for x,z in enumerate(v)),len(v)) for T in range(len(v)))
def marg(p,j):
 out=[F(0)]*(len(p)//2)
 for x,z in enumerate(p):out[(x&((1<<j)-1))|((x>>(j+1))<<j)]+=z
 return tuple(out)
def restrict(v,j,b):return tuple(z for x,z in enumerate(v) if ((x>>j)&1)==b)
def pg(a,b):
 n=a+b;s=F(1,1<<a);mu=1-2*s
 return tuple(mu*mu if T==0 else 4*s*s if T<(1<<a) else F(0) for T in range(1<<n))
def cal(raw,P):return (P[0],)+tuple((1-P[0])*q/(1-raw[0]) for q in raw[1:])
def build(a,b,r,Rt):
 n=a+b;N=1<<n;s=F(1,1<<a);e=F(2,1<<(n+r));mu=1-2*s;hh=e/s
 vals=tuple(1-2*int(x&((1<<a)-1)==0)+2*int(x==0) for x in range(1<<(n+r)))
 w=fourier(vals);P=tuple(x*x for x in w)
 Psrc=pg(a,b)
 M=tuple(sum(P[T+U*N] for U in range(1<<r)) for T in range(N))
 truth=tuple((1-hh)*Psrc[T]+hh*mu*int(T==0)+2*e/N for T in range(N))
 ref=tuple((1-hh)*Rt[T]+hh*mu*int(T==0)+2*e/N for T in range(N))
 ck(M==truth);ck(sum(ref)==sum(P)==1)
 Q=tuple(ref[x%N]*p/M[x%N] for x,p in enumerate(P));ck(sum(Q)==1);ck(min(Q)>0)
 return vals,P,Q
rows=[];flat_boundaries=0
for a in [1,2,3]:
 for b in [1,2]:
  for r in [1,2,3]:
   source=pg(a,b);N=len(source)
   for mode in ['matching','uniform','increasing','dummy-singleton-spiked']:
    raw=source if mode=='matching' else (F(1,N),)*N if mode=='uniform' else tuple(F(2*(i+1),N*(N+1)) for i in range(N)) if mode=='increasing' else tuple(F(1000 if i==(1<<a) else 1,1000+N-1) for i in range(N))
    Rt=cal(raw,source);v,P,Q=build(a,b,r,Rt);j=a;old=marg(Q,j)
    on=restrict(v,j,0);off=restrict(v,j,1);Poff=tuple(x*x for x in fourier(off))
    Rm=marg(Rt,j);Rn=cal(Rm,pg(a,b-1));vn,Pn,Qn=build(a,b-1,r,Rn)
    ck(vn==on);ck(len(set(on))==len(set(off))==2)
    if r>=2:ck(len(set(Qn))>1)
    elif len(set(Qn))==1:flat_boundaries+=1
    e=F(2,1<<(a+b+r));s=F(1,1<<a);t=F(1,1<<(a+b));hh=e/s
    for S,z in enumerate(pg(a,b-1)):
     if not z:continue
     T=(S&((1<<j)-1))|((S>>j)<<(j+1))
     if S:
      k=(2*s-e)**2/(4*s*s-4*s*e+2*e*t)
      ck(old[S]>=Rt[T]*(1-hh)*k);ck(1/k<=1+hh)
     else:ck(old[0]>=Rt[0])
    c=loglib.CE(source,Rt);offcost=loglib.CE(Poff,old)
    ck(loglib.sub(offcost,c)[1]<14*e)
    B=loglib.sub(loglib.CE(P,P),loglib.CE(marg(P,j),marg(P,j)))
    ck(B[1]<12*e)
    cn=loglib.CE(pg(a,b-1),Rn)
    local=loglib.add(B,loglib.mul(F(1,2),offcost),loglib.mul(F(1,2),loglib.add(cn,(20*e*(a+b+r-1),)*2)))
    W=loglib.add(c,(10*e*(a+b+r),)*2);ck(loglib.sub(local,W)[1]<9*e)
    rows.append({'a':a,'b':b,'r':r,'reference':mode})
    loglib.log.cache_clear()
# Exact discrete ancestor-reserve induction increments, including excluded boundaries.
for a in [1,2,3]:
 for b in range(7):
  for r in range(2,9):
   ck(5*a*(1<<(b+r))-8*(r-1)-9*b>=12)
   ck(5*a*(1<<(b+r))-9>0);ck(5*a*(1<<(b+r))-8>0)
ck(5*4-8==12)
out={'status':'PASS','flat_boundary_count':flat_boundaries,'roots':len(rows),'assertions':count,'seconds':time.perf_counter()-start,'representation':'direct characters and independent convex-mixture source/reference construction; only log interval primitive shared','boundary_scope':'b=0 has no dummy coordinate; r=1 dummy resets included; last control query r=1 excluded'}
(R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
