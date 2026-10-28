"""A043 reserve hierarchy v1. All outputs stay in this run; no subprocesses."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from itertools import product
import json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out'
OUT.mkdir(exist_ok=True)
SPEC={"helper":"A043-reserve-hierarchy-v1","family":"all Boolean signs n<=2, all 256 ternary signs at fair law, five ternary prime representatives, reflected prime56067",
"domain":"n<=2 and five ternary representatives: p in {1/4,1/2,3/4}; all ternary masks: fair; prime56067: 5^4 grid {1/16,1/4,1/2,3/4,15/16} and old exact witness",
"case_count":1180,"scalar_cases":455,"sharpness_paths":"AND2 at p=2^-k, k=2,4,8,16,32","symmetry":"none for exhaustive parts; five sourced ternary representatives are additional fixtures only",
"arithmetic":"Fraction exact moments, exact polynomial reserves; 24-term outward rational atanh logarithms after power-of-two reduction",
"memory_estimate_mb":60,"max_runtime_seconds":55,"automatic_dimension_escalation":False,
"m_values":[0,1,2,4,8,16,32],"purpose":"verify universal reserve identity/error bound and whether the old witness is repaired; no continuum payment inferred from samples"}
(OUT/'frozen_spec.json').write_text(json.dumps(SPEC,indent=2)+'\n',encoding='utf-8')
start=time.perf_counter();checks=0
def ck(condition):
 global checks
 checks+=1
 if not condition: raise AssertionError(checks)
def mul(xs):
 r=Q(1)
 for x in xs:r*=x
 return r
def log_series(x):
 z=(x-1)/(x+1)
 ck(0<=z<=Q(1,3))
 lo=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(24)),Q(0))
 return lo,lo+2*z**49/(49*(1-z*z))
L2=log_series(Q(2))
@lru_cache(None)
def ln(x):
 ck(x>=1)
 k=0
 while x>=2:x/=2;k+=1
 lo,hi=log_series(x)
 return lo+k*L2[0],hi+k*L2[1]
def h(t):
 if t==0 or t==1:return Q(0),Q(0)
 lo,hi=ln(1/t**2)
 return t*t*lo,t*t*hi
def sm_scalar(t,m):
 return t*(1-t)*sum((Q(2,k*(k+1))*(1-t)**k for k in range(1,m+1)),Q(0))
scalar=0
for j in range(65):
 t=Q(j,64);hl,hu=h(t)
 for m in SPEC['m_values']:
  lower=sm_scalar(t,m);tail=Q(2,m+1)*t*(1-t)
  ck(lower>=0)
  ck(lower<=2*t*(1-t)-hu)
  ck(2*t*(1-t)-hl<=lower+tail)
  ck(sm_scalar(t,m+1)-lower==Q(2,(m+1)*(m+2))*t*(1-t)**(m+2))
  scalar+=1

def profile(values,p):
 n=len(p);v=[4*x*(1-x) for x in p];mom=list(map(Q,values))
 for j in range(n):
  b=1<<j
  for x in range(1<<n):
   if x&b:continue
   a,c=mom[x],mom[x|b]
   mom[x]=(1-p[j])*a+p[j]*c
   mom[x|b]=p[j]*(1-p[j])*(c-a)
 c=[];mass=[]
 for s in range(1<<n):
  den=mul(p[j]*(1-p[j]) for j in range(n) if s>>j&1)
  c.append(mom[s]/(2**s.bit_count()*den));mass.append(mom[s]**2/den)
 ck(sum(mass)==1)
 delta=sum(((s.bit_count()-1)*mass[s] for s in range(1,1<<n)),Q(0))
 r=sum(((s.bit_count()-2)*mass[s] for s in range(1,1<<n) if s.bit_count()>=3),Q(0))
 d=[]
 for j in range(n):
  mean=second=Q(0)
  for x in range(1<<n):
   if x>>j&1:continue
   wt=mul(p[k] if x>>k&1 else 1-p[k] for k in range(n) if k!=j)
   diff=Q(values[x|(1<<j)]-values[x],2)
   mean+=wt*diff;second+=wt*diff*diff
  ck(mean==c[1<<j]);ck(second>=abs(mean));d.append(second)
 ck(sum((v[j]*(d[j]-c[1<<j]**2) for j in range(n)),Q(0))==2*delta-r)
 ck(0<=r<=delta)
 hlo=hhi=Q(0)
 for j in range(n):
  lo,hi=h(abs(c[1<<j]));hlo+=v[j]*lo;hhi+=v[j]*hi
 slo=4*delta-2*r-hhi;shi=4*delta-2*r-hlo
 reserves={}
 for m in SPEC['m_values']:
  sm=sum((v[j]*(2*(d[j]-abs(c[1<<j]))+sm_scalar(abs(c[1<<j]),m)) for j in range(n)),Q(0))
  bound=Q(2,m+1)*(2*delta-r)
  ck(sm>=0);ck(sm<=slo);ck(shi<=sm+bound);ck(bound<=Q(4,m+1)*delta)
  reserves[str(m)]=sm
 return delta,r,slo,shi,reserves

cases=0;grid_fail={str(m):0 for m in SPEC['m_values']};witness=None;sharpness=[]
def fixture(values,p,kind):
 global cases,witness
 if time.perf_counter()-start>55:raise TimeoutError('Frozen 55-second cap reached')
 delta,r,sl,sh,reserves=profile(values,p);cases+=1
 if kind=='prime-grid':
  for m in SPEC['m_values']:grid_fail[str(m)]+=int(reserves[str(m)]<4*r)
 if kind=='old-witness':
  witness={'p':list(map(str,p)),'delta':str(delta),'T':str(r),'S_interval':[str(sl),str(sh)],
  'S_m_minus4T':{m:str(s-4*r) for m,s in reserves.items()}}
  ck(reserves['1']-4*r==Q(-16029490109593689663,302231454903657293676544))
  ck(sl>=4*r)
 if kind.startswith('and-path-'):
  k=int(kind.rsplit('-',1)[1])
  row={'k':k,'error_over_delta_intervals':{m:[str((sl-s)/delta),str((sh-s)/delta)] for m,s in reserves.items()}}
  sharpness.append(row)
  if k==32:
   for m,s in reserves.items():ck((sl-s)/delta>Q(4,int(m)+1)-Q(1,10**6))

try:
 for n in range(3):
  for mask in range(1<<(1<<n)):
   values=[1 if mask>>x&1 else -1 for x in range(1<<n)]
   for p in product((Q(1,4),Q(1,2),Q(3,4)),repeat=n):fixture(values,p,'small-exhaustive')
 for mask in range(256):fixture([1 if mask>>x&1 else -1 for x in range(8)],[Q(1,2)]*3,'ternary-fair')
 for mask in (22,23,24,25,27):
  for p in product((Q(1,4),Q(1,2),Q(3,4)),repeat=3):fixture([1 if mask>>x&1 else -1 for x in range(8)],p,'prime-ternary')
 values=[]
 for i in range(16):
  a,x,y,z=[(i>>j)&1 for j in range(4)]
  values.append(-1+2*z+2*x*y-2*z*(a*x+(1-a)*y))
 for p in product((Q(1,16),Q(1,4),Q(1,2),Q(3,4),Q(15,16)),repeat=4):fixture(values,p,'prime-grid')
 fixture(values,[Q(1,2),Q(1,1024),Q(1,1048576),Q(1,16)],'old-witness')
 for k in (2,4,8,16,32):fixture([-1,-1,-1,1],[Q(1,2**k)]*2,'and-path-'+str(k))
 ck(cases==SPEC['case_count']);ck(scalar==SPEC['scalar_cases'])
 status='PASS'
except Exception as exc:
 status=type(exc).__name__+': '+str(exc)
result={'status':status,'boolean_cases':cases,'scalar_cases':scalar,'assertions':checks,'runtime_seconds':time.perf_counter()-start,
 'grid_failures_Sm_ge4T_finite_only':grid_fail,'old_witness':witness,'sharpness_paths':sharpness,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':'Polynomial/error checks on declared finite domain; universal theorem rests on analytic series proof, not these cases.'}
(OUT/'checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('old_witness','sharpness_paths')}))
if witness:print('witness gaps:',witness['S_m_minus4T'])
if status!='PASS':raise SystemExit(1)
