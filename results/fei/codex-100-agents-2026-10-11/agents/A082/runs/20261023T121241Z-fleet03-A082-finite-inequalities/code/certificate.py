from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib,shutil
R=Path(__file__).resolve().parents[1]
old=R.parent/'20261023T061304Z-fleet03-A082-finite-inequalities'
shutil.copyfile(old/'code/exact.py',R/'code/exact.py')
def save(n,x):(R/'out'/n).write_text(json.dumps(x,indent=2,default=str),encoding='utf-8')
spec=dict(helper_version='A082-binary-affinity-certificate-v2-cache-transform',family='Binary reference forks on four occupied labels; actual three-bit antipodal-pair defect embedded in three parity blocks of length3',domain='eta in {0,1/4,1/2,3/5,2/3,3/4}; one-level fork and complete depth2 adaptive physical tree querying first two bits of first block; all leaf outcomes',case_count='6 one-level and6 depth2 reference policies,4 physical leaves each; sharp universal estimate proved analytically rather than inferred from grid',symmetry='none on physical outcomes; equal atom multiplicities justified algebraically',arithmetic='Fraction Walsh butterflies, exact prime-log CE and rational atanh enclosures; symbolic sqrt2 chord proof',memory_estimate_mb=100,max_runtime_seconds=55,pilot_max_runtime_seconds=55,exhaustiveness='A binary pair reduces to midpoint weights M_i and t_i=(p_i-q_i)/(p_i+q_i), sum M_i t_i=0; t_i^2 in[0,1/2]. Two proved chord inequalities exhaust this continuum and every finite alphabet; no finite grid claimed exhaustive.')
save('FROZEN_SPEC_V2.json',spec)
import exact as e
start=time.monotonic();count=0
def ck(x):
 global count
 count+=1;assert x,count
 assert time.monotonic()-start<55,'frozen55second cap'
def ft(f):
 a=list(map(F,f));n=len(a);k=1
 while k<n:
  for i in range(0,n,2*k):
   for j in range(k):u,v=a[i+j],a[i+j+k];a[i+j]=u+v;a[i+j+k]=u-v
  k*=2
 return tuple(x/n for x in a)
def spectrum(f):return tuple(x*x for x in ft(f))
def kl(p,q):return e.sub(e.ce(p,q),e.ent(p))
def parity(x):return -1 if x.bit_count()%2 else 1
h=tuple(-1 if x in (0,7) else 1 for x in range(8))
f=tuple(h[sum(((1-parity((x>>(3*j))&7))//2)<<j for j in range(3))] for x in range(512))
P=spectrum(f);support=[i for i,p in enumerate(P) if p]
ck(len(support)==4);ck(all(P[i]==F(1,4) for i in support));ck(e.influence(f)==F(9,2))
Fhat=ft(f)
for j in range(9):ck(all(not(Fhat[t]*Fhat[t|(1<<j)]) for t in range(512) if not t&(1<<j)))
Q=P;rows=[]
for eta in map(F,['0','1/4','1/2','3/5','2/3','3/4']):
 leaves=[];qs=[];mass=F(1)-eta*eta
 for v0 in (0,1):
  f1=e.child(f,0,v0);P1=spectrum(f1);M1=e.marginal(P,0)
  ck(P1==M1);ck(not e.sub(e.ent(P),e.ent(M1)))
  for v1 in (0,1):
   fc=e.child(f1,0,v1);Pc=spectrum(fc);Mc=e.marginal(M1,0)
   ck(Pc==Mc);ck(not e.sub(e.ent(P1),e.ent(Mc)))
   Qc=[F(0)]*len(Pc)
   pulled=[]
   for k,t in enumerate(support):
    mapped=t>>2;z0=1 if k&1 else -1;z1=1 if k&2 else -1
    q=(1+(-1 if v0 else 1)*eta*z0)*(1+(-1 if v1 else 1)*eta*z1)/4
    Qc[mapped]=q;pulled.append(q)
   ck(sum(Qc)==1);qs.append(pulled)
   leaves.append(e.ce(Pc,Qc))
 # Product over four leaves is independent of occupied label.
 for k in range(4):
  prod=F(1)
  for q in qs:prod*=q[k]
  ck(prod==(mass/4)**4)
 # Z=mass; root effective reference is P. No irrational arithmetic needed.
 bill=e.scale(e.logform(mass),-1)
 mean={}
 for ce in leaves:mean=e.add(mean,e.scale(ce,F(1,4)))
 actual=e.sub(mean,e.ce(P,Q));ck(actual==bill)
 upper=2*eta*eta
 if eta*eta<=F(1,2):ck(e.interval(bill)[1]<=upper or not bill)
 if eta==F(3,5):
  # A=3, W=1/4, initial CE=2: SAME unused original U=3/4.
  U=F(3,4);ck(U-upper==F(3,100));ck(e.interval(bill)[1]<U)
 rows.append(dict(eta=eta,leaves=4,normalizer=mass,effective_root='actual P',bill=e.serial_form(bill),bill_interval=e.interval(bill),total_relative_variance=upper,paid_by_variance=eta*eta<=F(1,2),old_debit='1/4',original_allowance='3' if eta==F(3,5) else 'not asserted'))
 # One-fork probability laws have affinity squared1-eta^2.
 pp=tuple((1+eta*(1 if k&1 else -1))/4 for k in range(4))
 pm=tuple((1-eta*(1 if k&1 else -1))/4 for k in range(4))
 ck(sum(pp)==sum(pm)==1)
 for k in range(4):ck(pp[k]*pm[k]==mass/16)
 # At eta3/4 the purported larger-domain constant1 bound fails exactly.
 if eta==F(3,4):
  ck(2**23>7**8)
  ck(e.interval(e.scale(bill,F(1,2)))[0]>eta*eta)
save('CERTIFICATE.json',dict(status='PASS',physical_dimension=9,actual_spectral_support=support,actual_influence='9/2',actual_entropy_bits='2',policies=rows,assertions=count,primitive_assertions=e.ASSERTIONS,seconds=time.monotonic()-start,sharp_domain='t_i^2<=1/2',sharp_constant_bits='1',failed_extension_integer_certificate='2^23>7^8 for eta=3/4',formal_status='analytic symbolic proof; no Lean claim'))
print('PASS',count,'direct assertions;',e.ASSERTIONS,'primitive assertions; seconds',time.monotonic()-start,flush=True)
