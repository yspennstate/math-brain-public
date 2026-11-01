import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']: os.environ[k]='1'
import numpy as np
import json,itertools,time,sys
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/'out'
mode=sys.argv[1] if __name__=='__main__' else 'import'; ns=[2,3] if mode=='pilot' else [2,3,4]
start=time.perf_counter(); result={'helper':'A043-biased-prime-grid-v1','mode':mode,'complete':False,'bias_vectors':[],'max':None}
best=-1
def save():
 result['runtime_seconds']=time.perf_counter()-start
 (OUT/(mode+'_discovery.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
def prime_tables(n):
 N=1<<n; masks=np.arange(0,1<<N,2,dtype=np.int64)
 T=2*((masks[:,None]>>np.arange(N))&1)-1
 good=np.ones(len(masks),dtype=bool)
 for i in range(n): good &= np.any(T!=T[:,np.arange(N)^(1<<i)],axis=1)
 for k in range(2,n):
  for B in itertools.combinations(range(n),k):
   D=tuple(i for i in range(n) if i not in B)
   ix=np.array([[sum(((a>>i)&1)<<j for i,j in enumerate(B))|sum(((b>>i)&1)<<j for i,j in enumerate(D)) for b in range(1<<len(D))] for a in range(1<<k)])
   rows=((T[:,ix]+1)//2 * (1<<np.arange(1<<len(D)))).sum(axis=2)
   sortedrows=np.sort(rows,axis=1)
   distinct=1+(sortedrows[:,1:]!=sortedrows[:,:-1]).sum(axis=1)
   good &= distinct>=3
 return masks[good],T[good]
def moments(n,T,biasmask):
 N=1<<n; xs=np.arange(N); b=biasmask.bit_count(); D=4**b*2**(n-b)
 w=np.ones(N,dtype=np.int64); z=[]
 for i in range(n):
  x=2*((xs>>i)&1)-1
  if biasmask&(1<<i): w*=np.where(x==1,1,3); z.append(2*x+1)
  else: z.append(x)
 M=np.empty((N,N),dtype=np.int64)
 for S in range(N):
  v=w.copy()
  for i in range(n):
   if S&(1<<i): v*=z[i]
  M[:,S]=v
 A=T@M
 ks=np.array([(S&biasmask).bit_count() for S in range(N)],dtype=np.int64)
 degrees=np.array([S.bit_count() for S in range(N)],dtype=np.int64)
 p=A.astype(float)**2/(D*D*3.**ks)
 with np.errstate(divide='ignore',invalid='ignore'):
  terms=np.where(p>0,p*np.log2((.75**ks)/p),0)
 H=terms[:,1:].sum(axis=1); delta=(p[:,1:]*(degrees[1:]-1)).sum(axis=1)
 ratio=H/delta
 return A,ks,degrees,D,ratio
if __name__=='__main__':
 for n in ns:
  masks,T=prime_tables(n)
  expected={2:5,3:52,4:28620}[n]
  assert len(masks)==expected
  for biasmask in range(1<<n):
   if time.perf_counter()-start>50:
    result['stopped_reason']='50 second cap'; save(); print(json.dumps(result),flush=True); sys.exit(0)
   A,ks,deg,D,r= moments(n,T,biasmask)
   j=int(np.argmax(r)); val=float(r[j])
   entry={'n':n,'biasmask':biasmask,'represented_cases':len(masks),'max_ratio_float':val,'max_table_mask':int(masks[j])}
   result['bias_vectors'].append(entry)
   if val>best:
    best=val; result['max']={**entry,'weighted_moments':A[j].tolist(),'denominator':D,'bias_probabilities':['1/4' if biasmask&(1<<i) else '1/2' for i in range(n)]}
   save()
  print('n',n,'prime representatives',len(masks),'best',best,flush=True)
 result['complete']=True; save(); print(json.dumps(result['max'],indent=2),flush=True)
