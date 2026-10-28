from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1]; start=time.monotonic(); c=0; cases=0

def ok(v):
 global c
 assert v
 c+=1
 assert time.monotonic()-start<55
@lru_cache(None)
def shapes(n):
 # list one depth per original input; branch0 and branch1 consume low bit
 if n==0: return ((0,),)
 out=[(0,)*(1<<n)]
 for left in shapes(n-1):
  for right in shapes(n-1):
   out.append(tuple(1+(right[x>>1] if x&1 else left[x>>1]) for x in range(1<<n)))
 return tuple(out)
for n,wanted in enumerate((1,2,5,26)):
 ok(len(shapes(n))==wanted); N=1<<n
 for T in shapes(n):
  maxima=[-1]*(N+1); actual=[None]*(N+1)
  for event in range(1<<N):
   M=event.bit_count(); a=sum(T[x] for x in range(N) if (event>>x)&1)
   if a>maxima[M]: maxima[M]=a; actual[M]=event
   # every event is the error set of an actual Boolean table vs constant1
   f=tuple(1-2*((event>>x)&1) for x in range(N)); ok(sum(y<0 for y in f)==M)
   dual=min(L*M+sum(max(t-L,0) for t in T) for L in range(max(T)+1)); ok(a<=dual); cases+=1
  for M in range(N+1):
   dual,L=min((L*M+sum(max(t-L,0) for t in T),L) for L in range(max(T)+1)); ok(maxima[M]==dual)
   event=actual[M]
   ok(all(T[x]>=L for x in range(N) if (event>>x)&1)); ok(all(T[x]<=L for x in range(N) if not ((event>>x)&1)))
# Separate recursive physical tree, rather than a formula for its depth
fixtures=[]
for t in (1,2):
 k=2; n=k+2*t; N=1<<n
 def f(x): return 1 if (x&3) else (-1)**sum(((x>>(k+2*j))&1)*((x>>(k+2*j+1))&1) for j in range(t))
 depths={}; terminals=[]
 def visit(inputs,j):
  if j==n:
   vals={f(x) for x in inputs}; ok(len(vals)==1); terminals.append(inputs)
   for x in inputs: depths[x]=j
   return
  lo=tuple(x for x in inputs if not ((x>>j)&1)); hi=tuple(x for x in inputs if (x>>j)&1)
  if j<k:
   ok(all(f(x)==1 for x in hi)); terminals.append(hi)
   for x in hi: depths[x]=j+1
   visit(lo,j+1)
  else:
   visit(lo,j+1); visit(hi,j+1)
 visit(tuple(range(N)),0)
 ok(len(depths)==N); ok(sum(len(v) for v in terminals)==N)
 e=Q(sum(f(x)<0 for x in range(N)),N); db=Q(sum(depths.values()),N); a=Q(sum(depths[x] for x in range(N) if f(x)<0),N)
 ok(a==e*n); ok(db==Q(3,2)+Q(t,2)); ok(a>e*db)
 fixtures.append({'dimension':n,'mean_depth':str(db),'occupation':str(a),'all_terminals_constant':True})
# Adversarial negative arm: changing f but failing to transport c changes event
f=(1,1,1,-1); ref=(1,1,1,1); chi=(1,-1,1,-1)
f2=tuple(x*y for x,y in zip(f,chi)); c2=chi
old=tuple(x!=y for x,y in zip(f,ref)); transported=tuple(x!=y for x,y in zip(f2,c2)); stale=tuple(x!=1 for x in f2)
ok(old==transported); ok(old!=stale)
ok(Q(1933,1024)>Q(116,1024)); ok(Q(889,1024)>Q(116,1024)); ok(Q(2047,512)<4)
assert cases==6746
out={'status':'PASS','assertions':c,'tree_shapes':34,'joint_event_cases':cases,'physical_trees':fixtures,'elapsed_seconds':time.monotonic()-start,'method':'enumerate ALL error subsets; integer threshold-dual minima; separate recursive physical trees; stale-reference negative arm'}
(R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
