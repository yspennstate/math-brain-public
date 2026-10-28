"""Exact scoped-source endpoint audit and precise census predicate labels."""
from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'out'
def save(n,x):(OUT/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
save('SOURCE_AUDIT_FROZEN_SPEC.json',{'helper_version':'stage20-source-audit-v1','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'Same complete labelled Boolean census n0..3 as frozen primary, now explicitly separate pair-isospectral from singleton-zero predicates; fixed A085 minimal three-bit seed in original4-bit controller','domain_and_count':'278 same census tables, no dimension increase; 2 signs*3 seed coordinates*2 outcomes=12 full wrapper reset transactions','symmetry':'none','arithmetic':'Integer Walsh/Fraction; full KL sign as exact rational product with common denominator','memory_estimate_MB':120,'maximum_runtime_seconds':30,'reason':'Primary field all_coordinate_null means pair-isospectral; it does not enforce zero singleton. Review source predicate and exact full-wrapper positive reset cost separately.'})
start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
 if time.perf_counter()-start>30:raise TimeoutError(30)
def walsh(v):
 a=list(v); k=1
 while k<len(a):
  for i in range(0,len(a),2*k):
   for j in range(i,i+k):a[j],a[j+k]=a[j]+a[j+k],a[j]-a[j+k]
  k*=2
 return [F(x,len(v)) for x in a]
def restrict(v,j,t):return [v[(x&((1<<j)-1))|((x>>j)<<(j+1))|(t<<j)] for x in range(len(v)//2)]
census={}
for n in range(4):
 cnt=flat=0;paircnt=pairnonflat=0
 for truth in range(1<<(1<<n)):
  v=[1-2*((truth>>x)&1) for x in range(1<<n)];f=walsh(v)
  pair=all(f[s]*f[s|(1<<j)]==0 for j in range(n) for s in range(1<<n) if not s&(1<<j))
  nonflat=sum(x!=0 for x in f)>1
  if pair:paircnt+=1;pairnonflat+=nonflat
  if pair and all(f[1<<j]==0 for j in range(n)):cnt+=1;flat+=nonflat
 census[str(n)]={'tables':1<<(1<<n),'pair_isospectral':paircnt,'pair_isospectral_nonflat':pairnonflat,'zero_singleton_AND_pair_isospectral':cnt,'zero_singleton_AND_pair_isospectral_nonflat':flat}
 if n<3:ck(flat==0)
ck(census['3']['zero_singleton_AND_pair_isospectral_nonflat']>0)
a=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1];b=[1-x*x for x in a];A=walsh(a);B=walsh(b)
ck(sum(x*x for x in B)==F(3,8))
v=[-1 if x in (0,7) else 1 for x in range(8)];f=walsh(v);p=[x*x for x in f]
ck(sum(F(s.bit_count())*x for s,x in enumerate(p))==F(3,2))
ck([s for s,x in enumerate(p) if x]==[0,3,5,6])
base=F(131072,130977);ck(base>1);transactions=0
for sign in (-1,1):
 parent=[a[c]+sign*b[c]*v[t] for t in range(8) for c in range(16)];P=[x*x for x in walsh(parent)]
 for j in range(3):
  ck(f[1<<j]==0)
  for t in (0,1):
   child=restrict(v,j,t);h=walsh(child);pp=[x*x for x in h];ck(pp==[F(1,4)]*4)
   full=[a[c]+sign*b[c]*child[z] for z in range(4) for c in range(16)];pc=[x*x for x in walsh(full)]
   seedref=[F(1,4)]+[F(63,64)*F(1,4)+(F(3,256) if z==1 else 0) for z in range(1,4)]
   ck(sum(seedref)==1)
   q=[(A[c]+sign*h[0]*B[c])**2 if z==0 else B[c]**2*seedref[z] for z in range(4) for c in range(16)]
   ck(sum(q)==1)
   product=F(1);den=1024
   for s,mass in enumerate(pc):
    ck((mass*den).denominator==1)
    if mass:ck(q[s]>0);product*=(mass/q[s])**int(mass*den)
   ck(product==base**96);ck(product>1);transactions+=1
save('SOURCE_AUDIT.json',{'status':'PASS','assertions':checks,'runtime_seconds':time.perf_counter()-start,'predicate_clarification':'Primary all_coordinate_null counts pair-isospectral spectra only. Zero-singleton phase-null census is separately shown here. This label clarification changes no primary eligibility or assertion.','census':census,'full_signed_wrapper_reset_transactions':transactions,'exact_full_child_reset_cost':'(3/32)*log2(131072/130977)','rational_power_certificate':'product_s (P_child(s)/Q_changed(s))^(1024 P_child(s))=(131072/130977)^96 >1','source_scope':'A085 complete minimal-seed reset, minimality and phase-null clauses independently verified; no source-price or target-necessity inference'})
print(json.dumps({'status':'SOURCE_AUDIT_PASS','assertions':checks,'transactions':transactions,'census':census,'runtime_seconds':time.perf_counter()-start}))
