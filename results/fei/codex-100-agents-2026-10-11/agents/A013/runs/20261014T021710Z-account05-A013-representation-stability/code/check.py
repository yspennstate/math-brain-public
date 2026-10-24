from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time,hashlib
RUN=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def check(b):
 global checks
 checks+=1
 if time.perf_counter()-start>50:raise RuntimeError('50 second internal cutoff')
 if not b:raise AssertionError(checks)
def fwht(t):
 a=list(t);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):
    u,v=a[k],a[k+h];a[k]=u+v;a[k+h]=u-v
  h*=2
 return [F(x,len(a)) for x in a]
@lru_cache(None)
def factors(n):
 out=[];p=2
 while p*p<=n:
  e=0
  while n%p==0:n//=p;e+=1
  if e:out.append((p,e))
  p+=1
 if n>1:out.append((n,1))
 return tuple(out)
@lru_cache(None)
def lv(x):
 x=F(x);assert x>0;a={}
 for p,e in factors(x.numerator):a[p]=F(e)
 for p,e in factors(x.denominator):a[p]=a.get(p,F(0))-e
 return {p:e for p,e in a.items() if e}
def add(a,b,k=F(1)):
 a=dict(a)
 for p,v in b.items():
  a[p]=a.get(p,F(0))+k*v
  if not a[p]:del a[p]
 return a
def mul(a,k):return {p:v*k for p,v in a.items() if v*k}
def H(p):
 a={}
 for x in p:
  if x:a=add(a,lv(1/x),x)
 return a
def CE(p,q):
 a={}
 for x,y in zip(p,q):
  if x:
   check(y>0);a=add(a,lv(1/y),x)
 return a
def lniv(x):
 u=(x-1)/(x+1);lo=sum((2*u**(2*j+1)/F(2*j+1) for j in range(20)),F(0))
 return lo,lo+2*u**41/(41*(1-u*u))
lnlo,lnhi=lniv(F(2));check(lnlo>F(2,3));check(lnhi<1)
@lru_cache(None)
def logiv(x):
 x=F(x);k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 lo,hi=lniv(x);return F(k)+lo/lnhi,F(k)+hi/lnlo
def iv(v):
 lo=hi=F(0)
 for p,c in v.items():
  a,b=logiv(p);lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
 return lo,hi
def nonneg(v):check(not v or iv(v)[0]>=0)
def refs(p):
 u=[F(1,len(p))]*len(p)
 return [p,u,[(a+b)/2 for a,b in zip(p,u)]]
def cal(p,r,shared):
 rem=1-sum(p[s] for s in shared);old=1-sum(r[s] for s in shared)
 assert not rem or old>0
 return [p[s] if s in shared else (rem*r[s]/old if rem else F(0)) for s in range(len(p))]
def influence(t,n):return [F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(n)]

patterns=[(1,0,0,0,0,0,0,0),(F(1,2),)*3+(-F(1,2),)+(0,)*4,(F(3,4),)+(F(1,4),)*4+(-F(1,4),)*3,(-F(3,4),)+(F(1,4),)*7]
def row(a,b):
 m=a*a+b*b
 return mul(H([a*a/m,b*b/m]),m) if m else {}
def packet(cs,d):
 b=mul(lv(2),2*(d-8*d*d))
 for c in cs:b=add(b,row(c-d,d))
 return b
certs=[]
for k,cs in enumerate(patterns):
 for r in [0,1]:
  d=F(1,8*(1<<r));b=packet(cs,d);gap=add(mul(lv(2),4*d),b,F(-1));nonneg(gap)
  lo,hi=iv(gap);check(lo>0)
  certs.append({'pattern':k,'r':r,'d':str(d),'gap_prime_log':{str(p):str(v) for p,v in gap.items()},'gap_interval':[str(lo),str(hi)]})
