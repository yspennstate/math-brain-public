"""Independent direct-character all-core/all-policy finite frontier audit."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,sys,time,hashlib
run=Path(__file__).resolve().parents[1];out=run/'out'
if '--freeze' in sys.argv:
 (out/'FRONTIER_SPEC.json').write_text(json.dumps({'helper_version':'frontier-v1','sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'all uniform Boolean cores on0..3 variables, J_s(x,z)=s on x0,h on x1, s=+/-1','domain_cases':278,'policies':'all finite fresh-data stopping trees; independent policy for each sign; dynamic programming over complete truth-table restrictions','symmetry':'none; LSB coordinate deletion canonicalizes only remaining labels','arithmetic':'direct character sums, exact rational probabilities, independent40-term atanh intervals, interval min includes every policy even when endpoints overlap','memory_estimate_mb':60,'maximum_runtime_seconds':55,'pilot':'all22 cores on0..2 variables'},indent=2)+'\n',encoding='utf-8');print('FROZEN');sys.exit()
start=time.perf_counter();checks=0
def ck(v):
 global checks
 assert v;checks+=1
 if time.perf_counter()-start>55:raise TimeoutError('frozen55s')
def add(*a):return sum((v[0] for v in a),Q()),sum((v[1] for v in a),Q())
def sc(a,k):return (a[0]*k,a[1]*k) if k>=0 else (a[1]*k,a[0]*k)
def ln(x):
 z=(x-1)/(x+1);s=Q();p=z
 for j in range(40):s+=p/(2*j+1);p*=z*z
 return 2*s,2*s+2*p/(81*(1-z*z))
L2=ln(Q(2));D=1<<85
@lru_cache(None)
def lg(x):
 assert x>0;k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 lo,hi=ln(x);a=k+lo/L2[1];b=k+hi/L2[0]
 return Q(a.numerator*D//a.denominator,D),Q(-((-b.numerator*D)//b.denominator),D)
@lru_cache(None)
def ent(t):
 N=len(t);p=[Q(sum(t[u]*(-1)**((s&u).bit_count()) for u in range(N))**2,N*N) for s in range(N)]
 ck(sum(p)==1)
 return add(*(sc(lg(v),-v) for v in p if v))
@lru_cache(None)
def inf(t):return sum((Q(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(len(t).bit_length()-1)),Q())
def cut(t,j,b):return tuple(t[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(t)//2))
def surplus(t,s):
 mu=Q(sum(t),len(t));u=tuple(s if not x&1 else t[x>>1] for x in range(2*len(t)))
 a=inf(u);ck(a==(1-s*mu)/2+inf(t)/2)
 hj=ent(u);hh=ent(t);ck(hj[1]<2+hh[0]/2 or hj[1]-(2+hh[0]/2)<Q(1,10**20))
 val=add((4*a,4*a),sc(hj,-1))
 # The exact proof uses H(J)<=2+H(h)/2; intervals only corroborate it.
 ck(val[0]+2*s*mu>=-Q(1,10**20))
 return val
@lru_cache(None)
def dp(t,s):
 options=[surplus(t,s)];n=len(t).bit_length()-1
 for j in range(n):options.append(sc(add(dp(cut(t,j,0),s),dp(cut(t,j,1),s)),Q(1,2)))
 return min(x[0] for x in options),min(x[1] for x in options)
rows=[];minpair=None;worst=None
for n in range(3 if '--pilot' in sys.argv else 4):
 for bits in range(1<<(1<<n)):
  t=tuple(1-2*((bits>>x)&1) for x in range(1<<n));hh=ent(t);ii=inf(t)
  if ii:ck(hh[1]<4*ii)
  else:ck(hh==(0,0))
  mu=Q(sum(t),len(t))
  for j in range(n):ck(Q(sum(cut(t,j,0))+sum(cut(t,j,1)),len(t))==mu)
  p=dp(t,1);m=dp(t,-1);pair=sc(add(p,m),Q(1,2));ck(pair[0]>Q(1,2))
  if minpair is None or pair[0]<minpair:minpair=pair[0];worst=(n,bits)
  rows.append({'n':n,'truth_mask':bits,'pair_lower':str(pair[0]),'pair_upper':str(pair[1])})
result={'status':'PASS','cores':len(rows),'assertions':checks,'seconds':time.perf_counter()-start,'policy_counts_by_n':[1,2,9,244],'sign_policies_independent':True,'minimum_pair_lower':str(minpair),'worst_core':worst,'rows':rows}
(out/('FRONTIER_PILOT.json' if '--pilot' in sys.argv else 'FRONTIER.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print('PASS',len(rows),checks,result['seconds'],'minimum_pair_lower',float(minpair))
