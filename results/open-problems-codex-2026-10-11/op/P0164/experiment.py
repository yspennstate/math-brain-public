import numpy as np, json, math
from scipy.optimize import linprog
n=5;N=1<<n
X=2*((np.arange(N)[:,None]>>np.arange(n))&1)-1
# Antipodal pairs are indices j and 31-j. First sixteen values determine the table.
v=2*((np.arange(1<<16)[:,None]>>np.arange(16))&1).astype(np.int8)-1
F=np.concatenate((v,-v[:,::-1]),axis=1)
ok=np.ones(len(F),dtype=bool)
for i in range(n):
 lo=np.arange(N)[X[:,i]<0];hi=lo^(1<<i)
 ok &= (F[:,lo]<=F[:,hi]).all(axis=1)
F=F[ok]; print('monotone self-dual tables',len(F))
H=np.ones((N,N),dtype=np.int64)
for s in range(N):
 for i in range(n):
  if s>>i&1:H[:,s]*=X[:,i]
deg=np.array([s.bit_count() for s in range(N)])
out=[];spectra={}
for f in F:
 lp=linprog(np.ones(n),A_ub=-f[:,None]*X,b_ub=-np.ones(N),bounds=[(0,None)]*n,method='highs')
 if not lp.success:continue
 nums=f.astype(np.int64)@H
 wn=[int(np.sum(nums[deg==k]**2)) for k in range(n+1)]
 spectra.setdefault(tuple(wn),[]).append(lp.x.tolist());out.append(wn)
print('threshold tables',len(out),'spectra',len(spectra))
for w,ex in sorted(spectra.items()):print(w,'/1024',len(ex),'example',ex[0])
rhos=np.linspace(.00001,.99999,10000);gauss=2/np.pi*np.arcsin(rhos)
results=[]
for w,ex in spectra.items():
 stab=sum(w[k]/1024*rhos**k for k in range(6));gap=stab-gauss
 results.append(dict(numerators=w,denominator=1024,count=len(ex),weights=ex[0],minimum_grid_gap=float(gap.min()),rho=float(rhos[gap.argmin()])))
json.dump(dict(monotone_selfdual=len(F),thresholds=len(out),spectra=results),open('small_cases.json','w'),indent=2)
# Independent randomized search, float signs used only away from ties; exact Fourier squares.
rng=np.random.default_rng(164);records=[]
for n,trials in [(7,600),(9,500),(11,300),(13,120)]:
 N=1<<n;X=2*((np.arange(N)[:,None]>>np.arange(n))&1)-1;degs=np.array([s.bit_count() for s in range(N)])
 best=(1e9,None,None);ties=0
 for t in range(trials):
  mode=t%4
  w=rng.exponential(size=n) if mode==0 else np.exp(rng.normal(0,2,size=n)) if mode==1 else 1+.2*rng.normal(size=n) if mode==2 else rng.integers(1,12,size=n).astype(float)
  sums=X@w
  if np.any(np.abs(sums)<1e-9):ties+=1;continue
  f=np.sign(sums);a=f.copy()
  h=1
  while h<N:
   b=a.reshape(-1,2*h);u=b[:,:h].copy();v=b[:,h:].copy();b[:,:h]=u+v;b[:,h:]=u-v;h*=2
  a/=N;W=np.bincount(degs,weights=a*a,minlength=n+1)
  rs=np.concatenate((np.linspace(.001,.99,160),[.999,.9999]));gap=np.polynomial.polynomial.polyval(rs,W)-2/np.pi*np.arcsin(rs)
  j=gap.argmin()
  if gap[j]<best[0]:best=(float(gap[j]),float(rs[j]),w.tolist())
 records.append(dict(n=n,trials=trials,ties_skipped=ties,best_gap=best[0],rho=best[1],weights=best[2]));print(records[-1],flush=True)
json.dump(records,open('random_search.json','w'),indent=2)
