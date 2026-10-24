from fractions import Fraction as F
from itertools import permutations,product
from collections import defaultdict
from pathlib import Path
import json
Q=list(permutations(range(3)));S=[q for q in Q if sum(q[i]!=i for i in range(3))==2];identity=(0,1,2);eps=F(1,4);d=3
states=list(product(Q,Q))
def mul(a,b):return tuple(a[b[i]] for i in range(3))
def conv(P,K):
 R=defaultdict(F)
 for (a,b),p in P.items():
  for (s,t),q in K.items():R[mul(a,s),mul(b,t)]+=p*q
 return dict(R)
lam={(s,t):F(1,d*d) for s,t in product(S,S)}
nu={(s,t):eps/F(d*d)+(1-eps)/d*(s==t) for s,t in product(S,S)}
P={(identity,identity):F(1)};R=P;A=sum(lam[z]**2/nu[z] for z in lam);rows=[]
for k in range(1,7):
 P=conv(P,nu);R=conv(R,lam)
 assert sum(P.values())==sum(R.values())==1
 assert all(P.get(z,0)>=eps**k*q for z,q in R.items())
 chi=sum((R.get(z,0)-p)**2/p for z,p in P.items())
 assert chi<=A**k-1
 rows.append({'group':'S3, three transpositions','k':k,'endpoint_chi_squared_exact':str(chi),'path_chi_squared_bound_exact':str(A**k-1),'domination':'exactly verified','normalization':'exactly one'})
Path('prefix_exact_checks.json').write_text(json.dumps(rows,indent=2),encoding='utf8');print('Exact S3 convolution domination and chi-square contraction checked for k=1,...,6.')
