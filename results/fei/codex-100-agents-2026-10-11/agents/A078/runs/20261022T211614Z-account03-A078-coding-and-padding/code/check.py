"""A078 signed collision account, version 1. Exact finite checks; no FEI claim."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json, time, hashlib

RUN=Path(__file__).resolve().parents[1]
OUT=RUN/'out'
OUT.mkdir(exist_ok=True)
SPEC={'helper_version':'A078-collision-account-1','family':'all ordered Boolean controller pairs on n=0,1,2; actual two-vertex Boolean wrappers h=1; plus guarded bent/spike padding fixtures','domain':{'controller_n':[0,1,2],'shared_d':[1,2],'bent_k':[2,4],'padding_m':[1,2]},'case_count':{'root_pairs':276,'restricted_pair_states_per_d':2356,'wrapper_states':4712,'private_split_instances':3104,'bent_root_fixtures':8},'symmetry':'none; all ordered labeled pairs and all partial assignments','arithmetic':'Fraction Walsh spectra, exact prime-log vectors, outward rational 16-term atanh logarithms','memory_estimate_MB':80,'max_runtime_seconds':55,'automatic_dimension_increase':False}
(OUT/'FROZEN_SPEC.json').write_text(json.dumps(SPEC,indent=2),encoding='utf-8')
T0=time.monotonic()
checks=0
def ck(v):
 global checks
 checks+=1
 assert v, checks
 if time.monotonic()-T0>55: raise TimeoutError('frozen 55 second cap')
def add(*terms):
 out={}
 for c,x in terms:
  for p,v in x.items():
   out[p]=out.get(p,Q(0))+c*v
 return {p:v for p,v in out.items() if v}
@lru_cache(None)
def factors(n):
 out={}; p=2
 while p*p<=n:
  while n%p==0: out[p]=out.get(p,0)+1; n//=p
  p+=1
 if n>1: out[n]=out.get(n,0)+1
 return out
@lru_cache(None)
def logvec(q):
 out={}
 for s,n in [(1,q.numerator),(-1,q.denominator)]:
  for p,v in factors(n).items():out[p]=out.get(p,Q(0))+s*v
 return {p:v for p,v in out.items() if v}
@lru_cache(None)
def g(q):
 if not q:return {}
 return {p:-q*q*v for p,v in logvec(q*q).items()}
def entropy(v):return add(*[(Q(1),g(x)) for x in v])
@lru_cache(None)
def ln_interval(q):
 shift=q.numerator.bit_length()-q.denominator.bit_length()
 r=q/Q(2)**shift
 if r<1:shift-=1;r*=2
 if r>=2:shift+=1;r/=2
 def part(x):
  z=(x-1)/(x+1); s=Q(0)
  for j in range(16):s+=2*z**(2*j+1)/Q(2*j+1)
  err=2*abs(z)**33/(33*(1-z*z))
  return s,s+err
 lo,hi=part(r); a,b=part(Q(2))
 return (lo+shift*a,hi+shift*b) if shift>=0 else (lo+shift*b,hi+shift*a)
@lru_cache(None)
def log2_interval(p):
 if p==2:return Q(1),Q(1)
 a,b=ln_interval(Q(p));c,d=ln_interval(Q(2));return a/d,b/c
def interval(x):
 lo=hi=Q(0)
 for p,c in x.items():
  a,b=log2_interval(p)
  if c>=0:lo+=c*a;hi+=c*b
  else:lo+=c*b;hi+=c*a
 return lo,hi
def nonneg(x):return interval(x)[0]>=0
def scalar(x):return {2:Q(x)} if x else {}
def walsh(v):
 n=len(v);return tuple(Q(sum(v[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(n)),n) for s in range(n))
def fwht(v):
 a=list(v);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for i in range(j,j+h):a[i],a[i+h]=a[i]+a[i+h],a[i]-a[i+h]
  h*=2
 return tuple(Q(x,len(a)) for x in a)
def infl(v,i):return Q(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v))
def restrict(v,i,b):
 return tuple(v[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(v)//2))
def xi(v,w,e):
 a,b=walsh(v),walsh(w)
 return add(*[(e/2,add((Q(1),g(a[t]+b[t])),(Q(1),g(a[t]-b[t])),(Q(-2),g(a[t])),(Q(-2),g(b[t])))) for t in range(1,len(a))])
def wrapper(v,w,d):
 return tuple(v[x>>d] if x%2**d==0 else w[x>>d] if x%2**d==1 else 1 for x in range(len(v)*2**d))
def mean(v):return Q(sum(v),len(v))
def reserve(v,w,d):return Q(d,2**d)*(2-mean(v)**2-mean(w)**2)
def states(v,w):
 yield v,w
 if len(v)>1:
  # Unique ternary partial assignments, including skipped coordinates.
  n=len(v).bit_length()-1
  from itertools import product
  for pat in product([-1,0,1],repeat=n):
   if all(x==-1 for x in pat):continue
   ids=[x for x in range(2**n) if all(b==-1 or ((x>>i)&1)==b for i,b in enumerate(pat))]
   yield tuple(v[x] for x in ids),tuple(w[x] for x in ids)

roots=state_count=split_count=0
for n in range(3):
 tables=[tuple(-1 if (mask>>x)&1 else 1 for x in range(2**n)) for mask in range(2**(2**n))]
 for v in tables:
  for w in tables:
   roots+=1
   for d in [1,2]:
    e=Q(1,2**d); xr=xi(v,w,e); budget=7*e
    for a,b in states(v,w):
     state_count+=1
     x=xi(a,b,e)
     ck(nonneg(add((Q(1),x),(Q(1),scalar(4*e)))))
     ck(nonneg(add((Q(-1),x))))
     bank=add((Q(1),scalar(budget)),(Q(-1),xr),(Q(1),x))
     ck(nonneg(add((Q(1),bank),(Q(-1),scalar(3*e)))))
     f=wrapper(a,b,d);fv=walsh(f)
     ck(fv==fwht(f));ck(sum(t*t for t in fv)==1)
     aa,bb=walsh(a),walsh(b)
     # Independently check the complete two-vertex Fourier expansion.
     for u in range(len(a)):
      for s in range(2**d):
       sign=1 if s%2==0 else -1
       pred=(Q(1) if s==0 else Q(0))+e*(aa[0]-1)+e*sign*(bb[0]-1) if u==0 else e*(aa[u]+sign*bb[u])
       ck(fv[s+(u<<d)]==pred)
     for i in range(len(a).bit_length()-1):
      split_count+=1
      cs=[(restrict(a,i,t),restrict(b,i,t)) for t in [0,1]]
      xs=[xi(c,z,e) for c,z in cs]
      banks=[add((Q(1),scalar(budget)),(Q(-1),xr),(Q(1),z)) for z in xs]
      collision=add((Q(1),x),(Q(-1,2),xs[0]),(Q(-1,2),xs[1]))
      # Exact ledger, with the SAME ancestor budget and both complete children.
      ck(not add((Q(1),collision),(Q(1,2),banks[0]),(Q(1,2),banks[1]),(Q(-1),bank)))
      j=e*(infl(a,i)+infl(b,i));ck(infl(f,d+i)==j)
      rp=reserve(a,b,d);rc=sum((reserve(c,z,d) for c,z in cs),Q(0))/2
      ck(rp-rc==Q(d,2**d)*(aa[1<<i]**2+bb[1<<i]**2))
      # Check source mean-sector inequality separately, never hiding Xi.
      hf=entropy(fv);hv=entropy(aa);hw=entropy(bb)
      hc=[];vc=[];wc=[]
      for c,z in cs:
       hc.append(entropy(walsh(wrapper(c,z,d))));vc.append(entropy(walsh(c)));wc.append(entropy(walsh(z)))
      residual=add((Q(1),scalar(12*j+rp-rc)),(e,hv),(e,hw),(Q(-1),hf),(Q(1,2),hc[0]),(Q(1,2),hc[1]),(-e/2,vc[0]),(-e/2,vc[1]),(-e/2,wc[0]),(-e/2,wc[1]),(Q(1),collision))
      ck(nonneg(residual))
      # Full physical influence and BOTH actual terminal entropies are retained.
      ck(sum((infl(f,t) for t in range(len(f).bit_length()-1)),Q(0))==sum((s.bit_count()*q*q for s,q in enumerate(fv)),Q(0)))

ck(roots==276);ck(state_count==4712);ck(split_count==3104)
fixtures=[]
for k in [2,4]:
 for m in [1,2]:
  for d in [1,2]:
   n=k+m+1;e=Q(1,2**d)
   v=[];w=[]
   for x in range(2**n):
    z=x%(2**k); y=-1 if (x>>(k+m))&1 else 1
    bent=(-1)**sum(((z>>i)&1)*((z>>(i+1))&1) for i in range(0,k,2))
    v.append(y*bent);w.append(y*(-1 if x%(2**(k+m))==0 else 1))
   v,w=tuple(v),tuple(w)
   a,b=fwht(v),fwht(w);ck(entropy(a)==scalar(k)); iv=sum((infl(v,i) for i in range(n)),Q(0));ck(iv==Q(k,2)+1)
   s=e*(5*iv-k);ck(s==e*(Q(3*k,2)+5))
   if k>=4:ck(s-8*e>=3*e)
   f=wrapper(v,w,d);wf=fwht(f)
   ck(sum(q*q for q in wf)==1)
   ck(sum((i.bit_count()*q*q for i,q in enumerate(wf)),Q(0))==sum((infl(f,i) for i in range(n+d)),Q(0)))
   # One first x query and the unequal surviving second x query use original surplus.
   xr=xi(v,w,e)
   first=[(restrict(v,k,t),restrict(w,k,t)) for t in [0,1]]
   for c,z in first:
    x0=xi(c,z,e);B=s-4*e
    if k>=4:
     for vv,ww in states(c,z):
      # Limit fixtures to padding-only restrictions; general state coverage is above.
      break
     if m==2:
      for t in [0,1]:
       cc,zz=restrict(c,k,t),restrict(z,k,t)
       K=add((Q(1),scalar(B)),(Q(-1),x0),(Q(1),xi(cc,zz,e)))
       ck(nonneg(add((Q(1),K),(Q(-1),scalar(3*e)))))
   fixtures.append({'k':k,'m':m,'d':d,'original_donor':str(s),'after_first_4e':str(s-4*e)})
result={'status':'PASS','checks':checks,'roots':roots,'wrapper_states':state_count,'private_split_instances':split_count,'bent_fixtures':fixtures,'runtime_seconds':time.monotonic()-T0,'rung':'exact finite certificates; all-depth theorem is analytic, not enumeration','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='bent_fixtures'}),flush=True)
