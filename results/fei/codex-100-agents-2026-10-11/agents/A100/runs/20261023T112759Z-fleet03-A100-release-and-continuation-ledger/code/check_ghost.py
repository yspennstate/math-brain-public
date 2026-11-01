from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json,sys,time
R=Path(__file__).resolve().parents[1];O=R/'out';assert (O/'FROZEN_SPEC.json').exists();start=time.perf_counter();pilot='--pilot' in sys.argv;checks=0

def ck(v):
 global checks
 checks+=1
 assert v,checks
 assert time.perf_counter()-start<55,'frozen 55s guard'

def fft(v):
 a=list(v);h=1
 while h<len(a):
  for i in range(0,len(a),h*2):
   for j in range(i,i+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return tuple(F(x,len(a)) for x in a)
def direct(v):return tuple(F(sum(z*(-1 if (x&s).bit_count()%2 else 1) for x,z in enumerate(v)),len(v)) for s in range(len(v)))
@lru_cache(None)
def spectrum(v):
 a=fft(v);p=tuple(x*x for x in a);ck(sum(p)==1);return p
@lru_cache(None)
def factors(n):
 out=[];p=2
 while p*p<=n:
  count=0
  while n%p==0:n//=p;count+=1
  if count:out.append((p,count))
  p=3 if p==2 else p+2
 if n>1:out.append((n,1))
 return tuple(out)
@lru_cache(None)
def logform(x):
 assert x>0
 d=dict(factors(x.numerator))
 for p,k in factors(x.denominator):d[p]=d.get(p,0)-k
 return tuple((p,F(k)) for p,k in d.items() if k)
def linear(*terms):
 d={}
 for scale,form in terms:
  for p,k in form:d[p]=d.get(p,F(0))+scale*k
 return tuple(sorted((p,k) for p,k in d.items() if k))
def ce(p,q):
 terms=[]
 for x,y in zip(p,q):
  if x:ck(y>0);terms.append((-x,logform(y)))
 return linear(*terms)
def ins(x,j,b):return x%2**j+(x//2**j)*2**(j+1)+b*2**j
def children(v,j):return [tuple(v[ins(x,j,b)] for x in range(len(v)//2)) for b in (0,1)]
def marginal(v,j):return tuple(v[ins(x,j,0)]+v[ins(x,j,1)] for x in range(len(v)//2))
def erasure(p,j):
 terms=[]
 for x in range(len(p)//2):
  p0,p1=p[ins(x,j,0)],p[ins(x,j,1)];w=p0+p1
  for y in [p0,p1]:
   if y:terms.append((y,logform(w/y)))
 return linear(*terms)
def dstar(p,q,j):
 terms=[]
 for x in range(1,len(p)//2):
  ps=[p[ins(x,j,b)] for b in (0,1)];qs=[q[ins(x,j,b)] for b in (0,1)];w=sum(ps);v=sum(qs)
  for a,b in zip(ps,qs):
   if a:ck(v>0 and b>0);terms.append((a,logform(a*v/(w*b))))
 return linear(*terms)
@lru_cache(None)
def controller(a):
 b=tuple(1-v*v for v in a);return b,fft(a),fft(b),F(sum(b),len(b))
@lru_cache(None)
def wrapper(a,h,sigma):
 b,_,_,_=controller(a);return tuple(a[x]+sigma*b[x]*h[y] for y in range(len(h)) for x in range(len(a)))
def reference(a,h,sigma,q):
 b,A,B,beta=controller(a);m=F(sum(h),len(h));out=tuple((A[u]+sigma*m*B[u])**2 if v==0 else B[u]**2*q[v] for v in range(len(h)) for u in range(len(a)));ck(sum(out)==1);return out
ctrl=[tuple(x) for x in product([-1,0,1],repeat=2)]+[(-1,0,1,0),(0,0,0,0),(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1)]
parity=tuple((-1)**x.bit_count() for x in range(8));biased=tuple(-1 if x//2==0 else 1 for x in range(8));noniso=tuple((-1 if x&4 else 1)*(-1 if x%4==0 else 1) for x in range(8));const=(1,)*8
seeds=[tuple(1 if mask>>i&1 else -1 for i in range(4)) for mask in range(16)]+[parity,biased,noniso,const]
if pilot:ctrl=ctrl[:3];seeds=[parity]
cases=mixtures=genuine=zero_tail=zero_beta=0;records=[]
for a in ctrl:
 b,A,B,beta=controller(a);k=len(a).bit_length()-1
 ck(A==direct(a) and B==direct(b))
 for h in seeds:
  hs=fft(h);ck(hs==direct(h));p=spectrum(h);r=p[0];t=1-r
  for j in range(len(h).bit_length()-1):
   if hs[1<<j]:continue
   hc=children(h,j);pcs=[spectrum(z) for z in hc];ck(all(F(sum(z),len(z))**2==r for z in hc));ck(tuple((u+v)/2 for u,v in zip(*pcs))==marginal(p,j))
   refs=[]
   refs.append(p)
   refs.append(tuple(r if v==0 else F(7,8)*p[v]+(t/8 if v==(1<<j) else 0) for v in range(len(h))))
   refs.append(tuple(r if v==0 else F(3,4)*p[v]+t/F(4*(len(h)-1)) for v in range(len(h))))
   for sigma in (-1,1):
    G=wrapper(a,h,sigma);PG=spectrum(G);eg=erasure(PG,k+j);ck(eg==linear((beta,erasure(p,j))))
    for q in refs:
     cases+=1;rho=q[1<<j];theta=rho/t if t else F(0);ck(sum(q)==1 and q[0]==r);ck(not t or theta<1)
     qm=marginal(q,j)
     cal=tuple(r if v==0 else t*qm[v]/(t-rho) for v in range(len(qm))) if t else (F(1),)+(F(0),)*(len(qm)-1)
     ck(sum(cal)==1);Q=reference(a,h,sigma,q);QC=[reference(a,z,sigma,cal) for z in hc];PC=[spectrum(wrapper(a,z,sigma)) for z in hc]
     lhs=linear((1,eg),(F(1,2),ce(PC[0],QC[0])),(F(1,2),ce(PC[1],QC[1])),(-1,ce(PG,Q)))
     ds=dstar(p,q,j);rhs=linear((-beta,ds),(beta*t,logform(1-theta)))
     ck(lhs==rhs)
     # Reverse injection: remove current singleton ghost, then scale its old tail back to t.
     base=tuple(r if v==0 else (F(0) if v==(1<<j) else t*q[v]/(t-rho)) for v in range(len(q))) if t else q
     QB=reference(a,h,sigma,base);injection=linear((1,ce(PG,Q)),(-1,ce(PG,QB)))
     ck(injection==linear((-beta*t,logform(1-theta))))
     if not t:zero_tail+=1;continue
     if not beta:zero_beta+=1
     tail=[v/t for v in cal[1:]]
     for target in [[F(1)]+[F(0)]*(len(tail)-1),[F(1,len(tail))]*len(tail)]:
      for lam in [F(0),theta/2,theta]:
       new=(r,)+tuple(t*((1-lam)*v+lam*z) for v,z in zip(tail,target));ck(sum(new)==1)
       ck(all(new[v]>=(1-lam)*cal[v] for v in range(1,len(cal))));ck(1-lam>=1-theta)
       # Both outcomes retain their actual means/support and full controller-vacuum atoms.
       for hb in hc:
        QQ=reference(a,hb,sigma,new);PP=spectrum(wrapper(a,hb,sigma));ck(all(y>0 for x,y in zip(PP,QQ) if x))
       mixtures+=1
       if lam and tuple(new)!=tuple(cal):genuine+=1
# Sharp Boolean boundary, full wrapper and both complete terminal references.
sharp=[];a=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1);beta=controller(a)[3];ck(beta==F(3,8));h=parity;p=spectrum(h);j=0;hc=children(h,j);ck(all(fft(h)[1<<j]==0 for _ in [0]));ck(all(fft(h)[2*v]*fft(h)[2*v+1]==0 for v in range(4)))
for rho in [F(0),F(1,128),F(1,32),F(1,2)]:
 for lam in [F(0),F(1,64),F(1,32),F(1,2)]:
  q=tuple((1-rho)*p[v]+(rho if v==1 else 0) for v in range(8));qnew=(F(0),lam,F(0),1-lam)
  G=wrapper(a,h,1);Q=reference(a,h,1,q);lhs=linear((1,erasure(spectrum(G),4)),(-1,ce(spectrum(G),Q)),*[(F(1,2),ce(spectrum(wrapper(a,z,1)),reference(a,z,1,qnew))) for z in hc]);rat=(1-rho)/(1-lam)
  ck(lhs==linear((beta,logform(rat))));ck((rat<=1)==(lam<=rho));sharp.append({'rho':str(rho),'lambda':str(lam),'ratio':str(rat),'sign':'positive' if rat>1 else 'negative' if rat<1 else 'zero','both_children_nonconstant':all(min(z)!=max(z) for z in hc)})
if not pilot:ck(cases==1512)
result={'status':'PASS','pilot':pilot,'exact_assertions':checks,'transactions':cases,'mixture_floor_cases':mixtures,'genuine_changed_profile_cases':genuine,'constant_seed_transactions':zero_tail,'beta0_transactions':zero_beta,'sharp_cases':sharp,'runtime_seconds':round(time.perf_counter()-start,6),'arithmetic':'Exact prime-log linear normal forms over Fraction; integer Walsh plus direct characters; no approximate logarithms','scope':'Finite validation accompanies independently reconstructed all-parameter proof; source reference price supplied, not proved','independence':'No author code imported'}
(O/('PILOT_GHOST_REVIEW.json' if pilot else 'GHOST_REVIEW.json')).write_bytes((json.dumps(result,indent=2)+'\n').encode());print(json.dumps({k:v for k,v in result.items() if k!='sharp_cases'},indent=2))
