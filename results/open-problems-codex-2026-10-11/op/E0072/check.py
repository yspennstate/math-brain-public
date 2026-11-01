from functools import lru_cache
from itertools import product
from pathlib import Path
import json, time
@lru_cache(maxsize=100000)
def norm(w):
 if not w:return 0
 v=1+norm(w[1:])
 for j in range(1,len(w)):
  if w[j]==(w[0]^1):v=min(v,norm(w[1:j])+norm(w[j+1:]))
 return v
def red(w):
 s=[]
 for a in w:
  if s and s[-1]==(a^1):s.pop()
  else:s.append(a)
 return tuple(s)
def inv(w):return tuple(a^1 for a in w[::-1])
t=time.time(); count=0
for n in range(9):
 for w in product(range(4),repeat=n):
  v=norm(w)
  assert v==norm(red(w)),w
  assert (v==0)==(red(w)==()),w
  assert v==norm(inv(w)),w
  count+=1
small=[w for n in range(4) for w in product(range(4),repeat=n)]
pairs=0
for u in small:
 for v in small:
  assert norm(u+v)<=norm(u)+norm(v)
  assert norm(u+v+inv(u))==norm(v)
  pairs+=1
result={'words_checked':count,'maximum_length':8,'alphabet_size':4,'pairs_checked':pairs,'checks':['reduction invariance','nondegeneracy','inverse symmetry','triangle inequality','conjugation invariance'],'elapsed_seconds':time.time()-t}
Path(__file__).with_name('finite_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result),flush=True)
