import json,csv,math,collections,hashlib,time,resource,os
from pathlib import Path
import numpy as np
import mpmath as mp
from analysis import wht,evaluate,table_from_hex
mp.mp.dps=70

def hp(f):
 a=wht(f);N=len(a);n=N.bit_length()-1;norm=mp.mpf(N)**2;hist=collections.Counter(map(int,abs(a)))
 H=mp.mpf(0)
 for v,c in hist.items():
  if v:H-=c*mp.mpf(v*v)/norm*mp.log(mp.mpf(v*v)/norm,2)
 ds=[];es=[]
 for i in range(n):
  z=a.reshape(-1,2,1<<i);p=np.abs(z[:,0,:]).ravel();q=np.abs(z[:,1,:]).ravel()
  d=mp.mpf(int(q@q))/norm;ds.append(d);E=mp.mpf(0)
  counts=collections.Counter(zip(map(int,p),map(int,q)))
  for (v,w),c in counts.items():
   if not v or not w:continue
   vv=mp.mpf(v)**2;ww=mp.mpf(w)**2;s=vv+ww
   E+=c*(vv*mp.log(s/vv,2)+ww*mp.log(s/ww,2))/norm
  es.append(E)
 I=sum(ds);return dict(H=H,I=I,HI=H/I if I else mp.mpf(0),EI=sum(es)/I if I else mp.mpf(0),minratio=min((e/d for e,d in zip(es,ds) if d),default=mp.mpf(0)))
start=time.time();out=[];largest=0;keys=set();extrema={}
for n in range(1,7):
 rows=[r for r in csv.DictReader(open(f'census_n{n}.csv')) if float(r['I'])]
 for r in rows:r['HI']=float(r['H'])/float(r['I']);r['EI']=float(r['sumE'])/float(r['I'])
 extrema[n]={}
 for field in ['minratio','HI','EI']:
  mx=max(float(r[field]) for r in rows);ties=[r for r in rows if abs(float(r[field])-mx)<1e-11]
  extrema[n][field]=[dict(truth_hex=r['truth_hex'],minterms=[int(t) for t in r['minterms'].split('|')],dnf=' OR '.join('('+' AND '.join('x%d'%(i+1) for i in range(n) if int(t)>>i&1)+')' for t in r['minterms'].split('|')),orbit=int(r['orbit']),ratio=float(r[field])) for r in ties]
 for k,r in json.load(open('census_summary.json'))[str(n)].items():keys.add((n,r['truth_hex']))
for r in json.load(open('extra_rules.json'))['worst'].values():keys.add((6,r['truth_hex']))
for n,h in sorted(keys):
 f=table_from_hex(h,n);v=hp(f);s=evaluate(f);res=max(abs(float(v[k])-s[k]) for k in ['H','I','HI','EI','minratio']);largest=max(largest,res);out.append(dict(n=n,truth_hex=h,values={k:mp.nstr(x,65) for k,x in v.items()},max_float_residual=res))
for name in ['witnesses/hill_n7.npz','witnesses/hill_n8.npz','witnesses/profile_best.npz','witnesses/structured_n20.npz','witnesses/tribes_10x2.npz']:
 if not Path(name).exists():continue
 f=np.load(name)['f'];v=hp(f);s=evaluate(f);res=max(abs(float(v[k])-s[k]) for k in ['H','I','HI','EI','minratio']);largest=max(largest,res);out.append(dict(witness=name,n=s['n'],values={k:mp.nstr(x,65) for k,x in v.items()},max_float_residual=res))
json.dump(extrema,open('all_extrema.json','w'),indent=2)
result=dict(dps=70,cases=len(out),maximum_float_residual=largest,extremizers=out,npn_inputs={str(n):dict(path=f'../FEIB12/npn{n}.bin',sha256=hashlib.sha256(Path(f'../FEIB12/npn{n}.bin').read_bytes()).hexdigest(),count=Path(f'../FEIB12/npn{n}.bin').stat().st_size//4) for n in range(1,6)},elapsed_seconds=time.time()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,nice=os.getpriority(os.PRIO_PROCESS,0),threads=1)
json.dump(result,open('highprecision.json','w'),indent=2);print('cases',len(out),'max_float_residual',largest)
