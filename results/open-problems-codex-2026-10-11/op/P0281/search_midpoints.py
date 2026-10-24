import itertools,json,time
import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import expm_multiply
from pathlib import Path
out=[]
for n,M in [(2,30),(3,16),(4,10),(5,7)]:
 states=[tuple(reversed(x)) for x in itertools.combinations_with_replacement(range(M+1),n)]; idx={x:i for i,x in enumerate(states)}
 rows=[];cols=[];data=[]
 for x,j in idx.items():
  rate=0
  for k in range(n):
   if k==0 or x[k]<x[k-1]:
    rate+=1;y=list(x);y[k]+=1;y=tuple(y)
    if y in idx:rows.append(idx[y]);cols.append(j);data.append(1.)
  rows.append(j);cols.append(j);data.append(-rate)
 Q=csc_matrix((data,(rows,cols)),shape=(len(states),len(states)));v=np.zeros(len(states));v[idx[(0,)*n]]=1
 # Exhaust all same-parity pairs for n<=3; random pairs for larger n.
 groups={}
 for i,x in enumerate(states):groups.setdefault(tuple(a%2 for a in x),[]).append(i)
 rng=np.random.default_rng(281)
 pairs=[]
 if n<=3:
  for g in groups.values():pairs.extend(itertools.combinations(g,2))
 else:
  for g in groups.values():
   if len(g)>1:pairs.extend((int(a),int(b)) for a,b in rng.choice(g,size=(30000,2)))
 aa=np.array([a for a,b in pairs]);bb=np.array([b for a,b in pairs]);cc=np.array([idx[tuple((u+w)//2 for u,w in zip(states[a],states[b]))] for a,b in pairs]); del pairs
 for t in [.01,.1,.5,1,2,5,10,20]:
  p=expm_multiply(t*Q,v); valid=(p[aa]>1e-250)&(p[bb]>1e-250)&(p[cc]>1e-250)
  scores=2*np.log(p[cc[valid]])-np.log(p[aa[valid]])-np.log(p[bb[valid]])
  k=np.argmin(scores); inds=np.flatnonzero(valid);j=inds[k]
  r={'n':n,'M':M,'t':t,'pairs':int(valid.sum()),'min_log_ratio':float(scores[k]),'a':states[aa[j]],'b':states[bb[j]],'mid':states[cc[j]]};out.append(r);print(r,flush=True)
  Path('numerics.json').write_text(json.dumps(out,indent=2))
