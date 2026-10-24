import numpy as np
from itertools import combinations, permutations
from scipy.optimize import linprog
from fractions import Fraction
pairs=list(combinations(range(6),2));E=set(range(6));cols=[(a,b) for a in pairs for b in pairs if not set(a)&set(b)]
P=np.zeros((45,90),dtype=int)
for k,(a,b) in enumerate(cols):
 P[pairs.index(a),k]=1;P[15+pairs.index(b),k]=1;P[30+pairs.index(tuple(sorted(E-set(a)-set(b)))),k]=1
reps=[np.array([[0,1,2],[1,1,1],[2,1,0]]),np.array([[0,1,2],[1,2,0],[2,0,1]])]
ps=list(permutations(range(3)))
def colmap(col,p):return tuple(tuple(sorted(p[i] for i in a)) for a in col)
for C in reps:
 perms=[]
 for p in ps:
  for q in ps:
   if np.array_equal(C[list(p)][:,list(q)],C):perms.append(p+tuple(3+i for i in q))
   if np.array_equal(C.T[list(p)][:,list(q)],C):perms.append(tuple(3+i for i in q)+p)
 def orbit(c):
  ans=set()
  for p in perms:
   d=colmap(c,p);ans.add(d);ans.add(d[::-1])
  return ans
 remain=set(cols); orbs=[]
 while remain:
  c=min(remain);o=orbit(c);orbs.append(sorted(o));remain-=o
 A=np.column_stack([P[:,[cols.index(c) for c in o]].sum(axis=1) for o in orbs])
 a=np.array([1/12 if (i<3)==(j<3) else C[i,j-3]/18 for i,j in pairs]);h=np.array([0 if (i<3)==(j<3) else 1/9 for i,j in pairs])
 res=linprog(np.ones(len(orbs)),A_eq=A,b_eq=np.r_[a,a,h],bounds=(0,None),method='highs')
 print('C',C.tolist(),'group',len(perms)*2,'orbits',len(orbs),'ok',res.success)
 for o,x in zip(orbs,res.x):
  if x>1e-9:print(o[0],len(o),Fraction(float(x)).limit_denominator())
