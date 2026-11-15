#!/usr/bin/env python3
"""Finite structural checks of the DAG used in the proof; not a proof by computation."""
from functools import lru_cache
from pathlib import Path
import json
records=[]
for K in range(1,6):
 steps=((0,1),(1,0),(-1,K))
 def valid(x,y): return y>=0 and y+K*x>=0
 def S(z):x,y=z;return(-x,y+K*x)
 assert {S(s) for s in steps}==set(steps)
 @lru_cache(None)
 def vertices(x,y):
  if not valid(x,y):return frozenset()
  if (x,y)==(0,0):return frozenset({(0,0)})
  found={(x,y)}
  for dx,dy in steps:
   a,b=x-dx,y-dy
   if valid(a,b):found.update(vertices(a,b))
  return frozenset(found)
 # A cell is on a start-to-end path iff both endpoint displacements are in the cone.
 def diamond(x,y):
  return {(a,b) for b in range(y+1) for a in range(-y//K-1,x+y//K+2) if valid(a,b) and valid(x-a,y-b)}
 for y in range(1,13):
  for x in range(-y//K,y+1):
   if not valid(x,y):continue
   D=diamond(x,y);assert D==set(vertices(x,y));assert {S(z) for z in D}==diamond(*S((x,y)))
   assert all(2*dy+K*dx>0 for dx,dy in steps)
 for m in range(1,13):
  D=diamond(0,m);D2={(x,y+m) for x,y in D}
  assert D&D2=={(0,m)}
 records.append({'K':K,'reflection_steps':True,'diamond_independence':True,'endpoint_heights_checked':12})
Path('data/growth_graph_audit.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records))
