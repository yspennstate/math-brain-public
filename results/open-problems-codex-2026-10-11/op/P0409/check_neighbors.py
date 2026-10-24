import numpy as np,json,time
from pathlib import Path
from scipy.stats import kstest
rng=np.random.default_rng(40910);out={};start=time.time()
for d in [2,3]:
 n=d+1;p=d-1;marks=[];lengths=[];fail=0;max_points=0
 for rep in range(3000):
  while True:
   theta=rng.normal(size=(n,d));theta/=np.linalg.norm(theta,axis=1)[:,None]
   D=abs(np.linalg.det(np.c_[np.ones(n),theta]))
   if rng.random()*2**(n/2)<D:break
  us=[];aa=[]
  for i in range(n):
   kept=np.delete(theta,i,axis=0);_,_,vh=np.linalg.svd(kept[1:]-kept[0]);u=vh[-1]
   if (kept[0]-theta[i])@u<0:u=-u
   us.append(u);aa.append(kept[0]@u)
  us=np.array(us);aa=np.array(aa);S=rng.gamma(n)
  low=S;high=2*S;qs=np.ones(n);num=0;cert=False
  for block in range(24):
   N=rng.poisson(high-low);num+=N
   if num>500000:break
   ph=rng.normal(size=(N,d));ph/=np.linalg.norm(ph,axis=1)[:,None]
   rr=rng.uniform(low,high,N);h=(rr/S)**(1/p)
   den=h[:,None]*(ph@us.T)-aa
   with np.errstate(divide='ignore',invalid='ignore'):cand=(h[:,None]-1)/den
   cand[(den<=0)|(cand<=0)|(cand>=1)]=1
   if N:qs=np.minimum(qs,cand.min(axis=0))
   if np.all(qs<1):
    needed=S*np.max(((1-aa*qs)/(1-qs))**p)
    if high>=needed:cert=True;break
   low=high;high*=2
  if not cert:fail+=1;continue
  # Uniform neighbor: avoids treating correlated neighbors as independent data.
  i=rng.integers(n);q=qs[i]
  marks.append(S*((1-aa[i]*q)/np.sqrt(1-q*q))**p);lengths.append(np.arctanh(q));max_points=max(max_points,num)
 z=np.array(marks);ks=kstest(z,'gamma',args=(n,))
 out[str(d)]={'attempted':3000,'certified':len(z),'failed_budget':fail,'mean_neighbor_separation':float(z.mean()),'expected_mean':n,'mean_standard_error':float(z.std(ddof=1)/np.sqrt(len(z))),'KS_statistic':float(ks.statistic),'KS_pvalue':float(ks.pvalue),'max_points_one_sample':max_points,'mean_edge_length':float(np.mean(lengths))}
Path('neighbor_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2));print('elapsed',time.time()-start)
