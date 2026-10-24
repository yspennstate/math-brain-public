"""Frozen homogeneous point-tensor canonical reference audit; no floating proof."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import math,json,time,sys,hashlib
RUN=Path(__file__).resolve().parents[1];OUT=RUN/'out';OUT.mkdir(exist_ok=True)
CAP=128
DOMAIN=[(r,m) for r in range(1,CAP+1) for m in range(1,CAP//r+1)]
def dump(n,v): (OUT/n).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
if '--freeze' in sys.argv:
 dump('FROZEN_SPEC.json',{'helper_version':'minimize.py v1','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'F_h=(-1)^a if x=0; h if x=b=1; +1 otherwise. h is product of m disjoint width-r point defects.','parameter_domain':'positive integers r,m with r*m<=128','case_count':len(DOMAIN),'symmetry':'identical blocks and coordinate permutations only; all ordered parameter pairs retained','arithmetic':'discovery binary64 only; verification Fraction dyadic root brackets and atanh series with proved geometric tails; all cases at or below discovered minimum size certified','memory_estimate_mb':70,'maximum_runtime_seconds':55,'pilot':'six predetermined small/known-obstruction cases; pilot <60 seconds','no_dimension_escalation':True})
 print('FROZEN',len(DOMAIN));sys.exit()
START=time.perf_counter();CHECKS=0
def ck(b):
 global CHECKS
 assert b;CHECKS+=1
def mul(a,b):return min(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]),max(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
def sc(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def add(*args):return sum((a[0] for a in args),F(0)),sum((a[1] for a in args),F(0))
def neg(a):return -a[1],-a[0]
def rounded(a):
 d=1<<72
 return F(a[0].numerator*d//a[0].denominator,d),F(-((-a[1].numerator*d)//a[1].denominator),d)
def ln_unit(x):
 z=(x-1)/(x+1);z2=z*z;p=z;s=F(0)
 for k in range(28):s+=2*p/(2*k+1);p*=z2
 return s,s+2*p/(57*(1-z2))
LN2=ln_unit(F(2))
@lru_cache(maxsize=4096)
def log2q(x):
 ck(x>0)
 k=x.numerator.bit_length()-x.denominator.bit_length()
 y=x/F(2)**k
 if y<1:k-=1;y*=2
 ck(1<=y<=2)
 a,b=ln_unit(y)
 return rounded((F(k)+a/LN2[1],F(k)+b/LN2[0]))
def phi(x):return sc(log2q(x),-x) if x else (F(0),F(0))
def h2(x):return add(phi(x),phi(1-x))
def params(r,m):
 delta=F(1,2**r);mu=(1-2*delta)**m;t=(1-mu)/2;p0=(1-t)**2/4;v=1-p0
 infl=[(F(1,2),2),(t/2,1),(delta/2,r*m)]
 return delta,mu,t,p0,v,[(d/v,num) for d,num in infl],sum(d*num for d,num in infl)
def equation(c,rr):return math.prod((1-c*d)**num for d,num in rr)-(1-c)
def certify(r,m):
 d,mu,t,p0,v,rr,I=params(r,m);lo=F(1,2**50);hi=F(1)
 ck(equation(lo,rr)<0 and equation(hi,rr)>0)
 for _ in range(50):
  mid=(lo+hi)/2
  if equation(mid,rr)<0:lo=mid
  else:hi=mid
 ck(0<lo<hi<1)
 # Cross entropy affine in occupied membership; bound every log monotonically.
 ce=add(phi(p0),sc((log2q(lo/v)[0],log2q(hi/v)[1]),v),sc((log2q(1-hi)[0],log2q(1-lo)[1]),-v))
 for rate,num in rr:
  oddslo=(1-hi*rate)/(hi*rate);oddshi=(1-lo*rate)/(lo*rate)
  ce=add(ce,sc((log2q(oddslo)[0],log2q(oddshi)[1]),v*rate*num))
 excess=add(ce,(-4*I,-4*I));ck(excess[0]>0 or excess[1]<0)
 hp=add(phi((1-2*d)**2),sc(phi(4*d*d),2**r-1))
 hh=sc(hp,m)
 hg=add(phi((1-t)**2),phi(t*t),sc(add(hh,neg(phi(mu*mu))),F(1,2)),(4*t*(1-t),4*t*(1-t)))
 H=add((F(2),F(2)),sc(hg,F(1,2)))
 ck(H[1]<=4*I)
 # Query b, retain b=0, then one data coordinate on b=1; both nonconstant
 # active data children for m,r>=2. H/I leaf identities use exact tensor formulas.
 record={'r':r,'m':m,'physical_variables':r*m+3,'c':[str(lo),str(hi)],'p0':str(p0),'v':str(v),'I':str(I),'H':[str(x) for x in rounded(H)],'CE':[str(x) for x in rounded(ce)],'CE_minus_4I':[str(x) for x in rounded(excess)],'violates_rate4':excess[0]>0}
 return record
def discover(r,m):
 delta=2.0**(-r);mu=(1-2*delta)**m;t=(1-mu)/2;p0=(1-t)**2/4;v=1-p0
 rr=[(.5/v,2),(t/2/v,1),(delta/2/v,r*m)]
 lo=1e-7;hi=1.0
 for _ in range(50):
  c=(lo+hi)/2;e=math.prod((1-c*q)**num for q,num in rr)-(1-c)
  if e<0:lo=c
  else:hi=c
 c=(lo+hi)/2
 ce=-p0*math.log2(p0)+v*math.log2(c/v)-v*math.log2(1-c)
 for q,num in rr:
  if q:ce+=v*q*num*math.log2((1-c*q)/(c*q))
 return ce-4*(1+t/2+r*m*delta/2)
if '--pilot' in sys.argv:
 cases=[(1,1),(2,1),(2,2),(3,2),(2,32),(2,64)]
 rows=[certify(r,m) for r,m in cases]
 dump('PILOT.json',{'cases':rows,'assertions':CHECKS,'elapsed_seconds':time.perf_counter()-START,'status':'PASS'})
 print('PILOT PASS',len(rows),CHECKS,time.perf_counter()-START);sys.exit()
discovery=[(r,m,discover(r,m)) for r,m in DOMAIN]
wins=[(r*m,r,m,e) for r,m,e in discovery if e>1e-7]
ck(bool(wins));cost,r0,m0,_=min(wins)
dump('DISCOVERY.json',{'certifying':False,'domain_cases':len(discovery),'smallest_found':[cost,r0,m0],'positive_cases':wins})
rows=[]
for r,m in DOMAIN:
 if r*m<=cost:
  rows.append(certify(r,m))
  if time.perf_counter()-START>55:raise RuntimeError('Frozen runtime limit reached; incomplete domain')
positive=[a for a in rows if a['violates_rate4']]
minimum=min(a['physical_variables'] for a in positive)
ck(minimum==cost+3)
w=[a for a in positive if a['physical_variables']==minimum]
dump('CERTIFICATE.json',{'status':'PASS','discovery_domain':len(DOMAIN),'certified_cases':len(rows),'minimum_physical_variables_in_family':minimum,'minimizers':w,'records':rows,'assertions':CHECKS,'elapsed_seconds':time.perf_counter()-START})
dump('WITNESS.json',w[0]);print('PASS',len(rows),'cases',CHECKS,'assertions; minimum',minimum,'witness',[(a['r'],a['m']) for a in w],'seconds',time.perf_counter()-START)
