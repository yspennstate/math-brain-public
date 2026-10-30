from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,sys,time,hashlib
RUN=Path(__file__).resolve().parents[1];OUT=RUN/'out';pilot='--pilot' in sys.argv
start=time.perf_counter();assertions=0
def chk(v):
 global assertions
 assertions+=1
 assert v,assertions
 assert time.perf_counter()-start<55,'frozen 55s cap'
BITS=100;S=1<<BITS
def ceildiv(a,b):return -((-a)//b)
def ln_mantissa(x):
 # Integer intervals in units 2^-100; every rounding is outward.
 assert 1<=x<=2
 z=(x-1)/(x+1);lo=z.numerator*S//z.denominator;hi=ceildiv(z.numerator*S,z.denominator)
 z2lo=lo*lo//S;z2hi=ceildiv(hi*hi,S);pl,ph=lo,hi;sl=sh=0
 for k in range(24):
  sl+=2*pl//(2*k+1);sh+=ceildiv(2*ph,2*k+1)
  pl=pl*z2lo//S;ph=ceildiv(ph*z2hi,S)
 # z<=1/3 gives remainder <=9/[4*49*3^49].
 sh+=ceildiv(9*S,4*49*3**49)
 return sl,sh
L2,U2=ln_mantissa(F(2));assert 0<L2<=U2
@lru_cache(maxsize=20000)
def log2(x):
 assert x>0
 k=x.numerator.bit_length()-x.denominator.bit_length();mant=x/(F(2)**k)
 if mant<1:k-=1;mant*=2
 a,b=ln_mantissa(mant)
 return k*S+a*S//U2,k*S+ceildiv(b*S,L2)
def ce(p,q):
 lo=hi=F(0)
 for x,y in zip(p,q):
  if x:
   chk(y>0);a,b=log2(y);lo-=x*b;hi-=x*a
 return lo/S,hi/S
def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,t):return a[0]*t,a[1]*t
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def fft(f):
 a=list(f);h=1
 while h<len(a):
  for k in range(0,len(a),2*h):
   for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
def direct(f):return [sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(f)) for s in range(len(f))]
def spectrum(f,independent=False):
 w=fft(f)
 if independent:chk(w==direct(f))
 p=[F(x*x,len(f)**2) for x in w];chk(sum(p)==1);return p
def influence(f):
 n=len(f).bit_length()-1
 return sum(F(sum(f[x]!=f[x^(1<<j)] for x in range(len(f))),len(f)) for j in range(n))
def source(t,narrow,m):
 n=t+narrow+m;wm=(1<<t)-1;hm=((1<<narrow)-1)<<t
 return [(1 if x&wm else -1)*(1 if x&hm else -1) for x in range(1<<n)]
def model(t,narrow,m):
 g=source(t,narrow,m);f=g+g[:];f[len(g)]*=-1
 pg=spectrum(g);eps=F(1,len(g));support=[i for i,x in enumerate(pg) if x];W=2*eps-len(support)*eps*eps
 Q=[(1-W)*pg[i] if i<len(g) and pg[i] else eps*eps for i in range(len(f))]
 chk(sum(Q)==1);chk(all(q>0 for p,q in zip(spectrum(f),Q) if p));return f,Q,g
def insert(x,j,b):return (x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)
def query(f,Q,j):
 p=spectrum(f);N=len(f)//2;fs=[[f[insert(x,j,b)] for x in range(N)] for b in [0,1]];ps=[spectrum(g) for g in fs]
 pm=[p[insert(x,j,0)]+p[insert(x,j,1)] for x in range(N)];qm=[Q[insert(x,j,0)]+Q[insert(x,j,1)] for x in range(N)]
 chk(pm==[(x+y)/2 for x,y in zip(*ps)])
 raw=[[qm[x]*ps[b][x]/pm[x] if pm[x] else qm[x] for x in range(N)] for b in [0,1]]
 Z=[sum(x) for x in raw];chk(Z[0]>0 and Z[1]>0 and sum(Z)==2)
 qs=[[v/Z[b] for v in raw[b]] for b in [0,1]]
 for b in [0,1]:chk(sum(qs[b])==1);chk(all(q>0 for p,q in zip(ps[b],qs[b]) if p))
 return fs,ps,qs,Z
