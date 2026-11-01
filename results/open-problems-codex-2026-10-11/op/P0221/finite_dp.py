"""Certified dyadic enclosures for the source's Poisson recursion.
All root bounds are verified by integer signs, without floating point.
"""
from pathlib import Path
from math import isqrt
from collections import Counter
import json,time
ROOT=Path(__file__).resolve().parent
S=1<<70
def partitions(n,least=1):
 if n==0:
  yield ()
 else:
  for x in range(least,n+1):
   for p in partitions(n-x,x):yield (x,)+p
def children(p):
 c=Counter(p); keys=sorted(c)
 for ai,x in enumerate(keys):
  for y in keys[ai:]:
   count=c[x]*(c[x]-1)//2 if x==y else c[x]*c[y]
   if count==0:continue
   q=list(p);q.remove(x);q.remove(y);q.append(x+y)
   yield tuple(sorted(q)), count*x*y
def rootfloor(A,B,C):
 D=(B+S)**2-A*C
 assert D>=0
 return (B+S+isqrt(D))//A
def solve(n):
 states=sorted(partitions(n),key=lambda p: (len(p),p)); vals={}; widest=0
 for p in states:
  if len(p)==1:vals[p]=(0,0);continue
  edges=[(vals[q],w) for q,w in children(p)]
  A=sum(w for bounds,w in edges)
  Bl=sum(w*b[0] for b,w in edges);Cl=sum(w*b[0]**2 for b,w in edges)
  Bu=sum(w*b[1] for b,w in edges);Cu=sum(w*b[1]**2 for b,w in edges)
  lo=rootfloor(A,Bl,Cl);hi=rootfloor(A,Bu,Cu)+1
  assert lo>max(b[1] for b,w in edges), (p,'admissibility')
  assert sum(w*(lo-b[0])**2 for b,w in edges)-2*lo*S<=0
  assert sum(w*(hi-b[1])**2 for b,w in edges)-2*hi*S>=0
  assert lo<=hi
  vals[p]=(lo,hi);widest=max(widest,hi-lo)
 l,u=vals[(1,)*n]
 return {'n':n,'partitions':len(states),'lower_numerator':l,'upper_numerator':u,
         'denominator':S,'display_midpoint':(l+u)/(2*S),'largest_width_units':widest}
if __name__=='__main__':
 start=time.monotonic();results=[]
 for n in range(2,33):
  r=solve(n);results.append(r);print(n,r['partitions'],r['display_midpoint'],flush=True)
  (ROOT/'certified_costs.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
 tests={'strict_decrease_4_to_32':all(b['upper_numerator']<a['lower_numerator'] for a,b in zip(results[2:],results[3:])),
        'strict_increase_2_to_4':all(b['lower_numerator']>a['upper_numerator'] for a,b in zip(results[:2],results[1:3])),
        'states_checked':sum(r['partitions'] for r in results),'elapsed_seconds':time.monotonic()-start}
 (ROOT/'finite_checks.json').write_text(json.dumps(tests,indent=2),encoding='utf-8');print(tests)
