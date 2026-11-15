import json,csv,math,itertools,hashlib,os,resource,time
from pathlib import Path
import numpy as np
from analysis import wht,phi,evaluate,table_from_hex
start=time.time();max_parity_error=-1e9;allcoord=0;allcoord_witness=None;cases=0
for n in range(1,7):
 for r in csv.DictReader(open(f'census_n{n}.csv')):
  f=table_from_hex(r['truth_hex'],n);a=wht(f);mu=(a.astype(float)/len(f))**2
  even=sum(mu[x] for x in range(len(f)) if x.bit_count()%2==0)
  bound=float(phi(np.array([even]),np.array([1-even]))[0])
  if float(r['I']):
   er=list(map(float,r['erasure'].split('|')));inf=list(map(float,r['inf'].split('|')))
   max_parity_error=max(max_parity_error,max(er)-bound)
   assert max(er)<=bound+1e-12
   for i,(e,d) in enumerate(zip(er,inf)):
    if d and e/d>allcoord:allcoord=e/d;allcoord_witness=dict(n=n,truth_hex=r['truth_hex'],minterms=r['minterms'],coordinate=i)
  cases+=1
# Direct tests of the exact odd-block formula on all MAJ1/MAJ3 choices in the small base.
def threshold(n):return np.array([1 if x.bit_count()>n//2 else -1 for x in range(1<<n)],dtype=np.int64)
def hidden_sub(k,phis):
 n=1+sum(len(p).bit_length()-1 for p in phis);ix=np.arange(1<<n);ys=[];off=0
 for p in phis:
  m=len(p).bit_length()-1;ys.append(p[(ix>>off)&((1<<m)-1)]>0);off+=m
 maj=sum(y.astype(np.uint8) for y in ys)>k//2;ge=np.ones(len(ix),dtype=bool)
 for j in range(k//2):ge&=ys[j]
 return np.where(maj|((ix>>off&1==1)&ge),1,-1)
cs=list(csv.DictReader(open('census_n5.csv')));odd5=[]
for r in cs:
 f=table_from_hex(r['truth_hex'],5)
 if np.all(f==-f[::-1]):odd5.append(f)
configs=[(k,[threshold(m) for m in ms]) for k in [1,3,5] for ms in itertools.product([1,3],repeat=k)]
rng=np.random.default_rng(241112)
for _ in range(12):configs.append((3,[odd5[int(rng.integers(len(odd5)))] for j in range(3)]))
maxerr=0;mincharge=1e9;base_rows=[]
for k in range(1,20,2):
 f=hidden_sub(k,[threshold(1)]*k);s=evaluate(f);delta=2.**-k;a=math.comb(k-1,k//2)/2**(k-1)
 assert abs(s['I']-k*a)<1e-12;assert s['sumE']<=2*s['I']+1e-12;base_rows.append(dict(k=k,EI=s['EI'],xratio=s['erasure'][-1]/delta,I=s['I']))
for k,phis in configs:
 base=hidden_sub(k,[threshold(1)]*k);base_s=evaluate(base);base_mu=(wht(base)/len(base))**2;s=evaluate(hidden_sub(k,phis));delta=2.**-k
 assert abs(s['erasure'][-1]-base_s['erasure'][-1])<1e-12
 off=0
 for j,p in enumerate(phis):
  m=len(p).bit_length()-1;inner=evaluate(p)
  lo=np.array([t for t in range(len(base)) if not(t>>j&1)]);pp=base_mu[lo];qq=base_mu[lo|(1<<j)]
  for ell,tau in enumerate(inner['inf']):
   expected=float(phi(pp,tau*tau*qq).sum());maxerr=max(maxerr,abs(expected-s['erasure'][off+ell]))
   assert abs(expected-s['erasure'][off+ell])<1e-12
   assert abs(tau*base_s['inf'][j]-s['inf'][off+ell])<1e-12
   if tau:assert s['erasure'][off+ell]<=4*s['inf'][off+ell]+1e-12
  off+=m
 mincharge=min(mincharge,5*s['I']-s['sumE']);assert s['sumE']<=5*s['I']+1e-12
# Exact exchangeable fake laws, calculated by cardinality without an exponential array.
fake=[]
for n in [100,200,1000,10000,1000000]:
 p=1/n;q=1-(1-p)**n-n*p*(1-p)**(n-1);d=p*(1-(1-p)**(n-1))/q;b=.25
 delta=2*b*d/(1+math.sqrt(1-4*b*d));empty=1-b-n*delta**2
 assert empty>0 and n*delta**2<=1
 h=lambda t: -t*math.log2(t)-(1-t)*math.log2(1-t) if 0<t<1 else 0
 # Three exceptional pairs: T empty and T singleton; all |T|>=2 pairs have product ratio.
 def ph(a,c):return (a+c)*h(c/(a+c)) if a+c else 0
 pair0=ph(empty,delta**2)
 size2_each=b*p*p*(1-p)**(n-2)/q
 pair1=(n-1)*ph(delta**2,size2_each)
 pr2=1-(1-p)**(n-1)-(n-1)*p*(1-p)**(n-2)
 other=(b/q)*pr2*h(p);er=pair0+pair1+other
 assert er/delta>=math.log2(n)/288
 fake.append(dict(n=n,delta=delta,I=n*delta,singleton_total=n*delta**2,empty=empty,EI=er/delta))
result=dict(parity_census_cases=cases,maximum_parity_upper_violation_bits=max(0,max_parity_error),all_coordinate_max=allcoord,all_coordinate_witness=allcoord_witness,odd_block_composition_cases=len(configs),odd5_choices=len(odd5),max_leaf_formula_residual_bits=maxerr,minimum_charging_slack_bits=mincharge,base_hidden=base_rows,fake_spectral_laws=fake,elapsed_seconds=time.time()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,nice=os.getpriority(os.PRIO_PROCESS,0),threads=1)
json.dump(result,open('proof_checks.json','w'),indent=2);print(json.dumps(result,indent=2))
