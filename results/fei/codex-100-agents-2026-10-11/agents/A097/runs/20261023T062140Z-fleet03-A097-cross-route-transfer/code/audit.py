"""Independent full physical FWHT / prime-log witness and controller endpoint audit."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time,hashlib
RUN=Path(__file__).resolve().parents[1]
spec={'helper_version':'A097-fwht-prime-independent-v1','family':'explicit three-bit balanced zero-singleton seed times displayed four-bit controller; all81 partial controller restrictions','domain':'one full128-vertex physical root, both64-vertex children, one fixed prescribed full mixture at7/519;81 controller states*5 rational means','case_count':{'wrapper_roots':1,'children':2,'controller_states':81,'gram_mean_tests':405},'symmetry':'none','arithmetic':'integer FWHT, Fraction, exact prime logarithm coefficient identities, rational ln2>2/3 and ln(1+t)<t','memory_estimate_MB':40,'max_runtime_seconds':30,'automatic_dimension_escalation':False,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(RUN/'out/AUDIT_FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
start=time.perf_counter();checks=0
def ok(v):
 global checks
 checks+=1
 assert v,checks
def spectrum(v):
 a=list(v);k=1
 while k<len(a):
  for t in range(0,len(a),2*k):
   for i in range(t,t+k):a[i],a[i+k]=a[i]+a[i+k],a[i]-a[i+k]
  k*=2
 return tuple(F(x,len(a)) for x in a)
def p(v):return tuple(x*x for x in spectrum(v))
def factors(n):
 out={};k=2
 while k*k<=n:
  while n%k==0:out[k]=out.get(k,0)+1;n//=k
  k+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def add(a,b,c=F(1)):
 out=dict(a)
 for k,v in b.items():out[k]=out.get(k,F(0))+c*v
 return {k:v for k,v in out.items() if v}
def log(q):return add(factors(q.numerator),factors(q.denominator),-1)
def ce(a,b):
 out={}
 for x,y in zip(a,b):
  if x:ok(y>0);out=add(out,log(y),-x)
 return out
def restrict(v,j,t):return tuple(x for i,x in enumerate(v) if i>>j&1==t)
def marginal(v,j):
 out=[]
 for t in range(len(v)//2):
  z=(t&((1<<j)-1))+((t>>j)<<(j+1));out.append(v[z]+v[z+(1<<j)])
 return tuple(out)
A=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1);B=tuple(1-a*a for a in A)
h=tuple((-1 if (i&3)==0 else 1)*(-1 if i&4 else 1) for i in range(8))
v=tuple(a+b*z for z in h for a,b in zip(A,B));q=p(v);qbar=marginal(q,4);pbar=qbar
delta=add(ce(q,q),ce(pbar,pbar),-1);delta=add(delta,ce(q,q),-1)
ac,bc=spectrum(A),spectrum(B);eps=F(7,519);beta=sum(b*b for b in bc);child_receipts=[]
for bit in (0,1):
 ht=restrict(h,0,bit);truth=restrict(v,4,bit);pt=p(ht);full=p(truth)
 rn=tuple(F(0) if i==0 else (1-eps)*pt[i]+eps*(i==3) for i in range(4))
 qnew=tuple(ac[u]**2 if t==0 else bc[u]**2*rn[t] for t in range(4) for u in range(16))
 ok(sum(qnew)==1);ok(sum(full)==1);delta=add(delta,ce(full,qnew),F(1,2))
 child_receipts.append({'bit':bit,'seed_support':[i for i,x in enumerate(pt) if x],'full_nonzero':sum(x>0 for x in full)})
expected=add({2:-beta},log(F(519,512)),beta/2);ok(delta==expected)
x=F(21,4096)
# Multiply delta_bits by ln2; ln2>2/3 (first positive atanh term), ln(519/512)<7/512.
upper_nats=-beta*F(2,3)+(beta/2)*F(7,512);ok(upper_nats < -x)
# All physical controller endpoint configurations, including b=0 /Gamma=0.
zeros=0
for state in product((-1,0,1),repeat=4):
 av=tuple(a for i,a in enumerate(A) if all(t==-1 or i>>j&1==t for j,t in enumerate(state)))
 bv=tuple(1-a*a for a in av);a,b=spectrum(av),spectrum(bv)
 C=sum(u*u*w*w for u,w in zip(a,b));D=sum(u*w**3 for u,w in zip(a,b));E=sum(w**4 for w in b)
 gamma=C-D*D/E if E else F(0);ok(gamma>=0);ok(sum(u*w for u,w in zip(a,b))==0)
 if not E:zeros+=1;ok(all(w==0 for w in b))
 for m in (F(-1),F(-1,2),F(0),F(1,2),F(1)):
  ok(sum(w*w*(u+m*w)**2 for u,w in zip(a,b))>=gamma)
result={'status':'PASS','exact_assertions':checks,'runtime_seconds':time.perf_counter()-start,'witness_signed_log_prime_coefficients':delta,'expected_expression_bits':'-(3/8)+(3/16)log2(519/512)','rigorous_increment_upper_nats':str(upper_nats),'paid_energy_nats':str(x),'both_full_children':child_receipts,'controller_states':81,'zero_active_controller_states':zeros,'independence':'no imports/source helper calls; physical FWHT instead of direct character/factorized reference primitive'}
(RUN/'out/INDEPENDENT_AUDIT.json').write_text(json.dumps(result,indent=2,default=str)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','exact_assertions':checks,'seconds':time.perf_counter()-start}))
