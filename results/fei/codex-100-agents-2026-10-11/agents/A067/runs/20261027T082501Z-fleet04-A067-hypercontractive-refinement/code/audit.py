"""Independent integer orthogonality and exact all-policy occupation audit."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import itertools,json,time
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(v):
 global checks
 checks+=1
 assert v,checks
 assert time.monotonic()-start<58
def character(s,x):return (-1)**((s&x).bit_count())
def pack(x,labels):return sum(((x>>i)&1)<<j for i,j in enumerate(labels))
arrays=0
for signs in itertools.product((-1,0,1),repeat=8):
 k=sum(v!=0 for v in signs)
 if not k:continue
 arrays+=1
 transform=[sum(signs[x]*character(s,x) for x in range(8)) for s in range(8)]
 for mask in range(8):
  erased=[j for j in range(3) if (mask>>j)&1]; keep=[j for j in range(3) if not((mask>>j)&1)]
  for r in range(1<<len(keep)):
   ss=pack(r,keep)
   direct=sum(transform[ss|pack(t,erased)]**2 for t in range(1<<len(erased)))
   buckets=[sum(signs[x]*character(ss,x) for x in range(8) if all(((x>>j)&1)==((t>>i)&1) for i,j in enumerate(erased))) for t in range(1<<len(erased))]
   bucket=(1<<len(erased))*sum(a*a for a in buckets)
   ck(direct==bucket)
   ck(bucket==0 or (1<<len(erased))<=bucket<=(1<<len(erased))*k*k)

def erase(x,j):return (x&((1<<j)-1))|((x>>(j+1))<<j)
@lru_cache(None)
def max_occupation(n,marks):
 if not marks:return F(0)
 if n==0:return F(0) # constant node need not be queried
 best=F(0)
 for j in range(n):
  children=[tuple(sorted(erase(x,j) for x in marks if ((x>>j)&1)==b)) for b in (0,1)]
  best=max(best,1+(max_occupation(n-1,children[0])+max_occupation(n-1,children[1]))/2)
 return best
occupation_rows=[]
for mask in range(1,256):
 marks=tuple(x for x in range(8) if (mask>>x)&1);k=len(marks)
 # Fourth high input bit is dummy w, with all edits at w=0.
 L=max_occupation(4,marks)/2
 ck(L<=F((k-1).bit_length()+2,2))
 occupation_rows.append({'mask':mask,'k':k,'max_original_L':str(L)})
result={'status':'PASS','checks':checks,'signed_arrays':arrays,'all_policy_mark_sets':255,'cached_subproblems':max_occupation.cache_info().currsize,'runtime_seconds':time.monotonic()-start,'rows':occupation_rows}
(R/'out/AUDIT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