(RUN/'out/PROFILE_CERTIFICATES.json').write_text(json.dumps(certs,indent=2))
print('eight rational profile certificates PASS',flush=True)
profiles=0;pattern_counts=[0]*4
for mask in range(256):
 c=[1 if mask>>y&1 else -1 for y in range(8)];a=fwht(c)
 for w in range(8):
  cs=[a[t]*c[w]*(-1 if (t&w).bit_count()%2 else 1) for t in range(8)]
  k=next(k for k,p in enumerate(patterns) if sorted(cs)==sorted(p));pattern_counts[k]+=1
  for r in ([0,1,2,3] if mask in [255,3,7,1] else []):
   n=3+r;d=F(1,8*(1<<r))
   h=[c[x&7]*(-1 if (x&7)==w and (x>>3)==0 else 1) for x in range(1<<n)]
   ah=fwht(h);ag=[a[t] if t<8 else F(0) for t in range(1<<n)]
   for t in range(1<<n):check(ah[t]==ag[t]-2*d*c[w]*(-1 if (t&w).bit_count()%2 else 1))
   f=[c[x&7] if x<(1<<n) else h[x-(1<<n)] for x in range(1<<(n+1))]
   af=fwht(f)
   for t in range(1<<n):check(af[t]==(ag[t]+ah[t])/2);check(af[t+(1<<n)]==(ag[t]-ah[t])/2)
   check(influence(f,n+1)[n]==d)
   # Prime-log equality verifies actual spectra, not only the surrogate pattern.
   bc={}
   for t in range(8):bc=add(bc,row((ag[t]+ah[t])/2,(ag[t]-ah[t])/2))
   b=add(bc,mul(lv(2),2*(d-8*d*d)))
   check(b==packet(patterns[k],d))
   profiles+=1
 print('phase',mask,'complete',flush=True) if mask in [63,127,191,255] else None
source_cases=0
tables=[[1 if mask>>x&1 else -1 for x in range(8)] for mask in range(256)]
for gi in range(16):
 for hi in range(16):
  g=tables[gi];h=tables[17*hi]
  ag=fwht(g);ah=fwht(h)
  eg=[F(0)]*16;eh=[F(0)]*16
  for t in range(8):eg[t]=ag[t];eh[(t&3)|((t>>2)<<3)]=ah[t]
  d=(1-sum(a*b for a,b in zip(eg,eh)))/2
  if d>F(1,2):eh=[-a for a in eh];d=1-d
  delta=sum((eg[t]-eh[t])**2/4 for t in range(4));bc={};bout={}
  for t,(a,b) in enumerate(zip(eg,eh)):
   z=row((a+b)/2,(a-b)/2)
   if t<4:bc=add(bc,z)
   else:bout=add(bout,z)
  check(bout==mul(lv(2),2*(d-delta)));check(delta<=min(d,4*d*d))
  nonneg(add(mul(lv(2),4*d),add(bc,bout),F(-1)));source_cases+=1
print('source ownership/payment reconstruction PASS',flush=True)
# Exact proper-nonmember root witnesses, independently generated.
t=[1 if x.bit_count()>=2 else -1 for x in range(16)];minors=[]
for j in range(4):
 for v in [0,1]:
  for k in range(4):
   if k!=j:check(any(t[x]!=t[x^(1<<k)] for x in range(16) if (x>>j)&1==v))
for mask in range(1,15):
 if not mask&1:continue
 left=[x for x in range(16) if x&~mask==0];right=[x for x in range(16) if x&mask==0]
 witness=next((a,b,c,d) for a in left for b in left for c in right for d in right if t[a|c]*t[b|d]!=t[a|d]*t[b|c])
 minors.append({'partition':mask,'minor':witness})
(RUN/'out/NONMEMBER_RECHECK.json').write_text(json.dumps(minors,indent=2))
# Retain an arbitrary fixed terminal reference under a disjoint common factor.
tensor_cases=0
for mask in range(16):
 q=[1 if mask>>x&1 else -1 for x in range(4)];pq=[v*v for v in fwht(q)]
 for r in [0,1]:
  for cmask in [255,3,1,7]:
   c=[1 if cmask>>y&1 else -1 for y in range(8)];n=3+r
   h=[c[x&7]*(-1 if (x&7)==0 and (x>>3)==0 else 1) for x in range(1<<n)]
   f=[c[x&7] if x<(1<<n) else h[x-(1<<n)] for x in range(1<<(n+1))]
   pf=[a*a for a in fwht(f)];p=[a*b for a in pq for b in pf]
   actual=[q[x//len(f)]*f[x%len(f)] for x in range(4*len(f))]
   check([a*a for a in fwht(actual)]==p)
   for rq in refs(pq):
    ref=[a*b for a in rq for b in pf]
    check(sum(ref)==1);check(CE(p,ref)==add(CE(pq,rq),H(pf)))
    check(add(CE(p,ref),H(p),F(-1))==add(CE(pq,rq),H(pq),F(-1)))
    tensor_cases+=1
res={'status':'PASS','helper_version':'A013-three-bit-profile-v2','profiles':profiles,'classification_pairs':sum(pattern_counts),'pattern_counts':pattern_counts,'scalar_certificates':len(certs),'source_pairs':source_cases,'nonmember_partitions':len(minors),'retained_terminal_reference_cases':tensor_cases,'exact_assertions':checks,'elapsed_seconds':time.perf_counter()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(RUN/'out/EXACT_RESULTS.json').write_text(json.dumps(res,indent=2))
print(json.dumps(res),flush=True)
