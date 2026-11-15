"""Finite graph checks written independently of the submitted audit."""
from fractions import Fraction as F
from functools import lru_cache
import json,pathlib
results={}
checks=0
for K in range(1,8):
 steps=((0,1),(1,0),(-1,K))
 def S(p):i,j=p;return (-i,j+K*i)
 assert {S(p) for p in steps}==set(steps)
 def predecessors(p,vertical=True):
  i,j=p
  if p==(0,0):return []
  return [(i-di,j-dj) for di,dj in steps if (vertical or (di,dj)!=(0,1)) and j-dj>=0 and j-dj+K*(i-di)>=0]
 @lru_cache(None)
 def ancestors(p):
  if p==(0,0):return frozenset([p])
  return frozenset([p]).union(*(ancestors(q) for q in predecessors(p)))
 def value(p,vertical=True,reflect=False):
  @lru_cache(None)
  def go(v):
   if v==(0,0):return 0
   q=predecessors(v,vertical)
   if not q:return -10**20
   i,j=S(v) if reflect else v
   w=1+((i*131+j*137+K*157)%97) # positive test weights
   return max(go(u) for u in q)+w
  return go(p)
 for m in range(1,16):
  A=set(ancestors((0,m)));B={(i,j+m) for i,j in A}
  assert A&B=={(0,m)}
  assert not (A-{(0,0)}) & (B-{(0,m)})
  assert all(-m<=i<=m for i,j in A)
  for i in range(-m//K,m+1):
   j=max(m,-K*i)
   p=(i,j)
   assert value(p)==value(S(p),reflect=True)
   # Path dominators: intersect visited columns over every predecessor choice.
   @lru_cache(None)
   def common(v):
    if v==(0,0):return frozenset([0])
    qs=predecessors(v)
    c=set(common(qs[0]))
    for q in qs[1:]:c.intersection_update(common(q))
    c.add(v[0]);return frozenset(c)
   assert set(range(min(0,i),max(0,i)+1))<=common(p)
   if K==1:assert value(p,False)==value(p,True)
   checks+=1
 results[K]=dict(diamonds=15,reflection=True,mandatory_columns=True,vertical_removable=K==1)
# Check the coupling transform with rational arithmetic, not a numerical tolerance.
for r,a,s in [(F(1,2),F(1),F(3)),(F(3,10),F(7,10),F(11,13)),(F(1,2),F(1,2),F(1))]:
 assert a/(a+s)*(r/a+(1-r/a)*r/(r+s))==r/(r+s)
 assert (1-r/a)/r==1/r-1/a
out={'endpoint_checks':checks,'by_K':results,'rational_laplace_checks':3}
pathlib.Path('data/growth_checks.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
