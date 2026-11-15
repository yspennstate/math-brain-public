"""Second calculation: exact rational elimination, with no BLAS or floating solve."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
out=[]
for row in json.loads(Path('data/small_ring_validation.json').read_text()):
 n,K,m=row['n'],row['K'],row['mass'];alpha=[F(str(x)) for x in row['alpha']]
 states=[s for s in product(range(K+1),repeat=n) if sum(s)==m];idx={s:i for i,s in enumerate(states)};d=len(states)
 Q=[[F(0) for j in range(d)] for i in range(d)];rates=[F(0) for i in range(d)]
 for i,s in enumerate(states):
  for x in range(n):
   y=(x+1)%n
   if s[x] and s[y]<K:
    t=list(s);t[x]-=1;t[y]+=1;j=idx[tuple(t)]
    Q[i][j]+=alpha[x];Q[i][i]-=alpha[x];rates[i]+=alpha[x]/n
 A=[[Q[j][i] for j in range(d)]+[F(0)] for i in range(d)];A[-1]=[F(1)]*(d+1)
 for k in range(d):
  pivot=next(i for i in range(k,d) if A[i][k]);A[k],A[pivot]=A[pivot],A[k]
  a=A[k][k];A[k]=[v/a for v in A[k]]
  for i in range(k+1,d):
   if not A[i][k]:continue
   fac=A[i][k]
   for j in range(k,d+1):A[i][j]-=fac*A[k][j]
 pi=[F(0)]*d
 for i in range(d-1,-1,-1):pi[i]=A[i][-1]-sum(A[i][j]*pi[j] for j in range(i+1,d))
 assert sum(pi)==1 and min(pi)>0
 assert all(sum(pi[i]*Q[i][j] for i in range(d))==0 for j in range(d))
 J=sum(pi[i]*rates[i] for i in range(d));assert abs(float(J)-row['exact'])<1e-14
 out.append(dict(n=n,K=K,mass=m,alpha=row['alpha'],exact_current=str(J),float_current=float(J),exact_balance=True))
 print(n,K,str(J),flush=True)
Path('data/rational_validation.json').write_text(json.dumps(out,indent=2))
