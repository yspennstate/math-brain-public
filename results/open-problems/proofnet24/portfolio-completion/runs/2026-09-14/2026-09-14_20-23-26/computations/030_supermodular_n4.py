#!/usr/bin/env python3
"""Deterministic exploratory vertices of normalized n=4 supermodular cone."""
import itertools, json
from fractions import Fraction
import numpy as np
from scipy.spatial import HalfspaceIntersection
n=4
masks=[m for m in range(16) if 2<=m.bit_count()<=3]
ix={m:i for i,m in enumerate(masks)}
rows=[]; descriptions=[]
for i,j in itertools.combinations(range(n),2):
 p=(1<<i)|(1<<j); rest=15^p
 for t in range(16):
  if t&~rest: continue
  a=np.zeros(11)
  for m,s in [(t|p,1),(t,1),(t|1<<i,-1),(t|1<<j,-1)]:
   if m==15:a[-1]+=s
   elif m in ix:a[ix[m]]+=s
  rows.append(a);descriptions.append((i,j,t))
rows=np.array(rows)
x0=np.array([m.bit_count()*(m.bit_count()-1)/12 for m in masks])
hs=HalfspaceIntersection(-rows,x0)
unique={tuple(Fraction(float(x)).limit_denominator(1000) for x in v) for v in hs.intersections}
print('floating vertices',len(hs.intersections),'rational vertices',len(unique))
def mobius(f):
 c=list(f)
 for i in range(n):
  for m in range(16):
   if m>>i&1:c[m]-=c[m^(1<<i)]
 return c
rays=[]
for v in sorted(unique):
 f=[Fraction(0) for _ in range(16)]; f[-1]=Fraction(1)
 for m,x in zip(masks,v):f[m]=x
 c=mobius(f)
 assert all(sum(Fraction(int(z))*x for z,x in zip(a,tuple(v)+(Fraction(1),)))>=0 for a in rows)
 from math import lcm,gcd
 den=lcm(*(x.denominator for x in c))
 cr=tuple(int(x*den) for x in c)
 rays.append(cr)
perms=list(itertools.permutations(range(n)))
def pmask(m,p):return sum(1<<p[i] for i in range(n) if m>>i&1)
def key(c):return min(tuple(c[pmask(m,p)] for m in range(16)) for p in perms)
classes={}
for c in rays:classes.setdefault(key(c),[]).append(c)
print('permutation classes',len(classes))
for c,orbit in sorted(classes.items()):
 print('count',len(orbit),'nonzero',[(hex(m),x) for m,x in enumerate(c) if x])
with open('computations/030_supermodular_n4_vertices.json','w') as out:
 json.dump({'caveat':'floating HalfspaceIntersection with exact rational feasibility checks, not an exhaustion certificate','masks':masks,'rays':rays,'classes':[(c,len(orbit)) for c,orbit in sorted(classes.items())]},out,indent=2)
