import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import numpy as np, scipy.linalg as la, json, pathlib, time
ROOT=pathlib.Path(__file__).resolve().parent
def upsets(n):
 if n==0: return [0,1]
 prev=upsets(n-1); shift=1<<(n-1)
 return [a|(b<<shift) for a in prev for b in prev if a&~b==0]
def kernels(n,mask):
 vs=[x for x in range(1<<n) if mask>>x&1]; m=len(vs)
 A=np.array([[int((x^y).bit_count()==1) for y in vs] for x in vs],dtype=float)
 d=A.sum(axis=1); D=d.sum()
 P=np.eye(m)*.5+A/(2*d[:,None]); Q=A/(2*n)+np.diag(1-d/(2*n))
 return vs,A,d,P,Q,d/D
def mixing(K,pi):
 def dist(t): return np.max(np.abs(np.linalg.matrix_power(K,t)-pi[None,:]).sum(axis=1)/2)
 hi=1
 while dist(hi)>.25: hi*=2
 lo=0
 while hi-lo>1:
  mid=(hi+lo)//2
  if dist(mid)>.25: lo=mid
  else: hi=mid
 return hi,dist(hi),dist(hi-1)
out=[]; start=time.time()
for n in range(2,6):
 count=0; maxmix=(-1,None); maxratio=0; worstgap=1; mintransfer=1e9; err=0
 for mask in upsets(n):
  if mask.bit_count()<(1<<(n-1)): continue
  vs,A,d,P,Q,pi=kernels(n,mask); count+=1
  gapP=1-la.eigvalsh(np.eye(len(vs))*.5+A/(2*np.sqrt(d[:,None]*d[None,:])))[-2]
  gapQ=1-la.eigvalsh(Q)[-2]
  mintransfer=min(mintransfer,gapP-gapQ)
  worstgap=min(worstgap,n*gapP)
  err=max(err,float(np.max(np.abs(pi@P-pi))),float(np.max(np.abs(P.sum(axis=1)-1))))
  t,after,before=mixing(P,pi)
  if t>maxmix[0]: maxmix=(t,hex(mask))
  tq,_,_=mixing(Q,np.ones(len(vs))/len(vs)); maxratio=max(maxratio,t/tq)
 result=dict(n=n,count=count,max_mixing=maxmix,min_n_gap=worstgap,min_gapP_minus_gapQ=mintransfer,max_stationarity_error=err,max_tP_over_tQ=maxratio)
 out.append(result); print(json.dumps(result),flush=True)
 (ROOT/'experiment_results.json').write_text(json.dumps(out,indent=2),encoding='utf8')
assert min(x['min_gapP_minus_gapQ'] for x in out)>-1e-12
print('elapsed',time.time()-start,flush=True)

# Exact integer counts and analytic indicator log-Sobolev witnesses.
families=[]
for n in [8,16,32,64,128,256]:
 r=n//2; k=n-r-1
 DC=(n-1)*(1<<(n-1))+(1<<k)
 D=DC+(k+1)*(1<<k); volU=(k+1)*(1<<k)
 lower=2*(k+1)*np.log(D/volU)
 rec=dict(n=n,r=r,k=k,LS_lower=float(lower),LS_lower_over_n2=float(lower/n**2),branch_mass=float(volU/D),mean_escape=2*(k+1))
 families.append(rec); print(json.dumps(rec),flush=True)
(ROOT/'branch_results.json').write_text(json.dumps(families,indent=2),encoding='utf8')
