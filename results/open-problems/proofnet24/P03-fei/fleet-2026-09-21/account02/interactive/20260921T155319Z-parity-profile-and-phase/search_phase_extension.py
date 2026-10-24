import json,math
import numpy as np
from verify_fei_advance import walsh,basis
from itertools import combinations
rng=np.random.default_rng(202609211)
outputs=[]
for n, trials in [(5,10000),(6,5000),(7,1000)]:
 N=1<<n; edges=list(combinations(range(n),2)); K=1+n+len(edges)
 rows=[]
 for s in range(N):
  row=1
  for i in range(n):row |= ((s>>i)&1)<<(1+i)
  for e,(i,j) in enumerate(edges):row |= (((s>>i)&1)*((s>>j)&1))<<(1+n+e)
  rows.append(row)
 vals=rng.choice(np.array([-1,1],np.int64),size=(trials,N))
 W=walsh(vals); good=0;best=0;besttruth=None;phase_codes=[]
 degree=np.array([i.bit_count() for i in range(N)])
 for idx,w in enumerate(W):
  piv={};okay=True
  for s,a in enumerate(w):
   if a==0:continue
   row=rows[s];rhs=int(a<0)
   while row:
    p=row.bit_length()-1
    if p not in piv:
     piv[p]=(row,rhs);break
    row^=piv[p][0];rhs^=piv[p][1]
   if not row and rhs:okay=False;break
  if not okay:continue
  good+=1;code=0
  for p in sorted(piv):
   row,rhs=piv[p]
   if ((row&code).bit_count()%2)^rhs:code|=1<<p
  assert all(not a or ((rows[s]&code).bit_count()%2)==int(a<0) for s,a in enumerate(w))
  phase_codes.append(code)
  p=w.astype(float)**2/(N*N);H=-np.sum(p*np.log2(np.where(p>0,p,1)))
  D=int(np.dot(w*w,degree-degree%2));num=2*n*N*N-4*D
  hist={int(v):int(np.sum(np.abs(w)==v)) for v in np.unique(np.abs(w)) if v}
  lhs=math.prod((v*v)**(v*v*c) for v,c in hist.items())
  assert num<=0 or lhs>=1<<num, ('counterexample',n,idx,w.tolist(),code)
  ratio=H/(D/(N*N)) if D else 0
  if ratio>best:best=float(ratio);besttruth=''.join('1' if v<0 else '0' for v in vals[idx])
 outputs.append({'n':n,'sampled_functions':trials,'quadratic_compatible':good,'max_corrected_ratio_float':best,'extremal_sample_bits':besttruth,'exact_corrected_inequality_failures':0})
print(json.dumps({'seed':202609211,'sampling':'independent uniform truth tables, not exhaustive','outputs':outputs},indent=2))
