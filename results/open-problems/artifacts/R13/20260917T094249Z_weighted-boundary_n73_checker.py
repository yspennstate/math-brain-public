from fractions import Fraction as F
from functools import lru_cache
from itertools import product
SIGNS=[(1,)+x for x in product((-1,1), repeat=3)]
WEIGHTS=[]
for a in range(1,14):
 for b in range(1,15-a):
  for c in range(1,16-a-b):
   d=16-a-b-c
   if d>=1: WEIGHTS.append((a,b,c,d))

def set_partitions(n):
 out=[]; blocks=[]
 def rec(i):
  if i==n: out.append(tuple(tuple(b) for b in blocks)); return
  for b in blocks:
   b.append(i); rec(i+1); b.pop()
  blocks.append([i]); rec(i+1); blocks.pop()
 rec(0); return out
PARTITIONS=set_partitions(8)
def orientation_options(block):
 k=len(block)
 for tail in product((-1,1), repeat=k-1):
  sig=(1,)+tail
  yield tuple(sig[j]*(block[j]+1) for j in range(k))
def oriented_vectors(key):
 out=[]
 for z in key:
  sg=1 if z>0 else -1; s=SIGNS[abs(z)-1]
  out.append(tuple(sg*x for x in s))
 return out
@lru_cache(None)
def block_lb(key,a):
 vecs=oriented_vectors(key); k=len(vecs); P=a[0]*a[1]*a[2]*a[3]
 best=F(0)
 for mask in range(1,1<<k):
  q=mask.bit_count(); v=[0]*4
  for i,t in enumerate(vecs):
   if mask>>i&1:
    for j in range(4): v[j]+=t[j]
  if v==[0]*4:return None
  den=16*sum(F(v[j]*v[j],a[j]) for j in range(4))
  val=F(q*q,1)/den
  if val>best:best=val
 return best
C=(19,18,18,18); T2=F(55)
count=0; fail=None; worst_ratio=F(0); worst=None
for pi,part in enumerate(PARTITIONS):
 opts=[tuple(orientation_options(b)) for b in part]
 for keys in product(*opts):
  count+=1; best_ok=False; bestR=None; besta=None
  for a in WEIGHTS:
   total=F(0); infeas=False
   for key in keys:
    lb=block_lb(key,a)
    if lb is None: infeas=True; break
    total+=lb
   if infeas: best_ok=True; besta=a; break
   rhs=F(sum(a[j]*C[j] for j in range(4)),16)/T2
   if total>=rhs:
    best_ok=True; besta=a; break
   R=F(sum(a[j]*C[j] for j in range(4)),16)/total if total else None
   if R is not None and (bestR is None or R<bestR): bestR=R; besta=a
  if not best_ok:
   fail=(part,keys,bestR,besta); print('FAIL',count,fail); raise SystemExit
  if count%10000==0: print('count',count)
print('PASS',count,'cache',block_lb.cache_info())
