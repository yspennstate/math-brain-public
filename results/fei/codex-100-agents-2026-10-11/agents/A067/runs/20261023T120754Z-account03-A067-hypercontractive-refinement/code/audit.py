from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0;examined=0;members=0;quadratics=0;strict_examples=[]
def ck(x):
 global checks
 checks+=1;assert x,checks;assert time.monotonic()-start<55
def cut(v,j,b):return tuple(v[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(v)//2))
@lru_cache(None)
def entropy(v):
 coeff=[sum(v[x]*(-1)**((x&s).bit_count()%2) for x in range(len(v))) for s in range(len(v))]
 sq=[x*x for x in coeff if x];ck(all(x==sq[0] for x in sq));n=len(sq);ck(n&(n-1)==0);return F(n.bit_length()-1)
@lru_cache(None)
def maximum(v):
 h=entropy(v);best=F(0)
 for j in range(len(v).bit_length()-1):
  a,b=cut(v,j,0),cut(v,j,1);energy=F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v))
  best=max(best,h-(entropy(a)+entropy(b))/2-3*energy+(maximum(a)+maximum(b))/2)
 return best
for n in range(4):
 for truth in range(1<<(1<<n)):
  examined+=1;v=tuple(1-2*((truth>>x)&1) for x in range(1<<n));anf=[(truth>>x)&1 for x in range(1<<n)]
  for j in range(n):
   for s in range(1<<n):
    if s&(1<<j):anf[s]^=anf[s^(1<<j)]
  polys=[s for s in range(1,1<<n) if anf[s]]
  if any(s.bit_count()>2 for s in polys):continue
  quadratics+=1
  edges=[s for s in polys if s.bit_count()==2];covered=0;okay=True
  matrix=[sum((1<<j) for j in range(n) if j!=i and ((1<<i)|(1<<j)) in edges) for i in range(n)]
  rr=0
  for j in range(n):
   pivot=next((i for i in range(rr,n) if matrix[i]&(1<<j)),None)
   if pivot is None:continue
   matrix[rr],matrix[pivot]=matrix[pivot],matrix[rr]
   for i in range(n):
    if i!=rr and matrix[i]&(1<<j):matrix[i]^=matrix[rr]
   rr+=1
  ck(entropy(v)==rr);ck(maximum(v)<=F(rr,4))
  if maximum(v)<F(rr,4) and len(strict_examples)<2:strict_examples.append({'n':n,'truth_table_integer':truth,'rank':rr,'optimum':str(maximum(v))})
  for s in edges:
   if covered&s:okay=False
   covered|=s
  if any((s&covered) for s in polys if s.bit_count()==1):okay=False
  if not okay:continue
  members+=1;ck(entropy(v)==2*len(edges));ck(maximum(v)==F(len(edges),2))
ck(examined==278);ck(members==44);ck(quadratics==150);ck(bool(strict_examples))
result={'status':'PASS','checks':checks,'runtime_seconds':time.monotonic()-start,'all_Boolean_functions_examined':examined,'all_labelled_quadratic_phases':quadratics,'labelled_clean_members':members,'cached_adaptive_states':maximum.cache_info().currsize,'strict_general_bound_examples':strict_examples,'arithmetic':'Direct character sums / ANF / exact GF2 rank / rational Bellman; no author helper imported'}
(R/'out/INDEPENDENT_AUDIT.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