def show(a):
 k=1<<65
 return [str(F((a[0]*k).numerator//(a[0]*k).denominator,k)),str(F(ceildiv((a[1]*k).numerator,(a[1]*k).denominator),k))]
roots=[(4,0)] if pilot else [(4,0),(4,1),(5,0)]
records=[];positive=negative=0;rootdata=[]
for w,m in roots:
 f,Q,g=model(w,2,m);P=spectrum(f,True);Ig=influence(f);rootCE=ce(P,Q);delta=F(1,len(g));q=F(1,1<<(w-1))
 chk(Ig==1+w*q+delta*(m-w-1));chk(4*Ig-rootCE[1]>F(395,256))
 rootdata.append({'w':w,'m':m,'I':str(Ig),'root_CE':show(rootCE),'unused_reserve_lower':str(4*Ig-rootCE[1])})
 currentf,currentq=f,Q;old_off=(F(0),F(0));rho=F(1)
 for d in range(w+1):
  t=w-d;curP=spectrum(currentf);curCE=ce(curP,currentq)
  before=add(old_off,scale(curCE,rho));prior_release=sub(rootCE,before)
  chk(prior_release[1]>=0)
  fs,ps,qs,Z=query(currentf,currentq,t)
  oldchild=[ce(ps[b],qs[b]) for b in [0,1]]
  query_release=sub(curCE,scale(add(*oldchild),F(1,2)))
  chk(query_release[1]>=0)
  # Exact algebra gives old release+old terminal=rootCE; replacing one terminal adds only this reached difference.
  freshf,can,_=model(t,1,m);chk(fs[0]==freshf)
  if d<w:chk(min(fs[0])!=max(fs[0]) and min(fs[1])!=max(fs[1]))
  if not pilot or d in [0,w]:
   for eta in [F(0),F(1,8),F(1,4)]:
    fresh=[(1-eta)*x+eta/len(can) for x in can];chk(sum(fresh)==1);chk(min(fresh)>0)
    cost=ce(ps[0],fresh);lam=rho/2;charge=scale(cost,lam)
    chk(charge[1]<F(5,4))
    if eta==0:chk(charge[1]<1)
    excess=scale(sub(cost,oldchild[0]),lam)
    total=add(rootCE,excess);chk(total[1]<4*Ig-F(75,256))
    if eta==0:chk(total[1]<4*Ig-F(139,256))
    if excess[0]>0:positive+=1
    elif excess[1]<0:negative+=1
    # Direct reconstruction of complete old releases and both post-reset terminal costs.
    release=add(prior_release,scale(query_release,rho))
    after=add(old_off,scale(add(cost,oldchild[1]),lam))
    reconstructed=add(release,after)
    chk(max(reconstructed[0],total[0])<=min(reconstructed[1],total[1]))
    records.append({'w':w,'m':m,'d':d,'eta':str(eta),'lambda':str(lam),'child_normalizers':[str(x) for x in Z],'fresh_cost':show(cost),'reached_fresh_cost':show(charge),'signed_excess':show(excess),'whole_ledger':show(total),'remaining_quota_lower':str(4*Ig-total[1])})
  if d<w:
   fs0,ps0,qs0,_=query(currentf,currentq,0)
   old_off=add(old_off,scale(ce(ps0[1],qs0[1]),rho/2));currentf,currentq=fs0[0],qs0[0];rho/=2
# Independent scalar all-boundary checks support the analytic inductions without extrapolation.
for m in range(13):chk(16*m+17<=17*2**m)
result={'status':'PASS','pilot':pilot,'arithmetic':'Integer Walsh and independent direct characters; physical edges; Fraction references; outward100-bit integer log intervals,24 terms and proved tail','exact_assertions':assertions,'roots':rootdata,'reset_cases':len(records),'positive_signed_excess_cases':positive,'negative_signed_excess_cases':negative,'cases':records,'runtime_seconds':round(time.perf_counter()-start,6),'rung':'Independent analytic all-parameter reconstruction plus exact finite checks; not Lean-certified','hypothesis_guard':'Only one prescribed narrow reset after wide-only history; no renewed descendant account; arbitrary-core and repeated reset excluded'}
(OUT/('PILOT_NARROW_REVIEW.json' if pilot else 'NARROW_REVIEW.json')).write_bytes((json.dumps(result,indent=2)+'\n').encode())
print(json.dumps({k:v for k,v in result.items() if k not in ['cases','roots']},indent=2))
