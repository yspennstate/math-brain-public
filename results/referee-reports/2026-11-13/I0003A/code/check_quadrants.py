#!/usr/bin/env python3
"""Exact rational checks of the quadrant drift and its adjacent dipole formula."""
import os
if os.getpriority(os.PRIO_PROCESS,0)<10:os.setpriority(os.PRIO_PROCESS,0,10)
import json,random
from fractions import Fraction as Q
from pathlib import Path
rng=random.Random(300304)
R=lambda x,y:(abs(2*x+1)+abs(2*y+1))//2
e=lambda y:1 if y>=0 else -1
f=lambda x:-1 if x>=0 else 1
results=[]
for N in range(1,13):
 phi={r:Q(rng.randrange(-5,6),rng.randrange(1,7)) for r in range(1,N+1)}
 def p(r):return phi.get(r,Q(0))
 def u(x,y):return p(R(x,y))
 charges={}
 for r in range(2,N+2):
  charge=(p(r)-p(r-1))/2
  pairs=[((r-1,0),(r-1,-1)),((-r,-1),(-r,0)),((-1,r-1),(0,r-1)),((0,-r),(-1,-r))]
  for a,b in pairs:
   charges[a]=charges.get(a,Q(0))+charge
   charges[b]=charges.get(b,Q(0))-charge
 energy=Q(0)
 for x in range(-N-3,N+3):
  for y in range(-N-3,N+3):
   au=(e(y)*(u(x+1,y)-u(x-1,y))+f(x)*(u(x,y+1)-u(x,y-1)))/2
   assert au==charges.get((x,y),Q(0)),(N,x,y,au,charges.get((x,y),Q(0)))
   energy+=((u(x+1,y)-u(x,y))**2+(u(x,y+1)-u(x,y))**2)/2
 formula=4*sum(r*(p(r+1)-p(r))**2 for r in range(1,N+1))
 assert energy==formula
 results.append({'max_nonzero_radius':N,'energy':str(energy),'energy_formula':str(formula),'dipole_formula':'exact match'})
Path('data/quadrant_checks.json').write_text(json.dumps(results,indent=2)+'\n')
print('Exact rational quadrant identities passed for all 12 trial profiles.')
