from fractions import Fraction as F
from itertools import product,permutations
from collections import defaultdict
from pathlib import Path
import json
Q=list(permutations(range(3)));identity=(0,1,2)
def mul(a,b):return tuple(a[b[i]] for i in range(3))
def word(w):
 x=identity
 for a in w:x=mul(x,a)
 return x
def test(S,n):
 d=len(S);eps=F(1,4);P=defaultdict(F)
 for xs in product(S,repeat=n):
  for ys in product(S,repeat=n):
   p=F(1)
   for x,y in zip(xs,ys):p*=eps/F(d*d)+(1-eps)/d*(x==y)
   P[word(xs),word(ys)]+=p
 EKK=defaultdict(F);pbar=defaultdict(F)
 for mask in product([0,1],repeat=n):
  retained=[i for i in range(n) if not mask[i]];fresh=[i for i in range(n) if mask[i]]
  for vals in product(S,repeat=len(retained)):
   cweight=eps**len(fresh)*(1-eps)**len(retained)/d**len(retained);K=defaultdict(F)
   for fvals in product(S,repeat=len(fresh)):
    w=[None]*n
    for i,v in zip(retained,vals):w[i]=v
    for i,v in zip(fresh,fvals):w[i]=v
    K[word(w)]+=F(1,d**len(fresh))
   for g,a in K.items():
    pbar[g]+=cweight*a
    for h,b in K.items():EKK[g,h]+=cweight*a*b
 assert dict(P)==dict(EKK)
 assert sum(P.values())==1
 for g in Q:assert sum(P[g,h] for h in Q)==pbar[g]
 for g,h in product(Q,repeat=2):
  assert P[g,h]==P[h,g]
 # Test bounded endpoint covariance via exact conditional kernels above / matrix PSD numerical test separate.
 tv=sum(abs(P[g,h]-pbar[g]*pbar[h]) for g,h in product(Q,repeat=2))/2
 return {'generators':[list(s) for s in S],'n':n,'conditional_iid_identity':'exact Fraction equality verified','normalization':'exactly one','tv_fraction':str(tv)}
transpositions=[q for q in Q if sum(q[i]!=i for i in range(3))==2]
res=[test(transpositions,3),test([q for q in Q if q!=identity],3)]
Path('exact_checks.json').write_text(json.dumps(res,indent=2));print(res)
