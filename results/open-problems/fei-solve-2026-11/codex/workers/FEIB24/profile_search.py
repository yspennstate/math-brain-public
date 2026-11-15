"""All repeated symmetric-threshold layers with at most twenty leaves."""
import itertools,json,math,time,os,resource
from pathlib import Path
import numpy as np
from analysis import wht,phi,evaluate
start=time.time();rows=[];best=None
profiles=[]
def walk(p):
 for b in range(2,20//math.prod(p)+1):
  q=p+[b];profiles.append(q);walk(q)
walk([])
for profile in profiles:
 n=math.prod(profile);ix=np.arange(1<<n)
 for ts in itertools.product(*(range(1,b+1) for b in profile)):
  bits=((ix[:,None]>>np.arange(n))&1).astype(np.uint8)
  for b,t in reversed(list(zip(profile,ts))):bits=(bits.reshape(len(ix),-1,b).sum(axis=2)>=t).astype(np.uint8)
  f=2*bits[:,0].astype(np.int64)-1;a=wht(f);mu=(a.astype(float)/len(f))**2
  p=mu[0::2];q=mu[1::2];delta=float(q.sum());E=float(phi(p,q).sum());I=n*delta
  if I==0:continue
  H=float(-(mu[mu>0]*np.log2(mu[mu>0])).sum());r=dict(n=n,profile=profile,thresholds=ts,minratio=E/delta,EI=E/delta,HI=H/I,H=H,I=I)
  rows.append(r)
  if best is None or r['minratio']>best['minratio']:
   best=r.copy();np.savez_compressed('witnesses/profile_best.npz',f=f.astype(np.int8));print(json.dumps(best),flush=True)
json.dump(rows,open('profiles.json','w'),indent=2);json.dump(best,open('profile_best.json','w'),indent=2)
f=np.load('witnesses/profile_best.npz')['f'];audit=evaluate(f);assert max(audit['erasure'][i]/audit['inf'][i] for i in range(audit['n']))-audit['minratio']<1e-12
json.dump(audit,open('profile_audit.json','w'),indent=2)
json.dump(dict(elapsed_seconds=time.time()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,nice=os.getpriority(os.PRIO_PROCESS,0),threads=1,profiles=len(profiles),assignments=len(rows)),open('profile_resources.json','w'),indent=2)
